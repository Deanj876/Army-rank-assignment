import sys
import time
import os
def printz(text, delay=0.05):

    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

loop0 = 0

while loop0 == 0:
    os.system("clear")
    printz("Welcom to the United States Army Database with all the Infomation you need.\n\nAll of this Information is as of the year 2023 so be aware of that.\n\nWhat would you like to look at first: Rank (RANK)\nMOS/Job Contracts (MOS)\nor Sub-units/atatchments of the Army (Units)\n")
    mainInput = input('Example "Rank" :')

    if mainInput == "RANK" or mainInput == "Rank" or mainInput == "rank":
        import Rank
    elif mainInput == "MOS" or mainInput == "Mos" or mainInput == "mos":
        import MOS