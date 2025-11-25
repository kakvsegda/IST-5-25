#1st task
class Animal:
    weig=[]
    animo=[]
    def __init__(self, name, size, weight, foodchain_role):
        self.n = name
        self.s = size
        self.w = weight
        self.r = foodchain_role
        Animal.animo.append(name)
        Animal.weig.append(weight)
        
    def calling(self):
        return f'The {self.n} is a {self.s} animal, weighing at {self.w}, {self.r}'


class Mammals(Animal):
    def __init__(self, name, size, weight, foodchain_role, blooded):
        super().__init__(name, size, weight, foodchain_role)
        self.b = blooded
        
    def callf(self):
        print(self.n)
        if self.b=='warm-blooded':
            fur=input('Does it have a fur? (Y/n): ')
            if fur=='Y':
                self.b='mammals'
            else:
                milk = str(input(f'Do mothers of {self.n}s feed their newborns with a milk? (Y/n): '))
                if milk=='Y':
                    self.b='mammals'
                else:
                    return 'Stop kidding'
        return super().calling()+f' and belongs to {self.b}.'


class Reptiles(Animal):
    def __init__(self, name, size, weight, foodchain_role, blooded):
        super().__init__(name, size, weight, foodchain_role)
        self.b=blooded
    
    def callf(self):
        print(self.n)
        if self.b=='cold-blooded':
            fur=input('Does it have scales or scutes? (Y/n): ')
            if fur=='Y':
                self.b='reptiles'
            else:
                milk = str(input(f'Do {self.n}s have lung respiration? (Y/n): '))
                if milk=='Y':
                    self.b='reptiles'
                else:
                    return 'Stop kidding'
        return super().calling()+f' and belongs to {self.b}.'

#Test of 1st task
bear = Mammals("bear", "1 to 3 meters tall (if standing)", "150kg", "omnivore", "warm-blooded")
print(bear.callf())
crocodile = Reptiles('crocodile', '2 to 6(!) meters in length', 'roughly 250kg', 'carnivore', 'cold-blooded')
print(crocodile.callf())



#2nd task
class Zoo_show(Animal):
    print("Entering Zoospectacles...")
    def _Promotion(self, animal, weight):
        typ=''
        responce=str(input("Welcome to our newly opened Zoo-show!\nWe are offering you the best deals in the entire city: We have 3 tier tickets all according to the seat placements and visability for better exeprience. Do you want to visit our unforgettable spectacles? (Y/n):"))
        if responce == 'Y':
            typ = str(input("We have three shows planned these weekends: Bird show, Grand opening, and Dolphin dazzle!\n Which one do you want to see?\n(bird/grand/dolphin):"))
            if typ == "bird":
                responce=str(input("Join us at the Zoo_spectacles Bird Show, where intelligent and colorful birds demonstrate their amazing natural talents. Would you like to get a ticket and see them in action?\n(Y/n):"))
                if responce=="Y":
                    print("We got 3 tier ticket which allows you to book any non-booked seats, and in opposite to lower ones, you can freely choose the ones from the first raw (people on them by statistics get the best exeprience during it!); the second tear allows you to choose any left seat from the auditorium, still close to the main scene though, maybe if you want, even the balcony; and the first-tear are whatever is left!\nThe prices: 3rd tear - 49$\n 2nd tear - 46$\n 3rd tear 38$\n")
                    tk=int(input("Which one suits you the best? \n(1/2/3?):"))
                    if tk!=3 and tk!=2 and tk!=1:
                        return [0, 0, 0]
                    else:
                        quanti=int(input(f"How many of them would you want to buy?\n"))
                        return [tk, quanti, 'Bird show']
                else:
                    return 0
            elif typ == "grand":
                responce == str(input(f"The headliners of the show is a {weight[-1]} weighing, jaggling {animal[-1]} with riding the bicycle {animal[0]}! This time we give the chance to the new starters to perform and some of them are locals from this very city - and trust me, they got the talent. In overall, show will go on for 2 hours with your drinks and food permitted in.\nDo you want to buy a ticket? \n(Y/n):"))
                if responce=='Y':
                    print("We got 3 tier ticket which allows you to book any non-booked seats, and in opposite to lower ones, you can freely choose the ones from the first raw (people on them by statistics get the best exeprience during it!); the second tear allows you to choose any left seat from the auditorium, still close to the main scene though, maybe if you want, even the balcony; and the first-tear are whatever is left!\nThe prices: 3rd tear - 49$\n 2nd tear - 46$\n 3rd tear 38$\n")
                    tk=int(input("Which one suits you the best? \n(1/2/3?):"))
                    if tk!=3 and tk!=2 and tk!=1:
                        return [0, 0, 0]
                    else:
                        quanti=int(input(f"How many of them would you want to buy?\n"))
                        return [tk, quanti, 'Grand opening']
            elif typ == "dolphin":
                responce == str(input(f"Experience the elegance and playfulness of our dolphins in the Zoospectacles Dolphin Dazzle, as they showcase their incredible tricks and acrobatics. Would you like to get a ticket and see them dazzle you live?\n(Y/n):"))
                if responce=='Y':
                    print("We got 3 tier ticket which allows you to book any non-booked seats, and in opposite to lower ones, you can freely choose the ones from the first raw (people on them by statistics get the best exeprience during it!); the second tear allows you to choose any left seat from the auditorium, still close to the main scene though, maybe if you want, even the balcony; and the first-tear are whatever is left!\nThe prices: 3rd tear - 49$\n 2nd tear - 46$\n 3rd tear 38$\n")
                    tk=int(input("Which one suits you the best? \n(1/2/3?):"))
                    if tk!=3 and tk!=2 and tk!=1:
                        return [0, 0, 0]
                    else:
                        quanti=int(input(f"How many of them would you want to buy?\n"))
                        return [tk, quanti, 'Dolphin dazzle']
                else:
                    return [0, 0, 0]
            else:
                return [0, 0, 0]
        else:
            return [0, 0, 0]
        
    def __init__(self):
        prom = self._Promotion(Animal.animo, Animal.weig)
        self.tt=prom[0]
        self.qt=prom[1]
        self.show=prom[2]
        

    def buying(self):
        if self.qt>1:
            return f"You bought {self.qt} of {self.tt} tier tickets on the {self.show}."
        elif self.qt==1:
            return f"You bought {self.qt} of {self.tt} tier ticket on the {self.show}."
        elif self.qt==0 and self.tt==0:
            return "Okay, folk, get here when you will be sure.\nNo tickets were bought"
        else:
            return "-Was nice talking to you, but let me earn my bread"
            
        
#Yep.. nice, i wrote everything for just one show and now i see that there has to be several of them


#Test of 2nd task
me = Zoo_show()
print(me.buying())




#Kuznecov Vadim
