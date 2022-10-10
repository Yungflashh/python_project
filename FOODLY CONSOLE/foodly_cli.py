import home
import menu
import amount

exits = "YES"

print ("*"*20 ,"WELCOME TO THE FOODLY APP", "*"*20)

print ("""
        SELECT AN OPTION BELOW:
        1) LOG IN
        2) CREATE AN ACCOUNT""")
answer2 = int(input ("ENTER A NUMBER:"))

if answer2>3 or answer2<1:
    print ("invalid input")
elif answer2==1:
    while exits== 'YES' or exits == 'yes' or exits=='y':

        print ("""
        SELECT AN OPTION BELOW:
        1) TOP UP YOUR ACCOUNT BALANCE
        2) VIEW OUR MENU AND PRICING
        3) PLACE AN ORDER"""
           )
        answer = int(input ("ENTER A NUMBER:"))

        if answer>3 or answer<1:
            print ("invalid input")
        elif answer==2:
            menu.view_all_menu()
        elif answer2==1:
            amount.search()

        exits= input ("DO YOU WISH TO CONTINUE")


elif answer2==2:
    home.add_names()


