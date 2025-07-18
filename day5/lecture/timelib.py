# the time module helps us work with time
import time

# the time() function returns the current time in seconds since "the epoch" - 00:00:00 UTC on January 1, 1970
current_time = time.time()
print(current_time)

# the sleep() function pauses the program for the given number of seconds
time.sleep(2)

# we can time how long a block of code takes to run
start_time = time.time()
for i in range(7200000):
    print(i)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

