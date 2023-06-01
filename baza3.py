import sqlite3

# sqlite - baza sql w pliku
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # dodajemy insert do bazy
    insert = '''
        INSERT INTO software (id,name,price) VALUES(1, 'Python', 200);
    '''

    cursor = sql_connection.cursor()
    print("Baza została podłaczona....")
    # wykonujemy polecenie na bazie i commitujemy(zatwierdzamy)
    cursor.execute(insert)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Błąd podcczas podłaczania bazy", e)
finally:
    if sql_connection:
        sql_connection.close()
        print('Baza została zamknięta')
