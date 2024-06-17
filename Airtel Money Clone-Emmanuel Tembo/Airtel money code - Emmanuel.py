#emmanuel agape tembo *python Airtel money code*  
#welcoming message and options avaliabe on Airtel networks
import random
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

mb.showinfo("Airtel money", "Welcome to Airtel Money")
en1 =sd.askfloat("Airtel money", "Mobile money please select:\n1. send money\n2. withdraw cash\n3. SoChe, Ikali, Airtel or Data \n4. Na Sova Loans\n5. Account/PIN")


#generate fake moblie money account names

name1 = [
  "Beatrice", "john", "Mary", "Nalikena", "contildah", "Edward",
  "Ongani", "Caesar", "Johnath", "Moss", "Josh", "Adeline", "Obed"]
name2 = [
  "Jere", "Mumba", "sakala", "Banda", "sepiso" , "Zulu", 
  "Phiri", "Tembo", "Mwale", "Zimba", "Kabelenga", "Tollgate"]

one = random.choice(name1)
two = random.choice(name2)

fake_name = (one + " " + two)

#generate fake mobile money Agents names 

nam1 = [
  "Sean", "Patrick", "Snooch", "frackson", "Meckson", 
  "jackson", "Mercy", "Agape", "chipego", "Paul"]
nam2 = [
  "zulu","sikanyika", "Lungu", "Hamainda", "Tembo", 
  "Banda", "Mapalo", "Phiri", "Tembo", "Chewe","Mabisi"]

on = random.choice(nam1)
tw = random.choice(nam2)

fake_Agent = (on + " " + tw)

#responses according to user input

if en1 == 1:
  tt = sd.askfloat("Airtel Money","send Money\nselect:\n1. Enter number\n2. From favourite")
  if tt == 1:
    p1 = sd.askstring("Airtel Money","Enter phone number\n: ")
    p2 = sd.askstring("Airtel Money","Enter amount to be sent to " + fake_name  + " : ")
    p3 = sd.askfloat("Airtel Money","Send ZMW"+ p2 + " to " + fake_name + " please enter your pin to confirm transaction\n: ")
    mb.showinfo("Airtel Money","Your transaction was succeful.\npowered by Emmanuel.linked codes")
  else:
    mb.showerror("Airtel Money","Sorry services unavaliable at the moment due to technical problems")

#Responses if user wants to withdraw cash 

elif en1 == 2:
    en3 = sd.askfloat("Airtel Money","Airtel money cash out services.\nselect.\n1. Airtel Agent\n2. Banks\n3. Other Agent")
    if en3 == 1:
      sd.askstring("Airtel Money","Enter Agent code/Number ")
      p4 = sd.askfloat("Airtel Money","Enter amount")
      if p4 <= 100 :
        sd.askfloat("Airtel Money","Withdraw ZMW" + str(p4) + " from " + fake_Agent + " charge will be ZMW2.5\nEnter PIN")
        mb.showinfo("Airtel Money", "Your transaction was succeful.\npowered by Emmanuel.linked codes")
      else:
        sd.askfloat("Airtel Money","Withdraw ZMW" + str(p4) + " from " + fake_Agent + " charge will be ZMW5\nEnter PIN")
        mb.showinfo("Airtel Money","Your Transaction was succeful.\nPowered by Emmanuel.linked codes.")
    else:
      mb.showerror("Airtel Money","Emmanuel.linked codes is not responding at the moment try again later")
    
#Responses if user wants to buy SoChe pack

elif en1 == 3:
  p5 = sd.askfloat("Airtel Money","Please select:\n1. So Che pack\n2. Buy Airtime\n3. Data Bundles\n4. Ikali - Data and Voice")
  if p5 == 1:
    p6 = sd.askfloat("Airtel Money","SoChe Pack:\n1. Airtel Pack\n2. All networks")

#user wants Airtel pack 
   
    if p6 == 1:
      p7 = sd.askfloat("Airtel Money","Thanks for selecting Airtel minutes Packs.Press\n1. For 24hours Daily Pack\n2. For Weekly Pack\n3. For monthly Pack")

#user wants 24hours pack
      
      if p7 == 1:
        p8 = sd.askfloat("Airtel Money","Press:\n1. k2 = 9mins + 100SMS\n2. K5 = 36Mins + 20MB + 250SMS")

