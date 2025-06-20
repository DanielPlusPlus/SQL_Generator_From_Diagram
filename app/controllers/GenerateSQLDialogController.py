from app.views.GenerateSQLDialogView import GenerateSQLDialogView
from app.enums.RelationshipsEnum import RelationshipsEnum


class GenerateSQLDialogController:
    def __init__(self, ParentWindow, TablesModel, RelationshipsModel, InheritancesModel):
        self.ParentWindow = ParentWindow
        self.TablesModel = TablesModel
        self.RelationshipsModel = RelationshipsModel
        self.InheritancesModel = InheritancesModel

    def displayDialog(self):
        sqlCode = self.generateSQLCode()
        GenerateSQLDialog = GenerateSQLDialogView(self.ParentWindow)
        GenerateSQLDialog.setupUI(sqlCode)
        GenerateSQLDialog.displayDialog()

    def generateSQLCode(self):
        sqlStatements = []
        tablesWithTypesSet = set()

        for ObtainedInheritance in self.InheritancesModel.getInheritances():
            inheritanceSQL = self.generateInheritanceTypeSQLCode(ObtainedInheritance)
            sqlStatements.append(inheritanceSQL)

            tablesWithTypesSet.add(ObtainedInheritance.getFirstTable())
            tablesWithTypesSet.add(ObtainedInheritance.getSecondTable())

        for ObtainedTable in self.TablesModel.getTables():
            if ObtainedTable in tablesWithTypesSet:
                sqlStatements.append(self.generateCreateTableFromTypeSQLCode(ObtainedTable))
            else:
                sqlStatements.append(self.generateCreateTableSQLCode(ObtainedTable))

        for ObtainedRelationship in self.RelationshipsModel.getRelationships():
            sqlStatements.append(self.generateRelationshipSQLCode(ObtainedRelationship))

        return '\n\n'.join(sqlStatements)

    def generateCreateTableSQLCode(self, ObtainedTable):
        tableName = ObtainedTable.getTableName()
        columnsSQL = []
        pkColumns = []

        tableColumns = ObtainedTable.getTableColumns()
        for column in tableColumns:
            columnSQL = f'"{column["columnName"]}" {column["dataType"]}'
            if column["length"]:
                columnSQL += f'({column["length"]})'
            if column["notNull"]:
                columnSQL += " NOT NULL"
            if column["unique"]:
                columnSQL += " UNIQUE"
            columnsSQL.append(columnSQL)

            if column["pk"]:
                pkColumns.append(f'"{column["columnName"]}"')

        if pkColumns:
            columnsSQL.append(f'CONSTRAINT "pk_{tableName}" PRIMARY KEY ({", ".join(pkColumns)})')

        return f'CREATE TABLE "{tableName}" (\n    ' + ',\n    '.join(columnsSQL) + '\n);'

    def generateInheritanceTypeSQLCode(self, ObtainedInheritance):
        ChildTable = ObtainedInheritance.getFirstTable()
        ParentTable = ObtainedInheritance.getSecondTable()

        childTableName = ChildTable.getTableName()
        parentTableName = ParentTable.getTableName()

        parentColumns = ParentTable.getTableColumns()
        childColumns = ChildTable.getTableColumns()

        parentColumnsNames = {column["columnName"] for column in parentColumns}
        childOnlyColumns = [column for column in childColumns if column["columnName"] not in parentColumnsNames]

        parentTypeSQL = (
                f'CREATE OR REPLACE TYPE "{parentTableName}_T" AS OBJECT (\n    ' +
                ',\n    '.join(self.generateObjectColumns(parentColumns)) +
                '\n) NOT FINAL;'
        )

        childTypeSQL = (
                f'CREATE OR REPLACE TYPE "{childTableName}_T" UNDER "{parentTableName}_T" (\n    ' +
                ',\n    '.join(self.generateObjectColumns(childOnlyColumns)) +
                '\n);'
        )

        return parentTypeSQL + '\n\n' + childTypeSQL

    def generateCreateTableFromTypeSQLCode(self, ObtainedTable):
        tableName = ObtainedTable.getTableName()
        typeName = f'{tableName}_T'
        columnsConstraintsSQL = []
        pkColumns = []

        for column in ObtainedTable.getTableColumns():
            colName = column["columnName"]
            if column["pk"]:
                pkColumns.append(f'"{colName}"')
            if column["notNull"]:
                columnsConstraintsSQL.append(f'"{colName}" NOT NULL')
            if column["unique"]:
                columnsConstraintsSQL.append(f'UNIQUE ("{colName}")')

        if pkColumns:
            columnsConstraintsSQL.append(f'CONSTRAINT "pk_{tableName}" PRIMARY KEY ({", ".join(pkColumns)})')

        createTableSQL = f'CREATE TABLE "{tableName}" OF "{typeName}"'
        if columnsConstraintsSQL:
            createTableSQL += ' (\n    ' + ',\n    '.join(columnsConstraintsSQL) + '\n)'
        return createTableSQL + ';'

    def generateObjectColumns(self, obtainedColumns):
        columnsSQL = []
        for column in obtainedColumns:
            columnSQL = f'"{column["columnName"]}" {column["dataType"]}'
            if column["length"]:
                columnSQL += f'({column["length"]})'
            columnsSQL.append(columnSQL)
        return columnsSQL

    def generateRelationshipSQLCode(self, ObtainedRelationship):
        relationshipType = ObtainedRelationship.getRelationshipType()

        if relationshipType is RelationshipsEnum.REL_n_n:
            return self.generateCreateJunctionTableSQLCode(ObtainedRelationship)
        else:
            firstTableName = ObtainedRelationship.getFirstTable().getTableName()
            secondTableName = ObtainedRelationship.getSecondTable().getTableName()
            firstSelectedColumnName = ObtainedRelationship.getFirstSelectedColumnName()
            secondSelectedColumnName = ObtainedRelationship.getSecondSelectedColumnName()

            alterTableSQL = \
                f'ALTER TABLE "{secondTableName}" ' + \
                f'ADD CONSTRAINT "fk_{secondTableName}_{secondSelectedColumnName}" ' + \
                f'FOREIGN KEY ("{secondSelectedColumnName}")' + \
                f'REFERENCES "{firstTableName}"("{firstSelectedColumnName}");'
            return alterTableSQL

    def generateCreateJunctionTableSQLCode(self, ObtainedRelationship):
        firstTableName = ObtainedRelationship.getFirstTable().getTableName()
        secondTableName = ObtainedRelationship.getSecondTable().getTableName()

        junctionTableName = f"{firstTableName}_{secondTableName}"

        firstSelectedColumnName = ObtainedRelationship.getFirstSelectedColumnName()
        secondSelectedColumnName = ObtainedRelationship.getSecondSelectedColumnName()

        createJunctionTableSQL = \
            f'CREATE TABLE "{junctionTableName}" (\n' + \
            f'    "{firstTableName}_{firstSelectedColumnName}" NUMBER NOT NULL,\n' + \
            f'    "{secondTableName}_{secondSelectedColumnName}" NUMBER NOT NULL,\n' + \
            f'    CONSTRAINT "pk_{junctionTableName}" PRIMARY KEY ' + \
            f'("{firstTableName}_{firstSelectedColumnName}","{secondTableName}_{secondSelectedColumnName}"),\n' + \
            f'    CONSTRAINT "fk_{junctionTableName}_{firstTableName}" FOREIGN KEY ' + \
            f'("{firstTableName}_{firstSelectedColumnName}") REFERENCES ' + \
            f'"{firstTableName}"("{firstSelectedColumnName}"),\n' + \
            f'    CONSTRAINT "fk_{junctionTableName}_{secondTableName}" FOREIGN KEY ' + \
            f'("{secondTableName}_{secondSelectedColumnName}") REFERENCES ' + \
            f'"{secondTableName}"("{secondSelectedColumnName}")\n' + \
            f');'

        return createJunctionTableSQL
