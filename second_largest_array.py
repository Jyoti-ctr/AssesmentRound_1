noOfElements=int(input("Enter the number of elements you wants to add: "))
#Collecting  the input Elements
Array=[]
for i in range(0,noOfElements, 1):
    userInput=int(input("Enter your elements: "))
    Array.append(userInput) # Adding elements to List
print(Array)

#Sorting the Array for fast fetching

Array=set(Array)
Array=list(Array)
for i in range(0, len(Array)-1+1, 1):
    for j in range(i+1,len(Array)-1+1, 1):
        Array[i],Array[j]=Array[j],Array[i]
print("The second largest elements in array is : ",Array[1]) #Second largest elemnts