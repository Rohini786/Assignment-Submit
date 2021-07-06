def isprime(N):
  for i in range(2,N//2):
    if(N%i==0):
      return("it is not a prime number")
  return("Given no. is a prime number")
N=int(input("enter Number: "))
print(isprime(N))
