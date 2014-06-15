### AUthor: Dustin Hu
### DAte: 04-06-2014
### Purpose: To store the domino game class

import domino
import hand
import random
import table
import time
import collections

class DominoError(Exception):
    ### Author: Dustin Hu
    ### DAte: 12-06-2014
    ### Purpose: To flag a domino error
    pass
        

class DominoGame(object):
    ### Author: Dustin Hu
    ### DAte: 04-06-2014
    ### Purpose: To hold the DominoGame class
    
    ### Fields:
    ####### pHand: The player's hand
    ####### c1Hand: Compuetr 1's hand
    ####### c2Hand: Computer 2's hand
    ####### c3Hand: Computer 3's hand
    ####### available: A list of all the remaining dominoes to be handed out
    ####### table: The dominoes in the game
    

    ### Methods:
    ####### playable: Checks whetehr or not a move is valid
    ####### calcScore: Calculates the score 
    ####### playerTurn: Player's turn
    ####### startGame: Starts the game
    ####### isMove: Gets whether or not the computer should play
    ####### getDomino: Gets a domino for the computer to play
    ####### cpuTurn: Computer plays
    ####### genRandHand: Generatse a random list of teh available dominos
    ####### __init__: Initalizes the class

    def playable(self, hand, domino, placement):
        ### Author: DSUtin Hu
        ### Input: 11-06-2014
        ### Purpose: To check wehter or not a domino is valid
        ### Input: A hand to check wth, the domino that you want to play, and the placement o said domino
        ### Output: True or false
        playable = True
        
        placement = placement.upper()
        ends = self.table.getEnds()
        leftEnd = str(int(ends[0]))
        rightEnd = str(int(ends[1]))
        playable = []
        for domino in hand.dominoes:
            if int(domino.value) // 10 > 0:
                dom = str(domino)
            else:
                dom = "0" + str(domino)
                
            if dom[0] == rightEnd:
                playable.append((domino, "R"))
            elif dom[1] == leftEnd:
                playable.append((domino, "L"))
        print playable
        print (domino, placement)
        if (domino, placement) not in playable:
            playable = False
            
        return playable
        


    def calcScore(self, loser1, loser2, loser3):
        ### Author: Dustin Hu
        ### DAte: 11-06-2014
        ### Input: The three losers to calculate from
        ### Output: An integer value, the sum of all the hand's dominoes
        score = 0
        loser1 = [int(i.returnValue()) for i in loser1.dominoes]
        for i in loser1:
            score = score + i // 10
            score = score + i % 10
        loser2 = [int(i.returnValue()) for i in loser2.dominoes]
        for i in loser2:
            score = score + i // 10
            score = score + i % 10
        loser3 = [int(i.returnValue()) for i in loser3.dominoes]
        for i in loser3:
            score = score + i // 10
            score = score + i % 10
        return score
        
            
        

    def playerTurn(self, value = 0, position = False, index = 1, placement = "L"):
        ### Author: DUstin Hu
        ### Date: 08-06-2014
        ### Purpose: To allow the player to play a domion
        ### Input: The value tha the player wishes to play (A string) and teh placement, which end of the chain they wish it tobe placed on.
        ### OUtput: None

        if position == False:
            if value in self.pHand:
                placement = placement.upper()
                ends = self.table.getEnds()
                leftEnd = str(int(ends[0]))
                rightEnd = str(int(ends[1]))
                playable = []
                
                for domino in self.pHand.dominoes:
                    
                    if int(domino.value) // 10 > 0:
                        dom = str(domino)
                    else:
                        dom = "0" + str(domino)
                        
                    if dom[0] == rightEnd:
                        playable.append((domino, "R"))
                    elif dom[1] == leftEnd:
                        playable.append((domino, "L"))
                    
                # if dom[0] == leftEnd or dom[0] == rightEnd or dom[1] == leftEnd or dom[1] == rightEnd:
                #     if dom[0] == leftEnd:
                #         domino.flip()
                #         playable.append((domino, "L"))
                #     elif dom[0] == rightEnd:
                #         playable.append((domino, "R"))
                #     elif dom[1] == leftEnd:
                #         playable.append((domino, "L"))
                #     else:
                #         domino.flip()
                #         playable.append((domino, "R"))

            if (value, placement) in playable:
                self.table.addToTable(self.pHand[self.pHand.findValue(value)], placement)
                self.pHand.dropDomino(value)
            else:
                raise DominoError
        else:
            leftEnd = int(self.table.getEnds()[0])
            rightEnd = int(self.table.getEnds()[1])
            domino = int(self.pHand.dominoes[index].returnValue())
            if placement == "L":
                if leftEnd == domino % 10:
                    self.table.addToTable(self.pHand.dominoes[index], placement)
                    self.pHand.dropDomino(int(self.pHand.dominoes[index].returnValue()))
                else:
                    raise DominoError
            else:
                if rightEnd == domino // 10:
                    self.table.addToTable(self.pHand.dominoes[index], placement)
                    self.pHand.dropDomino(int(self.pHand.dominoes[index].returnValue()))
                else:
                    raise DominoError

                    
                
            


    def startGame(self):
        ### AUthor: Dustin Hu
        ### DAte: 08-06-2014
        ### Purpose: TO star the game
        ### Input: None
        ### Output: None
        startDomino = domino.Domino()
        startDomino.setValue(9, 9)
        self.table.addToTable(startDomino)
        

        # if self.pHand.findValue(66) != -1:
        #     self.table.addToTable(self.pHand[self.pHand.findValue(66)])
        #     self.pHand.dropDomino(66)
        # # elif self.c1Hand.findValue(66) != -1:
        #     self.table.addToTable(self.c1Hand[self.c1Hand.findValue(66)])
        #     self.c1Hand.dropDomino(66)
