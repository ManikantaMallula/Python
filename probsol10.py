'''IPL MATCH DETAILS:-

write a program that reads all the match outcomes and summarizes the information of all the matches.
Points are given to the teams based on the outcome of the match.A win esrns a team 3 points.A draw earns 
1.A loss earns O.
The following info is expected:

MP:Matches played
W:Matches Won
D:Matches Drawn(Tied)
L:Matches Lost
P:Points

The team info should be displayed in descending order of points

INPUT
----

The first line contains a single integer N,denoting the total no.of matches played.The following N lines contains outcomes of N matches.

Each of those lines has info on the teams(T1,T2)which played and the outcome(O)in format T1;T2;O.

The outcome(O)is one of 'win','loss','draw' and refers to the first team instead.see sample Input/output for better understanding.

The team name may contain spaces.

OUTPUT
------

The output should contain summarized info of all the matches in a format similar to
'Team:RCB,Matches played:3,Won:2,Lost:0,Draw:1,Points:7'for each team in anew line.

If there  are no teams to print in summary,print "No Output".

Constraints
----------- '''

##rcb=[0,0,0,0,0]
##mi=[0,0,0,0,0]
##
##matches=5
##while matches>0:
##    rcb[0]+=1
##    mi[0]+=1
##    winner=input("enter winning team name")
##    if winner=="rcb":
##        rcb[1]+=1
##        mi[2]+=1
##        rcb[4]+=3
##    elif winner=="mi":
##        mi[1]+=1
##        rcb[2]+=1
##        mi[4]+=3
##    elif winner=="draw":
##        rcb[3]+=1
##        mi[3]+=1
##        rcb[4]+=2
##        mi[4]+=2
##    matches-=1
##
##
##if rcb[4]>mi[4]:
##    print("Team: RCB ","Matches played: "rcb[0],"Won: ",rcb[1],"Lost: ",rcb[2],"Draw: ",rcb[3],"Points: ",rcb[4])
##elif rcb[4]<mi[4]:     
##    print("Team: mi ","Matches played: "mi[0],"Won: ",mi[1],"Lost: ",mi[2],"Draw: ",mi[3],"Points: ",mi[4])
##else:
##    print("equal points,no output")



























