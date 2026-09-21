from sqlalchemy import URL, create_engine
import pymysql


# Create a new session for database operations if it doesn't exist
connection = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "password"
)

with connection.cursor() as cursor:
    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS bookmyshow")

connection.close()

# Create a SQLAlchemy engine for the BookMyShow database

# Create  database URL for SQLAlchemy
database_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="password",
    host="127.0.0.1",
    port = 3306,
    database="bookmyshow"
)

engine = create_engine(database_url, echo=True)

# Test connection
with engine.connect() as connection:
    print("Connected to the database successfully!")