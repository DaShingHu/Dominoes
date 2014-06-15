### AUthor: DUstin Hu
### DAte: 02-05-0214
### Purpose: To be the domino class

from dice import Die

class Domino(object):
    ### Author: Dustin Hu
    ### Date: 02-06-2014
    ### Purpose: To be the domino class

    ### Fields:
    ####### size: THe size of the domion, must be 2:1
    ####### lstDice: A tuple containing both the dice that this game is made up. 
    ####### value: The value of the domino
    

    ### Methods:
    ####### flip: Flips the domino
    ####### __repr__: Returns the value of teh domino
    ####### __str__: Returns the value of the domino
    ####### __eq__: Equality tester
    ####### drawDots: Draws the dots onto a given canvas
    ####### displayValue: Displays the dominoonto a canvas
    ####### updateValue: Updates the value of the domino
    ####### returnValue: Returns the value of the domino
    ####### setValue: Sets the value of the dice
    ####### __init__: INitalizes the program

    def flip(self):
        ### Author: DustiN hu
        ### DAte: 05-06-2014
        ### Purpsoe: To flip the domino
        ### Input: None
        ### Output: None
        self.setValue(d1 = int(str(self.value)[1]), d2 = int(str(self.value)[0]))
    
    def __repr__(self):
        ### AUthor: Dsutin Hu
        ### DAte: 04-06-2014
        ### Purpose: To return the string of the domino
        ### Input: None
        ### Output: A string of the domino
        return str(self.value)



    def __str__(self):
        ### AUthor: Dsutin Hu
        ### DAte: 04-06-2014
        ### Purpose: To return the string of the domino
        ### Input: None
        ### Output: A string of the domino
        return str(self.value)

        

    def __eq__(self, domino):
        ### Author: Dustin Hu
        ### DAte: 02-06-2014
        ### Purpose: To test equlaity between two dominos
        ### Input: A domino to test against.
        ### Output: A true or false value
        eq = False
        if type(domino) == Domino:
            if self.returnValue() == domino.returnValue() or self.returnValue() == domino.returnValue()[::-1]:
                eq = True
        elif type(domino) == int:
            if int(self.returnValue()) == domino or self.returnValue == str(domino)[::-1]:
                eq = True
        return eq
        

    def drawDots(self, die, x, y, canvas):
        ### Author: Dustin Hu
        ### Date: 02-06-2014
        ### Purpsoe: To draw the dots of the die
        ### Input: A die to draw, either 1 or 0, depending on which one that yo uwish to draw, an x and a y to draw at, and a canvas to draw on.
        self.lstDice[die].draw(canvas, x, y)
        

    def displayValue(self, canvas, x, y, orientation = "V", faceup = True, reverse = False):
        ### AUthor: Dsutin Hu
        ### DAte: 02-06-2014
        ### Purpose: To draw domion
        ### Input: A canvas to draw on, a x and a y, the top left corner, an orientation, either "V" or "H", for Veritacl or Horizontal, and finally, faceup, which is True if it... well, faces up. If faceup == False; do not draw dots.
        ### OUtput: None
        if reverse == False:
            if orientation == "V":
                self.lstDice[0].draw(canvas, x, y)
                self.lstDice[1].draw(canvas, x, y + self.size)
            else:
                self.lstDice[0].draw(canvas, x, y)
                self.lstDice[1].draw(canvas, x + self.size, y)
        else:
            if orientation == "V":
                self.lstDice[1].draw(canvas, x, y)
                self.lstDice[0].draw(canvas, x, y + self.size)
            else:
                self.lstDice[1].draw(canvas, x, y)
                self.lstDice[0].draw(canvas, x + self.size, y)
        

    

    def updateValue(self):
        ### AUThor: Dustin Hu
        ### DAte: 02-06-2014
        ### Purpose: To update the value of the Domino
        ### Input: None
        ### Output: None
        self.value = str(self.lstDice[0].value) + str(self.lstDice[1].value)
        

    def returnValue(self):
        ### AUthor: Dustin Hu
        ### Date: 02-06-2014
        ### Purpose: To return the current value of the domino
        ### Input: None
        ### Output: An integer value between 0 and 66 whereby all the digits are less than or equal to 6.
        value = self.value
        if self.value <= 9:
            value = "0" + str(self.value)
        return str(value)


    def setValue(self, d1 = 0, d2 = 0):
        ### Author: DUstin Hu
        ### DAte: 02-06-2014
        ### Purpose: To set the values of the dice
        ### INput: Two integers in the range of 0 to 6.
        ### Output: None
        if d1 >= 0 and 9 >= d1:
            self.lstDice[0].setValue(d1)
        if d2 >= 0 and 9 >= d2:
            self.lstDice[1].setValue(d2)
        self.updateValue()
        

    def __init__(self, size = 30):
        ### Author: Dustin Hup
        ### DAet: 02-06-2014
        ### Purpose: To initalize the dmion cass
        ### Input: Size, the size of the die.n
        ### Output: None
        self.size = size
        self.lstDice = [Die(size = self.size), Die(size = self.size)]
        self.value = int(str(self.lstDice[0].value) + str(self.lstDice[1].value))

