import psycopg2 #lib for postgres connection

try:
    connection = psycopg2.connect(user = "postgres", password = "admin", host="localhost",port="5432",database="postgres")
    #connection data
    cursor = connection.cursor()
    #cursor of connection created
    print(connection.get_dsn_parameters())
    # Parameters of the connection
    cursor.execute("select * from info;")
    #execute query

    record = cursor.fetchall() #fetchone fetchall fetchmany

    #save result in record

    print(record)
    name ="sm"
    id = 4
    cursor.execute("insert into info values("+str(id)+" , '"+ name+"');")
    cursor.execute("select * from info;")
    # execute query

    record = cursor.fetchall()  # fetchone fetchall fetchmany

    # save result in record

    print(record)

except(Exception, psycopg2.Error) as error:

    print(error)

finally:
    if(connection):
        cursor.close();
        connection.close();
        print("done")
