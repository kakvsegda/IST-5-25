#Kuznecov Vadim

print("Hello, this program will compute average temperature of all given cities and villages")
i=0
n=4
State = ''
dataset = {}

#Counts up to 5 cities, and then asks State
city = str(input("Enter the city/village name: \n"))
while i<=n:
    temperature = int(input(f"Enter the temperature of {city}: \n"))

    dataset[f"{city}"] = temperature
    #Intended to stop the count of cities and ask the user for calculations
    if i==n:
        State=str(input("Do you want to start the computation? ('Yes' or 'No')\n"))
        if State=='Yes':
            print("Starting calculations")
        elif State=='No':
            #The number of cities that will be needed to enter in order to provoke the State clarification
            j=3
            n+=j
            j+=2
        else:
            State=str(input("Only 'Yes' or 'No' count, please provide one of the requested answers: \n"))

    

    #To prevent duplication of cities in dataset we use anti_dup as a filter in a for loop
    if i!=n:
        anti_dup = str(input("Enter another city/village name: \n"))
        for key in dataset.keys():
            while anti_dup == key:
                anti_dup=str(input("Please enter the city/village that is not already on the list: \n"))
    i+=1
    city = anti_dup

#Calculations
cities = list(dataset.keys())
print(f"The average temperature of {', '.join(cities)}:", sum(list(dataset.values()))/len(dataset))
print("Calculation is finished")
print("Thanks for using us, have a good day!")