class SUBNETEXO:
	
	def __init__(self, a, b, c, d, CIDR):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.CIDR = CIDR
		self.IP = str(a) + "." + str(b) + "." + str(c) + "." + str(d) + "/" + str(CIDR)
		

	def BinaryIP(self, a, b, c, d):
		iterate = [a, b, c, d]
		fullBinary = ""
		for part in iterate:
			binPart = bin(part).replace("0b", "")
			if len(binPart) != 8:
				binPart = ((8 - len(binPart)) * "0") + binPart
			fullBinary = fullBinary + binPart
		return fullBinary


	def IPRebuilder(self, binIP):
		newIP = ""
		octets = []
		count = 0
		for x in range(4):
			octets.append(binIP[x*8:(x+1)*8])
		for y in octets:
			if count < 3:
				newIP = newIP + str(int(y, 2)) + "."
				count += 1
			else:
				newIP = newIP + str(int(y, 2))
		return newIP


	def BinBroadcast(self):
		binIP = self.BinaryIP(self.a, self.b, self.c, self.d)
		filler = len(binIP) - self.CIDR
		adrBroadcast = binIP[:self.CIDR] + (filler * "1")
		return adrBroadcast
	
	
	def BinAdresseReseau(self):
		binIP = self.BinaryIP(self.a, self.b, self.c, self.d)
		filler = len(binIP) - self.CIDR
		adrReseau = binIP[:self.CIDR] + (filler * "0")
		return adrReseau
		
	
	def Broadcast(self):
		binBroadcast = self.BinBroadcast()
		broadcast = self.IPRebuilder(binBroadcast)
		return broadcast
		
		
	def AdresseReseau(self):
		binAdresseReseau = self.BinAdresseReseau()
		adresseReseau = self.IPRebuilder(binAdresseReseau)
		return adresseReseau


if __name__ == "__main__":
	
	import random as rng
	import os
	
	counter = 0
	correct = 0
	while counter < 10:
		a = rng.randint(0,192)
		b = rng.randint(0,255)
		c = rng.randint(0,255)
		d = rng.randint(0,255)
		CIDR = rng.randint(2,30)
		
		exo = SUBNETEXO(a, b, c, d, CIDR)

		broadcastAnswer = str(input("Entrez l'adresse de Broadcast pour l'IP " + exo.IP + " (SANS le CIDR):\n"))
		if broadcastAnswer == exo.Broadcast():
			print("\nCorrect\n")
			counter += 1
			correct += 1
		else:
			print("\nIncorrect, la réponse était: " + exo.Broadcast() + "\n")
			counter += 1
	
		adresseReseauAnswer = str(input("Entrez l'adresse du sous-réseau pour l'IP " + exo.IP + " (SANS le CIDR):\n"))
		if adresseReseauAnswer == exo.AdresseReseau():
			print("\nCorrect\n")
			correct += 1
		else:
			print("\nIncorrect, la réponse était: " + exo.AdresseReseau() + "\n")
		
		input("Appuyez sur \"Enter\" pour continuer: ")
		os.system('cmd /c "cls"')
			
	print("Terminé, vous avez obtenu: " + str(correct) + " sur 10:")
	
	
	

