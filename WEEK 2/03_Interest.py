"""
Program which calculate interest 
Author = Vraj Prajapati
"""
Principal = 175
years = 5
interest = 3

final_amount = Principal *(1+interest/100) ** years

print("Principal is $", Principal,sep="")
print("Final amount is " , final_amount,sep="")
