# Database connection interface
class DatabaseConnection:
    def connect(self):
        pass

# MySQL connection class
class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to MySQL database.")

# PostgreSQL connection class
class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to PostgreSQL database.")

# Connection factory class
class ConnectionFactory:
    @staticmethod
    def create_connection(db_type):
        if db_type == "MySQL":
            return MySQLConnection()
        elif db_type == "PostgreSQL":
            return PostgreSQLConnection()
        raise ValueError("Unknown database type")

# Usage
connection = ConnectionFactory.create_connection("PostgreSQL")
connection.connect()