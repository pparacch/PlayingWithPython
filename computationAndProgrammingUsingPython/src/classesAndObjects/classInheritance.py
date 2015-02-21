import datetime

class Person(object):
    """Person -> object"""
    def __init__(self, name):
        """create a person instance with the provided name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(" ")[-1]

    def getLastName(self):
        """return the last name of this person"""
        return self.lastName
        
    def setBirthday(self, day, month, year):
        """Set the birthday of this person"""
        self.birthday = datetime.date(year, month, day)
    
    def getAge(self):
        """return age of this person"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """override < behaviour"""
        if self.lastName == other.lastName:
            return self.name < other.name
        else:
            return self.lastName < other.lastName
    
    def __str__(self):
        """Override printing behaviour"""
        return self.name + ", " + self.lastName


##Try out our base class Person
#me = Person("PierLorenzo Paracchini")
#print me
#print me.getLastName()

#me.setBirthday(4, 10, 1971)
#print me.getAge()

#her = Person("Ingunn Ellingsen")
#print her.getLastName()

#plist = [me, her]

#for p in plist: print p

#plist.sort()
#for p in plist: print p

class MITPerson(Person): #inheritance from Person class
    nextIdNum = 0 #class variable
    
    def __init__(self, name):
        Person.__init__(self, name) #initialize the person attibutes
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other): #Override the sorting behaviour for MITPerson
        return self.idNum < other.idNum
    
    def __str__(self):
        return "%s, %s [%d]" % (self.name, self.lastName, self.idNum)


#p1 = MITPerson("Eric")
#p2 = MITPerson("John")
#p3 = MITPerson("John")
#p4 = MITPerson("Vibiane")
#p5 = Person("Ali Baba")

#print p1
#print p5
#
#print "p1 < p4", p1 < p4
#
#mlist = [p2,p4,p3,p1]
#for m in mlist: print m
#
#mlist.sort()
#for m in mlist: print m

#print p4 < p5 #Raise an error cause Person behave differently from MITPerson

##Buid up the hierachy introducing Student(s)

class Student(MITPerson):
    pass #Studen has exactly the same attributes/ behaviour as MITPerson

class UG(Student):
    def __init__(self, name, classYear):
        Student.__init__(self, name)
        self.classYear = classYear
        
    def getClassYear(self):
        return self.classYear

class TransferStudent(Student):
    pass

class Grad(Student):
    pass #same as a Student

def isStudent(obj):
    return isinstance(obj, Student) #includes UG, Grad, TransferStudent
    
s1 = UG("Fred", 2016)
s2 = Grad("Angela")
s3 = TransferStudent("Pippo")

p1 = Person("Pier Lorenzo Paracchini")
m1 = MITPerson("Eric")

print isStudent(s1)
print isStudent(s2)
print isStudent(s3)
print isStudent(p1)
print isStudent(m1)