#just wants option one
        
        if p8 == 1:
          p9 =  sd.askfloat("Airtel Money","please select:\n1. Mobile money\n2. Main account")
          if p9 == 1:
            sd.askstring("Airtel Money","Please enter your PIN")
            mb.showinfo("Airtel Money","Your transaction was succesful!.\nPower by Emmanuel.linked codes.")
          else:
            mb.showinfo("Airtel Money", "Your transaction was succesful!.\nPower by Emmanuel.linked codes.")
        
#Responses if user wants weekly pack
        
      elif p7 == 2:
          n1 = sd.askfloat("Airtel Money","Press:\n1. K20 = 180Min + 500SMS\n2. K10 = 65Min + 75MB + 200SMS\n3. K5 = 20Min + 100SMS")
          if n1 == 1:
            n2 = sd.askfloat("Airtel Money","Press:\n1. Airtel Account\n2. Main Account\n: ")
            sd.askfloat("Airtel Money","Please Enter your PIN")
            mb.showinfo("Airtel Money","Your transaction of Successful.\nPowered by Emmanuel.linked codes.")
          else:
            mb.showinfo("Airtel Money","Your transaction of Successful.\nPowered by Emmanuel.linked codes.")

#User wants monthly pack
     
      else:
          mb.showerror("Airtel Money","MMMH IWEH BOI, YOU'VE NEVER BOUGHT MONTHLY MINUTES ON YOUR PHONE, WHY TRY HERE!!!!!")

#Responses if user wants all networks
    
    else:
      n3 = sd.askfloat("Airtel Money","1. Daily Pack\n2. Weekly Pack\n3. Monthly Pack")

#If user wants daily pack
      
      if n3 == 1:
        n4 = sd.askfloat("Airtel Money","Press:\n1. K2 = 7Min + 100SMS\n2. K5 = 26Min + 20MB + 250SMS\n3. K10 = 60Min + 50MB + 500SMS")
        if n4 == 1:
          g = sd.askfloat("Airtel Money","1. airtel Money\n2. Main account")
          if g == 1:
            sd.askfloat("Airtel Money","Please Enter your PIN: ")
            mb.showinfo("Airtel Money","Your transaction was successful.\nPowered by Emmanuel.linked codes")
          else:
            mb.showinfo("Airtel Money","Your transaction was successful.\nPowered by Emmanuel.linked codes")
        elif n4 == 2:
          g1 = sd.askfloat("Airtel Money","1. airtel Money\n2. Main account")
          if g1 == 1:
            sd.askfloat("Airtel Money","Please Enter your PIN: ")
            mb.showinfo("Airtel Money","Your transaction was successful.\nPowered by Emmanuel.linked codes")
          else:
            mb.showinfo("Airtel Money","Your transaction was successful.\nPowered by Emmanuel.linked codes")  
        else:  
          g2 = sd.askfloat("Airtel Money","1. airtel Money\n2. Main account")
          if g2 == 1:
            sd.askfloat("Airtel Money","Please Enter your PIN: ")
            mb.showinfo("Airtel Money","Your transaction was successful.\nPowered by Emmanuel.linked codes")
          else:
            mb.showinfo("Airtel Money","Your transaction was successful.\nPowered by Emmanuel.linked codes")     

#If user wants weekly pack
     
      elif n3 == 2:
        t = sd.askfloat("Airtel Money","Press:\n1. K50 = 350Min + 250MB + 500SMS\n2. K20 = 120Min + 100MB + 500SMS\n3. K5 = 14Min + 200SMS")
        if t == 1:
          t1 = sd.askfloat("Airtel Money","1. Airtel Money\n2. Main Account")
          if t1 == 1:
            sd.askfloat("Airtel Money","Enter your PIN: ")
            mb.showinfo("Airtel Money","Your transaction was successful.\nPowered by Emmanuel.linked codes")
          else:
            mb.showinfo("Airtel Money","Your transaction was successful.\nPowered by Emmanuel.linked codes")

#user wnats monthly pack  
      
        else:
         mb.showerror("Airtel Money","MMH IWEH IT'S LIKE YOU DON'T LISTEN!! YOU CAN NOT AFFORD MONTHLY")
  else:
    mb.showerror("Airtel Money","sorry services unavaliable at the moment due to technical problems\nBut if you love Emmanuel send a K5 to 0977282006, Love you too")

#Responses if user wants to get a loan
    
elif en1 == 4:
  phone_number = sd.askstring("Airtel Money","Enter your Phone number to check for eligibility")

