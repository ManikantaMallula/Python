from pickle import *
from filepractice import *
with open("pic.txt","rb") as f:
    op=load(f)
    op.disply()
