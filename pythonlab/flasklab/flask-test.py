import flask

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

    city_name = word1

    if len(city_name) == 2:
        sql = "SELECT state_name from state_abbreviations WHERE state_code ='CA';"
        cur.execute(sql)
        city_name = cur.fetchone()
   
        sql = "SELECT SUM(population) AS total_population FROM us_cities WHERE state_code = %s;"
        
        cur.execute( sql, [city_name])
    
        row = cur.fetchone()
        return str(row[0]) + " is the total population of " + str(city_name[0])
    else:
        sql = "SELECT SUM(population) AS total_population FROM us_cities WHERE state_code = %s;"
        
        cur.execute( sql, [city_name])
    
        row = cur.fetchone()
        return str(row[0]) + " is the total population of " + city_name

if __name__ == '__main__':
    my_port = 5129
    app.run(host='0.0.0.0', port = my_port) 
