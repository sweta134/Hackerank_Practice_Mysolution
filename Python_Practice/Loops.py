#Task
#The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

#solution - Python 3
if __name__ == '__main__':
    n = int(input())
    for i in range(n): #Range(n) -> value of i=0 to n-1
        print(i*i) #or print(i**2) -> i to the power 2
