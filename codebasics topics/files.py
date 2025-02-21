"""
Create a new file and write to it 

reading file line by line

file open modes 

with statement"""

# write to file 
f=open("D:\\data\\funny.txt","a") # \\ denotes path and \ has some special meaning here

# write overwrites old content
f.write("I Love Python\nI Love javascript\nI love React, node js")
f.close() # closes opened file 

"""
w- overwrites old content 
a- doesn't remove the old content and appends new content to it"""
