"""
Problem: Given a sequence of up and down steps during a hike, determine 
the number of valleys traversed.

Input:
8
UDDDUDUU

Output: 1

Explanation: A valley is a sequence of consecutive steps below sea level. 
The example describes a single valley
"""

def count_valleys(steps, path):
    level = 0
    valley = 0
    for i in path:
        if i == "U":
            level += 1
            
        else:
            level -= 1
            if valley == 0:
                valley += 1
                
    return valley

        

steps = 8
path = "UDDDUDUU"
valleys_traversed = count_valleys(steps, path)
print(valleys_traversed)  
