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
    def __init__(self,id, name, age, gender, dob, designation, expn, salary, email,contactdeatils):
        super().__init__(name, age, gender, dob)
        self.id=id
        self.designation = designation
        self.expn=expn
        self.salary=salary
        self.email=email
        self.contactdetails=contactdeatils

    def getName(self): 
        print(self.name)

def getDeatils(contactnumber,obj):
    for object in obj : 
        if object.contactdetails.number==contactnumber:
            object.getName()
        

cont1=ContactDetail(9876545673,"Mysuru")
cont2=ContactDetail(898765434,"Bengaluru")
obj1 = Employee(1,'Raj', 22, "M", 12, "Intern", 1,'40k', 'prg@gmail.com',cont1)
obj2 = Employee(2,'Ram', 22, "M", 12, "Intern", 1,'40k', 'prg@gmail.com',cont2)

obj=[obj1,obj2]
getDeatils(9876545673,obj)