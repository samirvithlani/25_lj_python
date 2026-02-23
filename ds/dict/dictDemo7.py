data = {"Virat":[123,78,81],"rohit":[142,67,21]}
print(data.keys())
print(data.values())
print(data.get("Virat"))
data.get("Virat")[1]=91
# y = data.get("Virat")
# y[1]=90
print(data)
data.update({"Hardik":[52,67]})
print(data)
#print(data.get("Virat")[2])
sum=0
totalScore =0
for i,j in data.items():
    print(f"{i}")
    for r in j:
        sum+=r
        print(r)
    print("total =",sum)
    totalScore+=sum
    sum=0

print("ttoal score ==",totalScore)    