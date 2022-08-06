isim = input("Lütfen isminizi girin: ")
print( isim + ", oyunumuza hoşgeldin. Adam asmaca oynama zamanı!")

kelime = "Alper"
can = 10

dolu = ""


while can>0 :

	kalan_karakter = 0





	for har in kelime:
		if har in dolu:
			print(har)
		elif har not in dolu:
			print("-")
			kalan_karakter +=1
		
	

	if kalan_karakter==0:
		print("Kazandınız!")
		break






	harf = input("Lütfen bir harf girin: ")
	dolu += harf

	if harf in kelime:
		print("Evet, çok iyi!")
	elif harf not in kelime:
		print("Yanlış harf!")
		can -=1
		print(f"{can} adet canın kaldı.")
