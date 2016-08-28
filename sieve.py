# /usr/bin/pyhton3
def sieve(limit):
	a = [True]*limit
	a[0]=False
	a[1]=False
	for (i,isprime) in enumerate(a):
		if(isprime):
			yield i
			for n in range(i*i,limit,i):
				a[n]=False
# s=0
for i in sieve(2000000):
	print(i)
# print(s)