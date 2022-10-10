import sqlite3
import amount

connection = sqlite3.connect('Transit_manager.db')

cursor = connection.cursor()
def create_table():
    
    sql = '''
            create table TransitManager(
            id integer primary key autoincrement not null unique,
            Property text,
            Location text,
            price integer,
            Availability text
            )
            '''
    cursor.execute(sql)



def view_all():
    sql='select * from TransitManager'
    cursor.execute (sql)
    row_set = cursor.fetchall()
    for row in row_set:
        print (row)


def add_names():
    pname =input ("ENTER PROPERT NAME HERE:")
    loc =input ("ENTER LOCATION HERE:")
    price =input ("ENTER PRICE HERE:")
    avl =input ("AVAILABILITY (RENTED/FOR RENT):")
    print (pname)
    print (loc)
    print (price)
    print (avl)
    
    
    cursor.execute (""" insert into TransitManager
                    (Property,Location,price,Availability)
                    values (?,?,?,?)
                    """,(pname,loc,price,avl)


                    )
    connection.commit()
    print ("added succesfully")


def search():
    ur_id = input ("ENTER YOUR PROPERTY NAME HERE:")
    cursor.execute ("select * from TransitManager where Property=:user",{"user":ur_id})
    gotten = cursor.fetchall()
    if gotten==[]:
        print ("No result found!")
    else:
        print (gotten)


def update():
    old_name= input("ENTER YOUR PROPERTY OLD NAME HERE:")
    new_name= input("ENTER YOUR PROPERTY NEW NAME HERE:")

    cursor.execute ("UPDATE TransitManager SET Property=:topic WHERE Property=:prop1", {"topic":new_name, "prop1":old_name})
    connection.commit()
    return "UPDATED SUCCESSFULLY"


def delete():
    name= input("ENTER YOUR PROPERTY NAME HERE:")
    cursor.execute ("DELETE from TransitManager where Property=:topic", {"topic":name})
    connection.commit()
    print ("DELETED SUCCESSFULLY")
