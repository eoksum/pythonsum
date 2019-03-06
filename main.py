# Emrecan Öksüm
# 20181314060

import platform
import sys
import os

def toplama1(sayilar):
	
	sum = 0
	sum2 = 0

	for sayi in range(len(sayilar)):
	
		sum2 = sayilar[0] + sayilar[sayi]
		sum = sum + sum2

	return sum
	
def toplama2(sayilar):
	
	sum = 0
	sum2 = 0
	
	for ind in range(len(sayilar)-1):
		
		sum = sayilar[ind] + sayilar[ind + 1]
		sayilar[ind + 1] = sum #Swap
		
	return sum
	
def eol():
	
	if platform.system() == 'Windows':
		
		return "\r\n"
	
	if platform.system() == 'Linux':
		
		return "\n"
		
	if platform.system() == 'Darwin':
		
		return "\r"

if eol() == "\r\n":
		
	os.system("cls")
		
else:
		
	os.system("clear")

print("############ Toplama ############" + eol() + eol() + "Islem numarasi girin: " + eol() + "1 - Bir listenin ilk elemani ile diger tum elemanlari topla." + eol() + "2 - Bir listenin tum elemanlarini kendi aralarinda topla." + eol() + "Islem nu: ")
islemno = input()

if islemno == '1':
	
	if eol() == "\r\n":
		
		os.system("cls")
		
	else:
		
		os.system("clear")
	
	print("############ Toplama ############" + eol() + eol() + "~ Islem " + islemno + eol() + "Olusturulacak listenin eleman sayisini girin:")
	listelsay = int(input())
	print(eol())
	
	listem = []
	for ind in range(listelsay):
		
		print("Listenin " , ind + 1, " numarali elemani icin deger girin: ")
		listem.append(int(input()))
		print(eol())
	
	print("Sonuc: ", toplama1(listem))
	sys.exit()
	
if islemno == '2':
	
	if eol() == "\r\n":
		
		os.system("cls")
		
	else:
		
		os.system("clear")
	
	print("############ Toplama ############" + eol() + eol() + "~ Islem " + islemno + eol() + "Olusturulacak listenin eleman sayisini girin:")
	listelsay = int(input())
	print(eol())
	
	listem = []
	for ind in range(listelsay):
		
		print("Listenin " , ind + 1, " numarali elemani icin deger girin: ")
		listem.append(int(input()))
		print(eol())
	
	print("Sonuc: ", toplama2(listem))
	sys.exit()
	
print("HATA! Gecersiz islem numarasi! Uygulamadan cikiliyor..." + eol())
sys.exit()
