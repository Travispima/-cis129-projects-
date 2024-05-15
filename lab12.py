#Travis Greenberg
#5/15/2024
#Module 12 Lab
#Class Pet


#main module
def main():
    #declare input variables
    inputName = ''
    inputType = ''
    inputAge = 0

    #class variable to hold a pet
    animal = Pet()

    #create a pet object
    animal = Pet(inputName, inputType, inputAge)

    #get values for a pet
    print("Enter a pet name: ")
    inputName = input()
    animal.setName(inputName)

    print("Enter a pet type: ")
    inputType = input()
    animal.setType(inputType)

    print("Enter a pet age: ")
    inputAge = int(input())
    animal.setAge(inputAge)

    #show values for this pet
    print("The pet name is", animal.getName())
    print("The pet type is", animal.getType())
    print("The pet age is", animal.getAge())



class Pet:
    #constructor
    def __init__(self, n='', t='', a=0):
        self.name = n
        self.type = t
        self.age = a 

    #mutators
    def setName(self, n):
        self.name = n
    
    def setType(self, t):
        self.type = t

    def setAge(self, a):
        self.age = a 
    
    #accessors
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getAge(self):
        return self.age
    
if __name__ == "__main__":
    main()
