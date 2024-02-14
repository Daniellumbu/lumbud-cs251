from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import mysql.connector

app = Flask(__name__, 
        static_url_path='',
        static_folder='static',
        template_folder='templates')

@app.route('/')
def test_func():
    return app.send_static_file('NovoVoom.html')

@app.route('/internal')
def internal():
    return render_template('pages.html')

@app.route('/internal/')
def redirect_me():
    return redirect(url_for('internal'))

@app.route('/internal/it')
def info_tech():
    return render_template('info_tech.html')

@app.route('/internal/directory')
def direct_form():
    return render_template('direct_form.html')

@app.route('/internal/submit', methods = ['POST'])
def direct_submit():
    cnx = mysql.connector.connect(user='webapp', password='novovoom1web', host='db', database='NovoVoom')
    cursor = cnx.cursor(buffered=True)
    form_data = request.form
    last_name = form_data['last']

    query = "SELECT first, last, dept, phone FROM Employee WHERE last = '" + last_name + "'";
    
    q_list = query.split(';')
    for q in q_list:
        if (len(q) > 2):
            cursor.execute(q) 

    cnx.commit()

    output_str = ""
    for data in cursor:
        for item in data:
            output_str = output_str + str(item) + ",   "
        output_str = output_str + "\n"

    return render_template('results.html', output = output_str)

app.run(host='0.0.0.0', port=5000)
