from textblob import TextBlob


a=open("1.txt","r+")
d=a.read()
b=TextBlob(d)

print(b.translate(to="ta"))
a.close()


a=open("1.txt","w")
a.write(str(b.translate(to="ta")))
a.close()





