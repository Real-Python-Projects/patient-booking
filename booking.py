from tinydb import TinyDB,Query

time=['9.00am', '9.30am', '10.00am','10.30am','11.00am','11.30am','12.00pm']

db=TinyDB("data.json")
query=Query()

def registerDoctor():
    name=input("Enter Doctors Name :")
    specialization=input("Enter Doctors specialization :")
    db.insert({
        "name":name,
        "specialization":specialization,
        "bookings":[]
    })
    print("Doctor Registered!!!!!")

def bookDoctor():
    print("here are Doctors and their specs and available time \n")
    doctors=db.all()
    for i in doctors:
        print("name :",i['name']," specialization :",i['specialization']," booked slots :",i['bookings'])

    print("")
    name=input("enter doctors name :")
    print("choose booking e.g 1 for 9.00am :")
    for i in range(len(time)):
        print(i," -- ",time[i])        
    btime=int(input("enter time number  :"))
    try:
        booktime=time[btime]

        doctor=db.search(query.name==name)
        if len(doctor)==1:
            doctor=doctor[0]
            if booktime in doctor['bookings']:
                print("time was already booked  try again!!!")
                bookDoctor()
            else:
                doctor['bookings'].append(booktime)
                db.update(doctor)
                print("succesfully booked !!!")
        else:
            print("no such doctor in the system ")
        
    except:
        print("found an error")
  
    
if __name__=="__main__":
    x=int(input("choose \n 1 to register doctor \n 2. to do bookings \n "))
    if x==1:
        registerDoctor()
    elif x==2:
        bookDoctor()
    else:
        print("inavlid entry")
       