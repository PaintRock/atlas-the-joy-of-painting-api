from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="adelknode",
        password="MU8myHoHo",
        database="joy_of_coding"
    )
    print("Connection to MySQL database successful!")
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL database: {err}")
    exit(1)

@app.route('/episodes', methods=['GET'])
def get_episodes():
    # Get filter parameters from the request
    month = request.args.get('month')
    subjects = request.args.getlist('subject')
    colors = request.args.getlist('color')
    match_all = request.args.get('match_all', 'true').lower() == 'true'

    # Create a cursor object
    cursor = mydb.cursor()
    
    #try:
    #    cursor = mydb.cursor()
    #except mysql.connector.OperationalError as err:
     #   if err.errno == mysql.connector.errorcode.CR_SERVER_LOST:
        # Attempt to reconnect
    #        mydb = mysql.connector.connect(
    #            host="localhost",
    #            user="adelknode",
    #            password="MU8myHoHo",
    #            database="joy_of_coding"
    #    )
    #    cursor = mydb.cursor()
   # else:
       # print(f"Error creating cursor: {err}")

    # Build the SQL query based on the filters
    query = "SELECT EPISODE, Title, Month FROM Episodes"
    conditions = []

    if month:
        conditions.append("Month = %s")

    if subjects:
        subject_conditions = ["EXISTS (SELECT 1 FROM Subjects WHERE Episodes.EPISODE = Subjects.EPISODE AND Subject = %s)"] * len(subjects)
        conditions.append("(" + (" AND " if match_all else " OR ").join(subject_conditions) + ")")

    if colors:
        color_conditions = ["EXISTS (SELECT 1 FROM Colors WHERE Episodes.EPISODE = Colors.EPISODE AND Color = %s)"] * len(colors)
        conditions.append("(" + (" AND " if match_all else " OR ").join(color_conditions) + ")")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # Execute the SQL query with parameters
    parameters = []
    if month:
        parameters.append(month)
    if subjects:
        parameters.extend(subjects)
    if colors:
        parameters.extend(colors)

    cursor.execute(query, parameters)
    results = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    mydb.close()

    # Convert the results to a JSON-serializable format
    episodes = [{'episode': row[0], 'title': row[1], 'month': row[2]} for row in results]
    return jsonify(episodes)

if __name__ == '__main__':
    app.run(debug=True)
