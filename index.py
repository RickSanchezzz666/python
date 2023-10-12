def bubbleSort(students = []):
    leftElem = 0
    rightElem = 0
    for i in range(2, len(students)):
        leftElem = int(students[i - 1][3])
        rightElem = int(students[i][3])
        if (leftElem > rightElem):
            students[i - 1], students[i] = students[i], students[i - 1]

    for i in range(2, len(students)):
        leftElem = int(students[i - 1][3])
        rightElem = int(students[i][3])
        if (leftElem > rightElem):
            bubbleSort(students)

    return students

class Database:
    id = -1
    fname = ''
    lname = ''
    age = 0
    specialty = ''

    @classmethod
    def getNum(self):
        with open('students.csv', 'r') as file:
            num = len(file.readlines()) - 1
        return num

    @classmethod
    def createDatabase(self): 
        with open('students.csv', 'w') as file: 
            file.write('Id,FirstName,LastName,Age,Specialty;\n')
    
    @classmethod
    def addStudent(self, fname = '', lname = '', age = 0, specialty = '', sep = ','):
        with open('students.csv', 'a') as file:
            id = Database.getNum()
            student = sep.join([str(id), fname, lname, str(age), specialty]) + ';\n'
            file.write(student)

    @classmethod
    def readInfo(self):
        with open('students.csv', 'r') as file:
            print('Information about students:\n')
            info = file.readlines()
            for i in range(1, len(info)):
                print(info[i])

    @classmethod
    def findStudent(self, id = -1, fname = '', lname = '', age = 0, specialty = '', sep = ',', age_sign = '='):
        with open('students.csv', 'r') as file:
            students = file.readlines()
            for i in range(1, len(students)):
                students[i] = students[i].split(sep)
                students[i][4] = students[i][4][:-2]
            if(id != -1):
                cases = []
                for i in range(1, len(students)):
                    if(id == int(students[i][0])):
                        cases.append(students[i])
                if(len(cases) != 0 ):
                    print('\nFound students:')
                    for case in cases:
                        print(case)
                else:
                    print('None of students were found!')
                return cases
            if(fname != ''):
                cases = []
                for i in range(1, len(students)):
                    if(fname == students[i][1]):
                        cases.append(students[i])
                if(len(cases) != 0 ):
                    print('\nFound students:')
                    for case in cases:
                        print(case)
                else:
                    print('None of students were found!')
                return cases
            elif(lname != ''):
                cases = []
                for i in range(1, len(students)):
                    if(lname == students[i][2]):
                        cases.append(students[i])
                if(len(cases) != 0 ):
                    print('\nFound students:')
                    for case in cases:
                        print(case)
                else:
                    print('None of students were found!')
                return cases
            elif(age != 0):
                cases = []
                match age_sign:
                    case '=':
                        for i in range(1, len(students)):
                            if(age == int(students[i][3])):
                                cases.append(students[i])
                    case '>':
                        for i in range(1, len(students)):
                            if(int(students[i][3]) > age):
                                cases.append(students[i])
                    case '<':
                        for i in range(1, len(students)):
                            if(int(students[i][3]) < age):
                                cases.append(students[i])
                if(len(cases) != 0 ):
                    print('\nFound students:')
                    for case in cases:
                        print(case)
                else:
                    print('None of students were found!')
                return cases
            elif(specialty != ''):
                cases = []
                for i in range(1, len(students)):
                    if(specialty == students[i][4]):
                        cases.append(students[i])
                if(len(cases) != 0 ):
                    print('\nFound students:')
                    for case in cases:
                        print(case)
                else:
                    print('None of students were found!')
                return cases
                

    @classmethod
    def updateStudent(self, id = -1, sep = ','):
        with open('students.csv', 'r') as file:
            students = file.readlines()
            for i in range(1, len(students)):
                students[i] = students[i].split(sep)
                students[i][4] = students[i][4][:-2]
            if(id != -1):
                case = -1
                for i in range(1, len(students)):
                    if(id == int(students[i][0])):
                        case = i
                if(case != -1 ):
                    lineToChange = 0
                    while lineToChange not in ['1', '2', '3', '4']:
                        print("\nПараметри які можна змінити:\n1. Ім'я\n2. Призвіще\n3. Вік\n4. Спеціальність")
                        lineToChange = input('Введіть номер параметру який хочете змінити: ')
                    print(f'\nСтара інформація: {students[case][int(lineToChange)]}')
                    updatedInfo = input('Введіть нову інформацію: ')
                    students[case][int(lineToChange)] = updatedInfo
                    tempStudents = []
                    tempStudents.append('')
                    num = Database.getNum()
                    for i in range(1, num + 1):
                        tempStudents.append(students[i])
                    Database.createDatabase()
                    for i in range(1, num + 1):
                        Database.addStudent(tempStudents[i][1], tempStudents[i][2], tempStudents[i][3], tempStudents[i][4])
                    print('\nInformation succesfully updated!\n')
                else:
                    print('None of students were found!')
                return case
            else:
                print('Wrong id!')
        
    @classmethod
    def deleteStudent(self, id = -1, sep = ','):
        with open('students.csv', 'r') as file:
            students = file.readlines()
            for i in range(1, len(students)):
                students[i] = students[i].split(sep)
                students[i][4] = students[i][4][:-2]
            if(id != -1):
                case = -1
                for i in range(1, len(students)):
                    if(id == int(students[i][0])):
                        case = i
                if(case != -1 ):
                    tempStudents = []
                    tempStudents.append('')
                    num = Database.getNum()
                    for i in range(1, num + 1):
                        if(i == case):
                            pass
                        else:
                            tempStudents.append(students[i])
                    Database.createDatabase()
                    for i in range(1, num):
                        Database.addStudent(tempStudents[i][1], tempStudents[i][2], tempStudents[i][3], tempStudents[i][4])
                    print('\nStudent succesfully deleted!\n')
                else:
                    print('None of students were found!')
                return case
            else:
                print('Wrong id!')

    @classmethod
    def sortStudents(self, sep = ','):
        with open('students.csv', 'r') as file:
            students = file.readlines()
            for i in range(1, len(students)):
                students[i] = students[i].split(sep)
                students[i][4] = students[i][4][:-2]
            newStudents = bubbleSort(students)
            num = Database.getNum()
            Database.createDatabase()
            for i in range(1, num + 1):
                Database.addStudent(newStudents[i][1], newStudents[i][2], newStudents[i][3], newStudents[i][4])
            print('\nStudents sorted by age succesfully!\n')

    @classmethod
    def getStats(self, sep = ','):
        studentSpecialties = []
        with open('students.csv', 'r') as file:
            students = file.readlines()
            for i in range(1, len(students)):
                students[i] = students[i].split(sep)
                students[i][4] = students[i][4][:-2]
                for i in range(len(studentSpecialties)):
                    if(students[i][4] == studentSpecialties[i]):
                        pass
                    else:
                        studentSpecialties.append(students[i][4])
            for j in range(len(studentSpecialties)):
                for i in range(1, len(students)):
                    if(students[i][4] == studentSpecialties[j]):
                        studentSpecialties[j].append(int(students[i][3]))
            print(studentSpecialties[1][2])
            
                        

    def __init__(self, id = 0, fname = '', lname = '', age = 0, specialty = ''):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.specialty = specialty
    
Database.createDatabase()
Database.addStudent('Rick', 'Sanchez', 70, 'Science')
Database.addStudent('Vlad', 'Melnik', 18, 'Junkie')
Database.addStudent('Petro', 'Krakiw', 31, 'Trucker')
Database.addStudent('Sanya', 'Bulkin', 27, 'VideoMaking')
Database.addStudent('Vova', 'Zelenskiy', 45, 'Government')
Database.readInfo()
Database.findStudent(lname='Bulkin')
Database.findStudent(age=20, age_sign='>')
Database.updateStudent(id=3)
Database.readInfo()
Database.deleteStudent(id=1)
Database.readInfo()
Database.sortStudents()
Database.readInfo()

# additional
Database.createDatabase()
Database.addStudent('John', 'Doe', 22, 'Science')
Database.addStudent('Alice', 'Smith', 25, 'Science')
Database.addStudent('Bob', 'Johnson', 30, 'Science')
Database.addStudent('Vova', 'Zelenskiy', 45, 'Programming')
Database.addStudent('Eve', 'Adams', 21, 'Science')
Database.addStudent('Charlie', 'Brown', 28, 'Programming')
Database.readInfo()
Database.getStats()