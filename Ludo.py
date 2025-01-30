import random

def roll():
    sum=0
    for i in range (3):
        temp=random.randint(1,6)
        print(temp)
        sum+=temp
        if temp != 6:
            return sum
    return 0


def allow(roll,color):
    color_map = {'r': [p[1],2], 'g': [p[2],15], 'b': [p[3],28], 'y': [p[4],41]}
    base_count=0
    for i in range(5,9):
        if color[i]==False:
            base_count+=1

    allowed=min(roll//6,base_count)

    if allowed<1:
        return roll
    else:
        temp=5
        while temp>allowed:
            temp=int(input(f'enter how many pieces out of {base_count} you want to take out , you can take out {allowed} :'))
        temp2=0
        temp3=5
        while temp2!=temp:
            if color[temp3] is False:
                color[temp3]=True
                color[temp3-4] = color_map[color[0]][1]
                temp2+=1
            temp3+=1

        return roll-temp2*6


def move(color,board,temp,roll):
    color_map = {'r': [p[1],2,1,53], 'g': [p[2],15,2,14], 'b': [p[3],28,3,27], 'y': [p[4],41,4,40]}

    if True not in color:
        return board

    while roll!=0:
        temp1 = roll
        p_ald=[]
        while temp1>5:
            p_ald.append(6)
            temp1-=6
        p_ald.append(temp1)

        while True:
            pmove=int(input(f'which peice do you want to move you can play {p_ald} : '))

            if pmove in [1,2,3,4] and color[pmove+4] == True:
                break

        for i in range(p_ald[0]):

            if color[pmove]+i == color_map[color[0]][3]:

                board[color[pmove]]=board[color[pmove]].replace(color[0]+str(pmove),'  ')
                subchange=color_map[color[0]][3] - color[pmove]-1

                if p_ald[0] - subchange <= 6:
                    color[pmove]=p_ald[0]-subchange+52

                    if board[color[pmove]] == "  ":
                        board[color[pmove]]=color[0]+str(pmove)
                    else:
                        board[color[pmove]]+=color[0]+str(pmove)

                    color[pmove+8] = 1
                break
        else:


            if color[pmove]+p_ald[0] <=52 and color[pmove+8] == 0:

                board[color[pmove]]=board[color[pmove]].replace(color[0]+str(pmove),'  ')
                color[pmove]+=p_ald[0]

                temp[0]=board[color[pmove]]
                temp[1]=color[pmove]
                board[color[pmove]]=color[0]+str(pmove)

            elif color[pmove+8] == 1 and color[pmove]+p_ald[0] <=58:

                board[color[pmove]]=board[color[pmove]].replace(color[0]+str(pmove),'  ')
                color[pmove]+=p_ald[0]

                if board[color[pmove]] == "  ":
                        board[color[pmove]]=color[0]+str(pmove)
                else:
                        board[color[pmove]]+=color[0]+str(pmove)

                
                if color[pmove] ==58:
                    color[pmove+8] = 2

            elif color[pmove+8]==2:

                pas = 1


            elif color[pmove+8] == 0:
                board[color[pmove]]=board[color[pmove]].replace(color[0]+str(pmove),'  ')
                color[pmove]+= p_ald[0] -52

                temp[0]=board[color[pmove]]
                temp[1]=color[pmove]
                board[color[pmove]]=color[0]+str(pmove)



        roll-=p_ald[0]
        p_ald.pop(0)
    
    return board


def cut(temp,board,p):
    ss=[2,10,15,23,28,36,41,49]
    if temp[0]=='  ':
        return temp
    else:
        color_map = {'r': [p[1],1], 'g': [p[2],14], 'b': [p[3],27], 'y': [p[4],40]}
        if temp[0][0:1:] in color_map and temp[1] not in ss:

            color_map[temp[0][0:1:]][0][int(temp[0][1::])] = 0   # Reset the color piece
            color_map[temp[0][0:1:]][0][int(temp[0][1::])+4] = False

        else:
            board[temp[1]]+=temp[0]

    temp[0] = '  '
    temp[1] = '  '
    return temp
def print_board(board):

    print("#"*88)
    print("#///////////////////////////////////# "+board[51]+" | "+board[52]+" | "+board[1]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[50]+" | "+board[53]+" | "+board[2]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[49]+" | "+board[54]+" | "+board[3]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[48]+" | "+board[55]+" | "+board[4]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[47]+" | "+board[56]+" | "+board[5]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[46]+" | "+board[57]+" | "+board[6]+" #///////////////////////////////////#")
    print("# "+board[40]+"  | "+board[41]+"  | "+board[42]+"  | "+board[43]+"  | "+board[44]+"  | "+board[45]+"  | /#/| "+board[58]+" |/#/ | "+board[7]+"  | "+board[8]+"  | "+board[9]+"  | "+board[10]+"  | "+board[11]+"  | "+board[12]+"  #")
    print("# "+board[39]+"  | "+board[53]+"  | "+board[54]+"  | "+board[55]+"  | "+board[56]+"  | "+board[57]+"  | "+board[58]+" |####| "+board[58]+" | "+board[57]+"  | "+board[56]+"  | "+board[55]+"  | "+board[54]+"  | "+board[53]+"  | "+board[13]+"  #")
    print("# "+board[38]+"  | "+board[37]+"  | "+board[36]+"  | "+board[35]+"  | "+board[34]+"  | "+board[33]+"  | /#/| "+board[58]+" |/#/ | "+board[19]+"  | "+board[18]+"  | "+board[17]+"  | "+board[16]+"  | "+board[15]+"  | "+board[14]+"  #")
    print("#///////////////////////////////////# "+board[32]+" | "+board[57]+" | "+board[20]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[31]+" | "+board[56]+" | "+board[21]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[30]+" | "+board[55]+" | "+board[22]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[29]+" | "+board[54]+" | "+board[23]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[28]+" | "+board[53]+" | "+board[24]+" #///////////////////////////////////#")
    print("#///////////////////////////////////# "+board[27]+" | "+board[26]+" | "+board[25]+" #///////////////////////////////////#")
    print("#"*88)

temp=['  ','  ']
p=[[],['r',0,0,0,0,False,False,False,False,0,0,0,0],['g',0,0,0,0,False,False,False,False,0,0,0,0],['b',0,0,0,0,False,False,False,False,0,0,0,0],['y',0,0,0,0,False,False,False,False,0,0,0,0]]
board=[]
for i in range(52+6+1):
    board.append('  ')

print("This is Riddhiman's Ludo , A few rule changes here and there, you won't even notice")
print("Let's Start")
No_p=int(input("Enter no. of players"))
while True:

    if No_p > 0 :

        print("Play for Red")
        board = move(p[1],board,temp,allow(roll(),p[1]))
        cut(temp,board,p)
        print_board(board)

        if p[1].count(2)==4:
            print( str(p[1][0]) + " Wins")
        print()

    if No_p > 2 :
        print("Play for Green")
        board = move(p[2],board,temp,allow(roll(),p[2]))
        cut(temp,board,p)
        print_board(board)

        if p[2].count(2)==4:
            print( str(p[2][0]) + " Wins")
        print()


    if No_p >1:

        print("Play for Blue")
        board = move(p[3],board,temp,allow(roll(),p[3]))
        cut(temp,board,p)
        print_board(board)

        if p[3].count(2)==4:
            print( str(p[3][0]) + " Wins")
        print()

    if No_p >3:

        print("Play for Yellow")
        board = move(p[4],board,temp,allow(roll(),p[4]))
        cut(temp,board,p)
        print_board(board)

        if p[4].count(2)==4:
            print( str(p[1][0]) + " Wins")
        print()
