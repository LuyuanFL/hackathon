# -*- coding: utf-8 -*-
import serial
import datetime
from twilio.rest import Client
from time import time,localtime,strftime
def In_it():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("*******************欢迎使用“看门狗”安全系统!********************")
    print("*********Welcome to WatchDog Security System!*******************")
    print("Produced by 肥宅快乐组.")
    print(" ")
    print("1.我已经了解了本系统的使用方法，可以开始使用啦～")
    print("2.我还不太熟悉本系统，想看一下说明文档嘛～")
    print("3.我想退出～")
    str = input("请选择：")
    if(str == '1'):
        Interact_with_Arduino()
    if(str == '2'):
        print("敬请参考当前目录下 WatchDog_Instructions.pdf")
        exit();
    if(str == '3'):
        exit();

start_time_h = [0,10,10,14,14,10,8,8]
start_time_m = [0,30,30,0,0,3,0,0]
end_time_h = [0,12,12,16,16,12,10,10]
end_time_m = [0,30,30,0,0,30,0,0]


def User_input():
    print("初次次使用本系统，请您输入自己的不在寝室的时间，按星期几的顺序输入:")
    print("输入样例：")
    print("星期1  >>> 08 00 20 00 （意为从早上8点起，至晚上8点止）")
    print("全天不在请填 00 00 00 00，全天都在请填 00 00 24 00")
    for dayy in range(1,8):
        print("星期",end='')
        print(dayy,end='')
        print(">>>")

'''
        timestring=input()
        start_time_h[dayy] = start_time_h[dayy] + ord(timestring[0]) + ord(timestring[1]) - 96;
        start_time_m[dayy] = start_time_m[dayy] + ord(timestring[3]) + ord(timestring[4]) - 96;
        end_time_h[dayy] = end_time_h[dayy] + ord(timestring[6]) + ord(timestring[7]) - 96;
        end_time_m[dayy] = end_time_m[dayy] + ord(timestring[9]) + ord(timestring[10]) - 96;
        #start_time_h[dayy],start_time_m[dayy],end_time_h[dayy],end_time_m[dayy] = map(int,input().split())
        #print(start_time_h[dayy],start_time_m[dayy],end_time_h[dayy],end_time_m[dayy])
'''
def Detect_Whether_Intruded(now_time,number_representing_date):
    '''
    if(((now_time.hour > start_time_h[number_representing_date]) and (now_time.hour < end_time_h[number_representing_date])) or ((now_time.hour == start_time_h[number_representing_date]) and (now_time.minute > start_time_m[number_representing_date]) and (now_time.hour < end_time_h[number_representing_date])) or ((now_time.hour > start_time_h[number_representing_date]) and (now_time.hour == end_time_h[number_representing_date]) and (now_time.minute < end_time_m[number_representing_date]))):
        print("a")
    '''
    if(((now_time.hour > 10) and (now_time.hour < 20)) or ((now_time.hour == 10) and (now_time.minute > 20) and (now_time.hour < 20)) or ((now_time.hour > 10) and (now_time.hour == 20) and (now_time.minute < 20))):
        print("Intruder Detected , Sending Message")
        Send_Message()

def Send_Message():
    account_sid = "AC106cfe26ff23ab18d0b4ddc40d82e223"
    auth_token = "47caa3849bae812da2cbe503dc01b4fc"
    client = Client(account_sid, auth_token)
    message = client.messages.create(to="+8613817244335",from_="+19312728415",
    body="Your room may be in danger of being intruded. Better checkout immediately!")
    print(message.sid)

def Interact_with_Arduino():
    p = serial.Serial('/dev/ttyACM0', 9600) 
    User_input()
    print("Arduino检测模块已经开始运作啦～若要查看检测模块输出的详细信息，请参考当前目录下的“log”文件！要退出，请使用 Ctrl+C ")
    countt = 0
    statuss = 0
    statuss_switch_time = 0
    while 1:
    #    print(statuss,end = '-------')
    #    print(statuss_switch_time)
        intensity = p.readline()
        if(len(intensity) != 6):
            continue
        amount = (intensity[0]-48)*1000+(intensity[1]-48)*100+(intensity[2]-48)*10+(intensity[3]-48)
        if ((intensity[0]-48)*1000+(intensity[1]-48)*100+(intensity[2]-48)*10+(intensity[3]-48) >= 8000):
            now_time = datetime.datetime.now()
            x=localtime(time())
            countt = 0
            statuss = 0
            statuss_switch_time = 0
            print(statuss,end = ' ', file = f)
            #print(now_time.weekday(), end = ' ')
            print(now_time.strftime("%Y-%m-%d %H:%M:%S"),end = ' ', file = f)
            print(strftime("%a",x), file = f ,end = ' ')
            print("Hard Reset", file = f)

        if((amount>2000) and (amount<8000)):
            countt += 1
            if(countt > 4 and statuss_switch_time == 0):
                now_time = datetime.datetime.now()
                x=localtime(time())
                number_representing_date = strftime("%w",x);
                if(statuss == 0):
                    statuss = 1;
                elif (statuss == 1):
                    statuss = 0;
                if (statuss == 1 and statuss_switch_time == 0):
                    Detect_Whether_Intruded(now_time,number_representing_date)
                statuss_switch_time = 1
                print(statuss,end = ' ', file = f)
                #print(now_time.weekday(), end = ' ')
                print(now_time.strftime("%Y-%m-%d %H:%M:%S"),end = ' ', file = f)
                print(strftime("%a",x), file = f)

        else:
            countt = 0
            statuss_switch_time = 0
    p.close()

f = open("log","w")

In_it()
