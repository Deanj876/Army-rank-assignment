#https://www.google.com/search?q=every+rank+in+the+army&rlz=1C1GCEA_enUS1035US1035&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj85oO07aH-AhXTlWoFHbQwCQUQ0pQJegQIBRAC&biw=1777&bih=841&dpr=0.9#imgrc=CmjqPYEsl-D3mM
import sys
import time
import os
def printz(text, delay=0.05):

    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

loop1 = 0
loop2 = 0
loop3 = 0   
loop4 = 0

#enlisted Pay Grades
PayGrade1 = ("The Pay Grade / Contract Level of this Rank is a E-1: estimated $1,917.60 per Month (Base Pay)")
PayGrade2 = ("The Pay Grade / Contract Level of this Rank is a E-2: estimated $2,149.20 per Month (Base Pay)")
PayGrade3 = ("The Pay Grade / Contract Level of this Rank is a E-3: estimated $2,259.90 per Month (Base Pay)")
PayGrade4 = ("The Pay Grade / Contract Level of this Rank is a E-4: estimated $2,503.50 per Month (Base Pay)")
PayGrade5 = ("The Pay Grade / Contract Level of this Rank is a E-5: estimated $2,730.30 per Month (Base Pay)")
#non-commissioned officers Pay Grades
PayGrade6 = ("The Pay Grade / Contract Level of this Rank is a E-6: estimated $2,980.50 per Month (Base Pay)")
PayGrade7 = ("The Pay Grade / Contract Level of this Rank is a E-7: estimated $3,445.80 per Month (Base Pay)")
PayGrade8 = ("The Pay Grade / Contract Level of this Rank is a E-8: estimated $4,957.20 per Month (Base Pay with 8 Years of Service)")
PayGrade9 = ("The Pay Grade / Contract Level of this Rank is a E-9: estimated $6,055.50 per Month (Base Pay with 10 Years of Service)")
#warrent officer Pay Grades
PayGradeW1 = ("The Pay Grade / Contract Level of this Rank is a W-1: estimated $3,555.00 per Month (Base Pay)")
PayGradeW2 = ("The Pay Grade / Contract Level of this Rank is a W-2: estimated $4,050.30 per Month (Base Pay)")
PayGradeW3 = ("The Pay Grade / Contract Level of this Rank is a W-3: estimated $4,577.70 per Month (Base Pay)")
PayGradeW4 = ("The Pay Grade / Contract Level of this Rank is a W-4: estimated $5,012.40 per Month (Base Pay)")
PayGradeW5 = ("The Pay Grade / Contract Level of this Rank is a W-5: estimated $8,912.10 per Month (Base Pay with 20 Years of Service)")
#officer Pay Grades
PayGradeO1 = ("The Pay Grade / Contract Level of this Rank is a O-1: estimated $3,637.20 per Month (Base Pay)")
PayGradeO2 = ("The Pay Grade / Contract Level of this Rank is a O-2: estimated $4,190.70 per Month (Base Pay)")
PayGradeO3 = ("The Pay Grade / Contract Level of this Rank is a O-3: estimated $4,849.80 per Month (Base Pay)")
PayGradeO4 = ("The Pay Grade / Contract Level of this Rank is a O-4: estimated $5,516.40 per Month (Base Pay)")
PayGradeO5 = ("The Pay Grade / Contract Level of this Rank is a O-5: estimated $6,393.30 per Month (Base Pay)")
PayGradeO6 = ("The Pay Grade / Contract Level of this Rank is a O-1: estimated $7,669.20 per Month (Base Pay)")
PayGradeO7 = ("The Pay Grade / Contract Level of this Rank is a O-2: estimated $10,113.00 per Month (Base Pay)")
PayGradeO8 = ("The Pay Grade / Contract Level of this Rank is a O-3: estimated $12,170.70 per Month (Base Pay)")
PayGradeO9 = ("The Pay Grade / Contract Level of this Rank is a O-4: estimated $17,201.40 per Month (Base Pay with 20 Years of Service)")
PayGradeO10 = ("The Pay Grade / Contract Level of this Rank is a O-5: estimated $17,201.40 per Month (Base Pay with 20 Years of Service)")

