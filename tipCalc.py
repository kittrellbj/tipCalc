################################################################
# tipCalc - Don't forget to tip your waitress.                 #
# tipCalc calculates common tip percentages and displays       #
# appropriate tips based on levels of service provided.        #
# @author: Brian Kittrell                                      #
# @date: 08/11/2021                                            #
# @filename: tipCalc.py                                        #
################################################################

billTotal = float(input("Enter total bill: ")) # receive bill total from patron
tipPercentages = [.05,.10,.15,.20,.25] # list tip percentages
serviceQuality = ["Poor", "Below Average", "Standard", "Excellent", "Outstanding"] # Service quality list
i = 0 #iterator

print("Your bill is $" + str(billTotal) + ". Use the following chart to decide your tip: ") # Chart heading
for i, percent in enumerate(tipPercentages, start=0): # Chart constructor
    print("If service quality was " + serviceQuality[i] + ", the recommended tip is: $" + str(round(billTotal * tipPercentages[i], 2)))
