class Solution:
    
    
    def canAttendMeetings(self, intervals):
        
        intervals.sort()                                # Sort the list intervals
        
        for i in range(len(intervals) - 1):             # Iterate from 0 to length-1
            if intervals[i][1] > intervals[i + 1][0]:   # If the end of this intervarl is bigger than the start of the following interval
                return False                            # I cannot go to the meeting
        return True                                     # Otherwise in all cases, I can go to the meeting
            
