from astropy.cosmology import parameter
from tabulate import tabulate
personal = []
ap = []
ge = []
me = []
head_ge = ["EYMP ID", "NAME", "POST ASSIGNED"]
head_me = [["EYMP ID", "NAME", "POST ASSIGNED"]]
currentexp = []
workinghistory = []
timeinfo = []
salaryinfo = []
holiday = []
head_pd = ["EYMP. ID", "NAME", "PH. NO.", "HOMETOWN", "CURRENT CITY", "ADDRESS", "QUALIFICATION", "Gender"]
head_wh = ["EYMP. ID", "NAME", "WORK EXP", "PREVIOUS COMPANY NAME", "TIME PERIOD", "POST IN THAT COMPANY ","YEAR YOU LEFT THAT COMPANY"]
head_cd = ["EYMP. ID", "NAME", "POST ASSINGENED", "NET PACAKAGE GIVEN", " IN HAND SALARY", "PAYMENT MODE","TIME PERIOD OF CONTRACT", " HOLIDAYS ASSIGNED"]
x = int(input('''WELCOME TO CSE MANGMENT SYSTEM 🙏🙏

                 ENTER SECURITY KEY: '''))
if x == 1234568:
     def add():
            l = []
            global int
            global input
            global ppp
            ppp = []
            global pp
            pp = []
            A = "ID" + "[" + str(len(personal)) + "]"
            l.append(A)

            y = input('  ENTER  PERSONAL DETAILS \n'
                      '                                   \n'
                      '    ENTER FIRST NAME ::      ')
            y = y.upper()
            z = input("    ENTER LAST NAME  ::     ")
            z = z.upper()
            z_l = input("    ENTER D.O.B  ::     ")
            l.append(z_l)
            s = y + " " + z
            l.append(s)
            z = input("    ENTER PH. NO.  ::     ")
            l.append(z)
            g = input("    ENTER HOMETOWN  ::     ")
            l.append(g)
            C = input("    ENTER CURRUNT CITY  ::     ")
            l.append(C)
            j = input("    ENTER COMPLETE ADDRESS  ::     ")
            l.append(j)
            xx = input("    ENTER QUALIFICATION  ::     ")
            l.append(xx)
            o = input("    ENTER  Gender  ::     ")
            o = o.upper()
            l.append((o))
            if o == "MALE":
                A1 = "ID" + "[" + str(len(personal)) + "]"
                pp.append(A1)
                pp.append(s)
            if o == "FEMALE":
                A2 = "ID" + "[" + str(len(personal)) + "]"
                ppp.append(A2)
                ppp.append(s)
            personal.append(l)
            kk = input('''  ENTER  WORKING HISTORY  DETAILS 

     ENTER  NAME ::      ''')
        
            kk = kk.upper()
            i = []
            i.append(A)
            i.append(kk)
            y = input("     WITH EXP. OR NOT")
            y = y.upper()
            i.append(y)
            if y == "WITH":
                QW = input("      PREVIOUS COMPANY NAME   ")
                i.append(QW)
                YU = input("      TIME PERIOD  ")
                i.append(YU)
                io = input("      POST IN THAT COMPANY  ")
                i.append(io)
                r = input("      YEAR YOU LEFT THAT COMPANY   ")
                i.append(r)
                workinghistory.append(i)
            if y == "NOT":
                QW = "NONE"
                i.append(QW)
                YU = "NONE"
                i.append(YU)
                io = "NONE"
                i.append(io)
                r = "NONE"
                i.append(r)
                workinghistory.append(i)

            k3 = input('''  ENTER  CONTRACT DETAILS  DETAILS 

     ENTER  NAME ::      ''')

            O = []
            O.append(A)
            k3 = k3.upper()
            O.append(k3)
            N = input("    POST ASSINGENED")
            O.append(N)

            if o == "FEMALE":
                ppp.append(N)
            if o == "MALE":
                pp.append(N)
            ge.append(ppp)
            me.append(pp)

            K = input("    NET PACAKAGE GIVEN")
            O.append(K)
            U = input("    IN HAND SALARY")
            O.append(U)

            R = input("    PAYMENT MODE")
            O.append(R)
            P = input("    TIME PERIOD OF CONTRACT")
            O.append(P)

            bhen = input("    HOLIDAYS ASSIGNED")
            O.append(bhen)

            timeinfo.append(O)



     def retrive() :
            t = input(''' ENTER WHAT YOU WANT GET INFO OF EMPLOYEES TO  
                                     1.PERSONAL DETAILS 
                                     2.WORKING DETAILS
                                     3.CONTRACT DETAILS
                                     4.GENDER WISE
                                        ''')
            t = t.upper()
            if (t == "PERSONAL DETAILS"):
                a = input("Whole list or particular employee")
                a=a.lower()
                if a == "whole list":
                    print(tabulate(personal, headers=head_pd, tablefmt="grid"))
                elif a == "particular employee":
                    n = int(input("ENTER ID NO"))
                    poo = personal[n]
                    aa = [poo]
                    print(tabulate(aa, headers=head_pd, tablefmt="grid"))
                    print()
                    print()
            if (t == "WORKING DETAILS"):
                a = input("Whole list or particular employee")
                a=a.lower()
                if a == "whole list":
                    print(tabulate(workinghistory, headers=head_wh, tablefmt="grid"))
                elif a == "particular employee":
                    n = int(input("ENTER ID NO"))
                    poo = workinghistory[n]
                    aa = [poo]
                    print(tabulate(aa, headers=head_wh, tablefmt="grid"))
                    print()
                    print()

            if (t == "CONTRACT DETAILS"):

                a = input("Whole list or particular employee")
                a=a.lower()
                if a == "whole list":
                    print(tabulate(timeinfo, headers=head_cd, tablefmt="grid"))
                elif a == "particular employee":
                    n = int(input("ENTER ID NO"))
                    poo = timeinfo[n]
                    aa = [poo]
                    print(tabulate(aa, headers=head_pd, tablefmt="grid"))
                    print()
                    print()
            if (t == "GENDER WISE"):
                XXXC = input("ENTER MALE OR FEMALE LIST ")
                XXXC = XXXC.upper()
                if XXXC == "MALE":
                    a = input("Whole list or particular employee")
                    if a == "whole list":
                        print(tabulate(me, headers=head_me, tablefmt="grid"))
                    elif a == "particular employee":
                        n = int(input("ENTER ID NO"))
                        poo = me[n]
                        aa = [poo]
                        print(tabulate(aa, headers=head_me, tablefmt="grid"))
                        print()
                        print()
                if (XXXC == "FEMALE"):
                    a = input("Whole list or particular employee")
                    a=a.lower()
                    if a == "whole list":
                        print(tabulate(ge, headers=head_ge, tablefmt="grid"))
                    elif a == "particular employee":
                        n = int(input("ENTER ID NO"))
                        poo = ge[n]
                        aa = [poo]
                        print(tabulate(aa, headers=head_ge, tablefmt="grid"))
                        print()
                        print()
     def delete():
         print(" |CLEAR ALL| OR CLEAR DATA OF |SPECIFIC| ")
         B_I= input()
         B_I=B_I.upper()
         if (B_I == "CLEAR ALL"):
             currentexp.clear()
             workinghistory.clear()
             timeinfo.clear()
             salaryinfo.clear()
             personal.clear()
             ap.clear()
             ge.clear()
             me.clear()
         if (B_I=="SPECIFIC"):
             D_E=int(input("ENTER ID NO OF EMPLOYEE"))
             personal[D_E].clear()
             currentexp[D_E].clear()
             workinghistory[D_E].clear()
             timeinfo[D_E].clear()
             salaryinfo[D_E].clear()
             personal[D_E].clear()
             ap[D_E].clear()
             ge[D_E].clear()
             me[D_E].clear()
     def update():
         print(''' WHAT YOU WANT TO UPDATE 
                   1.PERSONAL DETAILS
                   2.WORKING HISTORY
                   3.CONTRACT DETAILS
                   ''')
         K_p=input()
         K_p=K_p.lower()
         U_E = int(input("ENTER ID NO OF EMPLOYEE     "))
         if(K_p=="personal details"):
             P_O= input("WANT TO UPDATE NAME OR NOT     ")
             P_O=P_O.lower()
             if P_O== "update":
                 personal[U_E][1]= input()
             P1_O = input("WANT TO UPDATE PH.NO OR NOT    " )
             P1_O = P1_O.lower()
             if P1_O == "update":
                 personal[U_E][2] = input()
             P2_O = input("WANT TO UPDATE HOMETOWN OR NOT   ")
             P2_O = P2_O.lower()
             if P2_O == "update":
                 personal[U_E][3] = input()
             P3_O = input("WANT TO UPDATE CURRENT CITY OR NOT    ")
             P3_O = P3_O.lower()
             if P3_O == "update":
                 personal[U_E][4] = input()
             P_O4 = input("WANT TO UPDATE ADRESS OR NOT")
             P_O4 = P_O4.lower()
             if P_O4 == "update":
                 personal[U_E][5] = input()
             P_O5= input("WANT TO UPDATE QUALIFICATION OR NOT")
             P_O5 = P_O5.lower()
             if P_O5 == "update":
                 personal[U_E][6] = input()
             P_O6 = input("WANT TO UPDATE GENDER OR NOT")
             P_O6 = P_O6.lower()
             if P_O6 == "update":
                 personal[U_E][7] = input()

         if(K_p=="working history"):
             W_O = input("WANT TO UPDATE NAME OR NOT     ")
             W_O = W_O.lower()
             if W_O == "update":
                 workinghistory[U_E][1] = input()
             W1_O = input("WANT TO UPDATE WORK EXP. OR NOT    ")
             W1_O = W1_O.lower()
             if W1_O == "update":
                 workinghistory[U_E][2] = input()
             W2_O = input("WANT TO UPDATE PREVIOUS COMPANY NAME OR NOT   ")
             W2_O = W2_O.lower()
             if W2_O == "update":
                 workinghistory[U_E][3] = input()
             W3_O = input("WANT TO UPDATE TIME PERIOD OR NOT    ")
             W3_O = W3_O.lower()
             if W3_O == "update":
                 workinghistory[U_E][4] = input()
             W_O4 = input("WANT TO UPDATE POST IN COMPANY OR NOT")
             W_O4 = W_O4.lower()
             if W_O4 == "update":
                 workinghistory[U_E][5] = input()
             W_O5 = input("WANT TO UPDATE YEAR YOU LEFT COMPANY OR NOT")
             W_O5 = W_O5.lower()
             if W_O5 == "update":
                 workinghistory[U_E][6] = input()
         if (K_p=="contract details") :
             C_O = input("WANT TO UPDATE NAME OR NOT     ")
             C_O = C_O.lower()
             if C_O == "update":
                 timeinfo[U_E][1] = input()
             C1_O = input("WANT TO UPDATE POST ASSIGNED OR NOT    ")
             C1_O = C1_O.lower()
             if C1_O == "update":
                 timeinfo[U_E][2] = input()
             C2_O = input("WANT TO UPDATE NET PACKAGE GIVEN OR NOT   ")
             C2_O = C2_O.lower()
             if C2_O == "update":
                 timeinfo[U_E][3] = input()
             C3_O = input("WANT TO UPDATE IN HAND SALARY OR NOT    ")
             C3_O = C3_O.lower()
             if C3_O == "update":
                 timeinfo[U_E][4] = input()
             C_O4 = input("WANT TO UPDATE PAYMENT MODE  OR NOT")
             C_O4 = C_O4.lower()
             if C_O4 == "update":
                 timeinfo[U_E][5] = input()
             C_O5 = input("WANT TO UPDATE TIME PERIOD OF CONTRACT OR NOT")
             C_O5 = C_O5.lower()
             if C_O5 == "update":
                 timeinfo[U_E][6] = input()
             C_O6 = input("WANT TO UPDATE HOLIDAY ASSIGNED OF CONTRACT OR NOT")
             C_O6 = C_O6.lower()
             if C_O6 == "update":
                timeinfo[U_E][7] = input()







     while True:
          print('''ENTER WHAT YOU WANT TO DO
                         1.ADD 
                         2.GET_INFO
                         3.DELETE
                         4.UPDATE
                        
                             ''')
          t22=""
          t22=input()
          t22 = t22.lower()
          if (t22 == "add"):
              add()
          if (t22=="delete"):
              delete()
          if (t22 == "get_info"):
              retrive()
          if(t22=="updates") :
              update()