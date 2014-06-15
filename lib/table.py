### AUthor: DUstin Hu
### DAte: 03-06-2014
### Purpsoe: To contain the table class of the Domino game

import hand
import domino

class Table(object):
    ### AUthor: Dustin Hu
    ### Date: 03-06-2014
    ### Purpose: To be the Table class

    ### Fields:
    ####### table: An array that can contain up to 28 dominoes.
    ####### size: The number of dominoes curerntly played
    ####### leftEnd: The leftmost domino's value
    ####### rightEnd: THe rightmost domion's value

    ### MethodS:
    ####### getCurrRight: Gets the current right x, y
    ####### checkInnerValid: Checks the validity of the list itself
    ####### drawTable: Draws the table, given the size of the canvas.
    ####### __str__: Returns the table and size
    ####### getEnds: Gets the ends of the table
    ####### checkValid: Checks if the move is valid
    ####### update: Updates the table
    ####### addToTable: Adds a domino to the table
    ####### __init__: THe initalization method  of the table class

    def getCurrRight(self, size):
        ### Author: DUsitn Hu
        ### Date: 13-06-2014
        ### Purpose: To get the coordinates of th ecurrent right end of the chain
        ### Input: Size, canvas#
        ### OUtput: tuple containing x, y, and a direction

        ### Jujst drawTable with displays removed.
        endX = size - 60
        startX = 130
        direction = "R"
        currX = 130
        currY = 130
        for i in xrange(0, len(self.table)):
            if direction == "R":
                currX = currX + 60
                if currX >= endX:
                    direction = "DR"
                    currX= currX - 30
                    currY = currY + 30
            elif direction == "DR":
                currY = currY + 30
                currX =  currX - 60
                direction = "L"
            elif direction == "L":
                currX = currX - 60
                if currX <= startX:
                    currY = currY + 30
                    currX = currX - 60
                    direction = "DL"
            elif direction == "DL":
                currY = currY - 30
                currX = currX + 90
                currY = currY + 60
                direction = "R"
        return (currX, currY, direction)


    def checkInnerValid(self):
        ### AUthor: DUstin hu
        ### Date: 10-06-2014
        ### Purpose: To check validity of the dominoes within the table
        ### Input: None
        ### Output: True or false
        valid = True
        for i in xrange(0, len(self.table) - 1):
            if i != 0:
                if self.table[i].value[1] != self.table[i + 1].value[0]:
                    valid = False
        return valid

        

    def drawTable(self, size, canvas):
        ### Author: Dustin Hu
        ### DAte: 09-06-2014
        ### Purpose: To draw the table
        ### Input: The size of the canvas to draw to and a canvas to draw to
        ### Output: None
        endX = size - 60
        startX = 130
        direction = "R"
        currX = 130
        currY = 130
        # startX = 30
        # direction = "R"
        # currX = 30
        # currY = 30
        for i in xrange(0, len(self.table)):
            if direction == "R":
                self.table[i].displayValue(canvas, currX, currY, orientation = "H")
                currX = currX + 60
                if currX >= endX:
                    direction = "DR"
                    currX= currX - 30
                    currY = currY + 30
            elif direction == "DR":
                self.table[i].displayValue(canvas, currX, currY, orientation = "V")
                currY = currY + 30
                currX =  currX - 60
                direction = "L"
            elif direction == "L":
                self.table[i].displayValue(canvas, currX, currY, orientation = "H", reverse = True)
                currX = currX - 60
                if currX <= startX:
                    currY = currY + 30
                    currX = currX - 60
                    direction = "DL"
            elif direction == "DL":
                currY = currY - 30
                currX = currX + 90
                self.table[i].displayValue(canvas, currX, currY, orientation = "V")
                currY = currY + 60
                direction = "R"
        
            


    def __str__(self):
        ### AUThor: Dustin hu
        ### DAte; 09-06-2014
        ### Puproes: To print out the table
        ### Input: None
        ### Output: A String containing the table and size
        return "table: " +  str(self.table) +  "\nsize:" +  str(self.size )

    def getEnds(self):
        ### AUthor: Dustin Hu
        ### Date: 05-06-2014
        ### Purpose: To get teh ends of the list
        ### Input:None
        ### Output: A tuple containg two integers
        return (self.leftEnd, self.rightEnd)

    def checkValid(self, domino, placement):
        ### Author: DUsitn UH
        ### DAte: 05-06-2014
        ### Purpose: To cehck if teh move is valid
        ### Input: None
        ### Output: Boolean true or false
        valid = True
#        print "In check valid"
        if str(domino.returnValue()) != "66":
            if placement == "L":
                # print "Placement = \"L\""
                # print str(domino.returnValue())[1], self.leftEnd
                if str(domino.returnValue())[1] != str(self.leftEnd):
#                    print str(domino.returnValue())[1]
                    valid = False
            if placement == "R":
                # print "Placement = \"R\""
                # print str(domino.returnValue())[0], self.rightEnd
                if str(domino.returnValue())[0] != str(self.rightEnd):
                    # print str(domino.returnValue())[0]
                    # print self.rightEnd
                    valid = False
        return valid
            

    def update(self):
        ### Author: DUstin Hu
        ### Date: 03-06-0214
        ### Purpose: To update the table
        ### Input: None
        ### Output: None
        self.size = len(self.table)
        self.leftEnd = int(self.table[0].value) // 10
        self.rightEnd = int(self.table[-1].value) % 10
            

    def addToTable(self, domino, placement = "L"):
        ### AUthor: DUstin Hu
        ### Date: 03-06-2014
        ### Purpose: To add a domino to the table
        ### Input: A domino to add and to add it either to the leftost or the rightmost.
        ### Output: None

        if self.checkValid(domino, placement) == True:
            if placement == "L":
                self.table.insert(0, domino)
            else:
                self.table.append(domino)
            self.update()
        else:
            print "Error"



    
    def __init__(self):
        ### Author: Dustin Hu
        ### Date: 03-06-2014
        ### Purpose: To initalize the table object
        ### Input: None
        ### Output: None
        self.table = []
        self.size = len(self.table)
        self.leftEnd = 0
        self.rightEnd = 0


    

        
