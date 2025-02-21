# read json data using loads 

f=open("D://data/book.txt","r")
s=f.read()
print(s) 
print(type(s))  # str 

import json 
book= json.loads(s) # converts string to dict 
print(type(book))
print(book)

# print details of each person 
for person in book:
    print(book[person])