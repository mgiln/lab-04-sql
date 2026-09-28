import os
import logging
import mysql.connector

# Read database settings from environment variables.
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def get_data_by_group(value):
    query = "SELECT * FROM mock WHERE `group` = %s;"

    try:
        logging.info("Getting rows for group: %s", value)
        cur.execute(query, (value,))
        results = cur.fetchall()

        output = []
        for r in results:
            output.append(r)
        return output

    except mysql.connector.Error as e:
        logging.error("MySQL Error: %s", e)
        return None


def plot_counts(groupby):
    """Return counts for each distinct value in the chosen column."""
    # Validate column names because SQL placeholders only accept values.
    data_columns = ["id", "group", "Location", "username", "gender", "job"]

    if groupby not in data_columns:
        logging.error("Invalid column name: %s", groupby)
        return None

    # Only a validated column name is inserted into the query.
    query = f"""
        SELECT `{groupby}`, COUNT(*) AS row_count
        FROM mock
        GROUP BY `{groupby}`;
    """

    try:
        logging.info("Counting rows by %s", groupby)
        cur.execute(query)
        results = cur.fetchall()

        output = []
        for r in results:
            output.append(r)
        return output

    except mysql.connector.Error as e:
        logging.error("MySQL Error: %s", e)
        return None


def main():
    """Demonstrate filtering rows and counting values."""
    print(get_data_by_group("coke zero"))
    print(plot_counts("group"))


# Run the demonstrations when this script is executed directly.
if __name__ == "__main__":
    try:
        # Open the connection and cursor used by both query functions.
        with mysql.connector.connect(
            host=DBHOST,
            database=DBNAME,
            user=DBUSER,
            password=DBPASS
        ) as connection:
            with connection.cursor() as cur:
                logging.info("Connected to MySQL")
                main()

    except mysql.connector.Error as e:
        logging.error("MySQL Error: %s", e)