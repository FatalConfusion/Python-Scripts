#Hackerrank Even-Odd query

def find(x,y):
    Status=''
    if x>y:
        return 1
    
    return pow(arr[x],find(x+1,y))

#getting the size and the array as input
N=int(input("Enter the size of the array: "))
arr=list(map(int,input("Enter the space seperated value of the array: ").split(" ")))
#inserting None at [0]th position to make the array 1-indexed
arr.insert(0,None)
Q=int(input("Enter the number of queries: "))
tempsol=0

for _ in range(Q):
    xin,yin=input("Enter the space seperated query values for arguments: ").split(" ")
    xin=int(xin)
    yin=int(yin)
    tempsol=find(xin,yin)
    if tempsol%2==0:
        print("Even")
    else:
        print("Odd")


