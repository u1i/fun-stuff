#!/usr/bin/python

# Nice little game, built using Python
# Introduction & rules: https://boardgamegeek.com/boardgame/432/6-nimmt
# written on a long plane ride, obviously in the absence of online Python references & cheat sheets

import random
from subprocess import call

ox_cards={"1":"1","2":"1","3":"2","4":"1","5":"1","6":"1","7":"1","8":"3","9":"1","10":"2","11":"1","12":"1","13":"4","14":"1","15":"1","16":"1","17":"1","18":"1","19":"1","20":"1","21":"1","22":"5","23":"1","24":"1","25":"1","26":"1","27":"1","28":"1","29":"2","30":"1","31":"4","32":"2","33":"1","34":"1","35":"1","36":"1","37":"2","38":"1","39":"1","40":"1","41":"2","42":"1","43":"1","44":"1","45":"3","46":"1","47":"1","48":"1","49":"1","50":"1","51":"1","52":"2","53":"1","54":"1","55":"5","56":"1","57":"1","58":"1","59":"1","60":"1","61":"1","62":"1","63":"1","64":"1","65":"1","66":"1","67":"1","68":"2","69":"1","70":"1","71":"2","72":"1","73":"1","74":"1","75":"3","76":"1","77":"4","78":"1","79":"1","80":"1","81":"1","82":"1","83":"1","84":"1","85":"2","86":"1","87":"1","88":"1","89":"1","90":"1","91":"1","92":"1","93":"2","94":"5","95":"1","96":"1","97":"1","98":"1","99":"1","100":"2","101":"1","102":"3","103":"1","104":"1","105":"1","106":"1","107":"1","108":"4","109":"1","110":"2","111":"1","112":"1","113":"1","114":"1","115":"1","116":"1","117":"1","118":"1","119":"1","120":"1",}

my_cards=[]
your_cards=[]
my_ox=0
your_ox=0

stack=[]

def get_ox_for_row(count_ox_row):
    oxen=0
    for card in count_ox_row:
        # print str(card) + " " + str(ox_for_card(card))
        oxen = oxen + int(ox_for_card(card))

    return oxen

def ox_for_card(card):
    return ox_cards[str(card)]

def how_many_cards(stack_or_row):
    c=0
    for d in stack_or_row:
        c=c+1
    return c

def is_card_in_deck(card, card_stack):
    found=False
    for c in card_stack:
            if str(c) == str(card):
                found=True
                break
    return found

def take_a_card_from_the_stack(card_stack):
    card = random.choice(card_stack)
    new_stack=[]

    for c in card_stack:
        if c != card:
            new_stack.append(c)

    return card,new_stack

def get_last_card_from_row(row):
    c = how_many_cards(row)
    return row[c-1]

def play_card_row(card):
    pcard = int(card)

    found_a_place=False

    good_rows=[]

    for r in range(5):
            current_row=rows[r]
            # print str(r) + " : " + str(current_row)
            lastcard = int(get_last_card_from_row(current_row))

            if lastcard > pcard:
                # print "Row " + str(r) + " is not good"
                dummy=7
            else:
                found_a_place = True
                delta = pcard - lastcard
                # print "Row " + str(r) + " is good, delta " + str(delta)
                good_rows.append([r,delta])

    if not found_a_place:
        return -1

    smallest_delta=9999
    best_row=-1

    for r in good_rows:
        rnum, rdelta = r

        # print "Row " + str(rnum)
        # print "Delta " + str(rdelta)

        if rdelta < smallest_delta:
            smallest_delta = rdelta
            best_row = rnum

    return best_row
    # print "Best row is " + str(best_row)

def append_card_to_row(pcard, row_to_put_card, rowsdata):
    new_rows=[]

    rc=0
    for r in rowsdata:
        #print r
        crow=[]
        for crow_data in r:
            #print crow_data
            crow.append(crow_data)

        if rc == row_to_put_card:
            crow.append(int(pcard))

        new_rows.append(crow)
        rc=rc+1

    return new_rows

def make_card_the_first_in_row(pcard, row_to_put_card, rowsdata):
    new_rows=[]

    rc=0
    for r in rowsdata:
        #print r
        crow=[]

        if rc == row_to_put_card:
            crow.append(int(pcard))
        else:
            for crow_data in r:
                #print crow_data
                crow.append(crow_data)
        new_rows.append(crow)
        rc=rc+1

    return new_rows

def remove_card(which_card, cardstack):
    new_stack=[]

    for ccard in cardstack:
        if int (ccard) != int(which_card):
            new_stack.append(int(ccard))

    return new_stack

def get_lowest_ox_row(rows):

    lowest_ox = 999999
    lowest_row = -1
    current_row = 0
    for r in rows:
        ox_for_row = get_ox_for_row(r)
        if ox_for_row < lowest_ox:
            lowest_ox = ox_for_row
            lowest_row = current_row

        current_row = current_row + 1

    return lowest_row


