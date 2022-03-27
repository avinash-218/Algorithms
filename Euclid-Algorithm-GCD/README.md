# Euclid's algorithm
## To find Greatest Common Divisor (Positive Numbers)

GCD-Greatest Common Divisor
GCD of two numbers is the greatest common divisor of both

Let's start with an example:
1)To find GCD of 14,35
    a) Factors of 14 are - 1,7,14
    b) Factors of 35 are - 1,5,7,35
    
    GCD is the greatest among the common factors of 14 and 35, which in this case is 7
    
   Note: Gcd of any number othewr than zero with zero is that number.
         i.e,GCD(33,0)=33
         
         GCD(0,0) is undefined
         
A simple way to find the GCD of two umbers is 
  1)Find the factors of the two numbers separately and store them in separate lists
  2)Find the common factors in the two list and store them in another list
  3)find the largest element in the list
  
  
To make our code optimised in terms of time ..., we use Euclid's Algorithm.
Because the above mentioned algorithm takes every factors of each element into consideration and find the common factors and blah blah blah...
Its tedious right? So we need an alternate algorithm to find the GCD with lesser cost in terms of memory and speed.

The concept of Euclid's Algorithm to find GCD of two numbers is explained below

Consider two numbers to find their GCD: A,B

Also note that, every positive number have 1 as a factor, which means that GCD of two numbers will have atleast one common divisor which is 1.
Let us consider that greatest common divisor of A and B as 'd'.
Therefore, A can be written as .... A = K1*d (for any number K1)
Similarly, B can be written as .... B = K2*d (for any number K2)

Let us subtract A and B to find any relation between GCD of two numbers and Gcd of difference of the two numbers and the smaller number ( GCD(A-B,B)... Assume A>B)
Therefore,
          A - B = K1*d - K2*d ...........#Equation 0
          A - B = (K1 - K2) * d ........#Equation 1
          
From equation 1, it can be said that d is a factor of A-B, A , B
Note d is the greatest common divisor of A and B. Now it is proved that d is the Greatest common divisor of A,B,A-B.
So, it is enough to find GCD(A-B,B) instead of GCD(A,B) which is costly in terms of time.
   
So it is proved that GCD(A,B)=GCD(A-B,B)    ...where A>B (Since A-B should be greater than 0)

We have not yet proved Euclid's Algorithm.
Till now ,we proved only  GCD(A,B)=GCD(A-B,B)   ............#Equation 2

By Equation 2,
    GCD(A-B,B) = GCD(A-B-B,B)
  =>GCD(A-B,B) = GCD(A-2B,B)    ...........#Equation 3
  
  GCD(A-2B,B) = GCD(A-2B-B,B)
  =>GCD(A-2B,B) = GCD(A-3B,B)   .............#Equation 4
  
By Equation 3 and Equation 4,
  GCD(A,B) = GCD(A-3B,B)
  
  Therefore,
  GCD(A,B) = GCD(A-M*B,B)     ...................#Equation 5
  
  But, A = M*B + R  ....where M is quotient and R is the Remainder of A%B
  => A - M*B = R      ............................#Equation 6
  
  By Equation 5 and Equation 6,
  GCD(A,B) = GCD(R,B)........where R is the Remainder of A%B
