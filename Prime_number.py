def getprime(num):
    for val in range(2, num):

       # If num is divisible by any number
       # between 2 and val, it is not prime
       if val > 1:
           for n in range(2, val):
               if (val % n) == 0:
                   break
           else:
               print(val)
getprime(10)
