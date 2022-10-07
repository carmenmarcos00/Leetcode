class Logger(object):

    def __init__(self):
        self.dictionary = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        # Corner cases
        if ((message == "") or (timestamp == None)):
            return null
        
                                                           # Look the dictionary where the key is the message and the value is the timestamp
        previousMessage = self.dictionary.get(message)     # Get the timestamp of the message last time
        if (previousMessage!= None) :                      # If the message exist in the dictionary, check the timestamp
                if (timestamp - previousMessage >=10):
                    self.dictionary[message] = timestamp   # Change the timestamp of the last time it was indexed
                    return True
                else:                                      # If enough time hasn't passed return false
                    return False                
        else:                                              # If the message has never been displayed
            self.dictionary[message] = timestamp
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
