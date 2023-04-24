import sqlite3

con=sqlite3.connect("baza.db",check_same_thread=False)
cursor=con.cursor()


def reg(id,first,sur,pos):
    try:
        cursor.execute('INSERT INTO main VALUES(?,?,?,?,0)',[id,first,sur,pos])
        con.commit()
        return 'Вы успешно зарегистрировались'
    except:
        return 'Ошибка регистации'

def namePerson(id):
    try:
        cursor.execute(f"SELECT first,sur FROM main WHERE id={id}")
        result=cursor.fetchone()
        if result ==None:
            result='Неизвестный человек'
        else:
            result= result[0]+' '+result[1]
        return result
    except:
        return 'Ошибка распознования лица'
