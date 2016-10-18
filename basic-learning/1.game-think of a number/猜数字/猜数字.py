#-*-coding:utf-8-*-
import random
bingo = False 
true_number = random.randint(1,100)
while bingo==False:
    get_number = int(input("your number: "))
    if get_number>true_number:
        print "big"
    if get_number < true_number:
        print "little"
    if get_number == true_number:
        bingo = True
        print "恭喜"

