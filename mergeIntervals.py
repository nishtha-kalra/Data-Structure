'''
Merge intervals: You are given a list of intervals, and the function should merge any overlapping intervals and return a list of the merged intervals.
intervals = [[15, 18], [2, 6], [1, 3], [8, 10]]
Output = [[1, 6], [8, 10], [15, 18]]
'''

def mergeIntervals(intervals):
    intervals.sort(key=lambda x:x[0])
    output = []
    for interval in intervals:
        if not output or output[-1][1] < interval[0]:
            output.append(interval)
        else:
            output[-1][1] = max(interval[1], output[-1][1])
    return (output)
    
    
intervals = [[15, 18], [2, 6], [1, 3], [8, 10]]
print('input:', intervals)
output = mergeIntervals(intervals)
print('output:', output)
