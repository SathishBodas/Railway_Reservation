import numpy as np
from random import *

print('------------Welcome to Railway Reservation System------------')
print('*************************************************************')

rail_info='''
Choose one of the following option:
1.Book Ticket
2.Cancel Ticket
3.Check PNR
4.Check seat availability
5.Create new account
6.Check previous bookings
7.Login
8.Exit
'''

a=0  #global variable
user_details={1234:['Sathish','nani@123','Jangaon',9848022338]}
train_details={'krishna':[17045,[[30,234],[20,424],[23,600]],'wed','jn','sec'],
               'Kakatiya':[67056,[[33,230],[25,460],[26,540]],'mon','jn','sec'],
               'falaknama':[45672,[[23,255],[34,345],[45,679]],'sun','bhuv','hyd']}
user_bookings={13456784:[1234,'Sathish','Krishna',2,'wed']}

def confirm_ticket(train_details,train,id,tickets,user_details,coach):
    con=input('confirm ? y/n : ')
    con=con.lower()
    if con== 'y':
        print('Booking succesful !')
        pnr = np.random.randint(100000000,999999999)
        user_bookings[pnr]=[id,user_details[id][0],train,tickets,train_details[train][2]]
        print('Your pnr number : ',pnr)
        print("!  please note your pnr number !")
        c=coach
        if c == '1ac':
            train_details[train][1][0][0] = train_details[train][1][0][0]-tickets
            print('Remaining tickets = ',train_details[train][1][0][0])
        elif c=='2ac':
            train_details[train][1][1][0]=train_details[train][1][1][0]-tickets
            print("remaining tickets : ",train_details[train][1][1][0])
        elif c=='sl':
            train_details[train][1][2][0]=train_details[train][1][2][0]-tickets
            print("remaining tickets : ",train_details[train][1][2][0])
    elif con == 'n':
        print('booking canceled !')
    else:
        print('please enter only y /n ')
        confirm_ticket(train_details,train,id,tickets,user_details,coach)

