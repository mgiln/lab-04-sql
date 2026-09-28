import os
import logging
import mysql.connector
import pandas as pd

#read database from enviroment variables
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def read_data(filename):
    #reading a csv file and returning a database
    data = pd.read_csv(filename)
    logging.info("Read %s rows from %s", len(data), filename)
    return data


def clean_data(data):
    #removing rows with missing values and returning the cleaned dataframe
    cleaned_data = data.dropna()
    logging.info("Removed %s incomplete rows", len(data) - len(cleaned_data))
    return cleaned_data


def load_data(data, table):
    #creating a mock table if it doesnt exist and uploading the dataframe into it
    table = "mock"
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=DBHOST,
            database=DBNAME,
            user=DBUSER,
            password=DBPASS
        )
        cursor = connection.cursor()
        logging.info("Connected to MySQL")

        #table creation if mock doesnt already exist.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mock (
                `id` BIGINT PRIMARY KEY,
                `group` VARCHAR(255),
                `Location` VARCHAR(255),
                `username` VARCHAR(255),
                `gender` VARCHAR(255),
                `job` VARCHAR(255)
            ) ENGINE=InnoDB
        """)

        # values passed into the placeholders
        query = """
            INSERT INTO mock
                (`id`, `group`, `Location`, `username`, `gender`, `job`)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for _, row in data.iterrows():
            values = (
                int(row["id"]),
                str(row["group"]),
                str(row["Location"]),
                str(row["username"]),
                str(row["gender"]),
                str(row["job"])
            )
            cursor.execute(query, values)

        # saves the values that were inserted
        connection.commit()
        logging.info("Uploaded %s rows to %s", len(data), table)

    except Exception:
        logging.exception("Database upload failed")
        if connection is not None:
            connection.rollback()
        raise

    finally:
        #closing the connection
        try:
            if cursor is not None:
                cursor.close()
        finally:
            if connection is not None:
                connection.close()


def main():
    #read, clean and loading the data
    logging.info("Processing")
    data = read_data("MOCK_DATA.csv")
    cleaned_data = clean_data(data)
    load_data(cleaned_data, "mock")
    logging.info("Process complete")


if __name__ == "__main__":
    main()