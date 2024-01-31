import psycopg2
conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lumbud",
        user="lumbud",
        password="spider665eyebrow")
        
cur = conn.cursor()
commands = """
        CREATE Table us_cities (
        city_name VARCHAR(255) NOT NULL,
        state_code VARCHAR(2) NOT NULL,
        population INTEGER,
        latitude DOUBLE PRECISION,
        longitude DOUBLE PRECISION
        )
        """
commands2 = """ CREATE TABLE state_abbreviations (
        state_id SERIAL PRIMARY KEY,
        state_name VARCHAR(255) NOT NULL,
        state_code VARCHAR(2) NOT NULL
                )
        """
cur.execute(commands)
cur.execute(commands2)

  
  
