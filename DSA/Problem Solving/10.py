"""
Shraddha Kapoor’s professor suggested that she study hard and prepare 
well for the lesson on seasons. If her professor says month then, she has 
to tell the name of the season corresponding to that month. So write the 
program to get the solution to the above task?
March to May – Spring Season
June to August – Summer Season
September to November – Autumn Season
December to February – Winter Season
Note: The entered month should be in the range of 1 to 12. If the user enters a 
month less than 1 or greater than 12 then the message “Invalid Month Entered”
should get displayed.

Sample Input 1:
Enter month: 6

Sample Output 1:
Season: Summer
"""

def get_season(month):
    if month>12 or month<1:
        return "Invalid Month Entered"
    else:
        if month == 3 or month == 4 or month == 5 :
            return "Season: Spring"
        elif month == 6 or month == 7 or month == 8 :
            return "Season: Summer"
        elif month == 9 or month == 10 or month == 11 :
            return "Season: Autumn"
        else:
            return "Season: Winter"

month = int(input("Enter month: "))
print(get_season(month))