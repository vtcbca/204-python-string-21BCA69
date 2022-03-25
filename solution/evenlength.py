# print even number of character
l=[]
count=0
def list(l):
    for i in range(5):
        b=input("Enter any string : ")
        l.append(b)
list(l)
def evenlenth(l):
    for i in l:
        count=0
        for j in i:
            count=count+1
        if(count%2==0):
            print("The List is {} and it's length is {}.".format(i,count))
evenlenth(l)
