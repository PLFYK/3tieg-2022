from http.client import OK
from turtle import circle
import pygame
import random

def main():
    pygame.init()
    OknoGry=pygame.display.set_mode((440,440),0,32)
    pygame.display.set_caption("3tieg")
    run=True
    zmienna=100
    zmienna2=100
    #losowanie pozycji jablka
    appleX=random.randint(0,21)*20+10
    appleY=random.randint(0,21)*20+10
    #liczenie punktow
    punkty=0
    #pozycje weza
    pozycja=[(zmienna2,zmienna)]
    #pozycja.append((120,100))
    dlugoscWeza=1

    while(run):
        OknoGry.fill((0,0,0))
        pygame.time.delay(100)
        for zdarzenie in pygame.event.get():
            if zdarzenie.type==pygame.QUIT:
                run=False
            elif zdarzenie.type==pygame.KEYDOWN:
                if zdarzenie.key==pygame.K_LEFT:
                    zmienna2=zmienna2-20
                elif zdarzenie.key==pygame.K_RIGHT:
                    zmienna2=zmienna2+20
                elif zdarzenie.key==pygame.K_DOWN:
                    zmienna=zmienna+20
                elif zdarzenie.key==pygame.K_UP:
                    zmienna=zmienna-20
                #sprawdzenie czy waz nie zjada siebie
                for location in pozycja[::]:
                    if zmienna==location[1] and zmienna2==location[0]:
                        pozycja=[(zmienna2,zmienna)]
                        dlugoscWeza=1
                        punkty=0
                #pozycje nowe weza
                pozycja.append((zmienna2,zmienna))
                #usuniecie poprzedniej pozycji weza

                if len(pozycja)>dlugoscWeza:
                    del pozycja[0]
        #tworzenie kwadratu jako drzewa
        r=pygame.Rect((zmienna2,zmienna),(20,20))
        pygame.draw.rect(OknoGry,(255,0,0),r)
        #rysowanie weza z pozycji
        for poz in pozycja[::-1]:
            r=pygame.Rect((poz[0],poz[1]),(20,20))
            pygame.draw.rect(OknoGry,(250,0,0),r)
        #tworzenie jablka za pomoca kola
        pygame.draw.circle(OknoGry,(128,0,0),(appleX,appleY),10)
        #sprawdza czy waz zje jablka
        if ((zmienna+10==appleY) and (zmienna2+10==appleX)):
            dlugoscWeza=dlugoscWeza+1
            appleX=random.randint(0,21)*20+10
            appleY=random.randint(0,21)*20+10
            pygame.draw.circle(OknoGry,(128,128,128),(appleX,appleY),10)
        #zwiekszenie liczby punktow
            punkty=punkty+1
        #wypisanie punktow na ekran
        czcionka=pygame.font.SysFont('comicsans',30)
        tekst=czcionka.render("Zdobyles punkty: {0}".format(punkty),1,(0,255,0))
        OknoGry.blit(tekst, (10,10))
        #zmienna=zmienna +20
        if zmienna>420:
            zmienna=0
        if zmienna2>420:
            zmienna2=0
        if zmienna<0:
            zmienna=420
        if zmienna2<0:
            zmienna2=420
        pygame.display.update()

main()