EnlistedRanks = ["Private", "Private Second Class (PV2)", "Private First Class (PV1)", "Specialist"]
NonCommissionedOfficers= ["Corporal", "Sergeant", "Staff Sergeant", "Sergeant 1st Class", "Master Sergeant", "1st Sergeant", "Sergeant Major", "Command sergeant Major", "Sergeant Major of the Army"]
WarrentOfficers = ["Warrent Officer", "Chief Warrent Officer 2", "Chief Warrent Officer 3", "Chief Warrent Officer 4", "Chief Warrent Officer 5"]
Officers = ["Second Lieutenant", "First Lieutenant", "Captain", "Major", "Lieutenant Colonel", "Colonel"]
Generals = ["Brigadier General", "Major General", "Lieutenant General", "General", "General of The U.S. Army"]

def PVTinfo():
    print("Rank: Private\nContract: E1\nInfo: Private is the lowest rank. Most Soldiers receive this rank during Basic Combat Training.\nPay Grade: " + PayGrade1 +"\nExtra Responsibilities: None to Minimal")
def PV2info():
    print("Rank: Private Second class\nContract: E2\nInfo: Enlisted Soldiers perform specific job functions and have the knowledge that ensures the success of their unit’s current mission within the Army.\nPay Grade: " + PayGrade2 +"\nExtra Responsibilities: Minimal")
def PV1info():
    print("Rank: Private First class\nContract: E3\nInfo: Soldiers are generally promoted to this level within a year by request of a supervisor. Soldiers serving at this rank make up the backbone of the Army. Their primary role is to carry out orders and complete missions.\nPay Grade: " + PayGrade3 +"\nExtra Responsibilities: Minimal")
def SPCinfo():
    print("Rank: Specialist\nContract: E4\nInfo: A Specialist can manage other lower-ranked enlisted Soldiers. A Soldier can be promoted to this rank after serving a minimum of two years and attending a training class. Recruits with a four-year degree may enter Basic Combat Training as a specialist.\nPay Grade: " + PayGrade4 +"\nExtra Responsibilities: Minimal")

def CPLinfo():
    print("Rank: Corporal\nContract: E4\nInfo: Corporal is the base level of the noncommissioned officer (NCO) ranks. Corporals serve as team leader of the smallest Army units. Like sergeants, they are responsible for individual training, personal appearance and cleanliness of Soldiers.\nPay Grade: " + PayGrade4 +"\nExtra Responsibilities: Minimal, Drill Instructor")
def SGTinfo():
    print("Rank: Sergeant\nContract: E5\nInfo: Sergeants typically command a fire team of around five Soldiers. Sergeants oversee Soldiers in their daily tasks, and are expected to set a standard for lower-ranked Soldiers to live up to.\nPay Grade: " + PayGrade5 +"\nExtra Responsibilities: Minimal, Drill Sergeant / Instructor")
def SSGinfo():
    print("Rank: Staff Sergeant\nContract: E6\nInfo: A staff sergeant commands a squad (nine to 10 Soldiers). Often, a staff sergeant will have one or more sergeants under his or her leadership. They are responsible for developing, maintaining and utilizing the full range of a Soldier’s potential.\nPay Grade: " + PayGrade6 +"\nExtra Responsibilities: Sizeable, Drill Sergeant / Instructor, Squad Leader")
def SFCinfo():
    print("Rank: Sergeant First Class\nContract: E7\nInfo: As the key assistant and advisor to the platoon leader, the sergeant first class generally has 15 to 18 years of Army experience.\nPay Grade: " + PayGrade7 +"\nExtra Responsibilities: Sizeable, Drill Sergeant / Instructor, Squad Leader, Platoon Assistant / Co-Leader")
def MSGinfo():
    print("Rank: Master Sergeant\nContract: E8\nInfo: The Master Sergeant is the principal noncommissioned officer at the battalion level and higher\nPay Grade: " + PayGrade8 +"\nExtra Responsibilities: Moderatly High, Drill Sergeant / Instructor, Squad Leader, Platoon Assistant / Co-Leader")
