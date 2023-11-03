
import random


#ctr+b-vel lehet sublime-ba py programot futtatni




#Írd ki, hogy melyik a legnagyobb szám a [100;100000] intervallumból, amelyiknek az utolsó számjegye nagyobb, mint az előtte lévő számjegyek összege.

def UtolsoLegnagyobb():
	talaltam_lista=[]

	for szam in range(100,100000):
		szamjegy_osszeg=0
		szam_str=str(szam)

		for szamjegy in szam_str:
			szamjegy_osszeg+=int(szamjegy)

		if(int(szam_str[-1]) > (szamjegy_osszeg-int(szam_str[-1]))):
			talaltam_lista.append(szam)

	print("Találtam lista:",talaltam_lista)
	print("Siker")















#Írd ki 100-tól kezdve a második 10 darab olyan számot, amelyiknek pontosan 7 osztója van (1-et és önmagát figyelmen kívül hagyva).

#  315 -> 31-(2*5)=21. 21 osztható 7-tel, tehát 315 is.


def PontosanHetOszto():
	szam = 100
	lista = []

	while len(lista) < 20:
		szam_str = str(szam)

		elsok = int(szam_str[:-1])
		utolsodupla = 2*int(szam_str[-1])


		if (elsok - utolsodupla) % 7 == 0:
			lista.append(szam)
			szam += 1
		else:
			szam += 1			

	print("Megfelelő számok:",lista[11:])
	print("Siker")

















#Írd ki annak a sorozatnak a 15. elemét, amelyet úgy kapsz meg, hogy minden következő elemet az előző szám számjegyeinek kétszereséből állítod elő! (1, 2, 4, 8, 16, 212, 424, 848, 16816)

def TizenotodikElem():
	szam=str(1)

	for valtozo_szam in range(1,15):
		kesz_dupla=""

		for i in range(len(szam)):
			szamjegy=szam[i]
			ketszeres=int(szamjegy)*2
			kesz_dupla+=str(ketszeres)

		szam=kesz_dupla

	print("15.elem:",szam)
	print("Siker")




















#Sorsolj ki egy 6 számjegyű számot. Add meg, hogy melyik prímszám van ehhez a legközelebb! Ha több ilyen van, írd ki mindet!

def LegkozelebbiPrim():
	sorsolt = random.randint(100000,999999)
	print("Sorsolt szám:",sorsolt)

	tol=sorsolt-5
	ig=sorsolt+5


	lista = []


	for szam in range(tol,ig):
		szam_int = int(szam)
		if szam_int>2 and szam_int % 2 == 0 or szam_int>3 and szam_int % 3 == 0 or szam_int>5 and szam_int % 5 == 0 or szam_int == 1:
			pass
		else:
			i = 5
			while i * i <= szam_int:
				if szam_int % i == 0 or szam_int % (i + 2) == 0:
					pass
				i += 6
			lista.append(szam_int)
	

	lista2 = []


	for i in lista:
		if i == sorsolt:
			pass
		else:
			lista2.append(abs(i-sorsolt))


	if sorsolt in lista:
		lista.remove(sorsolt)

	nyertes_prim = lista[lista2.index(min(lista2))]


	print("Legközelebbi prímszám:",nyertes_prim)
	print("Siker")






















#Sorsolj ki egy 10 számjegyű számot. Írd ki a számon belüli prímszámokat! (pl: 1123456789 -> 2, 3, 5, 7, 11, 23, 67, 89, 1123, 4567, 23456789) A prímszámokat növekvő sorrendben add meg! Ugyanazt a számot ne írd ki kétszer! Ha nincs ilyen, akkor írd ki, hogy nincs ilyen szám!

def BeluliPrimSzamok():
	sorsolt = random.randint(1000000000,9999999999)
	print("\n\nEredeti szám:",sorsolt)

	sorsolt_str = str(sorsolt)

	szamjegy_lista = []
	prim_szamok = []



	k = 0
	while k != 10:
		for i in range(1,len(sorsolt_str)+1):
		    szamjegy = sorsolt_str[k:i]
		    if szamjegy == "" or int(szamjegy) == 0 or szamjegy in szamjegy_lista: 
		    	pass
		    	print("hiba:",szamjegy)
		    else:
		    	szamjegy_lista.append(szamjegy)
		    	print("jó, csatol:",szamjegy)
		k += 1



		

	for szam in szamjegy_lista:
		szam_int = int(szam)
		if szam_int>2 and szam_int % 2 == 0 or szam_int>3 and szam_int % 3 == 0 or szam_int>5 and szam_int % 5 == 0 or szam_int == 1:
			pass
		else:
			i = 5
			while i * i <= szam_int:
				if szam_int % i == 0 or szam_int % (i + 2) == 0:
					pass
				i += 6
			if szam_int not in prim_szamok:   #pl 3 és 03
				prim_szamok.append(szam_int)
			else:
				pass


	print("Nincsenek benne prím számok" if prim_szamok==[] else "\nPrím számok benne:",sorted(prim_szamok))
	print("Siker")























