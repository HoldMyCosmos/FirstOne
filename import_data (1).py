import mysql.connector
import json
from tabulate import tabulate
try:
    connection = mysql.connector.connect(
        host="localhost", database="sde_test1", user="root", password="Abc123!@#"
    )

    mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS LibraryDB ( 
                             Id varchar(255) PRIMARY KEY,
                             isbn varchar(26) NOT NULL,
                             accession_number BIGINT(12) NOT NULL,
                             title varchar(255) NOT NULL,
                             author varchar(255) NOT NULL,
                             publisher varchar(255),
                             edition varchar(255),
                             year int(4),
                             category varchar(255),
                             pages int,
                             Price float NOT NULL);"""

    cursor = connection.cursor()
    cursor.execute(mySql_Create_Table_Query)


except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
    exit(1)

file = open("task1/books.json", "r")
text = file.read()
jsonData = []
for line in text.split("\n"):
    if line == "":
        continue
    jsonData.append(json.loads(line))

for data in jsonData:
    try:
        cursor.execute(
            "INSERT INTO LibraryDB (Id, isbn, accession_number, title, author, publisher, edition, year, category, pages, Price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                data["_id"]["$oid"],
                data["isbn"],
                data["accession_number"],
                data["title"],
                data["author"],
                data["publisher"],
                data["edition"],
                data["year"],
                data["category"],
                data["pages"],
                data["price"],
            ),
        )
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
        exit(1)
cursor.execute("SELECT * FROM LibraryDB;")
records = cursor.fetchall()
print(
    tabulate(
        records,
        headers=[
            "Id",
            "isbn",
            "accession_number",
            "title",
            "author",
            "publisher",
            "edition",
            "year",
            "category",
            "pages",
            "Price",
        ],
    )
)
if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
