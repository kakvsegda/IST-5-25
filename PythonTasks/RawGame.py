#Kuznecov Vadim
#Counting Dorks v0.1(Abstract game with many bags, raw)
print("WANNA COUNT SOME DORKS???>><<???")
start = str(input("Whisperer: Say 'YEEAAAH' \n"))
history=[]
play=1

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
            play=0
            return
    move = str(input("Move: 'Left', 'Right', 'Front', 'Down'\n"))

    history.append(f"Move: {move}, counted: ")
    history.append(continuing)
    print(history)
    return [move, continuing]
    
#func to count after the startf 
def middlef(continuing):
    continuing1=int(input("How many more Dorks do you see?!?!\n"))
    continuing=+continuing1
    history.append(f"Counted: {continuing},")
    try:
        continuing1 >= 15
        print("Lowkey a lot of them \nLet's go further!")
    except:
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
            play=0
            return
        
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
            play=0
            return
            
    history.append(f" .Move: {move}, counted")
    history.append(continuing)
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
if start == "YEEAAAH":
    startf()
    print("First stage passed")
    print(history)
    if history[-1] > 0:
        while play:
            if history[-1] > 0:
                middlef(history[-1])
                print("Second stage passed")
            else:
                play=0
    else:
        endo(history[-1])
        print("The end")
else:
    print("Cricket sound...")
    print(f"History: {history}")
