from math import factorial

def ncr2(n) :
    return n*(n-1)/2

for T in range(1, int(raw_input())+1) :
    case_input = raw_input().split(' ')
    lower = int(case_input.pop(0))
    upper = int(case_input.pop(0))
    
    result = 0
    mapping = {}
    digit = len(str(lower))
    #print "lower = %s, upper = %s, digit=%d" %(lower,upper,digit)
    for i in range(lower,upper+1) :
        #print "Considering: %d" %i
        count = 0
        tmp = str(i)
        for j in range(1,digit+1) :
            #print "--> Looping: %s" %(tmp)
            if lower <= int(tmp) <= upper and tmp[0] != '0' and not(mapping.has_key(tmp)) :
                count += 1
                mapping[tmp] = 'x'
                #print "--> count[%s] + 1 = %d" %(tmp,count)
            #else :
                #print "--> Out of condition!!"
            tmp = tmp[-1] + tmp[:-1]
        if count > 1 :
            result += ncr2(count)
        #print "result now = %d" %result
             
    
    print 'Case #%d: %d' % (T, result)
    #print '=================================================='