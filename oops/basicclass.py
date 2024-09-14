class Test:
    def __init__(self,firstname,lastname):
        self.lastName=lastname
        self.firstName=firstname
        
    def __str__(self):
        return self.firstName+' '+self.lastName
        
if __name__=='__main__':        
    t=Test("Harsh","Garg")
    print(t)