#############################
# Create a stack of 120 cards
c=1
while c <= 120:
    stack.append(c)
    c=c+1

# Hand out ten cards for each player

for h in range(10):
    new_card, stack = take_a_card_from_the_stack(stack)
    your_cards.append(new_card)

    # print "You got card " + str(new_card)

    new_card, stack = take_a_card_from_the_stack(stack)
    my_cards.append(new_card)

    # print "I got card " + str(new_card)

# 5 rows of cards
row1=[]
row2=[]
row3=[]
row4=[]
row5=[]

rows=[]

new_card, stack = take_a_card_from_the_stack(stack)
row1.append(new_card)

new_card, stack = take_a_card_from_the_stack(stack)
row2.append(new_card)

new_card, stack = take_a_card_from_the_stack(stack)
row3.append(new_card)

new_card, stack = take_a_card_from_the_stack(stack)
row4.append(new_card)

new_card, stack = take_a_card_from_the_stack(stack)
row5.append(new_card)

rows.append(row1)
rows.append(row2)
rows.append(row3)
rows.append(row4)
rows.append(row5)

def player_card(attrib, player_cards, player_ox, in_rows, card_to_play):
    row_for_card = play_card_row(card_to_play)

    if attrib == "my":
        actor = "I"
    else:
        actor = "you"

    if row_for_card == -1:
        lowest_row = get_lowest_ox_row(in_rows)
        print attrib + " card " + str(card_to_play) + " doesn't fit anywhere, taking row " + str(lowest_row+1)
        in_rows=make_card_the_first_in_row(card_to_play, lowest_row, in_rows)
        player_cards=remove_card(card_to_play, player_cards)
        player_ox = player_ox + get_ox_for_row(in_rows[lowest_row])
    else:
        if how_many_cards(in_rows[row_for_card]) == 5:
            print "6 in a row - " + actor + " have to take row " + str(row_for_card + 1) + "."
            player_ox = player_ox + get_ox_for_row(in_rows[row_for_card])
            in_rows=make_card_the_first_in_row(card_to_play, row_for_card, in_rows)
            player_cards=remove_card(card_to_play, player_cards)
        else:
            print "Adding " + attrib + " card " + str(card_to_play) + " to row " + str(row_for_card + 1)
            in_rows=append_card_to_row(card_to_play, row_for_card, in_rows)
            player_cards=remove_card(card_to_play, player_cards)

    return player_cards, player_ox, in_rows

def print_row_with_oxen(c_row):

    row_out = ""
    for card in c_row:
        oxdisp = ""
        oxen_for_this_card=ox_for_card(card)

        for oxen in oxen_for_this_card:
            oxdisp = oxdisp + "*"

        row_out = row_out + str(card) + "(" + oxdisp + ") "

    return row_out

call(["clear", ""])

# Main Loop
while your_cards != []:
    # call(["clear", ""])
    print "############ 6 Nimmt ############\n"

    for r in range(5):
        ox_row=get_ox_for_row(rows[r])
        print "Row " + str(r+1) + " : " + str(rows[r]) + "\t\t\t----- Oxen: " + str(ox_row)
        #rowstr = print_row_with_oxen(rows[r])

        #print str(r+1) + " : " + rowstr

    your_cards.sort()
    my_cards.sort()

    print "\n\nYour cards are " + str(your_cards)
    # print "My cards are " + str(my_cards)
    # print "Oxen: " + str(your_ox) + " (you) " + str(my_ox) + " (me)"

    # print "You have " + str(how_many_cards(your_cards)) + " cards"

    while True:
        play_card=raw_input("Which card do you want to play? : ")
        if is_card_in_deck(play_card, your_cards):
            break

    # For computer vs computer
    # play_card=random.choice(your_cards)

    computer_playcard=random.choice(my_cards)

    print "\nOK and my card is " + str(computer_playcard) + "\n"

    if int(computer_playcard) < int(play_card):
        # computer starts
        # print "My card is lower, I start."
        my_cards, my_ox, rows = player_card("my", my_cards, my_ox, rows, computer_playcard)
        your_cards, your_ox, rows = player_card("your", your_cards, your_ox, rows, play_card)

    else:
        # player starts
        # print "Your card is lower, you start."
        your_cards, your_ox, rows = player_card("your", your_cards, your_ox, rows, play_card)
        my_cards, my_ox, rows = player_card("my", my_cards, my_ox, rows, computer_playcard)

print "Total oxen: " + str(your_ox) + " (you) " + str(my_ox) + " (me)"

if your_ox == my_ox:
    print "It's a draw!"
    exit(150)

if your_ox <= my_ox:
    print "You win!"
    exit(100)

else:
    print "I win!"
    exit(200)
