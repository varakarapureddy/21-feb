#program for printing a,b,c,d 
n=int(input('enter n value'))
ascii_value=97
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(ascii_value),end=" ")
        ascii_value+=1
    print("\n")
