from flask import Flask, render_template, request, url_for, redirect
import datetime
import os
import psycopg2

# Initializing flask app
app = Flask(__name__)

def get_db_connection():
    # conn = psycopg2.connect(host='localhost',
    #                         database='portfolio',
    #                         user=os.environ['DB_USERNAME'],
    #                         password=os.environ['DB_PASSWORD'])
    url = os.environ['DATABASE_URL']
    conn = psycopg2.connect(url)
    return conn

# Route for seeing a data
x = datetime.datetime.now()
@app.route('/data')
def get_time():
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek",
        "Age":"22",
        "Date":x,
        "programming":"python"
        }

@app.route('/contact', methods = ('GET','POST'))
def contact():
   name = request.form.get('name')
   email = request.form.get('email')
   message = request.form.get('message')

   conn = get_db_connection()
   cur = conn.cursor()

   cur.execute('CREATE TABLE IF NOT EXISTS messages (id serial PRIMARY KEY,'
                                 'name varchar (150) NOT NULL,'
                                 'email varchar (150) NOT NULL,'
                                 'message text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

   cur.execute('INSERT INTO messages (name, email, message)'
        'VALUES (%s, %s, %s)',
        (name, email, message))

   conn.commit()
   cur.close()
   conn.close()
   return ('Message sent.', 200)

# Running app
if __name__ == '__main__':
    app.run(debug=True)