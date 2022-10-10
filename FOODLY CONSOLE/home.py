import sqlite3
import amount

connection = sqlite3.connect('foodly.db')

cursor = connection.cursor()
def create_table():
    sql = '''
            create table foodly (
            id integer primary key autoincrement not null unique,
            firstname text,
            lastname text,
            email text,
            pwrd text)
            '''
    cursor.execute(sql)



def view_all():
    sql='select * from foodly'
    cursor.execute (sql)
    row_set = cursor.fetchall()
    for row in row_set:
        print (row)


def add_names():
    firstname =input ("ENTER YOUR FIRSTNAME HERE:")
    lastname =input ("ENTER YOUR LASTNAME HERE:")
    email =input ("ENTER YOUR EMAIL HERE:")
    pwrd =input ("ENTER YOUR PASSWORD HERE:")
    print (firstname)
    print (lastname)
    print (email)
    print (pwrd)
    
    
    cursor.execute (""" insert into foodly
                    (firstname,lastname,email,pwrd)
                    values (?,?,?,?)
                    """,(firstname,lastname,email,pwrd)


                    )
    connection.commit()
    amount.add_price()
    print ("added succesfully")

