def fac(sayi):
	if(sayi>1):
		sayi = fac(sayi-1)*sayi

	return sayi






def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a


