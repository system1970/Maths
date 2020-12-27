from variables import *

class Expression(str):
    def superscript(self,power):
        return self.translate(str(power))

    def subscript(self,term):
        return self.translate(str(term))

    def expander(self,power):
        return f"{self} + {self.superscript(str(power))} + \N{SUPERSCRIPT MINUS}" if power < 0 else self + self.superscript(str(power)) if power > 1 else self

    def prettify(self,*args):
        indices = [i for i, x in enumerate(args) if x == "^"]
        for index in indices:
            indexIterator = index
            while not self[indexIterator].isnumeric() and indexIterator<len(str):
                if self[indexIterator].isnumeric():
                    self.expander(self,self[indexIterator])
                indexIterator+=1
        for i in args:
            self = self.replace(i[0],i[1])
        return self
