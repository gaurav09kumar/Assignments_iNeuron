#PythonCode

#create a function that returns reversed string
def reverse_string(string_value):
    return ''.join(reversed(string_value))

print("Enter First Name");
x = (reverse_string(input())); #Dynamically take inputs from conosle

print("Enter Last Name");
y = (reverse_string(input())); #Dynamically take inputs from conosle

print (x +" "+ y);
