f1=1
f2=1
f3=f1+f2
print(f1)
print(f2)
print(f3)
while f3<100:
      f1=f2
      f2=f3
      f3=f1+f2
      if f3>100:
         break
      print(f3)

