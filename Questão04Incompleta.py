#Para um elemento
def troca1(s, velho, novo): 
	for i in s:
		if i == velho:
			print(novo)
		else:
			print(i)
			
			
			
#Para 2 elementos
		
def maior(a,b):
	if a < b:
		return a
	else:
		return b
	
def troca(s, velho, novo):
	ps = 0 
	pv = 0
	for c in s:
		if c == velho[pv] and velho[pv+1] == s[ps+1]:
			print(novo[pv])
			ps += 1
		else:
			print(c)
		ps += 1
