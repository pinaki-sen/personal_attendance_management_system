import sqlite3 as lite
import os

## Basic functionality

class AttendanceManagement(object):
    def __init__(self):
        global con 
        try:
            con = lite.connect('attendance.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS attendance(code TEXT, subject TEXT, total_classes_taken INTEGER, personal_absent INTEGER, mass_bunk INTEGER)")
        except Exception:
            print("Unable to create a DataBase!")
            
    
    def insert_subject(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO attendance(code, subject, total_classes_taken, personal_absent, mass_bunk) VALUES (?,?,?,?,?)", data) 
                return True
        except Exception:
            return False
        
    def show_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM attendance")
                os.system('clear')
                for item in (cur.fetchall()):
                    print("Subject Code => " + str(item[0]))
                    print("Subject Name => " + str(item[1]))
                    print("Total Clases Taken => " + str(item[2]))
                    print("Classes attended => " + str(item[2] - item[3]))
                    print("Personal Absents => " + str(item[3]))
                    print("Mass Bunk => " + str(item[4]))

                    if(item[2]==0):
                        print("No classes has been taken yet. Update data")
                    
                    else:
                        # mass bunk not considered as absent
                        p = item[2] - item[3]
                        t = item[2]
                        ans = (p/t)*100
                        print("Percentage if mass bunk is not considered as absent => "+ str(ans) + "%")

                        # mass bunk considered as absent
                        p = item[2] - item[3]
                        t = item[2] + item[4]
                        ans = (p/t)*100
                        print("Percentage if mass bunk is also considered as absent => "+ str(ans) + "%")
                    print()
                    print()
                return True
        except Exception:
            return False

    def delete_data(self, code):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM attendance WHERE code = ?"
                cur.execute(sql, [code])
                return True
        except Exception:
            return False


    def update_data(self, code, is_mass_bunk, is_present, is_absent):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM attendance")

                for item in (cur.fetchall()):
                    if(item[0] == code):
                        classes = item[2]
                        absent = item[3]
                        #present = classes - absent
                        mass_bunk = item[4]

                        if(is_mass_bunk == 1):
                            mass_bunk += 1
                        else:
                            if(is_present == 1):
                                classes += 1
                            else:
                                classes += 1
                                absent += 1
                        data = [code, item[1], classes, absent, mass_bunk]
                        cur.execute("DELETE FROM attendance WHERE code = ?", [code])

                        cur.execute("INSERT INTO attendance(code, subject, total_classes_taken, personal_absent, mass_bunk) VALUES (?,?,?,?,?)", data)
                        print("Attendance of "+str(item[1])+" has been updated")
                        return True

        except Exception:
            return False

    def show_code(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM attendance")
                for item in (cur.fetchall()):
                    print(str(item[1]) + " => " + str(item[0]))
                return True
        except Exception:
            return False


                    
