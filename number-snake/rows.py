import sys

direction = "fwd"
row=1
for x in range(0,23000,3):
    out="Row " + str(row) + ": "

    if direction == "fwd":
        for y in range(1,4):
            out=out + "|" + str(x+y) + "|"
            direction = "back"

    else:
        for y in range(3,0,-1):
            out=out + "|" + str(x+y) + "|"
            direction = "fwd"

    print out

    row=row+1
