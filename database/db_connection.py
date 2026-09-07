import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Root@123",
    "database": "realtime_ecommerce",
}


def get_connection():
    """Create and return a MySQL database connection."""

    try:

        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
        )

        if connection.is_connected():
            return connection

        raise ConnectionError(
            "Unable to connect to MySQL."
        )

    except Error as error:

        raise ConnectionError(
            f"MySQL connection failed: {error}"
        ) from error


if __name__ == "__main__":

    try:

        connection = get_connection()

        print("MySQL connection successful.")

        connection.close()

    except ConnectionError as error:

        print(error)