
class Thing:
    normalvar = 5
    __privatevar = -1
    
    def GetVal(self):
        return self.__privatevar
    def SetVal(self, newval):
        self.__privatevar = newval


thing = Thing()
print(something.GetVal())
print("trying to access privatevar directly")
thing.__privatevar = 420
print(something.GetVal())  # still prints -1

print("doing it properly")
thing.SetVal(69)
print(something.GetVal())

print("printing privatevar directly")
print(thing.__privatevar)   # still 420 from earlier


