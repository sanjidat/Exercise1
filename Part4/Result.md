

C code for Exercise 1:

#include <pthread.h>
#include <stdio.h>



int i = 0;
int j=0;



// Note the return type: void*
void* incrementingThreadFunction(){
    


for(j=0; j<1000000; j++) { 
           i=i+1;  // TODO: increment i 1_000_000 times
    }
 return NULL;
}



void* decrementingThreadFunction(){
    


for(j=0; j<1000000; j++){
           i=i-1;    // TODO: decrement i 1_000_000 times
    } 
    return NULL;
}



int main(){
    



pthread_t incrementingThread;
    

pthread_t decrementingThread;
    

pthread_create(&incrementingThread, NULL, 

incrementingThreadFunction, NULL);
    

pthread_create(&decrementingThread, NULL, 


decrementingThreadFunction, NULL);  // TODO: declare 


incrementingThread and decrementingThread
    

pthread_join(incrementingThread, NULL);
    
pthread_join(decrementingThread, NULL);
    
printf("The magic number is: %d\n", i);
    
return 0;

}



Python Code for Exercise 1:


from threading import Thread

i = 0



# Define a function for the thread
def incrementingFunction():
    


for j in range(1000000):
        global i
        i += 1


\def decrementingFunction():
    for j in range(1000000):
        global i
        i -= 1



# Create two threads as follows


def main():
    incrementing = Thread(target = incrementingFunction, args = (),)
    decrementing = Thread(target = decrementingFunction, args = (),)
    
    
    incrementing.start()
    decrementing.start()
    
    incrementing.join()
    decrementing.join()
    
    print ("The magic number is %d" % (i))
main()




Go lang Code for Exercise 1:

package main

import (
    . "fmt"
    "runtime"
    "time"
)

var i = 0

func incrementing() {
    //TODO: increment i 1000000 times
    for j := 0; j < 10000; j++ {
		i++
	}
}

func decrementing() {
    //TODO: decrement i 1000000 times
    for j := 0; j < 10000; j++ {
		i--
	}
}

func main() {
    runtime.GOMAXPROCS(runtime.NumCPU())    // I guess this is a hint to what GOMAXPROCS does...
	                                    // Try doing the exercise both with and without it!

    // TODO: Spawn both functions as goroutines
    go incrementing()
    go decrementing()
	
    // We have no way to wait for the completion of a goroutine (without additional syncronization of some sort)
    // We'll come back to using channels in Exercise 2. For now: Sleep.
    time.Sleep(100*time.Millisecond)
    Println("The magic number is:", i)
}




In this part of exercise 1 we did a concurrent program. I got random variations of outputs with the Go lang and python language but with the C language i only got an specific output. 

























