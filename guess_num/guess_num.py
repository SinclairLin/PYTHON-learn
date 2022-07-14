from random import randint

f = open('game_data.txt','r')
txt_data = f.read().split()   #读取game_data.txt 的内容
f.close()
# times = int(txt_data[0])
times = 0
min_steps = 0
# ave_steps = txt_data[2]
ave_steps = 0
# steps = int(txt_data[3])
steps = 0
num = randint(0,100)   #从[0,100] 随机选取一个数
print ('give a num between 1 to 100')
flag = False
times += 1   #游戏次数+1

if times > 0:
    ave_steps = steps / times
else:
    ave_steps = 0

while flag == False:
    input_num = int(input())   #input
    min_steps += 1
    print('your num is ' + str(input_num))
    if input_num == num:
        print("right")
        flag = True

    elif input_num > num:
        print(str(input_num) + ' is too big')

    elif input_num < num:
        print(str(input_num) + ' is too small')


f = open('game_data.txt','w')
f.close()
