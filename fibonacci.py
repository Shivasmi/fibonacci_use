from functools import lru_cache
import logging 

logging.basicConfig(filename = 'logging.log', level = logging.DEBUG, 
                    format = '%(asctime)s -  %(levelname)s - %(message)s ')

@lru_cache (maxsize = 1000) #if you dont specify the maxsize, by default 128 number will compute 
def fibonacci(n):
    if type(n) != int:
        #raise TypeError("n must be an integer")
        logging.info(f'{n} is not an integer')
    if n < 1:
        #raise ValueError(" n  must bee a postive int")
        logging.error(f' {n} must be positive ')
    
    
    
    #this function will compute the nth number 
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        #here the function is calling it self which we called recursive function 
        return fibonacci(n-1) + fibonacci(n-2)
        
    
for n in range (1, 99):
    print (fibonacci(n))

    