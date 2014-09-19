#Currently Compatible with Python version 3.X
import random
import sys
import math

def is_probable_prime(n, k = 7):

    #use Rabin-Miller algorithm to return True (n is probably prime) or False (n is definitely composite)

   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here

      return [False, False, True, True, False, True][n]

   elif n & 1 == 0:  # should be faster than n % 2

      return False

   else:

      s, d = 0, n - 1

      while d & 1 == 0:

         s, d = s + 1, d >> 1

      # Use random.randint(2, n-2) for very large numbers
      # Use sys.maxint for 2.X versions

      for a in random.sample (range (2, min (n - 2, sys.maxsize)), min(n - 4, k)):

         x = pow(a, d, n)

         if x != 1 and x + 1 != n:

            for r in range(1, s):

               x = pow (x, 2, n)

               if x == 1:

                  return False  # composite for sure

               elif x == n - 1:

                  a = 0  # so we know loop didn't continue to end

                  break  # could be strong liar, try another a

            if a:

               return False  # composite if we reached end of this loop

      return True  # probably prime if reached end of outer loop

def generateLargePrime(k):

     #k is the desired bit length

     r = 100 * (int(math.log (k, 2)) + 1) #number of attempts max

     num_tries = r

     while r > 0:

        #randrange is mersenne twister and is completely deterministic

        #unusable for serious crypto purposes
        
        #use long for 2.X and int for 3.X

         n = int(random.randrange(2**(k-1) + 1,2**(k),2))

         r -= 1

         #print ("{0}, {1}, {2}, {3}, {4}").format(k, 2**(k-1), 2**l, n) - debug - problems at the borderline of 32 bit in pre-version 3 python due to long/int distinction resulting in integer overflow

         if is_probable_prime(n) == True:

             return n

     print ("Failure after " + str (num_tries) + " tries.")
     sys.exit()

def inp():

    try:

        bits = int(input ("Please enter the bits of encryption you would like in [32, 2048] as a power of 2: "))

        if bits < 32:

          print ("Error. Bit length is too small.\n")

        if bits > 2048:

          print ("Error. Bit length is too large.\n")

        if (math.log (bits, 2) + 1) % 1 != 0:

          print ("Error. Bit length is not a power of 2.\n")

        return bits

    except ValueError:

        print ("Error. Not a valid integer.\n")
        
        inp()
  
#print (generateLargePrime(bits))

