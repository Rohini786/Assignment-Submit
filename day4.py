H=int(input("Enter the altitude: "))
if(H<=1000):
  print("Safe to land")
elif(H>1000 and H<5000):
  print("Bring down to 1000ft")
else:
  print("Turn Around")
