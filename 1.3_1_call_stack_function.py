def closest_mod_5(x): 
	if x % 5 == 0:
		return x
	closest_mod_5(x+1)
	return closest_mod_5(x+1)
print(closest_mod_5(int(input())))
#!!2
'''closest_mod_5 = lambda x: ((x+4) // 5)*5
print(closest_mod_5(14))'''