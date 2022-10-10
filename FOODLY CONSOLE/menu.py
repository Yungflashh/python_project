import sqlite3

connection = sqlite3.connect('menu.db')

cursor = connection.cursor()
def create_table():
    sql = '''
            create table menu (
            id integer primary key autoincrement not null unique,
            menu text,
            price text)
            '''
    cursor.execute(sql)



def view_all_menu():
    sql='select * from menu'
    cursor.execute (sql)
    row_set = cursor.fetchall()
    for row in row_set:
        print (row)


def add_menu():
    menu =input ("ENTER YOUR FOOD MENU HERE:")
    price =input ("ENTER THE PRICE HERE:")
    print (menu)
    print (price)
    
    
    
    cursor.execute (""" insert into menu
                    (menu,price)
                    values (?,?)
                    """,(menu,price)


                    )
    connection.commit()
    print ("added succesfully")
