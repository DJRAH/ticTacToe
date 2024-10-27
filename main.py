
def affichage(table):
    j=0
    index=0
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


tableau = ['.' for i in range(9)]

affichage(tableau)