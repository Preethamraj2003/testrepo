class Subjects :
    def __init__(self, subject_name,marks) :
        self.subject_name=subject_name
        self.marks=marks
    
    
class Semester : 
    def __init__(self,sem_no,subjects):
        self.sem_no =sem_no
        self.subjects=subjects
        
class Student : 
    def __init__(self,id,name,semester):
        self.id = id
        self.name = name
        self.semester = semester

def getMarks(id, sem=None, stud=None):
    student = None
    for s in stud:
        if s.id == id:
            student = s
            
    if student:
        if sem:
            semester = sem
        else:
            semester = student.semester[-1]  

        print(f"Marks for {student.name} in semester {semester.sem_no}:")
        for subject in semester.subjects:
            print(f"{subject.subject_name}: {subject.marks}")
    else:
        print(f"Student with ID {id} not found.")    



sub1 = Subjects("M1",90)
sub2 = Subjects("M2",95)
sub3 = Subjects("M3", 85)

sem1 = Semester(1,[sub1,sub2])
sem2 = Semester(2,[sub2,sub3])

Stud1 = Student(11,"Ram",[sem1,sem2]) 
Stud2 = Student(12,"Raj",[sem1,sem2])

stud=[Stud1,Stud2]

getMarks(11,sem1,stud)