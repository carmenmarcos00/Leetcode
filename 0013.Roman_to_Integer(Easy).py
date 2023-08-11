

#Change just to check


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        previousValue = 99999
        actualValue = 0
        total = 0
        
        dictTranslations = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
            
        for romanNumber in s:                                                     # Iterate all the values in roman notation
            actualValue = dictTranslations[romanNumber]                          
            if (previousValue <actualValue):                                      # If actual value is bigger than the previous one I have to substract
                total = total - previousValue                                         # Substract the previous one that I already added
                total = total  + (actualValue - previousValue)                        # Add the diference between the previous and the actual
        
            else:
                total = total + actualValue                                       # If is smaller than the previous one I add the value
            previousValue = actualValue                                     
        return total                                                        # When all iterations are finished, return the value
