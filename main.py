import time
import replit 
from datetime import date
date = date.today()

##
##
##

##FUNCTIONS

def adminpanel():#childcost, adultcost, seniorcost
          cc = True
          ac = True
          sc = True
          print("Welcome Administrator")
          print()
          print("Would you like to edit ticket prices?")
          print()
          q1 = input(" Y/N >> ").upper()
          time.sleep(0.5)
          if q1 == "Y":
              while cc:
                try:
                  #childcost = 18
                  childcost = int(input("Input Child Entry Price >>  £"))
                  print()
                  cc = False
                except ValueError: 
                    print("You must enter a number.")
              while ac:
                try:
                  #adultcost = 19
                  adultcost = int(input("Input Adult Entry Price >>  £"))
                  print()
                  ac = False
                except ValueError:
                  print("You must enter a number.")
              while sc:
                try:
                  #seniorcost = 20
                  seniorcost = int(input("Input Senior Entry Price >>  £"))
                  print()
                  sc = False
                except ValueError:
                    print("You must enter a number")
          else:
              time.sleep(0.2)
              print()
              print("Thank you for using AdminPanel")

          return childcost, adultcost, seniorcost

def fticketsleft(ticketsleft, ca, aa, sa):
    ticketsleft -= aa
    ticketsleft -= ca
    ticketsleft -= sa
    return ticketsleft

def entrance(ca, aa, sa, wa, cc, ac, sc):
    aa = ac * aa
    ca = cc * ca
    sa = sc * sa
    wa = 20 * wa
    total_cost = aa + ca + sa + wa
    return total_cost

def collect_money(total_cost, notes_entered):
    loop = True
    print("This machine accepts £10, and £20 notes.")
    time.sleep(0.5)
    print("Please enter each note.")
    while loop:
      print(f"Current amount due: £{total_cost}")
      notes_entered = int(input("Please Input a 10, or a 20. >> "))
      print()
      if notes_entered == 2525: #DEBUG
         total_cost -= 5000
      if notes_entered == 10:
         total_cost -= 10
      if notes_entered == 20:
         total_cost -= 20
      if total_cost <= 0:
          print()
          time.sleep(1)
          print("Thank You, You have paid the full amount")
          change = total_cost
          time.sleep(1)
          print()
          print(f"Your change is: £{abs(change)}")
          loop = False
      else:
        time.sleep(0.5)
        print("Please only use £10 or £20 notes. ")
        print()

#FUNCTIONS

##
##
##

##
##
##

#ticketsleft
ticketsleft = 500

#ticketcost
childcost = 12
adultcost = 20
seniorcost = 11

#VARIABLES

##
##
##

