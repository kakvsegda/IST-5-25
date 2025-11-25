from time import sleep #to make some stops
from string import ascii_letters #alphabet
from random import shuffle #shuffling

#animation func
def text_animation(s: str, n=2, r=7):
    #preparations
    alphabet = ascii_letters
    alphabet_list = list(alphabet)
    shuffle(alphabet_list)

    limiter=0 #limiter allows to save energy on shuffle
    output=""
    for i in s:
        for j in alphabet_list[0:r]:
            print(f"\r{output}{j}", end="")
            sleep(0.02) 
        print(f"\r{output}{i}", end="")
        output += i
        if limiter%n==0:
            shuffle(alphabet_list)
        sleep(0.045)
    print()
    
    return output

if __name__=="__main__":
    text_animation("Test1, Test2, Test3")