def FSGinfo():
    print("Rank: First Sergeant\nContract: E8\nInfo: The first sergeant is the principal NCO and life-blood of a company. He is the disciplinarian and counselor. He instructs other sergeants, advises the commander and helps train all enlisted Soldiers. He assists officers at the company level (62 to 190 Soldiers).\nPay Grade: " + PayGrade8 +"\nExtra Responsibilities: Moderatly High, Drill Sergeant / Instructor, Squad Leader, Platoon Assistant / Co-Leader, Company Assistant")
def SGMinfo():
    print("Rank: Sergeant Major\nContract: E9\nInfo: Sergeants major serve as the chief administrative assistants for an Army headquarters, but their sphere of influence regarding leadership is generally limited to those directly under their charge. They are key enlisted members of staff elements at battalion level or higher.\nPay Grade: " + PayGrade9 +"\nExtra Responsibilities: Moderatly High, Drill Sergeant / Instructor, Squad Leader, Platoon Assistant / Co-Leader, Company Assistant")
def CSMinfo():
    print("Rank: Command Sergeant Major\nContract: E9\nInfo: Command sergeants major are the senior enlisted advisors to the commanding officer. They carry out policies and standards and advise the commander on the performance, training, appearance and conduct of enlisted Soldiers. A command sergeant major is assignable to battalion level or higher.\nPay Grade: " + PayGrade9 +"\nExtra Responsibilities: Moderatly High, Drill Sergeant / Instructor, Squad Leader, Platoon Assistant / Co-Leader, Company Assistant")
def SGMAinfo():
    print("Rank: Sergeant Major of the Army\nContract: E9\nInfo: There’s only one Sergeant Major of the Army. The SMA oversees all noncommissioned officers. He serves as the senior enlisted advisor and consultant to the Chief of Staff of the Army.\nPay Grade: " + PayGrade9 +"\nExtra Responsibilities: Advanced, Drill Sergeant / Instructor, Squad Leader, Platoon Assistant / Co-Leader, Company Assistant, Overseer of NCO's or Non-Commissioned Officers")
    
def WO1info():
    print("Rank: Warrent Officer 1\nContract: W1\nInfo: Warrant officers are the technical and tactical experts of the Army. At the base-level rank, warrant officers primarily support operations from team or detachment through battalion. Warrant officers are appointed by the Secretary of the Army.\nPay Grade: " + PayGradeW1 +"\nExtra Responsibilities: Moderatly High, Drill Instructor, Specialist / Specialties Instructor and coordinator.")
def CW2info():
    print("Rank: Chief Warrent Officer 2\nContract: W2\nInfo: The chief warrant officer two is an intermediate-level technical and tactical expert. He or she supports levels of operations from team or detachment through battalion\nPay Grade: " + PayGradeW2 +"\nExtra Responsibilities: Moderatly High, Drill Instructor, Specialist / Specialties Instructor and coordinator, Assistance to Battalions.")
def CW3info():
    print("Rank: Chief Warrent Officer 3\nContract: W3\nInfo: The chief warrant officer three is an advanced-level technical and tactical expert. They primarily support operations from team or detachment through brigade.\nPay Grade: " + PayGradeW3 +"\nExtra Responsibilities: Moderatly High, Drill Instructor, Specialist / Specialties Instructor and coordinator, Assistance to Brigades.")
def CW4info():
    print("Rank: Chief Warrent Officer 4\nContract: W4\nInfo: The chief warrant officer four is a senior-level technical and tactical expert. They primarily support battalion, brigade, division, corps, and echelons above corps operations.\nPay Grade: " + PayGradeW4 +"\nExtra Responsibilities: Moderatly High, Drill Instructor, Specialist / Specialties Instructor and coordinator, Assistance to Battalion, Brigade, Division, Corps, and Echelons above Corps Operations.")
