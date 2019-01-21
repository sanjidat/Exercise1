# Reasons for concurrency and parallelism


To complete this exercise you will have to use git. Create one or several commits that adds answers to the following questions and push it to your groups repository to complete the task.

When answering the questions, remember to use all the resources at your disposal. Asking the internet isn't a form of "cheating", it's a way of learning.

 ### What is concurrency? What is parallelism? What's the difference?

Concurrency:

When we talk about minimum two tasks or more, concurrency is essentially applicable there. Here it seems like tasks run simultaneously but essentially they may not. It takes the advantage of CPU time-slicing feature of operating system where each task run part of its task and then go to waiting state. CPU is assigned to its second task to complete its part of task when the first task is in waiting state.

Parallelism:

Multiple tasks or several parts of a unique tasks literally runs at the same time which is known as parallelism. It does not require two tasks to exit at the same time.

It seems ike concurrency and parallelism are same thing but they are not. The differences between concurrency and parallelism are given below:

1.Two tasks can start, run and complete in overlapping time period in Concurrency but tasks literally runs at the same time in parallelism.

2. There are composition of independently execution processes in concurrency and simultaneous execution of computations in parallelism.

3. Concurrency deals with lots of things at once and parallelism does lots of things at once.

4. An application can be concurrent – but not parallel, which means that it processes more than one task at the same time, but no two tasks are executing at same time instant.
An application can be parallel – but not concurrent, which means that it processes multiple sub-tasks of a task in multi-core CPU at same time.

 ### Why have machines become increasingly multicore in the past decade?

Multi core processors are typically a single processor which contains several cores on a chip. The individual cores on a multicore processor do not necessarily run as much as faster as highest performing single core processor. But they improve overall performance by handling more tasks in parallel. Multicore machines can handle more than one thread. The clock speed is also higher in multicore machine.  
 
### What kinds of problems motivates the need for concurrent execution?
 (Or phrased differently: What problems do concurrency help in solving?)
 
> The concurrent execution of activities can take place in different activities like single core processor, multi core processor, multiprocessor or in multiple machine. Apart from this the use of concurrency is generally motivated by performance gains. Concurrence also helps in 
1. Reducing Latency:
	A unit of work can be executed in shorter time by subdivision into parts by executing concurrently.

2. Hide Latency:
	Multiple long-running tasks are executed together by the underlying system. This is particularly effective when the tasks are blocked because of external resources they must wait upon, such as disk or network I/O operations.

3. Increase throughput:
By executing multiple tasks concurrently, the general system throughput can be increased. It is important to notice that this also speeds up independent sequential tasks that have not been specifically designed for concurrency yet.

### Does creating concurrent programs make the programmer's life easier? Harder? Maybe both?
 (Come back to this after you have worked on part 4 of this exercise)
 
> I think it depends. The exercise 1 was understandable enough using the concurrent program. But it is not necessary that everything will be easier with the concurrent program.
 
 ### What are the differences between processes, threads, green threads, and coroutines?
 
> The definition of processes, threads, green threads and coroutines are given below. Using that definitions we can easily understand the differences between them.

Processes:

1. Each process has its own virtual address space.
2. Processes can run in parallel with other processes on         different processors.
3. Processes can be interrupted by the system to allow another process to run.
4. The time overhead for creating and context switching between processes is relatively high.
5. The memory overhead of processes is high.

Threads:

1. Threads are "contained" within some particular process.
2. Threads which are in the same process share the same virtual address space.
3. Threads are interrupted by the system to allow another thread to run.
4. Threads can run in parallel with other threads on different processors.
5. The memory and time overheads associated with threads are smaller than processes, but still non-trivial.

Green Threads:

1. Green threads are user-space projections of the same concept as threads, but are not OS-managed.
2. They are not truely concurrent but probably best to consider this as interleaved or multiplexed.

Coroutines:

1. Some coroutine implementations are actually "shallow" cooperative threads.
2. Often coroutine frameworks have yield primitives that require the invoker to explicitly state which coroutine control should transfer to.

### Which one of these do `pthread_create()` (C/POSIX), `threading.Thread()` (Python), `go` (Go) create?
 
> pthread_create(). 
 
### How does pythons Global Interpreter Lock (GIL) influence the way a python Thread behaves?
 
> The python GIL is a mutex that allows only one thread to hold the control of the python interpreter that is only one thread can be in a state of execution at any point in time.
 
 ### With this in mind: What is the workaround for the GIL (Hint: it's another module)?
 
> In a multi processor multiple processes are used instead of thread. Each of the python process gets its own python interpreter and memory space in order to avoid GIL. 
 
 ### What does `func GOMAXPROCS(n int) int` change? 

> The function GOMAXPROCS limits the number of operating system threads which executes user level go code simultaneously. On behalf of go code there is no limit to the number of threads that can be block in system calls,those do not count against the GOMAXPROCS limit. The GOMAXPROCS function of this packages querries and changes the limit.

