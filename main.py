import pickle

class Doctors():
    def __init__(self, surname=0,name=0,patronymic=0,post=0,experience=0,academic_title=0, address=0,number=0):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.post = post
        self.experience = experience
        self.academic_title = academic_title
        self.address = address
        self.number = number

    def treat(self):
        print("Doctor" + self.surname + "treats a patient")

    def inspect(self):
        print("Doctor" + " " + self.surname + " " + "examines the patient")

    def __del__(self):
        print("Удаление объекта")

doc1 = Doctors("Ivanov","Artyom","Yurievich","Surgeon","5 years old","Master of medicine","Rasskazova street",6)

print("Одним из лучших врачей является" + " " + doc1.surname.title() + " " + doc1.name.title() + " " + doc1.patronymic.title())
doc1.inspect()


class Patients():
    def __init__(self, surname=0,name=0,patronymic=0,address=0,city=0,age=0,floor=0):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.city = city
        self.age = age
        self.floor = floor

    def being_treated(self):
        print("Patient" + " " + self.surname + " " + self.name + " " + " is being treated in the hospital")

    def __del__(self):
        print("Удаление объекта")

pat1 = Patients("Camenev", "Anton", "Mikhailovich", "Pravda street", "Arkhangelsk", "25 years old", "male")

print("Пациент" + " " + pat1.surname.title() + " " + pat1.name.title() + " " + " находится в больнице")
pat1.being_treated()


class Medical_history():
    def __init__(self, patient=0, doctor=0, treatment=0, date_ot_the_disease=0, date_of_recovery=0, type_of_treatment=0):
        self.patient = patient
        self.doctor = doctor
        self.treatment = treatment
        self.date_ot_the_disease = date_ot_the_disease
        self.date_of_recovery = date_of_recovery
        self.type_of_treatment = type_of_treatment

    def is_located(self):
        print("Doctor" + " " + self.doctor + " " + " prescribed" + " " + self.treatment + " " + self.patient)

    def __del__(self):
        print("Удаление объекта")

med1 = Medical_history("Andreev", "Ivanov", "rest", " 23 september", " 14 october", "outpatient treatment")

print("Доктор" + " " + med1.doctor.title() + " " + "назначил" + " " + med1.treatment.title() + " " + "пациенту" + " " + med1.patient.title())
med1.is_located()


class Department():
    def __init__(self,department_name=0, floor=0, room_number=0, full_name_of_the_head=0):
        self.department_name = department_name
        self.floor = floor
        self.room_number = room_number
        self.full_name_of_the_head = full_name_of_the_head

    def exists(self):
        print("The hospital has" + " " + self.department_name + " " + "department on the" + " " + self.floor + " " +"floor")

    def __del__(self):
        print("Удаление объекта")

dep1 = Department("Хирургия", "4", "123", "Королев Андрей Иванович")

print("Отделением" + " " + dep1.department_name + " " + "на" + " " + dep1.floor + " " + "этаже руководит" + " " + dep1.full_name_of_the_head)
dep1.exists()


class Service_personnel():
    def __init__(self, surname=0,name=0,patronymic=0,post=0,experience=0, address=0,number=0):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.post = post
        self.experience = experience
        self.address = address
        self.number = number

    def work(self):
        print(self.surname + " " + self.name + " " + "works in a hospital")

    def __del__(self):
        print("Удаление объекта полностью")

sev1 = Service_personnel("Milekova","Anna","Yurievna","laboratory assistant","10 years old","Victory street",6)

print("Девушка" + " " + sev1.name.title() + " " + sev1.surname.title() + " " + " работает в больнице больше" + " " + sev1.experience.title())
sev1.work()