def CW5info():
    print("Rank: Chief Warrent Officer 5\nContract: W5\nInfo: The chief warrant officer five is a master-level technical and tactical expert. They primarily support brigade, division, corps, echelons above corps and major command operations. They have special warrant officer leadership and representation responsibilities within their respective commands.\nPay Grade: " + PayGradeW5 +"\nExtra Responsibilities: Moderatly High, Drill Instructor, Specialist / Specialties Instructor and coordinator, Assistance to Brigade, Division, Corps, Echelons above Corps and Major Command Operations.")
    
def SLTinfo():
    print("Rank: Second Lieutenant\nContract: O1\nInfo: Most officers enter the Army at second lieutenant. They lead platoon-size units consisting of a platoon sergeant and two or more squads (16 to 44 Soldiers).\nPay Grade: " + PayGradeO1 +"\nExtra Responsibilities: Advance, Instructor, Platoon Leader")
def FLTinfo():
    print("Rank: First Lieutenant\nContract: O2\nInfo: Officers generally reach the rank of first lieutenant after 18 to 24 months of service. Soldiers at this rank may lead more specialized weapons platoons and indirect fire computation centers.\nPay Grade: " + PayGradeO2 +"\nExtra Responsibilities: Advance, Instructor, Specialties Platoon Leader, Basic Platoon Leader")
def CPTinfo():
    print("Rank: Captain\nContract: O3\nInfo: The Captain commands and controls company-sized units (62 to 190 Soldiers). He or she may also instruct at service schools and combat training centers or serve as a staff officer at the battalion level.\nPay Grade: " + PayGradeO3 +"\nExtra Responsibilities: Advance, Instructor, Company Leader")
def MAJinfo():
    print("Rank: Major\nContract: O4\nInfo: The major serves as the primary staff officer for brigade and task force command and manages personnel, logistical and operational missions.\nPay Grade: " + PayGradeO4 +"\nExtra Responsibilities: Advance, Instructor, Company Leader, Staff Officer for Brigades and Task Force Command")
def LTCinfo():
    print("Rank: Lieutenant Colonel\nContract: O5\nInfo: The lieutenant colonel typically commands battalion-sized units (300 to 1,000 Soldiers) with a command sergeant major as an NCO assistant. He or she may also be selected for brigade and task force executive officer.\nPay Grade: " + PayGradeO5 +"\nExtra Responsibilities: Advance, Instructor, Battalion Leader or Task Force Executive Officer")
def COLinfo():
    print("Rank: Colonel\nContract: O6\nInfo: The colonel typically commands brigade-sized units (3,000 to 5,000 Soldiers), with a command sergeant major as principal NCO assistant. They may also serve as the chief of divisional-level staff agencies.\nPay Grade: " + PayGradeO6 +"\nExtra Responsibilities: Advance, Instructor, Brigade Leader or Chief of Divisional-level Staff Agencies.")
    
def BGinfo():
    print("Rank: BRIGADIER GENERAL\nContract: O7\nInfo: The brigadier general serves as deputy commander to the commanding general for Army divisions. This rank is responsible for overseeing the staff’s planning and coordination of a mission.\nPay Grade: " + PayGradeO7 +"\nExtra Responsibilities: Majorly Advanced, Instructor")
def MGinfo():
    print("Rank: MAJOR GENERAL\nContract: O8\nInfo: The major general typically commands division-sized units (10,000 to 15,000 Soldiers).\nPay Grade: " + PayGradeO8 +"\nExtra Responsibilities: Majorly Advanced, Instructor, Division Leader")
def LTGinfo():
    print("Rank: LIEUTENANT GENERAL\nContract: O9\nInfo: The lieutenant general typically commands corps-sized units (20,000 to 45,000 Soldiers).\nPay Grade: " + PayGradeO9 +"\nExtra Responsibilities: Majorly Advanced, Instructor, Corps Leader")
def GENinfo():
    print("Rank: GENERAL\nContract: O10\nInfo: The senior level of commissioned officer typically has more than 30 years of experience and service. They command all operations that fall within their geographical area\nPay Grade: " + PayGradeO10 +"\nExtra Responsibilities: Unmost Importance, Instructor, Overseer of all aspects of Command")