godloop = True
while godloop:
    print("_____________Welcome to Copington Adventure Theme Park_____________")
    print()
    print()

    masterloop = True
    print(f"There are {ticketsleft} tickets left.")
    print()

    time.sleep(1)

    print("Press E to wake the machine up.")
    masterlooptrigger = input().upper()
    
    if masterlooptrigger == "ADMIN":
        adminpanel_childcost, adminpanel_adultcost, adminpanel_seniorcost = adminpanel()
        childcost = adminpanel_childcost
        adultcost = adminpanel_adultcost
        seniorcost = adminpanel_seniorcost 
        time.sleep(0.4)
        print()
        print(f"Child Ticket cost is now set to: £{childcost}")
        print(f"Adult Ticket cost is now set to: £{adultcost}")
        print(f"Senior Ticket cost is now set to: £{seniorcost}")
        print()

    if masterlooptrigger == "E":
      print()
      print("Please wait...")
      time.sleep(2)
      print()
      print()
      while masterloop:
        print("Ticket prices")
        print("_______________")
        print(f"Adult......................£{adultcost}")
        print(f"Child......................£{childcost}")
        print(f"Senior.....................£{seniorcost}")
        time.sleep(1)
        print()
        time.sleep(1)
        print("Wristbands")
        print("_______________")
        print("All Access Wristband.......£20")
        time.sleep(1)
        print()
        print("Parking")
        print("_______________")
        print("Parking Pass...............Free")
        print()
        print("______________________________________________________________________________")
        print()
        time.sleep(0.5)

        print("Please enter the amount of adult tickets you would like.")
        input_adult = True
        while input_adult:
          try:
            adult_amount = int(input(" >> "))
            input_adult = False
          except ValueError:
            print("Please input a number.")

        time.sleep(0.2)

        print("Please enter the amount of child tickets you would like.")
        input_child = True
        while input_child:
          try:
            child_amount = int(input(" >> "))
            input_child = False
          except ValueError:
            print("Please input a number.")

        time.sleep(0.2)

        print("Please enter the amount of senior tickets you would like.")
        input_senior = True
        while input_senior:
          try:
            senior_amount = int(input(" >> "))
            input_senior = False
          except ValueError:
            print("Please input a number.")

        time.sleep(0.2)

        print("Please enter the amount of wristbands you would like.")
        input_wristband = True
        while input_wristband:
          try:
            wristband_amount = int(input(" >> "))
            input_wristband = False
          except ValueError:
            print("Please input a number")
        time.sleep(0.2)

        total_cost = entrance(child_amount, adult_amount, senior_amount, wristband_amount, childcost, adultcost, seniorcost)
        ticketsleft = fticketsleft(ticketsleft, child_amount, adult_amount, senior_amount)

        time.sleep(1)
        print("______________________________________________________________________________")
        print()

        print("Please Input the lead bookers surname")
        surname_input = True
        while surname_input: 
          surname = str(input(" >> ").upper())
          checkbool = surname.isalpha()
          if checkbool == False:
            print("Please correctly input your surname.")
          else:
            surname_input = False

        time.sleep(0.2)
        print()

        print("Do you require a parking pass?")
        parking = str(input(" Y/N >> ").upper())

        time.sleep(0.2)
        print()
        time.sleep(0.2)
        print("______________________________________________________________________________")
        print("Your Total Cost")
        print("_______________")
        print("...")
        time.sleep(0.2)
        print("...")
        time.sleep(0.2)
        print(f"Total Cost: £{total_cost}")
        print()
        time.sleep(1)

        

        notes_entered = 0
        collect_money(total_cost, notes_entered)
        #total_cost = collect_money(total_cost, notes_entered)

        #Print a ticket (display lead booker surname, tickets purchased, wristbands purchased, today’s date*)

        print()
        print("Please wait while we print your ticket.")
        print()
        time.sleep(3)
        print("_________________COPINGTON ADVENTURE THEME PARK_________________________")
        time.sleep(0.2)
        print("________________________TICKET FOR ENTRY _______________________________")
        time.sleep(0.2)
        print(f"________BOOKER:{surname}___________________DATE:{date.today()}_______________")
        time.sleep(0.2)
        print(f"______ADULT TICKETS PURCHASED:{adult_amount}_________CHILD TICKETS PURCHASED:{child_amount}______")
        time.sleep(0.2)
        print(f"_____SENIOR TICKETS PURCHASED:{senior_amount}________WRISTBANDS PURCHASED:{wristband_amount}__________")
        time.sleep(0.2)
        print("________________/______-________________________/_\_____________________")
        time.sleep(0.2)
        print("______________/___\__/___\_______/_-_\________/_____\___________________")
        time.sleep(0.2)
        print("____________/_______\______-_-_/_______\/_-_-_________\_________________")
        time.sleep(0.2)
        print()
        time.sleep(0.2)
        print()
        time.sleep(0.2)
        print()
        time.sleep(0.2)
        print()
        time.sleep(0.2)

        if parking == "Y":
            time.sleep(2)
            print("Please wait while we print your parking pass")
            print()
            time.sleep(3)

            print("_________________COPINGTON ADVENTURE THEME PARK_________________")
            time.sleep(0.2)
            print("________________________PARKING PASS____________________________")
            time.sleep(0.2)
            print("________________________________________________________________")
            time.sleep(0.2)
            print(f"___________________VALID ONLY ON:{date.today()}_____________________")
            time.sleep(0.2)
            print("________________________________________________________________")
            time.sleep(0.2)
            print("________________________________________________________________")
            time.sleep(0.2)

        print()
        print("Thank You for your Purchase!")
        print()
        print("This machine will reset in 20 seconds.")
        time.sleep(10)
        print("This machine will reset in 10 seconds.")
        time.sleep(5)
        print("This machine will reset in 5 seconds.")
        time.sleep(5)
        print()
        print()
        print()
        print()
        replit.clear()
        masterloop = False
      if ticketsleft <= 0:
        print("_____________Welcome to Copington Adventure Theme Park_____________")
        print()
        print()

        print("Unfortunately, We are out of tickets. We are sorry for Any Inconvience.")
        godloop = False



#NOTES
#godloop, and masterloop are running fine. 
#not counting down from 500 - needs fixing.
#need to add admin permissions. 