#Responses if user is eligible
  
  if phone_number.startswith("097"):
    amount = sd.askfloat("Airtel Money","Please select amount\n10 - 40")
    total_figure = amount + 10
    if amount < 10:
      th = sd.askfloat("Airte Money","please enter amount above 10")
    elif amount > 40:
      th = sd.askfloat("Airtel Money","You are not eligible to get amounts above 40, enter amount less than 40")
      total = th + 10
      mb.showinfo("Airtel Money","Loan repayable before 7 May 2024, amount to be paid back is ZMW" +str(total))
      mb.showinfo("Airtel Money","Powered by Emmanuel.linked codes")
    else:
      mb.showinfo("Airtel Money","Loan repayable before 7 May 2024, amount to be paid back is ZMW" +str(total_figure))
      mb.showinfo("Airtel Money","Powered by Emmanuel.linked codes")
  else:
    mb.showerror("Airtel Money","Sorry, you are currently not eligible to get a laon, continue using Airtel money to be considered\nPowered by Emmanuel.linked codes")      

#Responses if user wants to make Account settings changes

elif en1 == 5:
  et = sd.askfloat("Airtel Money","Select:\n1. My PIN\n2. Check Balance\n3. Salary Wallet\n4. Favourites\n5. Reverse Transaction")

#For the My PIN option

  if et == 1:
    et1 = sd.askfloat("Airtel Money","Select:\n1. Change PIN\n2. Forgot PIN\n3. View Security Question\n4. Set/Change Security Question")
    if et1 == 1:
      sd.askfloat("Airtel Money","Enter old PIN: ")
      sd.askfloat("Airtel Money","Enter new PIN: ")
      mb.showinfo("Airtel Money","Your PIN has been successfully changed. Powered by Emmanuel.linekd codes")
    elif et1 == 2:
      sd.askstring("Airtel Money","Security Question\nPlease enter the answer you provided")

#Generate fake Mobile Money PINs

      number = random.randint(1000, 9000)
      message = f"Your PIN is {number}"
      mb.showinfo("Airtel Money", message)
      et2 = mb.askyesno("Airtel Money", "Would you like to change it?")

      if et2:
       new_pin = sd.askinteger("Airtel Money", "Enter New PIN:")
       if new_pin is not None:  # Check if the user entered a new PIN
           mb.showinfo("Airtel Money", "PIN was successfully changed.")
       else:
          mb.showwarning("Airtel Money", "Invalid PIN. PIN change cancelled.")
      else:
       mb.showinfo("Airtel Money", "PIN remains unchanged.")
    else:
     mb.showerror("Airtel Money","sorry services unavaliable at the moment,\nbut if you love Emmanuel send k10 to 0977282006. Thank you")
     mb.showinfo("Airtel Money","powered by Emmanuel.linked codes")    
  elif et == 2:
    sd.askfloat("Airtel Money","Enter your PIN")

#Generate fake account Balances
    
    money = ["250.40 ZMW", "10.23 ZMW","0.00 ZMW", "60.00 ZMW","15.15 ZMW", "24.78 ZMW", "4.45 ZMW", "8.78 ZMW", "700.98 ZMW",
             "67.56 ZMW", "41.67 ZMW", "97.01 ZMW", "400.00 ZMW", "7000.09 ZMW", "234.10 ZMW", "318.09 ZMW", "1.20 ZMW", 
             "1200.76 ZMW", "102.43 ZMW", "409.88 ZMW", "14.33 ZMW", "89.00 ZMW", "2.00 ZMW", "7.12 ZMW", "3.09 ZMW", 
             "0.00 ZMW", "0.00 ZMW", "0.00 ZMW", "0.00 ZMW", "24000.39 ZMW", "7000.00 ZMW", "600.37 ZMW", "9822.89 ZMW",
             "3625.76 ZMW", "2768.88 ZMW", "3234.87 ZMW", "5443.76 ZMW", "9822 ZMW", "2000.00 ZMW", "780.45 ZMW", "0.00 ZMW",
             "0.00 ZMW", "890.98 ZMW", "500.56 ZMW", "3450.00 ZMW", "0.00 ZMW"]
    balance = random.choice(money)

    funds = f"Your current account balance is {balance}"

    mb.showinfo("Airtel Money", funds)
    mb.showinfo("Airtel Money","Powered by Emmanuel.linked codes")
  else:
    mb.showerror("Airtel Money","Sorry services unavalible at the moment. but if you love Emmanuel send a k10 to 0977282006")
    mb.showinfo("Airtel Money","Powered by Emmanuel.linked codes.....")  
else:
  mb.showwarning("Airtel Money","Invalid input select options 1 - 5")

#By Emmanuel Agape Tembo
#Call or Text 0977282006 