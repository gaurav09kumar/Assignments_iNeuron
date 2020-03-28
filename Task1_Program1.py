#PythonCode

#create a empty list
z = []

#create a for loop to iterate between the range of numbers
for x in range (2000,3200):
    if(x%7==0) and (x%5==0):
        z.append(str(x));
print (','.join(z));
