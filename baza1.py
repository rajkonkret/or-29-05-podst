import sqlite3

# sqlite - baza sql w pliku
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza została podłaczona....")
except sqlite3.Error as e:
    print("Błąd podcczas podłaczania bazy", e)
finally:
    if sql_connection:
        sql_connection.close()
        print('Baza została zamknięta')

# Baza zosytała podłaczona....
# Baza została zamknięta