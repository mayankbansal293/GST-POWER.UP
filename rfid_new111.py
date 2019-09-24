import csv
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
from os import system
#function to display welcome screen
def welcome():
      print("\t\t\t\t\033[1;34;40mIOT DESIGN LAB")
      print("\t\t\t\033[1;32;40m   RFID-CHALLENGE PROBLEM")
      print("\033[1;35;40mAuthor:Akbon")
#function to create new database
def new_sys():
      file="C:/Users/akbon/Desktop/rfid project/records12.csv"
      fgh="C:/Users/akbon/Desktop/rfid project/no_id12.txt"
      fields=['Id','Name','Bal']
      with open(file,'w',newline='')as f1:
            write=csv.writer(f1)
            write.writerow(fields)
            f1.close()
      with open(fgh,'w')as f2:
            f2.write("0")
            f2.close()
            
#function to create new_id
def new_id(id):
      rows=[]
      CardReader=SimpleMFRC522()
      file="C:/Users/akbon/Desktop/rfid project/no_id12.txt"
      name=str(input("Enter Your Name: "))
      CardReader.write(name)
      bal=str(input("Enter opening balance: "))
      with open("C:/Users/akbon/Desktop/rfid project/records12.csv",'r')as f2:
            read=csv.reader(f2)
            fields=next(read)
            for r in read:
                  rows.append(r)
            f2.close()
      r=[id,name,bal]
      rows.append(r)
      with open("C:/Users/akbon/Desktop/rfid project/records12.csv",'w',newline='')as f2:
            write=csv.writer(f2)
            write.writerow(fields)
            write.writerows(rows)
            f2.close()
      with open(file,'r')as f1:
            records=f1.read()
            records=int(records)
            records+=1
            f1.close
      with open(file,'w')as f1:
            records=str(records)
            f1.write(records)
            f1.close()
#function to compare id
def compare(id):
      file="C:/Users/akbon/Desktop/rfid project/records12.csv"
      fgh="C:/Users/akbon/Desktop/rfid project/no_id12.txt"
      flag=0
      rows=[]
      with open(file,'r')as f1:
            read=csv.reader(f1)
            fields=next(read)
            for r in read:
                  rows.append(r)
            f1.close()
      with open(fgh,'r')as f2:
            ctr=f2.read()
            f2.close()
      ctr=int(ctr)
      for i in range(0,ctr):
            if(rows[i][0]==id):
                  flag=1
                  cf=i
                  break
            else:
                  flag=0
      if(flag is 1):
            return rows[cf][1]
      else:
            return "not found"
#defination to recharge card
def recharge(id):
      file="C:/Users/akbon/Desktop/rfid project/records12.csv"
      fgh="C:/Users/akbon/Desktop/rfid project/no_id12.txt"
      flag=0
      rows=[]
      with open(file,'r')as f1:
            read=csv.reader(f1)
            fields=next(read)
            for r in read:
                  rows.append(r)
            f1.close()
      with open(fgh,'r')as f2:
            ctr=f2.read()
            f2.close()
      ctr=int(ctr)
      for i in range(0,ctr):
            if(rows[i][0]==id):
                  flag=1
                  cf=i
                  break
            else:
                  flag=0
      if(flag is 1):
            bal=int(input("Enter the add value: "))
            balorj=int(rows[cf][2])
            bal+=balorj
            bal=str(bal)
            rows[cf][2]=bal
      with open("C:/Users/akbon/Desktop/rfid project/records12.csv",'w',newline='')as f2:
            write=csv.writer(f2)
            write.writerow(fields)
            write.writerows(rows)
            f2.close()
#defination to display balance
def balance():
      file="C:/Users/akbon/Desktop/rfid project/records12.csv"
      fgh="C:/Users/akbon/Desktop/rfid project/no_id12.txt"
      flag=0
      rows=[]
      with open(file,'r')as f1:
            read=csv.reader(f1)
            fields=next(read)
            for r in read:
                  rows.append(r)
            f1.close()
      with open(fgh,'r')as f2:
            ctr=f2.read()
            f2.close()
      ctr=int(ctr)
      for i in range(0,ctr):
            if(rows[i][0]==id):
                  flag=1
                  cf=i
                  break
            else:
                  flag=0
      if(flag is 1):
            print(rows[cf][2])
#program starts
new=str(input("Do you want to create new Database System?(Yes/No)"))
if(new=='Yes'):
      new_sys()
program_choice=1
while(program_choice==1):
      CardReader=SimpleMFRC522()
      system("cls")
      welcome()
      id,text=CardReader.read()
      id=int(id);
      cmd=compare(id)
      if(cmd == "not found"):       
            new_id(id)
      else:
            print(cmd)
      choice=int(input("Enter 1 To Recharge\n2 To Check Balance"))
      if choice is 1:
            recharge(id)
      elif choice is 2:
             balance()
      program_choice=int(input("Do you want the program to run again?(1,0)"))
      
             
