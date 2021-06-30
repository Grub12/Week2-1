grade = int(input('Please enter your PSTP grade:'))

if(grade >= 90):
  print('A1')
elif(grade >= 80 and grade < 90):
  print ('A2')
elif(grade >= 70 and grade < 80):
  print ('A3')
elif(grade >= 65 and grade < 70):
  print ('B1')
elif(grade >= 60 and grade < 65):
  print ('B2')
elif(grade >= 55 and grade < 60):
  print ('B3')
elif(grade >= 50 and grade < 55):
  print ('C1')
elif(grade >= 45 and grade < 50):
  print ('C2')
elif(grade >= 40 and grade < 45):
  print ('C3')
else:
  print('Unfortunately you failed, Fatality')
  
  