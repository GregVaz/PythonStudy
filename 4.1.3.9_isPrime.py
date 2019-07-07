def isPrime(num):
    l = []
    for i in range(2,num//2 + 1):
        if not num%i:
            l.append(False)
    if not l:
        return True
    else:
        return False

for i in range(1, 100):
	if isPrime(i + 1):
			print(i + 1, end=" ")