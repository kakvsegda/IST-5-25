#Kuznecov Vadim
#Counting Dorks v0.1
print("WANNA COUNT SOME DORKS???>><<???")
start = str(input("Whisperer: Say 'YEEAAAH' \n"))
history=[]

#starting function to begin the game
def startf():
    continuing=int(input("How many Dorks do you see?!?!\n"))
    if continuing>=10:
        print("Lowkey a lot of them \nLet's go further!")
    substi=str(input("HOOLD UP, did any dork just left??\n"))
    if substi == 'no' or substi=='No':
        print("Oh boy, I'm seeing things \nDon't bother, let's count in other places!!!")
    elif substi == 'Yes' or substi=="YEEAAAH" or substi=="yes":
        print("AHAAAA! Let's go after him!! He will lead us to more!!!")
        continuing-=1
    else:
        if_dork = str(input("Are you a dork?!\n"))
        if if_dork == "yes" or if_dork=="Yes":
            print("Hell, I knew it!!")
            print("Let's count your kind in other places!!!")
            continuing +=1
        elif if_dork== 'no' or if_dork=='No':
            print("Okay, suspicious 'Non'Dork!")
            print("Let's count in other places!!!")
        else:
            endo(continuing)
    move = str(input("Move: 'Left', 'Right', 'Front', 'Down'\n"))
    history.append(f"Counted: {continuing}")
    history.append(f"Move: {move}")
    return [move, continuing]
    
#func to count after the startf 
def middlef(continuing):
    continuing1=int(input("How many more Dorks do you see?!?!\n"))
    continuing=+continuing1
    history.append(f"Counted: {continuing}")
    if continuing1 >= 15:
        print("Lowkey a lot of them \nLet's go further!")
    else:
        if_dork = str(input("Are you a dork?!\n"))
        if if_dork == "yes" or if_dork=="Yes":
            print("Hell, I knew it!!")
            print("Let's count your kind in other places!!!")
            continuing =+1
            move = str(input("Move: 'Left', 'Right', 'Front', 'Down'\n"))
        elif if_dork== 'no' or if_dork=='No':
            print("Suspicious 'Non'Dork!")
            print("Let's count in other places!!!")
            move = str(input("Move: 'Left', 'Right', 'Front', 'Down'\n"))
        else:
            endo()
        
    substi=str(input("HOOLD UP, did any dork just left??\n"))
    if substi == 'no' or substi=='No':
        print("Oh boy, I'm seeing things \nDon't bother, let's count in other places!!!")
        move = str(input("Move: 'Left', 'Right', 'Front', 'Down'\n"))
    elif substi == 'Yes' or substi=="YEEAAAH" or substi=="yes":
        continuing=-1
        print("AHAAAA! Let's go after him!! He will lead us to more!!!")
        move = str(input("Move: 'Left', 'Right', 'Front', 'Down'\n"))
    else:
        if_dork = str(input("Are you a dork?!\n"))
        if if_dork == "yes" or if_dork=="Yes":
            print("Hell, I knew it!!")
            print("Let's count your kind in other places!!!")
            continuing =+1
            move = str(input("Move: 'Left', 'Right', 'Front', 'Down'\n"))
        elif if_dork== 'no' or if_dork=='No':
            print("Suspicious 'Non'Dork!")
            print("Let's count in other places!!!")
            move = str(input("Move: 'Left', 'Right', 'Front', 'Down'\n"))
        else:
            endo()
    history.append(f"Move: {move}")
    return [move, continuing]
                    
#function to end the game
def endo(continuing):
    end = str(input("Are you tired?\n"))
    if end== 'Yes' or end=='yes':
        print("DONE!")
    else:
        end1 = str(input("You want to become a dork?\n"))
        print('You: Oh yeaaah, i doooo')
        print('Well, enjoy')
    print(f"Dorks counted: {continuing}")
    history.append("End")
    return continuing
    


#the game itself

#Just funny thing bc python thinks that this is incorrect
# if start == "YEEAAAH":
#     startf()
#     if startf()[1] == 'Right' or startf()[1] == 'Left' or startf()[1]== 'Down' or startf()[1]=='Front':
# 	    middlef(middlef(startf(start)[0]))[0]
# 	    while True:
#             if middlef(middlef()[0])[0] == 'Right' or middlef(middlef()[0])[0] == 'Left' or middlef(middlef()[0])[0]== 'Down' or middlef(middlef()[0])[0]=='Front':
#                 middlef(middlef)
#             else:
#                 endo(middlef(middlef()[1]))
#                 break
#     else:
#         endo(middlef(startf()[0]))
# else:
#     print("Cricket sound...")
#But this one is cool
if start == "YEEAAAH":
    startf()
    if startf()[1] == 'Right' or startf()[1] == 'Left' or startf()[1]== 'Down' or startf()[1]=='Front':
            middlef(middlef(startf(start)[0]))[0]
            while True:
                if middlef(middlef()[0])[0] == 'Right' or middlef(middlef()[0])[0] == 'Left' or middlef(middlef()[0])[0]== 'Down' or middlef(middlef()[0])[0]=='Front':
                    middlef(middlef)
                else:
                    endo(middlef(middlef()[1]))
                    break
    else:
        endo(middlef(startf()[0]))
else:
    print("Cricket sound...")