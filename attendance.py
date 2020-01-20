from function import AttendanceManagement
import os
import time

# Terminal based user interface

def reload():
    print("Reloading the USER MANUAL")
    time.sleep(5)
    os.system('clear')

def main():
    print("*" * 40)
    print(" :: Terminal Based Personal Attendance Management System :: ")
    print("*" * 40)
    print()

    db = AttendanceManagement()

    flag = 0

    while(True):
        os.system('clear')
        print("#" * 40)
        print(" :: USER MANUAL :: ")
        print()
        print("Enter 1 => Get overall attendance information")
        print("Enter 2 => Update today's information")
        print("Enter 3 => See code of all subjects")
        print("Enter 4 => Add a new subject")
        print("Enter 5 => Delete any subject history(Subject code is required)")
        print("Enter 6 => Exit from the Attendance Management system")
        print("#" * 40)
        print()

        choice = int(input("Enter your choice => "))


        if(choice==1):
            os.system('clear')
            if(db.show_data()):
                print()
                i = int(input("press 1 to reload the USER MANUAL"))

                os.system('clear')
                reload()

            else:
                print("Something went wrong \nData can't be shown\n")
                reload()

        elif(choice==2):

            choosed_code = input("Enter the Subject Id => ")

            mass_bunk = input("Is it a mass bunk?(yes/no) => ")
            if(mass_bunk == "no"):
                is_mass_bunk = 0
                status = input("Have you attended the class?(yes/no) => ")
                if(status == "yes"):
                    is_present = 1
                    is_absent = 0
                else:
                    is_present = 0
                    is_absent = 1
            else:
                is_mass_bunk = 1
                is_present = 0
                is_absent = 0

            if(db.update_data(choosed_code, is_mass_bunk, is_present, is_absent)):
                print("Attendance data is updated successfully")
                reload()
            else:
                print("Data is not updated \n please try again")
                reload()

        

        elif(choice==3):
            os.system('clear')
            if(db.show_code()):
                print()
                i = int(input("press 1 to reload the USER MANUAL"))

                os.system('clear')
                reload()

            else:
                print("Something went wrong \nCode can't be shown\n")
                reload()




        elif(choice==4):
            os.system('clear')
            subject = input("Enter Subject Name => ")
            code = input("Enter Subject Code (code will be used when you will update attendnce later) => ")
            total_class_taken = 0
            personal_absent = 0
            mass_bunk = 0

            if(db.insert_subject([code, subject, total_class_taken, personal_absent, mass_bunk])):
                print("Subject added successfully")
                reload()
            else:
                print("Something went wrong\nData can't be added")
                reload()


            

        
        elif(choice==5):
            os.system('clear')
            choosed_code = input("Enter the Subject code => ")

            if(db.delete_data(choosed_code)):
                print("subject deleted Successfully")
                reload()
            else:
                print("something went wrong")
                reload()



    
        elif(choice==6):

            flag+=1


        else:
            print("Wrong Choice")
            reload()

        if(flag>0):
            os.system('clear')
            break


if(__name__ == "__main__"):
    main()
