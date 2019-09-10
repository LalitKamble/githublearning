# In this program three threads would try to find prime number between 200 to 500 . At the end each thread will print the prime numbers it found.
#
# 1.	There is an integer variable ‘count’ with value 200.
# 2.	There are three threads Thread1, Thread2 and Thread3.
# 3.	Each thread either increments or decrements the count by some amount as shown below.
# a.	Thread1 increments or decrements count by 1
# b.	Thread2 increments or decrements count by 2
# c.	Thread3 increments or decrements count by 3
# 4.	Each thread updates count as per below rules.
# a.	Thread1 increments count by 1 if count is even and decrements count by 1 if count is odd.
# b.	Thread2 increments count by 2 if count is even and decrements count by 2 if count is odd.
# c.	Thread3 increments count by 3 if count is even and decrements count by 3 if count is odd.
# 5.	If at any point count becomes greater than 500 program stops.
# 6.	If by incrementing or decrementing count, it becomes a prime number, then the thread which made it prime records it.
# 7.	At the end of program each thread should print the number of prime numbers it found.

from threading import *
from time import sleep

count1 = 200
count2 = 500
 # below functions return the number by increment depends on rule
def prime_odd(num):
    if (num %2) >0:
        num = num -1
        return num
    else:
        num =num + 1
        return num


def secon_prime_odd(num):
    if (num %2) >0:
        num = num -2
        return num
    else:
        num =num + 2
        return num


def third_prime_odd(num):
    if (num %2) >0:
        num = num -3
        return num
    else:
        num =num + 3
        return num

# thread class was start from below
class firstthread(Thread):
    def run(self):
        first_counter = 0
        for first in range(count1,count2+1,1):
            numvar = secon_prime_odd(first)  # calling the function
            # print(str(numvar)+ ' function return var')
            if numvar > 500:
                # print('count became more than 500')
                # print(str(numvar) + ' more than 500')
                print(str(first_counter)+' first thread counter')
                return

            else:
                if numvar >1:
                    for  i in range(2,numvar):
                        if (numvar % i) == 0:
                            # print(str(first_i)+ ' is a prime number')
                            break
                    else:
                        # print(str(numvar)+ ' first thread')
                        first_counter = first_counter +1
                        sleep(0.1) # just increase to prevent overlapping of another thread
                # print(numvar)
                # first_counter =first_counter +1
        print(str(first_counter)+ ' first thread count')




class secondthread(Thread):
    def run(self):
        second_counter = 0
        for first in range(count1,count2+1,2):
            numvar = prime_odd(first)
            # print(str(numvar)+ ' function return var')
            if numvar > 500:
                # print('count became more than 500')
                # print(str(numvar) + ' more than 500')
                print(str(second_counter)+' second thread count')
                return

            else:
                if numvar >1:
                    for  i in range(2,numvar):
                        if (numvar % i) == 0:
                            # print(str(first_i)+ ' is a prime number')
                            break
                    else:
                        # print(str(numvar)+ ' second thread')
                        sleep(0.1)
                        second_counter = second_counter +1
                # print(numvar)
                # first_counter =first_counter +1
        print(str(second_counter) +'second thread count')


class thirdthread(Thread):
    def run(self):
        third_counter = 0
        for first in range(count1,count2+1,3):
            numvar = third_prime_odd(first)
            # print(str(numvar)+ ' function return var')
            if numvar > 500:
                # print('count became more than 500')
                # print(str(numvar) + ' more than 500')
                print(str(third_counter)+' third thread count')
                return

            else:
                if numvar >1:
                    for  i in range(2,numvar):
                        if (numvar % i) == 0:
                            # print(str(first_i)+ ' is a prime number')
                            break
                    else:
                        # print(str(numvar)+ ' third thread')
                        sleep(0.1)
                        third_counter = third_counter +1
                # print(numvar)
                # first_counter =first_counter +1
        print(str(third_counter) + "third thread count")


# class hello(Thread):
#     def run(self):
#         for i in range(5):
#             # print('hi')
#             # print(count1+1)
#             sleep(i)
#
#
t1 = firstthread()
t2 = secondthread()
t3 = thirdthread()
t1.start()
sleep(.2) # just to see the results and to prevent overlapping
t2.start()
sleep(0.2)
t3.start()
