import sqlite3

# sqlite - baza sql w pliku
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    select = '''
        SELECT * FROM software;
    '''
    delete = '''
        DELETE FROM software where id = 1;
    '''
    update = '''
        UPDATE software SET price = 2000 WHERE id = 1
    '''
    cursor = sql_connection.cursor()
    print("Baza została podłaczona....")

    for row in cursor.execute(select):  # (1, 'Python', 200.0)
        print(row)

    # uruchomienie delete na bazie
    # cursor.execute(delete)

    # update na bazie
    cursor.execute(update)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Błąd podcczas podłaczania bazy", e)
finally:
    if sql_connection:
        sql_connection.close()
        print('Baza została zamknięta')
