#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：旷正强
日期：2021/12/1
"""
import random
a=random.randint(0,4)
def number_to_name(a):
    if a==0:
        a="石头"
    if a==1:
        a="史波克"
    if a==2:
        a="纸"
    if a==3:
        a="蜥蜴"
    if a==4:
        a="剪刀"
    return(a)

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数


    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果


     #编写执行代码,代码完成后将pass删除

def name_to_number(a):
    if a == ("石头"):
            a=0
    if a == ("史波克"):
            a=1
    if a == ("纸"):
            a=2
    if a == ("蜥蜴"):
            a=3
    if a == ("剪刀"):
            a=4
    return (a)

    #"""
    #将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    #"""

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

    pass #编写执行代码,代码完成后将pass删除

def rpsls(player_choice):
    a = name_to_number(player_choice)  # 将输入的转为数
    b = random.randint(0, 4)
    if a == 0 and b == [3 or 4]:
            c = str(number_to_name(b))  # 将电脑的数转为名
            print("----------------")
            print("您的选择是%s" % player_choice)
            print("机器的选择是%s" % c)
            print("你赢了")
    if a == 1 and b == [4 or 0]:
            c = str(number_to_name(b))
            print("----------------")
            print("您的选择是%s" % player_choice)
            print("机器的选择是%s" % c)
            print("你赢了")
    if a == 2 and b == [0 or 1]:
            c = str(number_to_name(b))
            print("----------------")
            print("您的选择是%s" % player_choice)
            print("机器的选择是%s" % c)
            print("你赢了")
    if a == 3 and b == [1 or 2]:
            c = str(number_to_name(b))
            print("----------------")
            print("您的选择是%s" % player_choice)
            print("机器的选择是%s" % c)
            print("你赢了")
    if a == 4 and b == [2 or 3]:
            c = str(number_to_name(b))
            print("----------------")
            print("您的选择是%s" % player_choice)
            print("机器的选择是%s" % c)
            print("你赢了")
    if a == b:
            c = str(number_to_name(b))
            print("----------------")
            print("您的选择是%s" % player_choice)
            print("机器的选择是%s" % c)
            print("平局")
    else:
            c = str(number_to_name(b))
            print("----------------")
            print("您的选择是%s" % player_choice)
            print("机器的选择是%s" % c)
            print("您输了")  # 各项结果及其可能
    return (player_choice)
   # """
    #用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

   #"""


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

     #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name in ("石头","史波克","纸","蜥蜴","剪刀") :
    rpsls(choice_name)
else:
    print("Error: No Correct Name")