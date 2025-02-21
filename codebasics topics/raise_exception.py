class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg 
    
    def handle(self):
        print("accident occured, take detour")
        
try:
    raise Accident('crash between 2 buses')
except Accident as e:
    e.handle()
    

def process_file():
    try:
        f=open("D:\\data\input.txt","r")
        x=1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up the file")
        f.close()

process_file()