import sqlite3

try:
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    print("Ühendus loodud")

    # Teostame päringu, et lugeda kõik andmed tabelist 'movies'
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()

    # Väljastame kõik loetud read
    for row in rows:
        print(row)

except sqlite3.Error as error:
    print("Tekkis viga andmebaasiga ühendamisel või päringu teostamisel:", error)
finally:
    if conn:
        conn.close()
        print("Ühendus suleti")