contactCheck={}

class Person : 
    def __init__(self,name, age, gender,dob, ):
        self.name=name
        self.age=age
        self.gender=gender
        self.dob=dob
    def getdeatils(self):
        print('Name:',self.name, 'Age:',self.age,'Gender:', self.gender,'DOB:', self.dob)

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
        self.conatctdeatils=contactdeatils
    def getdeatilsemp(self):
        print('Designation:',self.designation,'Email:', self.email,'Salary:', self.salary,'ContactNumber: ',self.conatctdeatils.number)
        
def getDetails(id,employees):
    for emp in employees: 
        if(emp==1) : 
            continue
        if (emp.id==id) : 
            emp.getdeatils()
            emp.getdeatilsemp()

     
contactCheck={}

def create_employee(id,name,age,gender,dob,designation,expn,salary,email,number, address):
        
        i = list(contactCheck.keys())
        if number in i : 
            print('Error: Number already exists')
            return(1)
            
        else : 
            cont= ContactDetail(number, address)
            contactCheck[number]=cont
            emp=Employee(id,name,age,gender,dob, designation,expn,salary,email,cont)
            return(emp)
        

emp1 = create_employee(1,"Ram",22,"Male",12,"Manager","4yrs","40k","ram@gmail.com",7162517283,"Mysuru")
emp2 = create_employee(2,"Raj",32,"Male",2,"TL","5yrs","50k","raj@gmail.com",9876543211,"Bengaluru")
emp3 = create_employee(3,"Rita",25,"FeMale",16,"Manager","6yrs","60k","ram@gmail.com",9876543212,"Mumabi")

# print(emp2)
employees=[emp1,emp2,emp3]
print(getDetails(2,employees))