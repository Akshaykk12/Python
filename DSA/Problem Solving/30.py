"""
Problem: Given a collection of intervals, merge all overlapping intervals.
Input:
Intervals: [[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]

Explanation: Intervals [1,3] and [2,6] overlap, so they are merged into 
[1,6]. The others remain unchanged.
"""

def overlap(interval):
    output = []
    for i in range (len(interval)):
        if output != [] and output[-1][0] < interval[i][0] < output[-1][1] < interval[i][1]:
            output[-1] = [output[-1][0], interval[i][1]]
        else:
            output.append([interval[i][0],interval[i][1]])

    return output

intervals= [[1,3],[2,6],[8,10],[15,18]]
print(overlap(intervals))
