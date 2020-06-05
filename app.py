import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "Feynman314",
                                  host = "localhost",
                                  port = "5432",
                                  database = "marken")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from marken"

    cursor.execute(postgreSQL_select_Query)
    records = cursor.fetchall() 

    print("Print each row and it's columns values")
    for row in records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")