def GOAinfo():
    print("Rank: GENERAL OF THE ARMY\nContract: Specialized O11\nInfo: This rank is only achievable in times of war, where the commanding officer must be equal or of higher than those commanding armies from allied nations. The last officers to hold this rank served during and immediately following World War II.\nPay Grade: With the Certain Circumstances of this Rank there is no set pay grade or contract currently found or accurate\nExtra Responsibilities: Unmost Importance, Instructor, Overseer and Leader of the United States Army During War efforts.")
    
    
while loop1 == 0:
    loop2 -= 1
    loop2 = 0
    os.system("clear")
    printz('Hello, Welcome to the U.S Army Rank Selection')
    printz("\n\nWhat Category Would you like to Look at first?\n\nEnlisted (E)\nEnlisted / Non-Commissioned Officers (NCO) \nWarrent Officers (WO)\nCommissioned Officers (CO)\nGenerals (G)\n Or go back to Main Menu (MM)")
    categorySelection = input('(Example "E"):')

    if categorySelection == "E" or categorySelection == "e":
        while loop2 == 0:
            loop3 -= 1
            loop3 = 0
            os.system("clear")
            printz("what Rank would you like to look at?\n\nPrivate (PVT)\nPrivate Second Class (PV2)\nPrivate First Class (PV1)\nSpecialist (SPC)\nOr Return to the Category Menu (MAIN)")
            rankSelection = input('(Example "PVT"):')
            if rankSelection == "PVT" or rankSelection == "Pvt" or rankSelection == "pvt":
                while loop3 == 0:
                    os.system("clear")
                    PVTinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "PV2" or rankSelection == "Pv2" or rankSelection == "pv2":
                while loop3 == 0:
                    os.system("clear")
                    PV2info()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "PV1" or rankSelection == "Pv1" or rankSelection == "pv1":
                while loop3 == 0:
                    os.system("clear")
                    PV1info()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "SPC" or rankSelection == "spc":
                while loop3 == 0:
                    os.system("clear")
                    PV2info()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "MAIN" or rankSelection == "Main" or rankSelection == "Main":
                loop2 += 1
    elif categorySelection == "NCO" or categorySelection == "Nco" or categorySelection == "nco":
        while loop2 == 0:
            loop3 -= 1
            loop3 = 0
            os.system("clear")
            printz("what Rank would you like to look at?\n\nCorporal (CPL)\nSergeant (SGT)\nStaff Sergeant (SSG)\nSergeant 1st Class (SFC)\nMaster Sergeant (MSG)\n1st Sergeant (FSG)\nSergeant Major (SGM)\nCommand Sergeant Major (CSM)\nSergeant Major of the Army (SGMA)\nBack to Category Menu (MAIN)")
            rankSelection = input('(Example "CPL"):')
            if rankSelection == "CPL" or rankSelection == "Cpl" or rankSelection == "cpl":
                while loop3 == 0:
                    os.system("clear")
                    CPLinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "SGT" or rankSelection == "Sgt" or rankSelection == "sgt":
                while loop3 == 0:
                    os.system("clear")
                    SGTinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "SSG" or rankSelection == "Ssg" or rankSelection == "ssg":
                while loop3 == 0:
                    os.system("clear")
                    SSGinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "SFC" or rankSelection == "Sfc" or rankSelection == "sfc":
                while loop3 == 0:
                    os.system("clear")
                    SFCinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "MSG" or rankSelection == "Msg" or rankSelection == "msg":
                while loop3 == 0:
                    os.system("clear")
                    MSGinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "FSG" or rankSelection == "Fsg" or rankSelection == "fsg":
                while loop3 == 0:
                    os.system("clear")
                    FSGinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "SGM" or rankSelection == "Sgm" or rankSelection == "sgm":
                while loop3 == 0:
                    os.system("clear")
                    SGMinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "CSM" or rankSelection == "Csm" or rankSelection == "csm":
                while loop3 == 0:
                    os.system("clear")
                    CSMinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "SGMA" or rankSelection == "Sgma" or rankSelection == "sgma":
                while loop3 == 0:
                    os.system("clear")
                    SGMAinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "MAIN" or rankSelection == "Main" or rankSelection == "Main":
                loop2 += 1
    elif categorySelection == "WO" or categorySelection == "Wo" or categorySelection == "wo":
        while loop2 == 0:
            loop3 -= 1
            loop3 = 0
            os.system("clear")
            printz("what Rank would you like to look at?\n\nWarrent Officer (WO1)\nChief Warrent Officer 2 (CW2)\nChief Warrent Officer 3 (CW3)\nChief Warrent Officer 4 (CW4)\nChief Warrent Officer 5 (CW5)\nBack to Category Menu (MAIN)")
            rankSelection = input('(Example "WO1"):')
            if rankSelection == "WO1" or rankSelection == "Wo1" or rankSelection == "wo1":
                while loop3 == 0:
                    os.system("clear")
                    WO1info()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "CW2" or rankSelection == "Cw2" or rankSelection == "cw2":
                while loop3 == 0:
                    os.system("clear")
                    CW2info()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "CW3" or rankSelection == "CW3" or rankSelection == "cw3":
                while loop3 == 0:
                    os.system("clear")
                    CW3info()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "CW4" or rankSelection == "Cw4" or rankSelection == "cw4":
                while loop3 == 0:
                    os.system("clear")
                    CW4info()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "CW5" or rankSelection == "Cw5" or rankSelection == "cw5":
                while loop3 == 0:
                    os.system("clear")
                    CW5info()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
    elif categorySelection == "CO" or categorySelection == "Co" or categorySelection == "co":
        while loop2 == 0:
            loop3 -= 1
            loop3 = 0
            os.system("clear")
            printz("what Rank would you like to look at?\n\nSecond Lieutenant (2LT)\nFirst Lieutenant (1LT)\nCaptain (CPT)\nMajor (MAJ)\nLieutenant Colonel (LTC)\nColonel (COL)\nBack to Category Menu (MAIN)")
            rankSelection = input('(Example "WO1"):')
            if rankSelection == "2LT" or rankSelection == "2lt" or rankSelection == "2lt":
                while loop3 == 0:
                    os.system("clear")
                    SLTinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "1LT" or rankSelection == "1lt" or rankSelection == "1lt":
                while loop3 == 0:
                    os.system("clear")
                    FLTinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "CPT" or rankSelection == "Cpt" or rankSelection == "cpt":
                while loop3 == 0:
                    os.system("clear")
                    CPTinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "MAJ" or rankSelection == "Maj" or rankSelection == "maj":
                while loop3 == 0:
                    os.system("clear")
                    MAJinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "LTC" or rankSelection == "Ltc" or rankSelection == "ltc":
                while loop3 == 0:
                    os.system("clear")
                    LTCinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "COL" or rankSelection == "Col" or rankSelection == "col":
                while loop3 == 0:
                    os.system("clear")
                    COLinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
    elif categorySelection == "G" or categorySelection == "g" or categorySelection == "g":
        while loop2 == 0:
            loop3 -= 1
            loop3 = 0
            os.system("clear")
            printz("what Rank would you like to look at?\n\nBrigadier General (BG)\nMajor General (MG)\nLieutenant General (LTG)\nGeneral (GEN)\nGeneral Of the Army (GOA)\nBack to Category Menu (MAIN)")
            rankSelection = input('(Example "BG"):')
            if rankSelection == "BG" or rankSelection == "Bg" or rankSelection == "bg":
                while loop3 == 0:
                    os.system("clear")
                    BGinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "MG" or rankSelection == "Mg" or rankSelection == "mg":
                while loop3 == 0:
                    os.system("clear")
                    MGinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "LTG" or rankSelection == "Ltg" or rankSelection == "ltg":
                while loop3 == 0:
                    os.system("clear")
                    LTGinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "GEN" or rankSelection == "Gen" or rankSelection == "gen":
                while loop3 == 0:
                    os.system("clear")
                    GENinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif rankSelection == "GOA" or rankSelection == "Goa" or rankSelection == "goa":
                while loop3 == 0:
                    os.system("clear")
                    GOAinfo()
                    exit = input("\n\nGo Back to the Previous Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
    elif categorySelection == "MM" or categorySelection == "Mm" or categorySelection == "mm":
        loop1 += 1