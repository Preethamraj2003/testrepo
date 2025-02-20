contactCheck={}

class Person : 
    def __init__(self,name, age, gender,dob, ):
        self.name=name
        self.age=age
        self.gender=gender
        self.dob=dob

class ContactDetail:
    def __init__(self, number, address):

        self.number=number
        self.address=address
        

class Employee(Person): 
    def __init__(self,id, name, age, gender, dob, designation, expn, salary, email):
        super().__init__(name, age, gender, dob)
        self.id=id
        self.designation = designation
        self.expn=expn
        self.salary=salary
        self.email=email
        

    
contactCheck={}

def CheckNumber(number, address):
        
        i = list(contactCheck.keys())
        if number in i : 
            print('Error: Number already exists')
        else : 
            cont= ContactDetail(number, address)
            contactCheck[number]=cont
            print("Object created")
# obj = Employee('prg', 22, "M", 12, "Intern", 1,'40k', 'prg@gmail.com')
CheckNumber(67876545678,"Bengaluru")
CheckNumber(7876545678,"Bengaluru")
CheckNumber(7876545678,"Bengaluru")