students = (
    {'name': 'SOFA', 'ORT': 110, 'male': 'f'},
    {'name': 'ALEX', 'ORT': 98, 'male': 'm'},
    {'name': 'LINA', 'ORT': 120, 'male': 'f'},
    {'name': 'TIMUR', 'ORT': 75, 'male': 'm'},
    {'name': 'DIANA', 'ORT': 135, 'male': 'f'},
    {'name': 'ERLAN', 'ORT': 88, 'male': 'm'},
    {'name': 'NURA', 'ORT': 147, 'male': 'f'},
    {'name': 'ALI', 'ORT': 52, 'male': 'm'},
    {'name': 'ZARA', 'ORT': 123, 'male': 'f'},
    {'name': 'OMAR', 'ORT': 101, 'male': 'm'},
    {'name': 'JANA', 'ORT': 111, 'male': 'f'},
    {'name': 'RUSLAN', 'ORT': 67, 'male': 'm'},
    {'name': 'MIRA', 'ORT': 89, 'male': 'f'},
    {'name': 'NURIS', 'ORT': 144, 'male': 'm'},
    {'name': 'LANA', 'ORT': 130, 'male': 'f'},
    {'name': 'DASTAN', 'ORT': 76, 'male': 'm'},
    {'name': 'AYNA', 'ORT': 93, 'male': 'f'},
    {'name': 'BAKT', 'ORT': 105, 'male': 'm'},
    {'name': 'ELINA', 'ORT': 114, 'male': 'f'},
    {'name': 'SAMAT', 'ORT': 83, 'male': 'm'},
    {'name': 'NINA', 'ORT': 134, 'male': 'f'},
    {'name': 'ASLAN', 'ORT': 60, 'male': 'm'},
    {'name': 'GULYA', 'ORT': 99, 'male': 'f'},
    {'name': 'ISLAM', 'ORT': 71, 'male': 'm'},
    {'name': 'RAISA', 'ORT': 149, 'male': 'f'},
    {'name': 'ARSLAN', 'ORT': 41, 'male': 'm'},
    {'name': 'SARA', 'ORT': 126, 'male': 'f'},
    {'name': 'TALGAT', 'ORT': 87, 'male': 'm'},
    {'name': 'AINURA', 'ORT': 138, 'male': 'f'},
    {'name': 'YERLAN', 'ORT': 53, 'male': 'm'},
    {'name': 'ALINA', 'ORT': 117, 'male': 'f'},
    {'name': 'AZAMAT', 'ORT': 109, 'male': 'm'}
)

#Function that specifies whether the inners will be displayed
def dork_definer(nlist=0, *numa):
    university =[]
    college=[]
    military=[]
    to_husband=[]
    for i in numa:
        if i['ORT']>=110:
            university.append(i['name'])
        elif (110>i['ORT']) and (i['ORT']>39):
            college.append(i['name'])
        elif (i['ORT']<40) and (i['male']=='m'):
            military.append(i['name'])
        elif (i['ORT']<40) and (i['male']=='f'):
            to_husband.append(i['name'])
        else:
            print(f"The mistake in key-value{i}")
    su = (university, college, military, to_husband)
    if nlist==1:
        print(f'Students into university: {(", ").join(university)} \nInto college: {(", ").join(college)} \nNowhere but military: {(", ").join(military)} \nNowhere but marry: {(", ").join(to_husband)}')
    return list(su)
    
print(f"{dork_definer(*students)} \n\nOr\n")
dork_definer(1, *students)



#Kuznecov Vadim
