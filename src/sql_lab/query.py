#!/usr/bin/env python3

import os
import logging
import mysql.connector

#read database settings from environment variables.
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def get_data_by_group(value):
    """Return all rows from mock where the group column matches the value"""
    query = "SELECT * FROM mock WHERE `group` = %s;"

    try:
        logging.info("Getting rows for group: %s", value)
        cur.execute(query, (value,))
        results = cur.fetchall()

        return results

    except mysql.connector.Error as e:
        logging.error("MySQL Error: %s", e)
        return None


def plot_counts(groupby):
    """counts each unique value in the chosen column"""
    data_columns = ["id", "group", "Location", "username", "gender", "job"]

    #if the filtered data is not in the columns, it outputs an error message, otherwise None
    if groupby not in data_columns:
        logging.info("Invalid column name: %s", groupby)
        return None

    #only the specified column name can be inserted.
    query = f"""
        SELECT `{groupby}`, COUNT(*) AS row_count
        FROM mock
        GROUP BY `{groupby}`;
    """

    try:
        logging.info("Counting rows by %s", groupby)
        cur.execute(query)
        results = cur.fetchall()

        #creates an empty list then appends that list with the new information to output the newly created list
        return results

        #catches an error in stores it into e, returning the error message if True, otherwise None
    except mysql.connector.Error as e:
        logging.error("MySQL Error: %s", e)
        return None


def main():
    """executes the filtering and counting values"""
    print(get_data_by_group("coke zero"))
    print(plot_counts("group"))


#Runs the entire code and outputs an error if it fails
if __name__ == "__main__":
    try:
        with mysql.connector.connect(
            host=DBHOST,
            database=DBNAME,
            user=DBUSER,
            password=DBPASS
        ) as connection:
            with connection.cursor() as cur:
                print("Connected to MySQL")
                main()

    except mysql.connector.Error as e:
        logging.error("MySQL Error: %s", e)