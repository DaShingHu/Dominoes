### AUthor: DUstin Hu
### DAte: 02-06-2014
### Purpose: To contain the Dice class

import random

class Die(object):
    ### Die Class
    ### Fields:
    ###### - Value: An integer between 0 and 6
    ###### - Size: An integer between 30 and 100
    ###### - Radius: The radius of the circle, equal to the size divided by 9
    ###### - Gap: The gap between circles and the edge, equal to the size divided by 10.

    ### Methods:
    ###### - getValue: Gets the value of the die from a user
    ###### - setValue: Sets the value of the die to a given amount
    ###### - setSize: Sets the size of the die to a new size between 30 and 100
    ###### - roll: Rolls the die, setting the value to a random one
    ###### - draw: Draws the die onto a  canvas
    
    

    def __init__(self, size = 50):
        ### Author: Dustin Hu
        ### Date: 22-04-2014
        ### Purpose: To initialize the die object.
        ### Input: A integer size from the program that creates it.
        ### Output: None
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 50
        self.radius = self.size / 9
        self.gap = self.size  / 10
        self.value = random.randint(0, 9)
            
    def __str__(self):
        ### Author: Dustin Hu
        ### Date: 22-04-2014
        ### Purpose: To print out the die object porperly
        ### Input: THe data elements within the object
        ### Output: A string with all the data elements.

        return "Size = " + str(self.size) + "\nRadius = " + str(self.radius) + "\nGap = " + str(self.gap) + "\nValue = " + str(self.value) + "\n"

    def getValue(self):
    ### Author: Dustin Hu
    ### Date: 22-04-2014
    ### Purpose: To get a positive integer value in the range of 1 to 6  from the user
    ### Input: The data elements within the object
    ### Output: The positive integer that has been intaken.
        
        blnExit = False
        while blnExit == False:
            intInput = raw_input("Please enter a valid integere between 1 and 6.\n>")
            if intInput.isdigit() == True:
                intInput = int(intInput)
                if intInput >= 0 and intInput <= 9:
                    self.value = intInput
                    blnExit = True
        
    def setValue(self, value = 1):
        ### AUthor: Dustin hu
        ### Date: 22-04-2014
        ### Purpose: To set the value of the die
        ### Input: THe data elements within the object
        ### Output: The modified data element
        
        if value >= 0 and value <= 9:
            self.value = value
        else:
            self.value = 0

    def setSize(self, size = 50):
        ### Author: Dustin Hu
        ### Date: 22-04-2014
        ### Purpose: To set the size of the die
        ### Input: An integer size between 30 and 100
        ### OUtput: A modified date object, with teh size set to the new size or a size set to 50 if it broke.
        if size >= 30 or size <= 100:
            self.size = size
            self.radius = self.size / 5
            self.gap = self.radius / 2
        else:
            self.size = 50
            self.radius = self.size / 8
            self.gap = self.radius / 2

    def roll(self):
        ### AUthor: Dustin Hu
        ### Date: 22-04-2014
        ### Purpose: To roll the die object, to change the value
        ### Input: THe data elements within the object
        ### Output: A modified data element
        self.value = random.randint(0, 9)




    def draw(self, canvas, x, y):
        ### Author: Dustin Hu
        ### Date: 22-04-2014
        ### Purpose: To draw the die object to a canvas
        ### Input: The data elements within the object, the canvas to draw upon, and the x and y for the top left of the die
        ### Output: A drawn ate object
        canvasMaxX = x + self.size
        canvasMaxY = y + self.size


        
        canvas.create_rectangle(x, y, x + self.size, y + self.size, width = 1, outline = "black", fill = "white")




        if self.value % 2 == 1:
            #### Middle x and y are treated as being the average of all 4 points of the square that is, (2x + self.size) / 2, and the same with the y.
            middleX = (2 * x + 30) / 2
            middleY = (2 * y + 30) / 2
            canvas.create_oval(middleX - 3, middleY - 3, middleX + 3, middleY + 3, outline = "black", fill = "black")

        if self.value >= 2:
            ### Draw circles at top left and bottom right
            canvas.create_oval(x + 3, y + 3, x + 9, y + 9, outline = "black", fill = "black")
            canvas.create_oval(canvasMaxX - 9, canvasMaxY - 9, canvasMaxX - 3, canvasMaxY - 3, outline = "black", fill = "black")
            if self.value >= 4:
                #### DRaws circles at bottom left and top right
                canvas.create_oval(x + 3, canvasMaxY - 9, x + 9, canvasMaxY - 3, outline = "black", fill = "black")
                canvas.create_oval(canvasMaxX - 9, y + 3, canvasMaxX - 3, y + 9, outline = "black", fill = "black")

                if self.value >= 6:
                    ### DRaws circles in the middle fo the sides
                    canvas.create_oval(x + 3, y + 12, x + 9, y + 18, outline = "black", fill = "black")
                    canvas.create_oval(canvasMaxX - 9, y + 12, canvasMaxX - 3, y + 18, outline = "black", fill = "black")

        if self.value >= 8:
            middleX = (2 * x + 30) / 2
            middleY = (2 * y + 30) / 2
            canvas.create_oval(middleX - 3, middleY - 3, middleX + 3, middleY + 3, outline = "black", fill = "black")


            canvas.create_oval(x + 12, y + 3, x + 18, y + 9, outline = "black", fill = "black")

        if self.value >= 9:
            canvas.create_oval(x + 12, canvasMaxY - 9, x + 18, canvasMaxY - 3, outline = "black", fill = "black")

                    # if self.value == 8:
                    #     ### Draws circel at the very top centre
                    #     canvas.create_oval(x + 12, y + 3, x + 18, y + 9, outline = "black", fill = "black")

                    #     if self.value == 9:
                    #         ### Draw circle at the very bottom centre
                    #         canvas.create_oval(x + 12, canvasMaxY - 9, x + 18, canvasMaxY - 3, outline = "black", fill = "black"
                            
                            

                        

            


        # if self.value >= 2:
        #     ### Draw circles at top left and bottom right
        #     canvas.create_oval(x + 5, y + 5, x + 15, y + 15, width = 1, outline = "black", fill = "black")
        #     canvas.create_oval(canvasMaxX - 5, canvasMaxY - 5, canvasMaxX - 15, canvasMaxY - 15, width = 1, outline = "black", fill = "black")

        #     if self.value >= 4:
        #         canvas.create_oval(canvasMaxX - 15, y + 5, canvasMaxX - 5, y + 30, width = 1, outline = "black", fill = "black")
        #         canvas.create_oval(x + 5, canvasMaxY - 15, x + 15, canvasMaxY - 5, width = 1, outline = "black", fill = "black")


        #         if self.value >= 6:
        #             canvas.create_oval(x + 5, y + 20, x + 15, y + 30, width = 1, outline = "black", fill = "black")
        #             canvas.create_oval(canvasMaxX - 15, y + 20, canvasMaxX - 5, y + 30, width = 1, outline = "black", fill = "black")
    

            
        
        
            
        # if self.value >= 2:
        #     ### Draw circles at top left and bottom right coordinates
        #     canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + 2 * self.radius, y + self.gap + 2 * self.radius, width = 1, outline = "black", fill = "black")
        #     canvas.create_oval(canvasMaxX - self.gap - 2 * self.radius, canvasMaxY - self.gap - 2 * self.radius, canvasMaxX - self.gap, canvasMaxY - self.gap, width = 1, outline = "black", fill = "black")
            
        #     if self.value >= 4:
        #         canvas.create_oval(x + self.gap, canvasMaxY - self.gap - 2 * self.radius, x + self.gap + 2 * self.radius, canvasMaxY - self.gap, width = 1, outline = "black", fill = "black")
        #         canvas.create_oval(canvasMaxX - self.gap - 2 * self.radius, y + self.gap, canvasMaxX - self.gap, y + self.gap + 2 * self.radius, width = 1, outline = "black", fill = "black")

        #         if self.value == 6:
        #             ### Centers of top and bottom circles
        #             circleMidY = (y + self.gap + canvasMaxY - self.gap) / 2
        #             canvas.create_oval(x + self.gap, circleMidY - self.radius, x + self.gap + 2 * self.radius, circleMidY + self.radius, width =1, outline = "black", fill = "black")
        #             canvas.create_oval(canvasMaxX - self.gap, circleMidY - self.radius, canvasMaxX - 2 * self.radius - self.gap, circleMidY + self.radius, width = 1, outline = "black", fill = "black")
            


    
    
