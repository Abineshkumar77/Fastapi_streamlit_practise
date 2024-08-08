from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

student={
    1:{
        "name":"jhon",
        "age":17,
        "Class":"cse"
    }
}

class Student(BaseModel):
    name:str
    age:int
    Class:str

class UpdateStudent(BaseModel):
     name:Optional[str]=None
     age:Optional[int]=None
     Class:Optional[str]=None


@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(...,description="enter students id",gt=0)):
    return student[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id,name : Optional[str] = None,test=int):
    for student_id in student:
        if student[student_id]["name"]==name:
            return student[student_id]
    return {"date":"not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, students : Student):
    if student_id in student:
        return {"Error" : "Student exists"}
    
    student[student_id] = students
    return student[student_id]

@app.put("/update-student/{student_id}")
def upadate_student(student_id: int, students:UpdateStudent):
    if student_id not in student:
        return{"Error" : "Students does not exist"}
    
    if students.name != None:
        student[student_id].name = students.name
    
    if students.age != None:
        student[student_id].age = students.age

    if students.Class != None:
        student[student_id].Class = students.Class

    return student[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in student:
        return {"Error":"Student does not exit"}
    
    del student[student_id]
    return {"Message" : "Student deleted successfully"}