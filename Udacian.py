class Udacian:
    def __init__(self,name,city,enrollment,nanodegree,status):
        self.name =name
        self.city=city
        self.enrollment=enrollment
        self.nanodegree=nanodegree
        self.status=status
    def print_udacian(self):
        print(self.name+" is enrolled in " + self.city+ " studying " + self.nanodegree + " in sat am with ms.lujain , he/she is " + self.status)


Abdulrahman = Udacian("Abdulrahman","Riyadh","FSND","Full web stack development","On track")
Abdulrahman.print_udacian()