#        elif self.c2Hand.findValue(66) != -1:
            # self.table.addToTable(self.c2Hand[self.c2Hand.findValue(66)])
        #     # self.c2Hand.dropDomino(66)
        # else:
        #     self.table.addToTable(self.c3Hand[self.c3Hand.findValue(66)])
        #     self.c3Hand.dropDomino(66)
        
            

    def isMove(self):
        ### Author: DUstin hu
        ### Date: 05-06-2014
        ### Purpsoe: To check whether or not the computer should play or if it should just pass
        ### Input: None
        ### Output: Boolean true or false, true if it should play, false otherwise

        #### Basically, go through all the available dominoes in the game, get the ends of teh table
        #### and then check to see if you can make a list that excludes the opponent.
        pass

    def getDomino(self):
        ### Author: Dustin Hu
        ### Date: 05-06-2014
        ### Purpose: To get a domino for the computer to play, allowing for teamwork
        ### Input: None
        ### Output: A domino to play
        domino = None
        playOrder = []
        leftEnd = int(self.table.getEnds()[0])
        rightEnd = int(self.table.getEnds()[1])
        
        #### Basically, loop through each one of the computres, see if any one
        #### of them has a domino that will fit, and then if they do, skip until that can be reached.
        #### Preferably, you'd have a series of 3 playmoves in one, and they'd "See" your available 
        #### dominoes, such taht they can play tehir stuff.
        for i in xrange(0, len(self.c1Hand.dominoes)):
            pass

    def cpuTurn(self, cpuhand):
        ### Author: Dustin Hu
        ### DAte: 05-06-2014
        ### Purpose: T obe the computer's hand
        ### Input: Computer's hand ot use
        ### Output: None
        ends = self.table.getEnds()
        leftEnd = str(int(ends[0]))
        rightEnd = str(int(ends[1]))
        playable = []
        # print "leftEnd = ", leftEnd
        # print "rightEnd = ", rightEnd
        for domino in cpuhand.dominoes:
            dom = str(domino)
            if dom[0] == leftEnd or dom[0] == rightEnd:
                if dom[0] == leftEnd:
                    domino.flip()
                    dom = str(domino)
                    playable.append((domino, "L"))
#                    print "dom[0] == leftEnd"
                else:
                    playable.append((domino, "R"))
                #     print "dom[0] == rigtEnd"
                # print domino
            if dom[1] == leftEnd or dom[1] == rightEnd:
                if dom[1] == leftEnd:
                    playable.append((domino, "L"))
 #                   print "dom[1] == leftEnd"
                else:
                    domino.flip()
                    dom = str(domino)
                    playable.append((domino, "R"))
#                    print "dom[1] == rightEnd"
        #### Stupid AI, just plays whatever
        #### If you want smart, replace this with osmetihng else
        if len(playable) != 0:
            # print playable
            # print playable[0]
            # print playable[0][0]
            cpuhand.dropDomino(int(playable[0][0].returnValue()))
            self.table.addToTable(playable[0][0], placement = playable[0][1])
