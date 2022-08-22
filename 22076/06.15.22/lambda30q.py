'''Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.'''

##r1=lambda x:x+15
##r2=lambda x,y:x*y
##print(r1(10))
##print(r2(10,2))

'''2. Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number. Go to the editor
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75 '''

##def numbers(n):
##    return lambda x:x*n
##r=numbers(2)
##print("Double the number =",r(15))
##r1=numbers(3)
##print("Triple the number =",r1(15))
##r2=numbers(4)
##print("Triple the number =",r2(15))
##r3=numbers(5)
##print("Triple the number =",r3(15))

'''3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''

##subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##print("Original list of tuples:")
##print(subject_marks)
##subject_marks.sort(key = lambda x: x[1])
##print("\nSorting the List of Tuples:")
##print(subject_marks)













