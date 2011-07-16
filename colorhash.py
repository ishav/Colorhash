# -*- coding: cp1252 -*-

import hashlib
import png

def make_remap(rader):
	"""skapar en dict f�r att matrcha ett tecken fr�n ett hash med ett element i en lista"""
	c = 0
	t = {}
	
	for i in "0123456789abcdef":
		t[i] = c
	
		c += 1

		if c >= len(rader):
			c = 0
	
	return t

def colorhash(string_to_hash):
	""" skapar rutor av denna typ:
	
	012
	345
	678
	
	med tv� parametrar,
	
	rutor: antalet rutor per rad
	storlek hur m�nga tecken bred en ruta �r
	
	"""
	
	rutor = 5
	storlek = 20


	# hashet vi anv�der f�r att skapa bilderna
	hashet = hashlib.sha1(string_to_hash).hexdigest()
	
	#F�rg palleterna som anv�nds
	farger = [ [[104, 138, 111],[128, 150, 111],[216, 181, 115],[192, 143, 100]],
			[[247, 224, 220],[242, 213, 204],[234, 201, 183],[230, 190, 163]],
			[[245, 202, 91],[245, 104, 91],[186, 224, 61],[156, 210, 241]] ]
	

	
	pallet_remap = make_remap(farger)
	
	farger = farger[pallet_remap[hashet[0]]]
	

	# l�gger till en m�rkare variant av alla f�rger som finns i f�rgpalleten
	t = []
	for i in farger:
	    s = [i[0]+13, i[1]+13, i[2]+13]
	
	    for k in range(0,3):
	        if s[k] > 255:
	            s[k] = 255
	
	    t.append(s)
	
	farger += t
	
	
	#dict f�r att matcha vilket tecken i sha1 hashet som ska bytas ut mot vilken f�rg 
	hash_farger_remap = make_remap(farger)
	
	# breddden och h�jden png.py beh�ver detta
	size = rutor * storlek
	
	temp = []
	
	for k in range(0,rutor):
	    p = []
	    for i in range(0,rutor*storlek):
	        #p += farger[(i/storlek+(rutor*k))]
	
	        t1 = hashet[(i/storlek+(rutor*k))]
	        t2 = hash_farger_remap[t1]
	        p += farger[t2]
	        
		# repeterar raden vi skapade som ineh�ller r�tt andelar av varje f�rg f�r att bilda rutor
	    for printrow in range(0, storlek):
	        temp.append(p)
	
	
	f = open(string_to_hash + '.png', 'wb')
	w = png.Writer(size, size)
	w.write(f, temp)
	f.close()

if __name__ == "__main__":
    colorhash("Java")
    colorhash("C#")
    colorhash("C++")
    colorhash("Python")
    colorhash("Javascript")
    colorhash("PHP")
    colorhash("Lua")
    colorhash("Ruby")