#Sorsolj ki egy 10 számjegyű számot. Melyik az a legnagyobb legalább kétjegyű szám ezen belül, amelyiknek a számjegyei növekvő sorrendben állnak? (pl: 1234345673 -> 34567) Ha nincs ilyen, akkor írd ki, hogy nincs ilyen szám!

def SzamjegyNovekvo():
	sorsolt = random.randint(1000000000,9999999999)
	print("\nEredeti szám:",sorsolt,"\n")

	sorsolt_str = str(sorsolt)

	szamjegy_lista = []



	for k in range(len(sorsolt_str)):
		for i in range(k, len(sorsolt_str) + 1):
			szamjegy = sorsolt_str[k:i]
			if szamjegy == "" or int(szamjegy) == 0:
				pass
			else:
				sorrend = True
				for p in range(len(szamjegy) - 1):
					if int(szamjegy[p]) != int(szamjegy[p+1]) - 1:
						sorrend = False
						break
				if sorrend:
					szamjegy_lista.append(int(szamjegy))




	nyertes = max(szamjegy_lista)

	if len(str(nyertes))<2:
		print("Nincs növekvő sorrendben álló számjegysorozat ebben a számban.")
	else:
		print(f"\nA legnagyobb növekvő sorrendben álló számjegysorozat ebben: {sorsolt} -- {nyertes}")
	print("Siker")



















#Sorsolj ki egy 10 számjegyű számot. Írd ki azokat a számjegyeket, amelyek nem fordulnak elő a számban! Ha nincs ilyen, írd ki, hogy nincs hiányzó számjegy!


def Szamjegyes():
	sorsolt_szam = random.randint(1000000000,9999999999)
	print("Eredeti szám:",sorsolt_szam)


	alap_szamok = [0,1,2,3,4,5,6,7,8,9]
	hianyzo_szamok = []

	sorsolt_szam_str = str(sorsolt_szam)



	for szamjegy in sorsolt_szam_str:
		if(int(szamjegy) in alap_szamok):
			alap_szamok.remove(int(szamjegy))
		else:
			pass


	print("Számjegyek amik nem szerepelnek benne:",alap_szamok)
	print("Siker")


























#Sorsolj ki egy 10 számjegyű számot. Írd ki azokat a 3 számjegyű számokat, amelyek az eredeti számjegyekből összerakhatóak úgy, hogy a számjegyeik növekvő sorrenden állnak. Ugyanazt a számot ne írd ki kétszer! Ha nincsenek ilyenek, akkor írd ki, hogy nincsenek ilyen számok!

def HaromSzamjegyu():
	sorsolt = random.randint(1000000000,9999999999)
	print("Sorsolt szám:",sorsolt)
	sorsolt_str = str(sorsolt)
	nyertesek_lista = []


	for i in range(len(sorsolt_str) - 2):

		elso_szamjegy = int(sorsolt_str[i])
		masodik_szamjegy = int(sorsolt_str[i + 1])
		harmadik_szamjegy = int(sorsolt_str[i + 2])


		if (elso_szamjegy+1 == masodik_szamjegy and masodik_szamjegy+1 == harmadik_szamjegy):
			talalt_szam = str(elso_szamjegy)+str(masodik_szamjegy)+str(harmadik_szamjegy)
			nyertesek_lista.append(talalt_szam)


	print("Nyertesek:", nyertesek_lista)
	print("Siker")





























#Sorsolj ki egy 5 számjegyű számot. Írd ki, hogy van-e olyan számjegye, amelyik nagyobb a többi számjegy összegénél! Ha van ilyen, írd ki melyik az! Ha nincs ilyen, írd ki, hogy nincs ilyen számjegy!

def OtSzamjegyu():
	sorsolt = random.randint(10000,99999)
	print("Sorsolt szám:",sorsolt)

	osszeg=0

	nyertes_str = str(sorsolt)
	szamjegy_lista=[]

	for szamjegy in nyertes_str:
		szamjegy_lista.append(szamjegy)
		osszeg+=int(szamjegy)
	print("Összeg:",osszeg)

	szamjegy_lista.sort()



	legnagyobb=""

	for szam in szamjegy_lista:
		if(int(szam)>osszeg-int(szam)):
			legnagyobb=szam

	if(legnagyobb==""):
		print("Nincs olyan számjegy ami nagyobb lenne a többi számjegy összegénél")
	else:
		print("Találtunk:",legnagyobb)

	print("Siker")






