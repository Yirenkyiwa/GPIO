#printing the length of strings
from functools import *
names = ["sam", "john", "james"]
map(len, names)
def sqr(x):
    return x ** 2
print(list(map(sqr, map(len,names))))

#printing old ages from a list
def is_old(x):
    return x > 30
ages = [22, 25, 29, 34, 56, 24, 12]
print(list(filter(is_old, ages)))

#printing young ages from a list
def is_young(x):
    return x < 30
ages = [22, 25, 29, 34, 56, 24, 12]
print(list(filter(is_young, ages)))

#using classes
class person:
    
    def _init_(self,age):
        self.age = age
    
    def get_age(self,age,name):
        return self.age
        return self.name
    
Michael = person()
#Michael.age=23
Michael.get_name=input("Enter name: ")
Michael.get_age=input("Enter age: ")
print(Michael.get_name,"is", Michael.get_age, "years old")

#splitting of a sentence into words
nice="The quick brown fox jumps over the lazy dog"
words=nice.split()
print(words)

#printing the length of words in a sentence
wonder=[len(word) for word in words if word !="fox"]
print(wonder)

#printing out positive numbers from a list
numbers = [-5,6,50,-12,65,34.67,-23.5,45.6]
for p in numbers:
    if p >=0:
        print(p)
    if p%2==0:
        print(p)
        
#printing even numbers from a list 
num = [3,5,7,8,6.56,12.9]
for a in num:
    if a%2==0:
        print(a)
    if p%2==0:
        print(p)
 #printing even numbers from a list in a list form 
digits = [3,7,8,94,4.8]
num3=[n for  n in digits if n%2==0]
print(num3)

items = [1, 2, 3, 4, 5]
squares = map((lambda x: x ** 2), items)
print(list(squares))

#using is_even function to return odd numbers from a list
def is_even ():
    q=[1,56,234,87,4,76,24,69,90,135]
    marie=[m for m in q if m%2==1]
        #if m%2==1:
    print("The odd numbers from the list are: ",marie)

is_even()

#using the odd function to return odd numbers from a list
def is_odd ():
    r=[1,56,234,87,4,76,24,69,90,135]
    good=[s for s in r if not s%2==0]
        #if s%2==1:
    print("The odd numbers are: ",good)

is_odd()

#using fold 
total = reduce(lambda item, running_total: item + running_total,nice)
print(total)

#using fold  to add numbers
total_2 = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print(total_2)

#joining strings
def join_strings ():
    words = ["hello", "world"]
    helloworld = "*".join(words)
    return helloworld
print(join_strings())

words = ["hello", "my", "name", "is", "Sam"]
for win in words:
    okay = win.upper(), len(win)
    print(okay)




   
 