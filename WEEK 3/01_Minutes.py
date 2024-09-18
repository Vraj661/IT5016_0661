"""
Program which calculate Minutes using function
Author = Vraj Prajapati
"""

def get_minutes(hours , minutes):
    total = hours*60 + minutes
    return total

total_minutes = get_minutes(5,30)
print(total_minutes)