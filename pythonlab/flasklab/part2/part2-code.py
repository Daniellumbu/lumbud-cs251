import psycopg2
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("state.html")

@app.route('/pop/<word1>')
def total_population(word1):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lumbud",
        user="lumbud",
        password="spider665eyebrow")

    cur = conn.cursor()
    city_name = word1.upper()
    sql = f"SELECT state_name FROM state_abbreviations WHERE state_code = '{city_name}';"
    cur.execute(sql)
    state_name = cur.fetchone()

    sql = "SELECT SUM(population) AS total_population FROM us_cities WHERE state_code = %s;"
    cur.execute( sql, [state_name])

    row = cur.fetchone()
    return render_template("results.html", randstr = str(str(row[0]) + " is the total population of " + str(state_name[0])))
    

if __name__ == '__main__':
    my_port = 5129
    app.run(host='0.0.0.0', port = my_port) 
