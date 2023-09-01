class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # number of _ moves
        numUnknownMoves = 0
        currentPos = 0
        
        # iterate through commands
        for command in moves:
            # use match-case statement to check for each command
            match command:
                # case R: increment
                case "R":
                    currentPos += 1
                
                # case L: decrement
                case "L":
                    currentPos -= 1
            
                # case _: increment number of _ moves
                case "_":
                    numUnknownMoves += 1
        
        # check sign of current position
        if abs(currentPos) == currentPos:
            currentPos += numUnknownMoves
        else:
            currentPos -= numUnknownMoves
        
        # return absolute value of current position
        return abs(currentPos)
