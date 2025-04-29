import threading
import time
import math
def PrimeOrNot(start, end, prime_number_list):
    for number in range(start, end+1):
        if number < 2:
            continue
        x = True
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                x = False
                break
        if x :
            prime_number_list.append(number)
            
if __name__ == "__main__":
    prime_number_list = []
    start = 0
    end = 100
    process_number = 4
    ranges = [(0, 1000000), (1000000, 2000000), (2000000, 3000000), (3000000, 4000000)]

    threads = []
    start_time = time.time()
    for start, end in ranges:
        thread = threading.Thread(target=PrimeOrNot, args=(start, end, prime_number_list))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    finish_time = time.time()
    total_time = finish_time - start_time
#    print("Prime Numbers: ",  sorted(prime_number_list))
    print("Total number of prime numbers between 0 and 4000000: ",  len(prime_number_list))
    print(f"Total Time: {total_time} seconds")