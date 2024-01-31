from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'test1234'
app.config['MYSQL_DATABASE_DB'] = 'flask_db'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql = MySQL(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        # Get data from the request
        data = request.get_json()
        firstName = data['firstName']
        lastName = data['lastName']

        # Create a MySQL cursor
        cur = mysql.connection.cursor()

        # Insert data into the database
        cur.execute("INSERT INTO users (FirstName, LastName) VALUES (%s, %s)", (firstName, lastName))

        # Commit changes
        mysql.connection.commit()

        # Close the cursor
        cur.close()

        return jsonify({"message": "Row added successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
