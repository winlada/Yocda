def main(num, num2):
	summ = summation(num, num2)
	subb = substraction(num, num2)
	return subb, summ

def substraction(var1, var2):
	return var1 - var2

def summation(n1, n2):
	return n1 + n2
main(int(input()), int(input()))
