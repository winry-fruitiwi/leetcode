class Solution:
    # n friends are playing a game where they pass a ball to each other. each round,
    # they pass the ball roundNum*k indices to the right. this function calculates
    # which friends lost the game and returns a list of them in ascending order.
    # the winners get the ball, and the game ends when one friend gets the ball twice
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # define the list of friends with a range function. n+1 is due to range()
        # being uninclusive in Python
        friends = list(range(1, n + 1))
        
        # define the number of rounds, starting from 0
        roundNum = 0
        
        # define who gets the first ball, starting at index 0
        ballIndex = 0
        
        
        # iterate until a friend gets the ball twice. the only way is to loop forever
        # and then break the loop when a friend gets the ball
        while True:
            # calculate where the ball is going to go next
            ballIndex = (ballIndex + roundNum * k) % n
            
            # if the index there is already 0, break the loop because that friend
            # has already gotten the ball once
            if friends[ballIndex] == 0:
                break
            
            # otherwise, set the list at that index to 0 to show that friend has already
            # been passed the ball
            friends[ballIndex] = 0
            
            # increment the number of rounds
            roundNum += 1
        
        # the list of losers. gets filled out every time I find a non-zero valued friend
        losers = []
        
        # after the loop is done, the list looks something like [0, 2, 3, 0, 0, 6], so I need 
        # to remove all the zeroes
        for friend in friends:
            if friend > 0:
                losers.append(friend)
        
        return losers
