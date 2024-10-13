class student:
    def __init__(self, studentnummer, name):
        self.studentnummer = studentnummer
        self.name = name


    def __str__(self):
        return f"{self.studentnummer} is jouw nummer"

Max = student(123456789, "max")

print(Max)
