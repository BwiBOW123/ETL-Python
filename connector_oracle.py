import cx_Oracle
from dotenv import load_dotenv
import os

load_dotenv()
# Set your Oracle connection credentials
username = os.getenv("orcl_user")
password = os.getenv("orcl_password")
dsn = os.getenv("orcl_dsn")  # Data Source Name, usually a TNS entry in your tnsnames.ora file
def connOracle():
    try:    
        # Establish a connection to the Oracle database
        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    
        # Check if the connection is successful
        if connection:
            print("Connection established successfully!")
        # Create a cursor
        cursor = connection.cursor()
        # Close the cursor and connection
        cursor.close()
        connection.close()

    except cx_Oracle.Error as error:
        print("Error occurred:", error)


def connOracle():
    try:    
        # Establish a connection to the Oracle database
        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    
        # Check if the connection is successful
        if connection:
            print("Connection established successfully!")
        
        return connection

    except cx_Oracle.Error as error:
        print("Error occurred:", error)
        return None

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except cx_Oracle.Error as error:
        print("Error occurred while executing query:", error)
        return None

def insert_data(connection,query, data):
    try:
        cursor = connection.cursor()

        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        print("Data inserted successfully!")
    except cx_Oracle.Error as error:
        print("Error occurred while inserting data:", error)

def update_data(connection, update_query):
    try:
        cursor = connection.cursor()
        cursor.execute(update_query)
        connection.commit()
        cursor.close()
        print("Data updated successfully!")
    except cx_Oracle.Error as error:
        print("Error occurred while updating data:", error)

def delete_data(connection, delete_query):
    try:
        cursor = connection.cursor()
        cursor.execute(delete_query)
        connection.commit()
        cursor.close()
        print("Data deleted successfully!")
    except cx_Oracle.Error as error:
        print("Error occurred while deleting data:", error)
