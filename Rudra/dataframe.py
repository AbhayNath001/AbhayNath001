import pandas as pd                             #pip install pandas
import sqlite3                                  #pip install db-sqlite3

try:
    db = sqlite3.connect('College.sqlite')
    data = pd.DataFrame([["CSPIT", "CIVIL ENGINEERING (BTECH)", 60, 128000, "4 years"],
                         ["CSPIT", "COMPUTER ENGINEERING (BTECH)", 120, 128000, "4 years"],
                         ["CSPIT", "COMPUTER SCIENCE AND ENGINEERING (BTECH)", 60, 128000, "4 years"],
                         ["CSPIT", "ELECTRICAL ENGINEERING (BTECH)", 30, 128000, "4 years"],
                         ["CSPIT", "ELECTRONICS AND COMMUNICATION ENGINEERING (BTECH)", 90, 128000, "4 years"],
                         ["CSPIT", "INFORMATION TECHNOLOGY (BTECH)", 120, 128000, "4 years"],
                         ["CSPIT", "MECHNICAL ENGINEERING (BTECH)", 60, 128000, "4 years"],
                         ["CSPIT", "AI AND ML (BTECH)", 60, 128000, "4 years"],
                         ["CSPIT", "ADVANCED MANUFACTURING TECHNOLOGY (MTECH)", 18, 159000, "2 years"],
                         ["CSPIT", "COMPUTER ENGINEERING (MTECH)", 18, 159000, "2 years"],
                         ["CSPIT", "STRUCTURAL ENGINEERING (MTECH)", 18, 159000, "2 years"],
                         ["CSPIT", "THERMAL ENGINEERING (MTECH)", 18, 159000, "2 years"],
                         ["CSPIT", "CYBER SECURITY (POST GRADUATE DIPLOMA)", 15, 150000, ""],
                         ["DEPSTAR", "COMPUTER ENGINEERING (BTECH)", 120, 98000, "4 years"],
                         ["DEPSTAR", "COMPUTER SCIENCE AND ENGINEERING (BTECH)", 120, 98000, "4 years"],
                         ["DEPSTAR", "INFORMATION TECHNOLOGY (BTECH)", 120, 98000, "4 years"]],
                         columns = ["College","Department", "Intake", "Fees", "Duration"])
    data.to_sql("College", db, if_exists='replace')
    try:
        db1 = sqlite3.connect('University.sqlite')
        data = pd.DataFrame([["BTECH", "DEPSTAR", "INFORMATION TECHNOLOGY"],
                            ["BTECH", "DEPSTAR", "COMPUTER SCIENCE ENGINEERING"],
                            ["BTECH", "DEPSTAR", "COMPUTER ENGINEERING"],
                            ["BTECH", "CSPIT", "COMPUTER SCIENCE ENGINEERING"],
                            ["MTECH", "CSPIT", "COMPUTER SCIENCE ENGINEERING"],
                            ["BTECH", "CSPIT", "MECHNICAL ENGINEERING"],
                            ["MTECH", "CSPIT", "MECHNICAL ENGINEERING"],
                            ["BTECH", "CSPIT", "INFORMATION TECHNOLOGY"],
                            ["MTECH", "CSPIT", "INFORMATION TECHNOLOGY"],
                            ["BTECH", "CSPIT", "CIVIL ENGINEERING"],
                            ["MTECH", "CSPIT", "CIVIL ENGINEERING"],
                            ["BTECH", "CSPIT", "COMPUTER ENGINEERING"],
                            ["MTECH", "CSPIT", "COMPUTER ENGINEERING"],
                            ["BTECH", "CSPIT", "ELECTRICAL AND COMMUNICATION ENGINEERING"],
                            ["MTECH", "CSPIT", "ELECTRICAL AND COMMUNICATION ENGINEERING"],
                            ["BTECH", "CSPIT", "ELECTRICAL ENGINEERING"],
                            ["MTECH", "CSPIT", "ELECTRICAL ENGINEERING"],
                            ["B.SC", "PDPIAS", ""],
                            ["M.SC", "PDPIAS", ""],
                            ["B.PHARMA", "RPCP", ""],
                            ["M.PHARMA", "RPCP", ""],
                            ["BBA", "IIIM", ""],
                            ["PGDM", "IIIM", ""],
                            ["MBA", "IIIM", ""],
                            ["B.SC NURSING", "MTIN", ""],
                            ["GNM", "MTIN", ""],
                            ["M.SC NURSING", "MTIN", ""],
                            ["B.SC[IT]", "SMT.CMPICA", ""],
                            ["BCA", "SMT.CMPICA", ""],
                            ["MCA", "SMT.CMPICA", ""],
                            ["M.SC[IT]", "SMT.CMPICA", ""]],
                            columns = ["Degrees","Colleges","Departments"])
        data.to_sql("University", db1, if_exists='replace')
    except:
        print("")
except:
    print("Initializing Database...")

def College_information():
    college = input("Enter the College Name: ")
    department = input("Enter the Department: ")
    
    fees = db.execute("SELECT Fees FROM College WHERE College=? AND Department=?",(college, department))
    fees_result = fees.fetchone()
    
    intake = db.execute("SELECT Intake FROM College WHERE College=? AND Department=?",(college, department))
    intake_result = intake.fetchone()
    
    duration = db.execute("SELECT Duration FROM College WHERE College=? AND Department=?",(college, department))
    duration_result = duration.fetchone()
    
    if fees_result:
        print("Fees for the {} College and {} Department is: {}".format(college, department, fees_result[0]) + " Rs")
        print("Intake for the {} College and {} Department is: {}".format(college, department, intake_result[0]))
        print("Course Duration for the {} College and {} Department is: {}".format(college, department, duration_result[0]))
        
    else:
        print("No data found for the given College and Department")


def University_information():
    degree = input("Enter the Degree: ")
    
    colleges = db1.execute("SELECT Colleges FROM University WHERE Degrees=?",(degree,)).fetchall()
    #colleges_result = colleges.fetchall()
    
    departments = db1.execute("SELECT Departments FROM University WHERE Degrees=?",(degree,)).fetchall()
    #departments_result = departments.fetchall()
    
    if colleges:
        print("Colleges for the {} Degrees are:".format(degree))
        for i in range(len(colleges)):
            print("{}. {}".format(i + 1, colleges[i][0]) + " ({}. {})".format(i + 1, departments[i][0]))
            #print("Departments in the colleges are: " + "{}. {}".format(i + 1, departments[i][0]))
            #print("{}. {}".format(i + 1, departments[i][0]))
        
        # print("Departments in the colleges are:")
        # for i in range(len(departments)):
            # print("{}. {}".format(i + 1, departments[i][0]))
        
    else:
        print("No data found for the given Degree")

College_information()
