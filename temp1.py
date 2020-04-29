
p1 = 5000
p2 = 5000
p3 = 5000

BetTotal =0

a = 5
v = 5
s = 5

winner = 1
round_fee = 15
copy_winner = 0
while 1:
    if winner == 4:
        winner = copy_winner
        Final = 0
    else:
        p1 -= 5
        p2 -= 5
        p3 -= 5
        Final = 0
    if winner ==1:                                              # Abzal winner
        while p1>0 and p2>0 and p3>0 and Final!=1:
            if s!="p" and p3>0:
                bet3 = int(input("Samat's round: "))
                p3 -= bet3
                print ("Samat's bank is: ", p3, "\n")
            if v!="p" and p2>0:
                bet2 = int(input("Vadim's round: "))
                p2 -= bet2
                print ("Vadim's bank is: ", p2, "\n")
            if a!="p" and p1>0:
                bet1 = int(input("Abzal's round: "))
                p1 -= bet1
                print ("Abzal's bank is: ", p1, "\n")
                Final = int(input("Final round 1 (finished) or 0 (not finished)? "))
                BetTotal += bet1+bet2+bet3
        winner = int(input('who is winner: abz (1), vad (2), sam (3), azi (4): '))
        print('')
        if winner == 1:
            p1 += BetTotal+round_fee
            BetTotal = 0
        elif winner == 2:
            p2 += BetTotal+round_fee
            BetTotal = 0
        elif winner == 3:
            p3 += BetTotal+round_fee
            BetTotal = 0
        else:
            print("next round AZI")
            copy_winner = 1

        print ("Abzal bank is: ", p1)
        print ("Vadim bank is: ", p2)
        print ("Samat bank is: ", p3, "\n")
        print ("Total bank is: ", p1+p2+p3, "\n")
        
    elif winner ==3:                                            # Samat winner
        while p1>0 and p2>0 and p3>0 and Final!=1:
            if v!="p" and p2>0:
                bet2 = int(input("Vadim's round: "))
                p2 -= bet2
                print ("Vadim's bank is: ", p2, "\n")
            if a!="p" and p1>0:
                bet1 = int(input("Abzal's round: "))
                p1 -= bet1
                print ("Abzal's bank is: ", p1, "\n")
                next
            if s!="p" and p3>0:
                bet3 = int(input("Samat's round: "))
                p3 -= bet3
                print ("Samat's bank is: ", p3, "\n")
                Final = int(input("Final round 1 (finished) or 0 (not finished)? "))
                BetTotal += bet1+bet2+bet3
        winner = int(input('who is winner: abz (1), vad (2), sam (3), azi (4): '))
        if winner == 1:
            p1 += BetTotal+round_fee
            BetTotal = 0
        elif winner == 2:
            p2 += BetTotal+round_fee
            BetTotal = 0
        elif winner == 3:
            p3 += BetTotal+round_fee
            BetTotal = 0
        else:
            print("next round AZI")
            copy_winner = 3

        print ("Abzal bank is: ", p1)
        print ("Vadim bank is: ", p2)
        print ("Samat bank is: ", p3, "\n")
        print ("Total bank is: ", p1+p2+p3, "\n")

    elif winner ==2:                                            # Vadim winner
        while p1>0 and p2>0 and p3>0 and Final!=1:
            if a!="p" and p1>0:
                bet1 = int(input("Abzal's round: "))
                p1 -= bet1
                print ("Abzal's bank is: ", p1, "\n")
                next
            if s!="p" and p3>0:
                bet3 = int(input("Samat's round: "))
                p3 -= bet3
                print ("Samat's bank is: ", p3, "\n")
            if v!="p" and p2>0:
                bet2 = int(input("Vadim's round: "))
                p2 -= bet2
                print ("Vadim's bank is: ", p2, "\n")
                Final = int(input("Final round 1 (finished) or 0 (not finished)? "))
                BetTotal += bet1+bet2+bet3
        winner = int(input('who is winner: abz (1), vad (2), sam (3), azi (4): '))
        if winner == 1:
            p1 += BetTotal+round_fee
            BetTotal = 0
        elif winner == 2:
            p2 += BetTotal+round_fee
            BetTotal = 0
        elif winner == 3:
            p3 += BetTotal+round_fee
            BetTotal = 0
        else:
            print("next round AZI")
            copy_winner = 2

        print ("Abzal bank is: ", p1)
        print ("Vadim bank is: ", p2)
        print ("Samat bank is: ", p3, "\n")
        print ("Total bank is: ", p1+p2+p3, "\n")
