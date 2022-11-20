import time

#record start time
start = time.time()

#define a sample code segment
a = 0
for i in range(1000):
    a += (i**100)

end = time.time()

print("The time of execution of above program is: ",(end-start)*10**3,"ms")

