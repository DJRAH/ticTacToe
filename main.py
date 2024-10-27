
def affichage(table):
    j=0
    index=1
    print("\n\n")
    for i in range(7):
        if i==0:
            print(' '*14+str(index)+' |'+' '*13+str(index+1)+' |'+' '*12+str(index+2))
            index+=3
        elif i==3:
            print(' '*7+str(tableau[j])+' '*7+' |'+' '*7+str(tableau[j+1])+' '*7+'|'+' '*7+str(tableau[j+2])+' '*7)
            j+=3
        else:
            print(' '*15+' |'+' '*15+'|'+' '*15)
    print('-'*47)
    for i in range(7):
        if i==0:
            print(' '*14+str(index)+' |'+' '*13+str(index+1)+' |'+' '*12+str(index+2))
            index+=3
        elif i==3:
            print(' '*7+str(tableau[j])+' '*7+' |'+' '*7+str(tableau[j+1])+' '*7+'|'+' '*7+str(tableau[j+2])+' '*7)
            j+=3
        else:
            print(' '*15+' |'+' '*15+'|'+' '*15)
    print('-'*47)
    for i in range(7):
        if i==0:
            print(' '*14+str(index)+' |'+' '*13+str(index+1)+' |'+' '*12+str(index+2))
            index+=3
        elif i==3:
            print(' '*7+str(tableau[j])+' '*7+' |'+' '*7+str(tableau[j+1])+' '*7+'|'+' '*7+str(tableau[j+2])+' '*7)
        else:
            print(' '*15+' |'+' '*15+'|'+' '*15)
    print("\n\n")


def check_input(inpt1, inpt2, table):
    free_case=[]
    tst=1
    print("\n")
    for i in range(len(table)):
        if table[i]=='.':
            free_case.append(i+1)
    if (inpt1 in set(free_case))==False:
        print('Player 1 please entre a number of a free case')
        tst=0
    if (inpt2 in set(free_case))==False:
        print('Player 2 please entre a number of a free case')
        tst=0
    print("\n")
    return tst
    
""" def check_game(tbl):

    if (tbl[0]==tbl[1]==tbl[2]) or (tbl[3]==tbl[4]==tbl[5]) or (tbl[6]==tbl[7]==tbl[8]) or (tbl[0]==tbl[3]==tbl[5]) or (tbl[1]==tbl[4]==tbl[7]) or (tbl[2]==tbl[5]==tbl[8]) or (tbl[0]==tbl[4]==tbl[8]) :
        #ya un gagnat
        return 1 #ou 2 
    
    
    return 3 """

tableau = ['.' for i in range(9)]
affichage(tableau)


#miss condition to stop while
while True:
    check_input_ok=0
    print("Player1: choose a free case and enter his number plz : ")
    plr1 = input()
    print("Player2: choose a free case and enter his number plz : ")
    plr2 = input()

    #check player's input
    try: 
        player1 = int(plr1)
        player2 = int(plr2)
    except ValueError:
        print("\n")
        print("Veuillez bien rentrer un int entre 1 et 9 en plus que la case sois libre !")
        print("\n")
    else:
        check_input_ok = check_input(player1, player2, tableau)
        
    if check_input_ok:
        tableau[int(player1-1)]='X'
        tableau[int(player2-1)]='O'
        affichage(tableau)
    
    #check_game_state = check_game(tableau)

    #check win 1 2, equal 0, continujeu 3, 
    # 
    # if 1 2 0 ==> nex game, exit