import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='BLOG',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connected to MySQL database successfully!")
except pymysql.Error as e:
    print("Error connecting to MySQL:", e)
