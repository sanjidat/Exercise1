#	Python Code for Exercise 1:


from threading import Thread

i = 0



#Define a function for the thread
def incrementingFunction():
    


for j in range(1000000):
        
	global i
      
	i += 1


\def decrementingFunction():
    
	for j in range(1000000):
        
	global i
     	
	i -= 1


#Create two threads as follows


def main():

incrementing = Thread(target = incrementingFunction, args = (),)

decrementing = Thread(target = decrementingFunction, args = (),)
    
    
    incrementing.start()
    decrementing.start()
    
    incrementing.join()
    decrementing.join()
    
    print ("The magic number is %d" % (i))
main()