while True:
    print(rail_info)
    option=input('Enter your option : ')
    if option == '1':
        def check_user_id(user_details):
            id=int(input('enter your user id : '))
            if id in user_details:
                def check_password(user_details):
                    passwd=input('Enter your password : ')
                    if passwd == user_details[id][1]:
                        print("Welcome ",user_details[id][0] ,' !')
                        source_station=input('Enter Source Station : ')
                        destination_station=input('Enter destination Station : ')
                        def check_train_details(train_details,a):
                            for i in train_details:
                                if source_station in train_details[i] and destination_station in train_details[i]:
                                    print('Train name: ',i,' Train number : ',train_details[i][0],' Day of Travel : ',train_details[i][2])
                                    a=1
                                else:
                                    a=a+1 # we given 3 trains it check for 3 trains 
                                    if a == 3:
                                        print('No trains found !')
                                        return 3
                        b = check_train_details(train_details,a)
                        if b == 3:
                            pass
                        else:
                            def check_train_num(train_details,a):
                                train_number = int(input('enter train number : '))
                                for i in train_details:
                                    if train_number in train_details[i]:
                                        print("No of seats available in 1AC :",train_details[i][1][0][0])
                                        print("No of seats available in 2AC :",train_details[i][1][1][0])
                                        print("No of seats available in SL :",train_details[i][1][2][0])

                                        train = i
                                        def check_coach(train_details,train):
                                            coach=input('Enter coach : ')
                                            coach = coach.lower()
                                            tickets=int(input('Enter number of tickets : '))
                                            if coach == '1ac':
                                                print("you have to pay : ",(train_details[train][1][0][1])*tickets)
                                                confirm_ticket(train_details,train,id,tickets,user_details,coach)
                                            elif coach == '2ac':
                                                print("you have to pay : ",(train_details[train][1][1][1])*tickets)
                                                confirm_ticket(train_details,train,id,tickets,user_details,coach)
                                            elif coach == 'sl':
                                                print("you have to pay : ",(train_details[train][1][2][1])*tickets)
                                                confirm_ticket(train_details,train,id,tickets,user_details,coach)
                                            else:
                                                print('Enter coach properly !')
                                                check_coach(train_details,train)
                                        
                                        check_coach(train_details,train)

                                    else:
                                        a=a+1
                                        if a==3:
                                            print('Invalid train number !')
                                            check_train_num(train_details,a)
                            check_train_num(train_details,a)
                    else:
                        print('Invalid password !')
                        check_password(user_details)
                check_password(user_details)
            else:
                print('Invalid Id !')
                check_user_id(user_details)
        check_user_id(user_details)
        main=input("press any key to enter main menu: ")
    elif option == '2':
        def check_user_id(user_details):
            id = int(input("Enter user ID : "))
            if id in user_details:
                def check_password(user_details):
                    pass_word = input("Enter your password : ")
                    if pass_word==user_details[id][1]:
                        print("Welcome ",user_details[id][0],"!")
                        pnr_number = int(input("Enter your PNR number : "))
                        if pnr_number in user_bookings:
                            print("booked tickets are : ")
                            print("Name : ",user_bookings[pnr_number][1])
                            print("Train : ",user_bookings[pnr_number][2])
                            print("No of tickets : ",user_bookings[pnr_number][3])
                            print("Day of travel : ",user_bookings[pnr_number][4])
                            print()
                            print("Do you want to cancel the tickets")
                            cancel =input('confirm  ? y/n : ')
                            cancel = cancel.lower()
                            if cancel == 'y':
                                user_bookings.pop(pnr_number)
                                print("Canceled tickets successfully!")
                                print("Money will refund in 2 days :)")
                            else:
                                print('Not cancelled !')
                        else:
                            print('No bookings !')
                    else:
                        print('Invalid password !')
                        check_password(user_details)
                                  
                check_password(user_details)
            else:
                print('Invalid Id !')
                check_user_id(user_details)
        check_user_id(user_details)
        main=input("press any key to enter main menu: ")

    elif option == '3':
        def check_pnr(user_bookings):
            pnr=int(input('Enter your pnr : '))
            if pnr in user_bookings:
                print('User id : ',user_bookings[pnr][0])
                print('Username : ',user_bookings[pnr][1])
                print('Train name : ',user_bookings[pnr][2])
                print('No.of tickets booked : ',user_bookings[pnr][3])
                print('Day of Travel : ',user_bookings[pnr][4])
            else:
                print('Invalid pnr !')
                check_pnr(user_bookings)
        check_pnr(user_bookings)
        main=input("press any key to enter main menu: ")
    elif option=='4':
        source=input('ENter source station : ')
        destination=input('Enter destination station : ')
        def check_train_details(train_details,a):
            for i in train_details:
                if source in train_details[i] and destination in train_details[i]:
                    print('Train name : ',i,'train number : ',train_details[i][0],' Day of Travel : ',train_details[i][2])
                    a=1
                else:
                    a=a+1
                    if a==3:
                        print('No trains available')
                        return 3
        b=check_train_details(train_details,a)
        if b==3:
            pass
        else:
            def check_train_number(train_details,a):
                train_number=int(input('Enter train number : '))
                for i in train_details:
                    if train_number in train_details[i]:
                        print('---Available seats--- in ',i)
                        print("No of seats available in 1AC :",train_details[i][1][0][0])
                        print("No of seats available in 2AC :",train_details[i][1][1][0])
                        print("No of seats available in SL :",train_details[i][1][2][0])

            check_train_number(train_details,a)
            main=input("press any key to enter main menu: ")
    elif option=='5':
        user_name=input("Enter your name: ")
        user_passwd=input('Enter your password : ')
        home_town=input('Enter your hometown : ')
        phone_no=int(input('Enter your phone num : '))
        user_id=np.random.randint(1000,9999)
        user_details[user_id]=[user_name,user_passwd,home_town,phone_no]
        print('Your user id : ',user_id)
        main=input("press any key to enter main menu: ")

    elif option=='6':
        def check_user_id(user_details):
            id=int(input('Enter your user id : '))
            if id in user_details:
                def check_passwd(user_details):
                    passwd=input('Enter your password : ')
                    if passwd == user_details[id][1]:
                        print('Welcome ',user_details[id][0] ,'!')
                        def check_user_bookings(user_bookings):
                            for p in user_bookings:
                                if id in user_bookings[p]:
                                    print("PNR NO: ",p," ","Train Name: ",user_bookings[p][2]," ","No of Tickets: ",user_bookings[p][3]," ","Day of travel: ",user_bookings[p][4])
                        check_user_bookings(user_bookings)
                    else:
                        print('Invalid password !')
                        check_passwd(user_details)
                check_passwd(user_details)
            else:
                print('Invalid user id !')
                check_user_id(user_details)
        check_user_id(user_details)
        main=input("press any key to enter main menu: ")
    elif option=='7':
        def check_user_id(user_details):
            id = int(input("Enter user ID : "))
            if id in user_details:
                def check_password(user_details):
                    pass_word = input("Enter your password : ")
                    if pass_word==user_details[id][1]:
                        print("Welcome ",user_details[id][0],"!")
                        print("Villege: ",user_details[id][2])
                        print("Cell no: ",user_details[id][3])   
                    else:
                        print("Invalid password")
                        check_password(user_details)
                check_password(user_details)
            else:
                print("Invalid User ID")
                check_user_id(user_details)            
        check_user_id(user_details)
        main=input("press any key to enter main menu: ")
    elif option=='8':
        print("-"*20,'Thank you','-'*20)
        break
    else :
        print("Please Enter valid option !")

#######--------THANK YOU-------#######



            



