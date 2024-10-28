
#affichage du jeu en ligne de commande
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

#validate inputs
def check_input(num_player, entered_case, table):
    free_case=[]
    tst=0
    print("\n")
    for i in range(len(table)):
        if table[i]=='.':
            free_case.append(i+1)
    if (entered_case in set(free_case))==False:
        print("Player"+ str(num_player) +" please entre a number of a free case")
        tst=1
    print("\n")
    return tst

#state of the game  
def check_game(tbl, numPlayer):
    
    free_case=0
    x1 = 0
    x2 = 0
    for i in range(len(tbl)):
        if tbl[i]=='.':
            free_case+=1
        if tbl[i]=='X':
            x1+=1
        if tbl[i]=='O':
            x2+=1
    if (tbl[0]==tbl[1]==tbl[2]!='.') or (tbl[3]==tbl[4]==tbl[5]!='.') or (tbl[6]==tbl[7]==tbl[8]!='.') or (tbl[0]==tbl[3]==tbl[6]!='.') or (tbl[1]==tbl[4]==tbl[7]!='.') or (tbl[2]==tbl[5]==tbl[8]!='.') or (tbl[0]==tbl[4]==tbl[8]!='.') :
        return numPlayer#gagner la partie
    if free_case==0:
        return 0# partie égal
    return 3 #continuer le jeu

#play a game
def play_partie(tableau):
    check_game_state=0
    player=1
    
    for tour in range(10):

        check_input_ok=1
        while check_input_ok:
            print("Player"+str(player)+": choose a free case and enter his number plz : ")
            plr = input()

            #check player's input
            try: 
                entered_case = int(plr)
            except ValueError:
                print("\n")
                print("Veuillez bien rentrer un int entre 1 et 9 en plus que la case sois libre !")
                print("\n")
            else:
                check_input_ok = check_input(player, entered_case, tableau)
        
        if player==1:
            tableau[int(entered_case-1)]='X'
        else:
            tableau[int(entered_case-1)]='O'

        affichage(tableau)
        
        check_game_state = check_game(tableau, player)

        if check_game_state == 0 :
            print('egualité')
            break
        if check_game_state ==1 or check_game_state==2:
            print("Player"+str(player)+" a gagner la partie")
            break


        if player==1:
            player=2
        else:
            player=1




while True:

    print('\n \n')
    print('------------- new Tour --------------')
    print('\n \n')

    tableau = ['.' for i in range(9)]
    affichage(tableau)

    play_partie(tableau)

    resp="_"
    while resp=="_":
        print("Nouvelle parite ? (yes/no)")
        resp = input()
        if resp=="yes" or resp=="no":
            break
        else:
            print('Veuillez répondre par yes or no plz!')
            resp="_"
    
    if resp=="no":
        print("\n Merci d'avoir jouer! see you soon!! \n")
        break


