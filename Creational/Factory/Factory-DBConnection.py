# Database connection interface
class DatabaseConnection:
    def connect(self):
        pass


# MySQL connection class
class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to MySQL database.")


# PostgresSQL connection class
class PostgresSQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to PostgresSQL database.")


# Connection factory class
class ConnectionFactory:
    @staticmethod
    def create_connection(db_type):
        if db_type == "MySQL":
            return MySQLConnection()
        elif db_type == "PostgresSQL":
            return PostgresSQLConnection()
        raise ValueError("Unknown database type")


# Usage
connection = ConnectionFactory.create_connection("PostgresSQL")
connection.connect()
