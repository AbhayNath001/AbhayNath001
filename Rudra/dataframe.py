import pandas as pd                             #pip install pandas
import sqlite3                                  #pip install db-sqlite3

try:
    db = sqlite3.connect('College.sqlite')
    data = pd.DataFrame([["CSPIT", "BTECH","CIVIL ENGINEERING", 60, 128000, "4 years"],
                         ["CSPIT", "BTECH","COMPUTER ENGINEERING", 120, 128000, "4 years"],
                         ["CSPIT", "BTECH","COMPUTER SCIENCE AND ENGINEERING", 60, 128000, "4 years"],
                         ["CSPIT", "BTECH","ELECTRICAL ENGINEERING", 30, 128000, "4 years"],
                         ["CSPIT", "BTECH","ELECTRONICS AND COMMUNICATION ENGINEERING", 90, 128000, "4 years"],
                         ["CSPIT", "BTECH","INFORMATION TECHNOLOGY", 120, 128000, "4 years"],
                         ["CSPIT", "BTECH","MECHNICAL ENGINEERING", 60, 128000, "4 years"],
                         ["CSPIT", "BTECH","AI AND ML", 60, 128000, "4 years"],
                         ["CSPIT", "MTECH","ADVANCED MANUFACTURING TECHNOLOGY", 18, 159000, "2 years"],
                         ["CSPIT", "MTECH","COMPUTER ENGINEERING", 18, 159000, "2 years"],
                         ["CSPIT", "MTECH","STRUCTURAL ENGINEERING", 18, 159000, "2 years"],
                         ["CSPIT", "MTECH","THERMAL ENGINEERING", 18, 159000, "2 years"],
                         ["CSPIT", "POST GRADUATE DIPLOMA","CYBER SECURITY", 15, 150000, ""],
                         ["DEPSTAR", "BTECH","COMPUTER ENGINEERING", 120, 98000, "4 years"],
                         ["DEPSTAR", "BTECH","COMPUTER SCIENCE AND ENGINEERING", 120, 98000, "4 years"],
                         ["DEPSTAR", "BTECH","INFORMATION TECHNOLOGY", 160, 98000, "4 years"]],
                         columns = ["College", "Degree","Department", "Intake", "Fees", "Duration"])
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
    degree = input("Enter the degree: ")
    
    fees = db.execute("SELECT Fees FROM College WHERE College=? AND Department=? AND Degree=?",(college, department, degree))
    fees_result = fees.fetchone()
    
    intake = db.execute("SELECT Intake FROM College WHERE College=? AND Department=? AND Degree=?",(college, department, degree))
    intake_result = intake.fetchone()
    
    duration = db.execute("SELECT Duration FROM College WHERE College=? AND Department=? AND Degree=?",(college, department, degree))
    duration_result = duration.fetchone()
    
    if fees_result:
        print("Fees for the {} College and {} Department with {} Degree is: {}".format(college, department, degree, fees_result[0]) + " Rs")
        print("Intake for the {} College and {} Department with {} Degree is: {}".format(college, department, degree, intake_result[0]))
        print("Course Duration for the {} College and {} Department with {} Degree is: {}".format(college, department, degree, duration_result[0]))
        
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
