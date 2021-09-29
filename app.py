from dbconfig import db

def bookAppointment(doctor):
    db.insert('appointment', {
        'patient_id': 2,
        'status': 0,
        'accepted_by': doctor
    })

def showPatientMenu():
    print("1. See list of doctors")
    print("2. Show confirmed appointments")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        rows = db.getAll('user', '*', 
        ('ut_id = %s', [2])
        )
        for row in rows:
            print(row)

        chooseDoctor = int(input("Choose the doctor"))
        bookAppointment(chooseDoctor)


showPatientMenu()
