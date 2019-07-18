def fib(f1, f2, count):
	fib_sum = f1 + f2
	while count >= 2:
		count -= 1
		return fib(f2, fib_sum, count)
	return fib_sum


def fib2(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib2(x-1) + fib2(x-2)


def rabbits(f1, f2, months, mult):
	if months < 2:
		return f2
	else:		
		months -= 1
		return rabbits(f2, f1*mult+f2, months, mult)
	return f2


def rabbits2(months, mult):
	mature = 0
	young = 1
	total = mature + young
	if months < 2:
		return total
	else:
		while months > 2:
			next_mature = mature + young
			next_young = mature * mult
			mature = next_mature
			young = next_young
			months -= 1
		return young + mature

	
def rabbits3(n, k):
	a, b = 0,1
	for i in range(1,n):
    		a, b = b, k * a + b
	return b
