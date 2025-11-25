#Kuznecov Vadim
#MODIFIED

'''
#Создать два пустых списка letters и numbers
'''
letters = []
numbers = []
print(f"1st task: letters={letters}, numbers={numbers}")
'''
# Пройтись циклом for по кортежу data_tuple, добавить 
все строки в список letters, а всё остальное в number
'''
data_tuple = ('u', 'o', 6.13,  True,'y', '1', 'e', 'r', 'a', ' ', 'w', 'o', 'h', ' 3', 'e', 'n', 'o', ' ', 'y', 'n', 'a', ' ', 'o', 'l', 'l', 'e', 'h')
data_tuple=list(data_tuple)
for i in data_tuple:
    try:
        if type(i)==bool:
            numbers.append(bool(i))
        elif type(i)==float:
            numbers.append(float(i))
        else:
            numbers.append(int(i))

    except ValueError:
        if i==str(i):
            letters.append(i)
data_tuple=tuple(data_tuple)
print(f"\n2nd task: {letters}")
print(numbers)

'''
#Из списка numbers удалить число 6.13 и переместить
True в конец списка letters, затем вставить число 
2 между 3 и 1
'''        
numbers.remove(6.13)
letters.append(numbers.pop(0))
numbers.insert(1, 2)
print(f"\n3rd task: {letters}")
print(numbers)

'''
#Отсортировать numbers, реверсировать letters и 
изменить пару букв в letters
'''

numbers.sort()
letters.reverse()
letters[-1] = 'z'
letters[-2] = 'x' 
print(f"\n4th task: {letters} \n{numbers}")
