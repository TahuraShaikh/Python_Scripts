class Hospital:
    Hospital="Get Well Care"
    def __init__(self,patient_name,age,visit,appointment_num):
        self.name=patient_name
        self.age=age
        self.visit=visit
        self.num=appointment_num

    @staticmethod                     #Used as a message to greet
    def greet():
        print("\nWelcome to Get Well Care\n")

    def get_info(self):
        print(f"Patient name : {self.name}")
        print(f"Age of {self.name} is: {self.age}")
        print(f"This is patient's {self.visit}")
        with open("Record.txt", "a") as f:                 #patient name appended in "record" text file.
            f.write(f"{self.name}\n")

    def appoint_info(self):
        if (self.num > 0 and self.num<20):                     # will check for appointment nnumbers between 1 to 20
            print(f"{self.name} you can visit the Doctor at prescribed time.")
            self.num=self.num-1
        else:
            print("Sorry there are no appointment's available")

    def cancel_appoint(self):
        pass


p1=Hospital("Susan",35,"First Visit",1)
p1.greet()
p1.get_info()
p1.appoint_info()

p2=Hospital("Aron",29,"Second Visit",18)
p2.greet()
p2.get_info()
p2.appoint_info()

p3=Hospital("Andy",33,"First Visit",21)
p3.greet()
p3.get_info()
p3.appoint_info()




