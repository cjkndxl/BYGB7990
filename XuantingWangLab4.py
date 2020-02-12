#Xuanting Wang Lab4
gasPrice = 3
milesPerGallon = 35

origin = input('Please enter your starting location:\n>>')
firstOrigin = origin
keepGoing = 'y'
tripCost = 0
outputStrings = []
while keepGoing == 'y':
    s = 'From ' +origin+', where will you travel?\n>>'
    nextLocation = input(s)
    st = 'How far away is ' +nextLocation+ ' from ' + origin +'?\n>>'
    distance = float(input(st))
    legPrice = distance/milesPerGallon*gasPrice
    outputString = origin + ' to ' + nextLocation + ' will cost ' + '${:,.2f}'.format(legPrice)
    outputStrings.append(outputString)
    tripCost += legPrice
    origin = nextLocation
    keepGoingQuestion = 'Will you be travelling beyond '+ nextLocation + '(Enter y for yes):\n>>'
    keepGoing = input(keepGoingQuestion)
print('Your entire trip from', firstOrigin, 'to', nextLocation, 'will cost', tripCost)
for leg in outputStrings:
    print(leg) 