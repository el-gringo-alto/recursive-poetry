from time import sleep
from os import system

# enter name of poem
system('clear')
file = input("poem: ")
file = file.lower()

# poem to list
with open(file + '.txt', 'r') as f:
    text = [line.strip() for line in f]
    
# print poem
def poem():
    for i in range(len(text)):
        print(text[i])
        sleep(2.5)         
    poem() # recursion

system('clear')
    
poem() # initialize
