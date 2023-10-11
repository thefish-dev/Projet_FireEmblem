class File:
    
    def __init__(self, content: list):
        self.content = content
    
    def est_vide(self):
        return self.content == []
    
    def __str__(self):
        return str(self.content)
    
    def enfiler(self, element):
        self.content.insert(0, element)
            
    def regarder_tete(self):
        old = self.defiler()
        print(old)
        self.enfiler(old)
    
    def defiler(self):
        if not self.est_vide(): return self.content.pop(-1)
        else: return None
    
    def inverser(self):
        if not self.est_vide():
            element = self.defiler()
            self.inverser()
            self.enfiler(element)