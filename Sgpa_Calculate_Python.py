'''count your sgpa by python
   write program by Shilu Pradhan
    #TheCoderShilu'''
    
'''if you fail in a sub then grade point of that sub not to be taken''' 
   
sememstar = input("which Sememtar You Study :")
totalpaper = int(input("how many paper you study in semestar :"))
totalpoint = 0
totalcredit = 0

for i in range(1,totalpaper+1):
    subname = input(f"enter the Name of sub{i} :")
    submark = int(input(f"enter your mark of {subname}  :"))
    
    if(submark>=90):
            grade = int("10")
            print(f"the grade of {subname} is O")      
    elif(submark>=80):   
            grade = int("9")
            print(f"the grade of {subname} is A+")            
    elif(submark>=70):   
            grade = int("8")
            print(f"the grade of {subname} is A") 
    elif(submark>=60):   
            grade = int("7")
            print(f"the grade of {subname} is B+")
    elif(submark>=50):
            grade = int("6")
            print(f"the grade of {subname} is B")
    elif(submark>=40):
            grade = int("5")
            print(f"the grade of {subname} is C")
    elif(submark>=35):
            grade = int("4")
            print(f"the grade of {subname} is P")        
    else:
        grade = 0
    
    if(grade == 0):
       print(f"You are fail in {subname}")
    else:   
       subcredit = int(input(f"enter your credit of {subname}  :"))
       point = grade*subcredit
       totalpoint = point + totalpoint 
       totalcredit = subcredit + totalcredit  
    
if totalpoint == 0:
      print(f"You are fail in every subject\n Your SGPA not show!")
else:    
   sgpa = totalpoint/totalcredit
   print(f"Your SGPA of {sememstar} Semestar is : {sgpa}")
           
   