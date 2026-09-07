import mysql.connector

from database.db_connection import get_connection


INSERT_QUERY = """
INSERT INTO ecommerce_events (
    event_id,
    order_id,
    customer_id,
    product,
    category,
    quantity,
    unit_price,
    total_amount,
    city,
    event_time,
    processed_at
)
VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s
)
"""


def save_event(event):
    """Save a processed event into MySQL."""

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            INSERT_QUERY,
            (
                event["event_id"],
                event["order_id"],
                event["customer_id"],
                event["product"],
                event["category"],
                event["quantity"],
                event["unit_price"],
                event["total_amount"],
                event["city"],
                event["event_time"],
                event["processed_at"],
            ),
        )

        connection.commit()

        print(
            f"Database | Saved order: "
            f"{event['order_id']}"
        )

        return True

    except mysql.connector.IntegrityError as error:

        if error.errno == 1062:
            print(
                f"Database | Duplicate event ignored: "
                f"{event['event_id']}"
            )

            return False

        print(f"Database Integrity Error | {error}")

        if connection:
            connection.rollback()

        return False

    except mysql.connector.Error as error:

        print(f"Database Error | {error}")

        if connection:
            connection.rollback()

        return False

    finally:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()