import Transit_manager

exits = "YES"

print ("*"*20 ,"WELCOME TO PROPERTY MANAGER", "*"*20)

while exits== 'YES' or exits == 'yes' or exits=='y':

        print ("""
        SELECT AN OPTION BELOW:
        1) LIST ALL AVAILABLE PROPERTIES FOR RENT
        2) REGISTER NEW PROPERTIES
        3) UPDATE EXISTING PROPERTIES
        4) DELETE A PROPERT
        5) SEARCH FOR A PROPERT
        """
           )
        answer = int(input ("ENTER A NUMBER:"))

        if answer>5 or answer<1 or answer=="":
            print ("invalid input")
            
        elif answer==1:
            Transit_manager.view_all()
            
        elif answer==1:
            Transit_manager.add_names()
        elif answer==3:
            Transit_manager.update()
        elif answer==4:
            Transit_manager.delete()
        elif answer==5:
            Transit_manager.search()


        exits= input ("DO YOU WISH TO CONTINUE")
