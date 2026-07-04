from pydantic import BaseModel, EmailStr, Field
from typing import Optional



def combo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

combo(1, 2, 3, name="Ram", age=20)

print("*" * 50)
class Student(BaseModel):
    name : str

new_dict = {"name" : "Rohit"}

student = Student(**new_dict)
print(student)



###### DEFAULT VALUES

# class Student(BaseModel):
#     name : str = "rohit"

# new_dict = {}

# student = Student(**new_dict)
# print(student)




####### OPTIONAL VALUES
# from typing import Optional
# class Student(BaseModel):
#     name : str
#     age : Optional[int] = None   #### if age doesn't given it print none

# new_dict = {"name" : "Rohit"}

# student = Student(**new_dict)
# print(student)




# class Student(BaseModel):
#     name : str
#     age : Optional[int]
#     email : EmailStr

# new_dict = {"name" : "Rohit", "email" : "somethingxyz@gmail.com", "age" : 32}

# student = Student(**new_dict)
# print(type(student))







# class Student(BaseModel):
#     name : str
#     age : Optional[int] = None
#     email : EmailStr
#     cgpa : float = Field(gt = 0, lt = 10)

# new_dict = {"name" : "Rohit", "email" : "somethingxyz@gmail.com", "age" : 32, "cgpa" : 9}

# student = Student(**new_dict)
# student_dict = dict(student)
# student_json = student.model_dump_json()
# print(student_dict["age"])
