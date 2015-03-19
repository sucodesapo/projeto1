# -*- coding: utf-8 -*-

from random import randint

print("Esta eh uma aperfeicoacao do jogo pedra-papel-tesoura, seu diferencial faz com que diminua as chances de empate.")
print("Alem dos elementos jah citados, existe ainda o Spock e o lagarto.")
print("Suas regras são:")
print("• Tesoura corta papel")
print("• Tesoura corta papel")
print("• Papel cobre pedra")
print("• Pedra esmaga lagarto")
print("• Lagarto envenena Spock")
print("• Spock esmaga tesoura")
print("• Tesoura decapita lagarto")
print("• Lagarto come papel")
print("• Papel refuta Spock")
print("• Spock vaporiza pedra")
print("• Pedra quebra tesoura")
print("• Vence a partida quem repetir o feito três vezes")
print("""OBS:
1=Tesoura
2=Papel
3=Pedra
4=Lagarto
5=Spock""")

tesoura=1
papel=2
pedra=3
lagarto=4
spock=5
w="Boa!"
l="Nao teve sorte!"

x=randint(1,5)
y=0

player=0
computer=0

while player<=3 and computer<=3:
    y=int(input("Jogue agora\n"))
    if x==1 and y==2:
        print(l)
        computer+=1
    elif x==1 and y==4:
        print(l)
        computer+=1
    elif x==1 and y==3:
        print(w)
        player+=1
    elif x==1 and y==5:
        print(w)
        player+=1
    elif x==2 and y==3:
        print(l)
        computer+=1
    elif x==2 and y==4:
        print(w)
        player+=1
    elif x==2 and y==5:
        print(l)
        computer+=1
    elif x==2 and y==1:
        print(w)
        player+=1
    elif x==3 and y==4:
        print(l)
        computer+=1
    elif x==3 and y==5:
        print(w)
        player+=1
    elif x==3 and y==2:
        print(w)
        player+=1
    elif x==3 and y==1:
        print(l)
        computer+=1
    elif x==4 and y==5:
        print(l)
        computer+=1
    elif x==4 and y==3:
        print(w)
        player+=1
    elif x==4 and y==1:
        print(w)
        player+=1
    elif x==4 and y==2:
        print(l)
        computer+=1
    elif x==5 and y==1:
        print(l)
        computer+=1
    elif x==5 and y==4:
        print(w)
        player+=1
    elif x==5 and y==3:
        print(l)
        computer+=1
    elif x==5 and y==2:
        print(w)
        player+=1
    elif x==y:
        print("empate")

if x==3: 
    print("Tente outra vez, novato")
elif y==3:
        print("Teve sorte")         