from lvm import create,increase,decrease
from os import system
from time import sleep
#import var
while True:
    system("tput setaf 6")
    print("""\n\t\tWelcome To hadoop Menu TUI Program\n
\t\t\t\t1. Assign storage to datanode
\t\t\t\t2. Increase Storage
\t\t\t\t3. Decrease Storage
\t\t\t\t4. Exit""")
    system("tput setaf 3")

    choice = int(input("Enter your choice: "))
    system("tput setaf 2")
    if choice == 1:
        Disk1 = input("Enter disk one: ")            
        Disk2 = input("Enter disk two: ")
        VolGrp = input("Enter volume group name: ") or "g1"
        lv = input("Enter logical volume name: ") or "lv1"
        size = input("Enter Size of LV to create: ") or "0"
        directory= input("Enter path to mount: ") or "/testDir"
        create(Disk1,Disk2,VolGrp,lv,size,directory)
        sleep(10)
        system("clear")
    elif choice == 2:
        vg = input("Enter volume group name: ") or "vg"
        lv = input("Enter logical volume name: ") or "lv"
        size = input("Enter Size of LV to create: ") or "0"
        increase(vg,lv,size)
        sleep(10)
        system("clear")
    elif choice == 3:
        vg = input("Enter volume group name: ") or "vg"
        lv = input("Enter logical volume name: ") or "lv"
        size = input("Enter Size of LV to create: ") or "0"
        directory= input("Enter path to mount: ") or "/testDir"
        decrease(vg,lv,size,directory)
        sleep(10)
        system("clear")
    elif choice == 4:
        system("clear")
        print("Signing out bye have a nice day :)")
        sleep(3)
        break
    else:
        print("Wrong choice")
        sleep(5)
        system("clear")
