# Author Daniel Lumbu
import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'
    
@app.route('/add/<word1>/<word2>')
def my_sum(word1,word2):
    sum = int(word1) + int(word2)
    return str(sum)

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
    return str(row[0]) + " is the total population of " + str(state_name[0])

if __name__ == '__main__':
    my_port = 5129
    app.run(host='0.0.0.0', port = my_port) 
