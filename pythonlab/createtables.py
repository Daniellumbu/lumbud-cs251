import psycopg2
from config import load_config


conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lumbud",
        user="lumbud",
        password="spider665eyebrow")
        
cursor = conn.cursor()

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE Table us_cities (
        city_id SERIAL PRIMARY KEY,
        city_name VARCHAR(255) NOT NULL,
        state_code VARCHAR(2) NOT NULL,
        population INTEGER,
        latitude DOUBLE PRECISION,
        longitude DOUBLE PRECISION
        )
        """,
        """ CREATE TABLE state_abbreviations (
        state_id SERIAL PRIMARY KEY,
        state_name VARCHAR(255) NOT NULL,
        state_code VARCHAR(2) NOT NULL
                )
        """)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()