#        print "Computer is thinking....."




            
#            dom = str(cpuhand.dominoes[i])
            # print dom
            # if dom[1] == leftEnd:
            #     print "dom[1] == leftEnd"
            #     self.table.addToTable(cpuhand.dominoes[i], placement = "L")
            #     cpuhand.dropDomino(int(cpuhand.dominoes[i].value))

            # elif dom[0] == rightEnd:
            #     print "dom[0] == rightEnd"
            #     self.table.addToTable(cpuhand.dominoes[i], placement = "R")
            #     cpuhand.dropDomino(int(cpuhand.dominoes[i].value))
            # elif dom[::-1][1] == leftEnd:
            #     print "dom[::-1][1] == leftEnd"
            #     cpuhand.dominoes[i].flip()
            #     self.table.addToTable(cpuhand, dominoes[i], placement = "L")
            #     cpuhand.dropDomino(int(cpuhand.dominoes[i].value))
            # elif dom[::-1][0] == rightEnd:
            #     print "dom[::-1][0] == rightEnd"
            #     cpuhand.dominoes[i].flip()
            #     self.table.addToTable(cpuhand, dominoes[i], placement = "R")
            #     cpuhand.dropDomino(int(cpuhand.dominoes[i].value))
            # else:
            #     pass
                                
                                
            # if dom[1] == leftEnd or dom[0] == rightEnd:
            #     if dom[0] == leftEnd:
            #         self.addToTable(cpuhand.dominoes[i], placement = "L")
            #     else:
            #         self.addToTable(cpuhand.dominoes[i], placement = "R")
            #     cpuhand.dropDomino(int(cpuhand.dominoes[i].value))
                
            # if dom[0][::-1] == leftEnd or dom[1]
                
    def genRandHand(self):
        ### Author: Dustin Hu
        ### DAte: 04-06-2014
        ### Purpose: To generate a random list of available dominoes
        ### Input: None
        ### Output: A list of dominoes
        values = []
        while len(values) != 14:
            i = random.randint(0, 99)
            if self.available[i] == True:
                tempDomino = domino.Domino()
                tempDomino.setValue(i // 10, i % 10)
                values.append(tempDomino)
        return values
        #     i = 19
        #     while (i % 10 <= 6 ) == False:
        #         i = random.randint(0, 66)
        #     if self.available[i] == True:
        #         if str(i)[0] <= str(i)[-1]:
        #             self.available[i] = False
        #             c = i
        #             if c <= 9:
        #                 c = "0" + str(c)
        #             else:
        #                 c = str(c)
        #             tempDomino = domino.Domino()
        #             tempDomino.setValue(int(c[0]), int(c[1]))
        #             values.append(tempDomino)
        # return values
                    

    def __init__(self):
        ### Atuhor: Dustin Hu
        ### Date: 04-06-2014
        ### Purpose: To initalize the dominogame
        ### Input: None
        ### Output: None
        self.available = []

        ### Creates the available cards
        for i in xrange(0, 100):
            if i % 10 >= i // 10:
                self.available.append(True)
            else:
                self.available.append(False)


        self.table = table.Table()
        self.pHand = hand.Hand(self.genRandHand())
        self.c1Hand = hand.Hand(self.genRandHand())
        self.c2Hand = hand.Hand(self.genRandHand())
        self.c3Hand = hand.Hand(self.genRandHand())
                


        
#### IGNORE EVERYTHING BELOW THIS POINT 
def test():
    for i in xrange(0, 3000):
        a = DominoGame()
        b = set(a.pHand)
        c = set(a.c1Hand)
        d = set(a.c2Hand)
        e = set(a.c3Hand)
        if len(b.intersection(c)) != 0:
            print "Failed at i"
            print b, c, d, e
            return
        if len(b.intersection(d)) != 0:
            print "Failed at i"
            print b, c, d, e
            return

        if len(b.intersection(e)) != 0:
            print "Failed at i"
            print b, c, d, e
            return

        if len(c.intersection(d)) != 0:
            print "Failed at i"
            print b, c, d, e
            return

        if len(c.intersection(e)) != 0:
            print "Failed at i"
            print b, c, d, e
            return
            
