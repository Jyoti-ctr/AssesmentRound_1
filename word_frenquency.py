stringInput=input("Enter the Sentence: ") # user Input
Words=[]
Words.append(stringInput)
count=0
for i in range(0, len(Words)-1+1, 1):
    for j in range(i+1,len(Words)-1+1, 1) :
        if Words[i]==Words[j]:
            count=count+1
            
print(count)
print(stringInput)
print()