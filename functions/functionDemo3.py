def getUserData(age,salary,name):
    print(f"name  ={name}")
    print(f"Salary  ={salary}")
    print(f"AGe  ={age}")


getUserData(20,20000,"abc")    
getUserData(23000,"pqr",23)

#named param argumen....

#getUserData(age=23,name="amit",salary=67000)
#getUserData(age=23,name="amit",23000) #error
#getUserData(age=23,name="amit",age=24) #error  keyword argument repeated: age
#getUserData(23,name="amit",salary=34500)
#getUserData(23,"ok",salary=34500) error...