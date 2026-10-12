class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        #we are going to go through each interval in our intervals list, and check whether the end of interval i is greater than the start of i + 1, if it's the case, we create a new list [start i, end i + 1] and we append it to our result list, if not we just append both lists to our list.

        #first we create our result list:

        intervals.sort()
        result = []
        result.append(intervals[0])

        print(result)
        #then we check each list in intervals and apply the algo explained earlier:
        
        for start, end in intervals[1:]:
            last_end = result[-1][1]
            if last_end >= start:
                new_interval = [result[-1][0], max(last_end, end)]
                result[-1] = new_interval
            else:
                result.append([start, end])
            
       
        return result
       
            
                
            
                
            
        