#-*-coding:utf-8-*-
import random
name = raw_input("输入你的名字：")
f = open(r"E:\Python27\learn python\1.game-think of a number\game.txt")
lines = f.readlines()
scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:5]
score = scores.get(name)
if score is None:
    score = [0, 0, 0, 0]
game_times = int(score[0])
total_times = int(score[1])
min_times = int(score[2])
avg_times = float(score[3])
times = 0
if game_times > 0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0
print "你已经玩了%d次，总计%d轮，最少%d轮得到答案，平均轮数%.2f" % (game_times, total_times, min_times, avg_times)
bingo = False
true_number = random.randint(1, 10)
game_times += 1
while bingo==False :
    get_number = int(input("your number: "))
    times += 1
    if get_number>true_number:
        print "big"
    if get_number < true_number:
        print "little"
    if get_number == true_number:
        bingo = True
        print "恭喜猜数字正确：正确数字"+str(true_number)
if game_times == 1 or times < min_times:
    min_times = times
total_times += times
avg_times = float(total_times)/game_times
scores[name] = [str(game_times), str(total_times), str(min_times), str(avg_times)]
result = ""
for n in scores:
    line = n + " " + " " .join(scores[n]) + "\n"
    result += line
f = open("E:\Python27\learn python\game.txt","w")
f.write(result)
f.close()





