class Solution:
    # Takes in a string of commands: L (left), R (right), or _ (either left or right).
    # Find the furthest distance from the origin you can go if you replace each _ with
    # either a left or a right.
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # number of _ moves
        numUnknownMoves = 0
        currentPos = 0
        
        # iterate through commands
        for command in moves:
            # use match-case statement to check for each command
            match command:
                # case R: move to the right on a number line
                case "R":
                    currentPos += 1
                
                # case L: move to the left on a number line
                case "L":
                    currentPos -= 1
            
                # case _: increment number of _ moves
                case "_":
                    numUnknownMoves += 1
        
        return abs(currentPos) + numUnknownMoves
