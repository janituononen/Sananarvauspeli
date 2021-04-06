#TTC2030-3012 Harjoitustyö -- Sananarvauspeli
#Ohjelmaan on ennalta syötetty 20 sanaa, joista se arpoo sanan, jota pelaajan tulee arvata. 
#Ohjelma antaa arvata sanaa niin kauan, että pelaaja arvaa oikean sanan tai pelaaja on saanut syötettyä kaikki sanassa esiintyvät kirjaimet.
#Jokaisen arvauksen jälkeen tulostetaan montako kertaa pelaaja on arvannut.
#Jos pelaaja yrittää arvata jo kerran arvaamaansa kirjainta tai sanaa arvausten määrä ei lisäänny.
#Kun pelaaja arvaa oikean vastauksen tai on arvannut kaikki oikeat kirjaimet pelaajalle kerrotaan oikea sana, kuinka montaa kertaa pelaja on arvannut, mitä kirjaimia ja mitä vääriä sanoja hän on arvannut.

#Tuodaan generaattori sananarvontaa varten.
import random

#Pelaaja syöttää nimen ja hänet toivotetaan tervetulleeksi pelaamaan.
nimi = input("Anna nimesi: ")
while nimi.isalpha() == False:
    print("Nimen tulee sisältää vain aakkosia ja siinä ei saa olla välilyöntejä.")
    nimi = input("Anna nimesi: ")

print("{}, Tervetuloa pelaamaan!".format(nimi))

#Lista mahdollisista sanoista.
sanat = ['avaruuskapseli', 'kahvinkeitin', 'kattolamppu', 'sananarvauspeli', 'tasavalta', 'syyntakeeton', 'ohjelmointikurssi', 'harjoitusmatka',
         'rahaliikenne', 'keittokirja', 'kantoraketti', 'satelliittivastaanotin', 'vuorovesivaikutus', 'adjektiivialkuinen', 'argumentaatioanalyysi',
         'ydinfyysikko', 'vuonohevostalli', 'automaatioasentaja', 'kirkollisvero', 'yhdyssanaharjoitus']

#Arvotaan satunnainen sana listalta.
sana = random.choice(sanat)
#Muutetaan kirjaimet suuriksi selkeyden vuoksi.
sana = sana.upper()
tyhjat = '_' * len(sana) 
vastaus = False
arvatutKirjaimet = []
arvatutSanat = []
arvaus_lkm = 0
oikeatKirjaimet = 0

#Pelaaja saa arvata, kunnes arvaa oikean sanan.
while not vastaus:
    #Näytetään pelaajalle kuinka monta kirjainta sanassa on.
    print(tyhjat, len(sana), "kirjainta")
    arvaus = input("Arvaa kirjainta tai oikeaa sanaa: ").upper()
    #Tarkistetaan onko arvauksessa vain 1 kirjain.
    if len(arvaus) == 1 and arvaus.isalpha():
        #Jos arvattua kirjainta on jo yritetty arvata. Arvausten määrä ei lisäänny.
        if arvaus in arvatutKirjaimet:
            print("Olet jo arvannut", arvaus, "kirjainta")
        #Jos arvattu kirjain ei ole arvattavassa sanassa. Arvausten määrä lisääntyy.
        elif arvaus not in sana:
            print(arvaus, "kirjain ei ole arvattavassa sanassa.")
            arvaus_lkm += 1
            arvatutKirjaimet.append(arvaus)
        #Pelaaja arvaa kirjaimen oikein.
        else:
            print(nimi, "arvasit oikein kirjaimen!")
            arvaus_lkm += 1
            arvatutKirjaimet.append(arvaus)
            kirjaimetListalla = list(tyhjat)
            indeksit = [k for k, kirjain in enumerate(sana) if kirjain == arvaus]
            for indeksi in indeksit:
                kirjaimetListalla[indeksi] = arvaus
            tyhjat = "".join(kirjaimetListalla)
            oikeatKirjaimet += 1
            #Jos pelaaja on saanut kaikki oikeat kirjaimet, peli loppuu
            if oikeatKirjaimet == len(set(sana)):
                arvaus = True
                print(nimi, "arvasit oikein!!!")
                print("Oikea sana oli:", sana)
                print("Arvasit", arvaus_lkm, "kertaa")
                print("Kirjaimet joita arvasit: ", arvatutKirjaimet)
                print("Väärät sanat joita arvasit: ", arvatutSanat)
                break
    #Kokeillaan onko pelaajan arvaama sana jota haetaan.
    elif arvaus != sana and arvaus.isalpha():
        #Onko pelaaja jo arvannut kyseistä sanaa.
        if arvaus in arvatutSanat:
            print("Olet jo arvannut", arvaus, "sanaa")
        #Onko arvaus eri kuin sana jota arvataan.
        elif arvaus != sana:
            print("Arvasit väärää sanaa.")
            arvatutSanat.append(arvaus)
            arvaus_lkm += 1
    #Jos pelaaja arvaa sanan oikein, peli loppuu
    elif arvaus == sana:
            arvaus = True
            arvaus_lkm += 1
            print(nimi, "arvasit oikein!!!")
            print("Oikea sana oli:", sana)
            print("Arvasit", arvaus_lkm, "kertaa")
            print("Kirjaimet joita arvasit: ", arvatutKirjaimet)
            print("Väärät sanat joita arvasit: ", arvatutSanat)
            break
    #Pelaajan vastaus sisältää muuta kuin aakkosia
    else:
        print("Anna vastauksesi aakkosissa (ABCDEFGHIJKLMNOPQRSTUVXYZ)")
    
    print("Yrityksiä:", arvaus_lkm)

