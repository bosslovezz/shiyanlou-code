a=0;
while(a <= 100):
	t = str(a)
	m = t.find('7')
	if a % 7 != 0 and m == -1:
		print(a)
	a+=1
