import psycopg2
try:
    connection = psycopg2.connect(user = "postgres", password = "admin", host="localhost",port="5432",database="postgres")
    cursor = connection.cursor()
    cursor.execute("create table two(no int primary key, name varchar(20));")
    print("sucessfull")
    cursor.execute("insert into two values(4);")
    print("added sucessfully")
    cursor.execute("select * from two;")
    record = cursor.fetchall()
    print(record)
except(Exception, psycopg2.Error):
    print("error")

finally:
    print("done")