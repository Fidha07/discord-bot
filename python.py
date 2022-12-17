import datetime
import re
from datetime import datetime
text = input("enter a string")
date=str(re.findall(r'\d+/\d+/\d+',text))

def alert(date):
    cdate=datetime.now()
    if date==cdate:
        print("You have a meeting today")
    else:
        return
alert(date)