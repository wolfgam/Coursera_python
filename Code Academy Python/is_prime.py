def is_prime(x):
    if x<2:
        return False
    elif x==2 or x==3:
        return True
    else:    
        for n in range(2,x-1):
        
            if x%n==0:
                return False
                break
    return True
  
