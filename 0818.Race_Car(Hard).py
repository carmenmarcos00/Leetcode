class Solution:
    def racecar(self, target):
      
        # Done efficiently. As a binary tree, but only opening the branches of deceleration when I have surpased the target position
        queue = deque([(0, 1, 0)]) #position, speed, length                                   # Initialize the queue with the initial state
        visited = set()                                                                       # Create the visited set
            
        while queue:                                                                          # Iterate all the queue
            pos, speed, length = queue.popleft()                                                   # Pop the actual element
            if pos == target:                                                                      # If the position of the actual element is the target
                return length                                                                           # Finish and return length
            if (pos, speed) in visited:                                                            # If I have already visited this state (position, element)
                continue                                                                                # Do nothing about it
            visited.add((pos, speed))                                                              # Add this state to the set
            queue.append((pos+speed, speed*2, length+1))                                           # Append to the queue the next state if I accelerate   
            if (speed + pos> target and speed >0) or (speed + pos < target and speed < 0):         # En caso de que me haya pasado, tengo que volver atras 
                if(speed > 0):                                                                          # Decelero en el caso de que mi velocidad sea positiva
                    queue.append((pos, -1, length+1))                                                     # Add to the queue
                else:                                                                                   # Decelero en el caso de mi velocidad fuese negativa
                    queue.append((pos, 1, length+1))                                                      # Add to the queue
