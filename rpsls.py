#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����ǿ
���ڣ�2021/12/1
"""
import random
a=random.randint(0,4)
def number_to_name(a):
    if a==0:
        a="ʯͷ"
    if a==1:
        a="ʷ����"
    if a==2:
        a="ֽ"
    if a==3:
        a="����"
    if a==4:
        a="����"
    return(a)

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��


    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


     #��дִ�д���,������ɺ�passɾ��

def name_to_number(a):
    if a == ("ʯͷ"):
            a=0
    if a == ("ʷ����"):
            a=1
    if a == ("ֽ"):
            a=2
    if a == ("����"):
            a=3
    if a == ("����"):
            a=4
    return (a)

    #"""
    #������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    #"""

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    pass #��дִ�д���,������ɺ�passɾ��

def rpsls(player_choice):
    a = name_to_number(player_choice)  # �������תΪ��
    b = random.randint(0, 4)
    if a == 0 and b == [3 or 4]:
            c = str(number_to_name(b))  # �����Ե���תΪ��
            print("----------------")
            print("����ѡ����%s" % player_choice)
            print("������ѡ����%s" % c)
            print("��Ӯ��")
    if a == 1 and b == [4 or 0]:
            c = str(number_to_name(b))
            print("----------------")
            print("����ѡ����%s" % player_choice)
            print("������ѡ����%s" % c)
            print("��Ӯ��")
    if a == 2 and b == [0 or 1]:
            c = str(number_to_name(b))
            print("----------------")
            print("����ѡ����%s" % player_choice)
            print("������ѡ����%s" % c)
            print("��Ӯ��")
    if a == 3 and b == [1 or 2]:
            c = str(number_to_name(b))
            print("----------------")
            print("����ѡ����%s" % player_choice)
            print("������ѡ����%s" % c)
            print("��Ӯ��")
    if a == 4 and b == [2 or 3]:
            c = str(number_to_name(b))
            print("----------------")
            print("����ѡ����%s" % player_choice)
            print("������ѡ����%s" % c)
            print("��Ӯ��")
    if a == b:
            c = str(number_to_name(b))
            print("----------------")
            print("����ѡ����%s" % player_choice)
            print("������ѡ����%s" % c)
            print("ƽ��")
    else:
            c = str(number_to_name(b))
            print("----------------")
            print("����ѡ����%s" % player_choice)
            print("������ѡ����%s" % c)
            print("������")  # �������������
    return (player_choice)
   # """
    #�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

   #"""


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if choice_name in ("ʯͷ","ʷ����","ֽ","����","����") :
    rpsls(choice_name)
else:
    print("Error: No Correct Name")