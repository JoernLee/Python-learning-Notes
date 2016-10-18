#-*-coding:utf-8-*-
f = open("E:\Python27\learn python\game.txt")
score = f.read().split()
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times>0 :
    avg_times = float(total_times)/game_times
else :
    avg_times = 0
print "你已经玩了%d次，最少%d轮得到答案，平均轮数%.2f"%(game_times,min_times,avg_times)
import random
bingo = False 
true_number = random.randint(1,100)
while bingo==False :
    get_number = int(input("your number: "))
    if get_number>true_number:
        print "big"
    if get_number < true_number:
        print "little"
    if get_number == true_number:
        bingo = True
        print "恭喜猜数字正确：正确数字"+str(true_number)

