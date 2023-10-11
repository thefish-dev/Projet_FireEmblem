from random import shuffle
class File_dattente:
    
    def __init__(self, n: int,file=[]):
        self.n=n
        self.file=File(self.ouverture(n))
        self.numero=1
        while not self.file.est_vide():
            self.passage()
    def __str__(self) :
        return str(self.file)
    
    def ouverture(self, n: int):
        l=[]
        for i in range (1,n+1) :
            l.append(i)
        shuffle(l)
        return l
    
    def passage(self):
        
        a=self.file.defiler()
        if a==self.numero :
            self.numero+=1
        
        else :
            self.file.enfiler(a)
                    
                    