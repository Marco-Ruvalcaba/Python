# Classes Exercise

class Person:
    def __init__(self, firstname, surname, age, height, weight):
        self.Firstname = firstname
        self.Surname   = surname
        self.Age       = age
        self.Height    = height
        self.Weight    = weight

    def ShowData(self):
        print( "---------------------------" )
        print( "Firstname:    ", self.Firstname )
        print( "Surname:      ", self.Surname   )
        print( "Complete name:", self.Firstname + " " +self.Surname   )
        print( "Age:          ", self.Age       )
        print( "Height:       ", self.Height    )
        print( "Weight:       ", self.Weight    )
        print( "" )


"""
class Pet:
    def __init__():
"""
