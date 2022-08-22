''' 1) write a program on magical method add , pos and neg? '''
##class Meth:
##    def __init__(self,kilos):
##        self.kilos=kilos
##    def __add__(self,otherWeight):
##        return Meth(self.kilos+otherWeight)
##w1=Meth(10)
##w2=Meth(20)
##tot=w1.__add__(w2)
##print(tot.kilos)

'''2) write a program convert day number to date in particular year? '''
##from datetime import datetime 
##day_num = input("Enter the day number: ")
##day_num.rjust(3 + len(day_num), '0') 
##year = input("Enter the year: ")
##res = datetime.strptime(year + "-" + day_num, "%Y-%j").strftime("%d-%m-%Y") 
##print("The day number: " + str(day_num)) 
##print("The date in the particular year: " + str(res))

'''3) write a dictionary to a file in python? '''
##import pickle
##athletes = {
##    "Name": ["Neymar","Lionel Messi", "Cristiano Ronaldo", "Eden Hazard", "Erling Halland" ],
##    "Club": ["PSG", "PSG", "Manchester United", "Real Madrid", "manchester City"]
## }
##athletes_files=open("athletes.txt","wb")
##pickle.dump(athletes,athletes_files)
##athletes_files.close()
##athletes_file = open("athletes.txt", "rb")
##athletes = pickle.load(athletes_file)
##athletes_file.close()
##print(athletes)

''' 4) find the most repeated word in a text file? '''
##from collections import Counter
##f=open("words1.txt","r")
##r=f.read()
##r=r.split()
###print(r)
##count=Counter(r)
##l=list(count)
##print("The most repeated words in file is:",l[0])

''' 5) write a program on sprial number?

eg:-1 2 3
    8 9 4
    7 6 5 '''
##class Solution(object):
##   def generateMatrix(self, n):
##      row1 = 0
##      col1 = 0
##      row2 = n
##      col2 = n
##      result = [ [0 for i in range(n)] for j in range(n)]
##      num = 1
##      while num<=n**2:
##         for i in range(col1,col2):
##            result[row1][i] = num
##            num+=1
##         if num > n**2:
##            break
##         for i in range(row1+1,row2):
##            result[i][col2-1] = num
##            num+=1
##         if num > n**2:
##            break
##         for i in range(col2-2,col1-1,-1):
##            result[row2-1][i] = num
##            num+=1
##         if num > n**2:
##            break
##         for i in range(row2-2,row1,-1):
##            result[i][col1] = num
##            num+=1
##            row1+=1
##            row2-=1
##            col1+=1
            col2-=1
      return result
ob1 = Solution()
print(ob1.generateMatrix(3))
