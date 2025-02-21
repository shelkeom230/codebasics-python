"""
JSON = JAVASCRIPT OBJECT NOTATIONS

JSON is a data exchange format similar to XML 

e.g) 
JSON 
{
    "name":"tom",
    "address":"1 green street, NY".
    "phone":"2344444"
}

XML 
<name>tom</name>
<address>1 green stree, NY</address>
<phone> 22333333 </phone>

JSON IS LIGHWEIGHT FORMAT THAN XML 

our programs 
1. to create an address book and write some records in it
2. read this address book 
"""

book={}
book["tom"]={
    'name':'tom',
    'address':'1 red street, NY',
    'phone':228282828
}
book['bob']={
    'name':'bob',
    'address':'greater noida',
    'phone':48848383
}

import json 
s=json.dumps(book) #takes in a dict and converts into a string of type json 

# store in a file 
with open("D://data/book.txt","w") as f:
    f.write(s)
    
"""
you can now read this JSON data using any language which supports json such as js , cpp etc.

hence , this is called as data exchange format (i.e exchanging data from python program to js program)
"""
