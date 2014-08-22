# O >> e always so a >> b always and this implementation will always work

def EEA (a, b, x1, x2, y1, y2):
    quot = int(a/b)
    rem = a%b
    x = x1 - quot*x2
    y = y1 - quot*y2
    #print (quot, rem, x, y) #-- debug
    if rem == 0:
    	return y2
    return EEA (b, rem, x2, x, y2, y)