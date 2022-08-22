1.write a python program do multiplication program using generators and use sys module to find memory size
'''
##import sys
##def mul(num):
##    for i in range(1,11):
##        yield f"{num} x {i} ={num*i}"
##num=int(input("enter a number:"))
##a=mul(num)
##for i in a:
##    print(i)
##print(sys.getsizeof(a))
'''
2..write a python program do multiplication program using function
'''
##def mul(num):
##    for i in range(1,11):
##        print(f"{num} x {i} ={num*i}")
##num=int(input("enter a number:"))
##a=mul(num)
'''
3.Write a Python program to extract characters from various text
files and puts them into a list.
'''
##f=open("file1.txt",mode="r")
##r=f.read()
##b=[]
##for i in r:
##    b.append(i)
##print(b)
'''
4. Write a Python program to create a file where all letters of
English alphabet are listed by specified number of letters on each line.
'''
##import string
##def letters_file_line(n):
##   with open("words1.txt", "w") as f:
##       alphabet = string.ascii_uppercase
##       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
##       f.writelines(letters)
##letters_file_line(3)
'''
5.write a python program in twin prime using outer and inner functions
'''
##def outer():
##    def is_prime(n):
##       for i in range(2, n):
##          if n % i == 0:
##             return False
##       return True
##
##    def generate_twins(start, end):
##       for i in range(start, end):
##          j = i + 2
##          if(is_prime(i) and is_prime(j)):
##             print("{:d} and {:d}".format(i, j))
##
##    generate_twins(2, 100)
##outer()
