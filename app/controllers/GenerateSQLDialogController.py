from app.views.GenerateSQLDialogView import GenerateSQLDialogView
from app.enums.RelationshipsEnum import RelationshipsEnum


class GenerateSQLDialogController:
    def __init__(self, ParentWindow, TablesModel, RelationshipsModel, InheritancesModel):
        self.TablesModel = TablesModel
        self.RelationshipsModel = RelationshipsModel
        self.InheritancesModel = InheritancesModel
        self.GenerateSQLDialogView = GenerateSQLDialogView(ParentWindow)

    def displayDialog(self):
        sqlCode = self.generateSQLCode()
        print(sqlCode)
        self.GenerateSQLDialogView.setupUI()
        self.GenerateSQLDialogView.displayDialog()

    def generateSQLCode(self):
        sqlStatements = []

        tables = self.TablesModel.getTables()
        for ObtainedTable in tables:
            createTableSQL = self.generateCreateTableSQLCode(ObtainedTable)
            sqlStatements.append(createTableSQL)

        relationships = self.RelationshipsModel.getRelationships()
        for ObtainedRelationship in relationships:
            createRelationshipSQL = self.generateRelationshipSQLCode(ObtainedRelationship)
            sqlStatements.append(createRelationshipSQL)

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
            columnsSQL.append(f"CONSTRAINT pk_{tableName} PRIMARY KEY ({", ".join(pkColumns)})")

        return f'CREATE TABLE "{tableName}" (\n    ' + ',\n    '.join(columnsSQL) + '\n);'

    def generateRelationshipSQLCode(self, ObtainedRelationship):
        relationshipType = ObtainedRelationship.getRelationshipType()

        if relationshipType is RelationshipsEnum.REL_n_n:
            return self.generateCreateJunctionTableSQLCode(ObtainedRelationship)
        else:
            firstTableName = ObtainedRelationship.getFirstTable().getTableName()
            secondTableName = ObtainedRelationship.getSecondTable().getTableName()
            firstSelectedColumnName = ObtainedRelationship.getFirstSelectedColumnName()
            secondSelectedColumnName = ObtainedRelationship.getSecondSelectedColumnName()

            alterTableSQL = (
                f'ALTER TABLE "{secondTableName}" '
                f'ADD CONSTRAINT fk_{secondTableName}_{secondSelectedColumnName} FOREIGN KEY ("{secondSelectedColumnName}") '
                f'REFERENCES "{firstTableName}"("{firstSelectedColumnName}");'
            )
            return alterTableSQL

    def generateCreateJunctionTableSQLCode(self, ObtainedRelationship):
        firstTableName = ObtainedRelationship.getFirstTable().getTableName()
        secondTableName = ObtainedRelationship.getSecondTable().getTableName()

        junctionTableName = f"{firstTableName}_{secondTableName}"

        firstSelectedColumnName = ObtainedRelationship.getFirstSelectedColumnName()
        secondSelectedColumnName = ObtainedRelationship.getSecondSelectedColumnName()

        createJunctionTableSQL = \
            f'CREATE TABLE "{junctionTableName}" (\n' + \
            f'    "{firstTableName}_{firstSelectedColumnName}" INTEGER NOT NULL,\n' + \
            f'    "{secondTableName}_{secondSelectedColumnName}" INTEGER NOT NULL,\n' + \
            f'    CONSTRAINT pk_{junctionTableName} PRIMARY KEY ' + \
            f'("{firstTableName}_{firstSelectedColumnName}","{secondTableName}_{secondSelectedColumnName}"),\n' + \
            f'    CONSTRAINT fk_{junctionTableName}_{firstTableName} FOREIGN KEY ' + \
            f'"{firstTableName}_{firstSelectedColumnName}" REFERENCES ' + \
            f'"{firstTableName}"("{firstSelectedColumnName}"),\n' + \
            f'    CONSTRAINT fk_{junctionTableName}_{secondTableName} FOREIGN KEY ' + \
            f'"{secondTableName}_{secondSelectedColumnName}" REFERENCES ' + \
            f'"{secondTableName}"("{secondSelectedColumnName}")\n' + \
            f');'

        return createJunctionTableSQL

