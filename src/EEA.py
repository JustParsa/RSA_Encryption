# O >> e always so a >> b always and this implementation will always work
#Recursive -- wrote myself
def EEA (a, b, x1, x2, y1, y2):
    quot, rem = a//b, a%b
    x, y = x1 - quot*x2, y1 - quot*y2
    #print (quot, rem, x, y) #-- debug
    if rem == 0:
    	return y2
    return EEA (b, rem, x2, x, y2, y)

#Iterative -- this one I stole from the interwebs to do some debugging
# def egcd(a, b):
#     x,y, u,v = 0,1, 1,0
#     while a != 0:
#         q, r = b//a, b%a
#         m, n = x-u*q, y-v*q
#         b,a, x,y, u,v = a,r, u,v, m,n
#     gcd = b
#     return y
