# Brute force testing
largest = 0
checked = 0

for i in range(999,99,-1):
	if(i*999) < largest:
		break

	if i%11 == 0:
		b = 999
		db = 1
	else:
		b = 990
		db = 11

	for j in range(b,i-1,-db):
		checked += 1
		if i*j < largest:
			break
		x = i*j
		xs = str(x)
		if xs==xs[::-1] and x>largest:
			largest = x
			print "found new largest: " +str(i)+ "*" +str(j)+ "=" +xs + "; checked " + str(checked)

print checked
