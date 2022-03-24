def createList():
    l=[]
    for i in range(5):
        b=input("Enter 5 String :")
        l.append(b)
    return(l)
a=createList()
print(a)
count=0
def strlen(l):
     count=0
     for i in l:
         for j in i:
             if(l%2==0):
                 count+=1
     return(count)       
