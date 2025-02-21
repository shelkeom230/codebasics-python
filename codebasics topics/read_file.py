# read the contents of file line by line and count no. of words in each line 

# write line and no. of words in a new file 

f=open("D:\\data\\funny.txt","r")
f_out=open("D:\\data\\funny_wc.txt","w")

for line in f:
    token=line.split(' ')
    f_out.write("word count "+str(len(token))+" "+line)
f.close()
f_out.close()


with open("D:\\data\\funny.txt","r") as f:
    print(f.read())
print(f.closed)
"""
file reading modes 
r - read only mode , throws error if file does not exists

w - write only mode , if file doesn't exists , then it will create a new one. it overwrites the file contents.

r+ - opens file for reading and writing both 

w+ - opens file for reading and writing both, if file doesn't exists, then it will create a new file, if exists, then it overwrites the content

a - open file for append mode, whatever you writen gets appended at the end of the file witout removing anything from the file 
"""

"""

with statement 

with open("D:\\data\\omkar.txt","w") as f:
    f.write() 

we need not to close the file in this mode 

"""