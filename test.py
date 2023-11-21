class File :
    def __init__(self):
        self.list=list

    def enfile(self, element):
        self.list.append(element)

    def defile(self):
        return self.list.pop(0)

    def est_vide(self):
        return len(self.list) == 0

   