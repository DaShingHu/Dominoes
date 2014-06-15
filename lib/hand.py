
### AUthor: Dustin Hu
### DAte: 02-06-2014
### Purpose: To contain the Hand class, which depends upon the Domino class, which in turn, depends upon the Dice class

import domino

class Hand(object):
    ### Author: Dustin Hu
    ### Date: 02-06-2014
    ### Purpose: To be the class for the hand object, which is the remainder of teh game

    ### Fields:
    ####### dominoes: THe dominoes of the hand
    ####### size: The size of the dominoes to be drawn
    
    ### Methods:
    ####### drawSquare: Draws a empty square
    ####### __getitem__: Allows for indexing of the hand to access dominoes
    ####### __str__: Returns a string of a the list of domiones
    ####### sortHigh: sorts the dominoes from highest to lowest
    ####### dropDomino: Removes a domino with the given value from the hand.///
    ####### findValue: Returns the index of a give value in teh hand 
    ####### displayHand: Draws the hand on a canvas
    ####### addDomino: Adds a domino to the hand
    ####### getHandSize: Returns the length of the hand
    ####### valueOfDomino: Returns the value of the domino at the ith position 
    ####### __init__: The initnaliziation method of this hand

    def __getitem__(self, i):
        ### AUthor: DUstin Hu
        ### DAte: 07-06-2014
        ### Purpose: TO allow for indexing of the dominoes by indexing the hand, i.e, say hand.dominoes = [04, 55, 66], you cand do hand[0] to get 04.
        ### Input: Integer i to find at
        ### Output: VAlue of dominoes at i.
        return self.dominoes[i]

    def __str__(self):
        ### Author: Dustin Hu
        ### Date: 02-06-2014
        ### Purpose: To return a string of the list of dominose
        ### Input: None
        ### Output: A string containing the list of dominoes

        return str(self.dominoes)


    def sortHigh(self):
        ### AUthor: Dustin Hu
        ### Date: 02-06-2014
        ### Purpsoe: To sort the dominoes from lowest to highest
        ### Input: None
        ### Output: None
        self.dominoes = sorted(self.dominoes, key = lambda domino: int(domino.value))

    def dropDomino(self, value):
        ### Author: Dustin Hu
        ### DAte: 02-06-2014
        ### Purpose: To drop a domino from the hand
        ### Input: A value between 0 and 66 with neither digit being greater than 66
        ### OUtput: None
        if value in self.dominoes:
            # b = domino.Domino()
            # b.setValue(value)
            self.dominoes.remove(value)
#            del self.dominoes[self.findValue(value)]

    def findValue(self, x):
        ### AUthor: DUstin hu
        ### DAte: 02-06-2014
        ### Purpsoe: To find the index of the hand
        ### Input: THe value of which to find the index
        ### Output: The index at which it is at, lest it not be found, in which case, return -1
        value = [int(i.returnValue())for i in self.dominoes]
        if x in value:
            a = value.index(x, 0)
        else:
            a = -1
        return a

    def drawRectangle(self, canvas, x, y, orientation = "H"):
        #### AUthor: DUstin Hu
        ### DAte: 10-06-2014
        ### Purpose: To draw a rectangle
        ### Input; A canvas to draw, a x and a y to draw at, and an orientation to draw in.
        ### Output: None
        if orientation == "V":
            self.drawSquare(canvas, x, y)
            self.drawSquare(canvas, x, y + self.size)
        else:
            self.drawSquare(canvas, x, y)
            self.drawSquare(canvas, x + self.size, y)
            
    


    def drawSquare(self, canvas, x, y):
        ### AUtohr: DUstin Hu
        ### DAte: 10-06-2014
        ### Purpose:To draw a empty square
        ### Input: A canvas to draw to, an x and a y to draw to
        canvasMaxX = x + self.size
        canvasMaxY = y + self.size
        canvas.create_rectangle(x, y, x + self.size, y + self.size, width = 1, outline = "black", fill = "white")

    def displayHand(self, x, y , canvas,orientation = "V", faceup = True):
        ### Author: Dustin Hu
        ### Date: 02-06-2014
        ### Purpose: To display the hand onto a canvas
        ### Input: A x and a y, the top left corner of the hand, orientatoin which is either "V" or "H"
#        print self.dominoes
        if faceup == True:
            if orientation == "V":
                for i in xrange(0, len(self.dominoes)):
                    self.dominoes[i].displayValue(canvas, x = x, y = y + ( i + 1) *  (self.size + 5 ), orientation = "H")
            

            else:
                for i in xrange(0, len(self.dominoes)):
                    self.dominoes[i].displayValue(canvas, x = x + (i + 1) *  (self.size + 5), y = y, orientation = "V")
        else:
            if orientation == "V":
                for i in xrange(0, len(self.dominoes)):
                    self.drawRectangle(canvas, x, y + (i + 1)  * (self.size + 5), orientation = "H")
            else:
                for i in xrange(0, len(self.dominoes)):
                    self.drawRectangle(canvas, x + (i + 1) *  (self.size + 5 ), y , orientation = "V")


    def addDomino(self, domino):
        ### AUthor: Dustin Hu
        ### Date: 02-06-2014
        ### Purpose: To add a domino to the hand
        ### Input: A domino to add to the list
        ### Output: Nothing
        self.dominoes.append(domino)

    def getHandSize(self):
        ### AUthor: Dustin Hu
        ### Date: 02-06-2014
        ### Purpose: To return the hand's size
        ### Input: None
        ### Output: The size of the hand
        return len(self.dominoes)


    def valueOfDomino(self, i):
        ### Author: dustin Hu
        ### Date: 02-06-2014
        ### Purpose: To return the ith domino's value.
        ### Input: i, the value to look at
        ### Output: The value of the domino at i.
        return self.dominoes[i].returnValue()
        
    def __init__(self, lstDominoes, size = 30):
        ### AUthor: Dustin Hu
        ### Date: 02-06-2014
        ### Purpose: AN initalization procuderu, will initalize the hand 
        ### Input: A list of the dominoes to be in the hand, and the sizeto draw at.
        ### OUtput: None
        self.dominoes = lstDominoes
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 30
        

    
