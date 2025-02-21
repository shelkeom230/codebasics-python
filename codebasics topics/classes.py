# classes and objects 
class Human:
    def __init__(self, n, o):
        self.name = n 
        self.occupation = o 
    
    def do_work(self):
        if self.occupation=="tennis player":
            print (self.name," plays tennis")
        elif self.occupation=="actor":
            print (self.name," shoots a film")
    
    def speaks(self):
        if self.occupation=="tennis player":
            print (self.name," says i love tennis")
        elif self.occupation=="actor":
            print (self.name," says i love acting")

if __name__=="__main__":
    tom=Human("tom cruise","actor")
    tom.do_work()
    tom.speaks()