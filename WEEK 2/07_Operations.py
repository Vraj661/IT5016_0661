"""
Program which calculate the Operations  
Author = Vraj Prajapati
"""
print('''
+ Addition
- Subtraction
* Multiplication
/ Division
''')
A=int(input("Enter the value1:-"))
B=int(input("Enter the value2:-"))
Operation=input("Enter The Operator")
if Operation=="+":
	print(A+B)
elif Operation=="-":
	print(A+B)
elif Operation=="*":
	print(A*B)
elif Operation=="/":
 	print(A/B)
elif Operation=="//":
	print(A//B)
elif Operation=="%":
    print(A%B)
else:
    print("Invalide operation... please enter valid operation") 
