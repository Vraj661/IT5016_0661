'''
PROGRAM WHICH IS REVERSE
NAME VRAJ PRAJAPATI
'''
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def main():
    original_str = input("Enter a String : ")
    reversed_str = reverse_string(original_str)
    print(f"Original : {original_str}")
    print(f"Reversed : {reversed_str}")
    
main()