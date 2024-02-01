# Author Daniel Lumbu
import psycopg2

# Checks if Northfield is a city in our database
def is_Northfield():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lumbud",
        user="lumbud",
        password="spider665eyebrow")

    cur = conn.cursor()

    sql = "SELECT latitude,longitude FROM us_cities WHERE city_name = 'Northfield'; "
    
    cur.execute( sql )

    # fetchone() returns one Northfield row that matches your quer
    row = cur.fetchone()

    if row is not None:
        print( "Northfield" )
        print("Latitude:", row[0])
        print("Longitude:", row[1])
    else:
        print( "Northfield is not part of the Data base" )
    return None

# Prints the largest city in our dataset and the smallest city in minnesota
def largest_Smallest_city():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lumbud",
        user="lumbud",
        password="spider665eyebrow")

    cur = conn.cursor()

    sql1 = "SELECT city_name FROM us_cities WHERE population = (SELECT MAX(population) FROM us_cities);"
    sql2 = "SELECT city_name FROM us_cities WHERE state_code = 'Minnesota' AND population = (SELECT MIN(population) FROM us_cities WHERE state_code = 'Minnesota');"
    cur.execute( sql1 )
    row1 = cur.fetchone()
    cur.execute( sql2 )
    row2 = cur.fetchone()

    print(str(row1[0]) + " is the Largest City")
    print(str(row2[0]) + " is the Smallest City in Minnesota")

#prints the furthest cities north, east, south and west
def North_west():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lumbud",
        user="lumbud",
        password="spider665eyebrow")

    cur = conn.cursor()

    sql1 = "SELECT city_name FROM us_cities WHERE latitude = (SELECT MAX(latitude) FROM us_cities);"
    sql2 = "SELECT city_name FROM us_cities WHERE longitude = (SELECT MAX(longitude) FROM us_cities);"
    cur.execute( sql1 )
    row1 = cur.fetchone()
    cur.execute( sql2 )
    row2 = cur.fetchone()
    sql3 = "SELECT city_name FROM us_cities WHERE latitude = (SELECT MIN(latitude) FROM us_cities);"
    sql4 = "SELECT city_name FROM us_cities WHERE longitude = (SELECT MIN(longitude) FROM us_cities);"
    cur.execute( sql3 )
    row3 = cur.fetchone()
    cur.execute( sql4 )
    row4 = cur.fetchone()
    print(str(row3[0]) + " is the Furthest South")
    print(str(row4[0]) + " is the Furthest West")

# Takes user input and returns the total population of a city
def total_population():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lumbud",
        user="lumbud",
        password="spider665eyebrow")

    cur = conn.cursor()

    city_name = input("Enter City Name: ")

    if len(city_name) == 2:
        sql = "SELECT state_name from state_abbreviations WHERE state_code ='CA';"
        cur.execute(sql)
        city_name = cur.fetchone()
   
    sql = "SELECT SUM(population) AS total_population FROM us_cities WHERE state_code = '%s';"
    
    cur.execute( sql, [city_name])

    row = cur.fetchone()
    print(str(row[0]) + " is the total population of " + city_name)

is_Northfield()
largest_Smallest_city()
North_west()
total_population()
