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
        city_name text,
        state_code text,
        population real,
        latitude real,
        longitude real
        )
        """
commands2 = """ CREATE TABLE state_abbreviations (
        state_name text,
        state_code text
                )
        """
cur.execute(commands)
cur.execute(commands2)
conn.commit()

  
  
