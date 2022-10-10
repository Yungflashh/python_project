import sqlite3

connection = sqlite3.connect('balance.db')

cursor = connection.cursor()
def create_table():
    sql = '''
            create table balance (
            id integer primary key autoincrement not null unique,
            price integer
            )
            '''
    cursor.execute(sql)



def view_balance():
    sql='select * from balance'
    cursor.execute (sql)
    row_set = cursor.fetchall()
    for row in row_set:
        print (row)


def add_price():
    
    price =input ("ENTER AMOUNT YOU WISH TO DEPOSIT INTO YOUR ACCOUNT:")
    print (price)
    
    
    
    cursor.execute (""" insert into balance
                    (price)
                    values (?)
                    """,([price])


                    )
    connection.commit()
    print (price + "added succesfully")


def search():
    ur_id = input ("ENTER YOUR FIRSTNAME HERE:")
    cursor.execute ("select * from balance where price=:user",{"user":ur_id})
    gotten = cursor.fetchall()
    if gotten==[]:
        print ("No result found!")
    else:
        print (gotten)
