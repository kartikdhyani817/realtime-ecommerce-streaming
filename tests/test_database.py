from database.db_connection import DB_CONFIG


def test_database_configuration():

    assert DB_CONFIG["host"] == "localhost"
    assert DB_CONFIG["user"] == "root"
    assert DB_CONFIG["database"] == "realtime_ecommerce"


def test_database_name():

    assert DB_CONFIG["database"] == "realtime_ecommerce"