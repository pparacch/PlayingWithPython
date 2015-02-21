def genPrimes():
    i = 2
    
    while True:
        prime = True
        
        if i > 2:
            for j in range(2,i):
                if i%j == 0:
                    prime = False
                    break
        if prime:
            yield i
        
        i += 1
        
# test = genPrimes()
# test.next()