import re 

while True:
    a = input("typein:")
    if re.match ("\d+cm|\d+inch|\d+m|\d+foot *",a,re.I):
        print ("1")
    else:
        print ("2")