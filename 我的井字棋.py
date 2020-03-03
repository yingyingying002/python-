import random

def init():
    print("""
    欢迎来到我的井字棋游戏，尊贵的客人。
    您将会和电脑进行一场小小的井字棋游戏，我对于你的智商并没有什么担忧，
    因为早晚，电脑将战胜您。
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 | 9 |
    -------------
    规则很简单，每个位置都由如图对应数字确定。每次输入您想要落子的位置即可，呵呵。
    """)
    input("输入任意键开始对局")

def computer(ch,table):
    pos= random.randint(0,8)
    while(table[pos]!=' '):
        pos=random.randint(0,8)
    res = []
    res = table[0:pos] + list(ch)
    if (pos < 9):
        res += table[pos + 1:9]
    return res

def player (ch,table):
    pos =int( input("请输入您想要落子的位置") )
    while(table[pos]!=' '):
        pos=int( input("人类，这个位置已被占用，你脑子没问题么？重新输入：  ") )
    res = []
    res = table[0:pos]+list(ch)
    if(pos<9):
        res+=table[pos+1:9]
    return res

def judge(a):
    ways = (
          (0, 1, 2), (3, 4, 5), (6, 7, 8),
          (0, 3, 6), (1, 4, 7), (2, 5, 8),
          (0, 4, 8), (2, 4, 6) )  # 八种获胜局势
    for i in ways:
        if(a[i[0]]==a[i[1]]==a[i[2]]!=' '):#获胜
            return 2
    for i in range(9):
        if(a[i]==' '):
            return 1 #继续
    return 0  #平局


def first_hand():
    print("""
    让我们用硬币决定一下先手，如果您选择正面，请输入‘ 0 ’
    如果您选择反面，请输入‘ 1 ’
    """)
    choice = int( input("请输入：  ") )
    while (choice!=1 and choice !=0):
        choice = int ( input( "您输入了一个非法的输入，我的目的是与您下棋，不是对话。\n 请重新输入 " ) )
    num = random.randint(0,1)
    if(num == choice):
        print("恭喜，您获得了先手")
        ch_player = "O"
        ch_com = 'X'
    else :
        print("恭喜，您获得了后手")
        ch_player = "X"
        ch_com = 'O'
    return ch_player,ch_com


def game_over(pos,ch_player,ch_com,win):
    if(win==2):
        if(pos%2==0 and ch_player=='X') or (pos%2==1 and ch_player=='O'):
            print("""
            人类，这次是你的胜利，但
            这只是暂时的
            """)
        else:
            print("""
            人类，你过于弱小
            """)
    else:
        print("""
        战争，将会继续······
        """)
    input("\t\nGAME OVER")


def display(table):
    print("\n\n-------------")
    i=0
    while(i<3):
        print("| %s | %s | %s |"%(table[i*3],table[i*3+1],table[i*3+2]))
        print("-------------")
        i+=1

def main():
    init()
    ch_player,ch_com = first_hand()
    #print(ch_player,ch_com)
    table = []
    for i in range(9):
        table.append(' ')
    ind = int(ch_player == 'O')
    pos = 0
    display(table)
    while(judge(table)==1):
        pos+=1
        if((pos+ind)%2==0):
            table=player(ch_player,table)
        else:
            table=computer(ch_com,table)
        display(table)
    game_over(pos,ch_player,ch_com,judge(table))



main()

