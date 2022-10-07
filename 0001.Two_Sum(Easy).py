    def twoSum(self, nums, target):
        hashmap = {}                      
        for i in range(len(nums)):            # Iterate all numbers
            complement = target - nums[i]         # Calculate the complement of the actual number
            if complement in hashmap:             # If that number is in the hashmap I have finish
                return [i, hashmap[complement]]    
            hashmap[nums[i]] = i                  #If the complementary has not been visited yet (in the hashmap) I add actual number
