lec={}
choose=0
class Lecture():
    def __init__(self,lecname,professor,limit,place) :
        self.name =lecname
        self.professor =professor
        self.limit =limit
        self.place =place

    def changeLimitOfStudent(self,new_limit):
        self.limit=new_limit
    def changePlace(self,new_place):
        self.place=new_place
    def printInfo(self):
        print("Professor : ", self.professor)
        print("Number of students : ", self.limit)
        print("Place: ",self.place)
class seasonLecture (Lecture):
    def __init__(self,lecnmae,professor,limit,place,season):
        self.season=season
        Lecture.__init__(self,lecname,professor,limit,place)
    def changeSeason(self,new_season):
        lec[lecname].season=new_season
    def printInfo(self):
        super().printInfo()
        print("Season : ",self.season)
            
while True:
    print("********************************")
    print("           Time table           ")
    print("********************************")
    print("  1.Open new class")
    print("  2.Change limit of students")
    print("  3.Change calssroom")
    print("  4.Print lecture info")
    print("  5.Change season")
    print("  6.Exit")
    print("********************************")
    print()
    choose=int(input("Choose >>"))
    if choose==1:
        class_type=input("Are you opening lecture or season lecture? :")
        lecname=input("Lecture name : ")
        professor=input("Professor : ")
        limit=int(input("Limit of student :"))
        place=input("Place : ")
        if class_type=='season':
            season=input("Season:")
            lec[lecname]=seasonLecture(lecname,professor,limit,place,season)
        else:
            lec[lecname]=Lecture(lecname,professor,limit,place)
    elif choose==2:
        lecname=input("Enter lecture name : ")
        new_limit=int(input("Enter new limit of students : "))
        lec[lecname].changeLimitOfStudent(new_limit)
    elif choose==3:
        lecname=input("Enter lecture name : ")
        new_place=input("Enter new classroom :")
        lec[lecname].changePlace(new_place)
    elif choose==4:
        lecname=input("Enter lecture name : ")
        lec[lecname].printInfo()
    elif choose==5:
        lecname=input("Enter lecture name : ")
        new_season=input("Enter new season : ")
        lec[lecname].changeSeason(new_season)
    elif choose==6:
              break
