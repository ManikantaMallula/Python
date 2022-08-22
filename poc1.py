import pandas as pd
import datetime
import smtplib
import os

cwd=os.getcwd()
print(cwd)
os.chdir(cwd)

gmailid=input("enter email id: ")
passw=input("enter your password: ")

def sendemail(to,sub,msg):
    print(f"Email to {to} sent: \nSubject: {sub} ,\nMessage: {msg}")
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(gmailid,passw)
    s.sendmail(gmailid,to,f"Subject: {sub} \n\n {msg}")
    s.quit()

    if __name__=="__main__":
        df=pd.read_excel("data.xlsx")
        today=datetime.datetime.now().strftime("%d-%m")
        yearnow=datetime.datetime.now().strftime("%y")

    wish=[]
    for r,c in df.iterrows():
        bd=item["birthday"]
        bd=datetime.datetime.strptime(bd,"%d-%m-%y")
        bd=datetime.datetime.strftime("%d-%m")
        if (bd==today) and yearnow not in str[item["LastWishedYear"]]:
            sendemail(item["email"],"many more happy...",item["dialogue"])
            wish.append(r)
                                             
    if writeInd != None:
        for i in writeInd:
            oldYear = df.loc[i, 'LastWishedYear']
            df.loc[i, 'LastWishedYear'] = str(oldYear) + ", " + str(yearnow)

    df.to_excel('data.xlsx', index=False)
    
    
    
