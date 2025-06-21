import oracledb


class OracleDatabaseController:
    def __init__(self):
        username = "root"
        password = "root"
        host = "localhost"
        port = 1521
        serviceName = "xepdb1"
        self.connectStr = f"{username}/{password}@{host}:{port}/{serviceName}"

    def executeSQLCode(self, sqlCode):
        connection = None
        messages = []

        try:
            connection = oracledb.connect(self.connectStr)
            messages.append("Connected to Oracle database.")

            with connection.cursor() as cursor:
                statements = [stmt.strip() for stmt in sqlCode.split(';') if stmt.strip()]
                for statement in statements:
                    try:
                        cursor.execute(statement)
                        messages.append(f"Executed:\n{statement}")
                    except oracledb.DatabaseError as e:
                        error_message = str(e)
                        messages.append(f"ERROR in statement:\n{statement}\n{error_message}")
                connection.commit()
                messages.append("All changes committed.")

        except oracledb.Error as e:
            messages.append(f"Connection or general error:\n{str(e)}")

        finally:
            if "connection" in locals():
                connection.close()
                messages.append("Connection closed.")

        return "\n\n".join(messages)
