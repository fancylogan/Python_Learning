import re 

typein = "A123F"
if re.match ("\d+f|\d+F|\d+c|\d+C",typein):
    print ("1")
else:
    print ("2")