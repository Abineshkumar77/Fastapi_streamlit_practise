import streamlit as st
import requests


base_url = "http://127.0.0.1:8000"  


st.title("Student Management System")


operation = st.selectbox("Choose an operation", ["Get Student", "Create Student", "Update Student", "Delete Student"])


if operation == "Get Student":
    student_id = st.number_input("Enter Student ID", min_value=1, step=1)
    if st.button("Get Student"):
        response = requests.get(f"{base_url}/get-student/{student_id}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Student not found")

elif operation == "Create Student":
    student_id = st.number_input("Enter New Student ID", min_value=1, step=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    class_name = st.text_input("Class")

    if st.button("Create Student"):
        student_data = {
            "name": name,
            "age": age,
            "Class": class_name
        }
        response = requests.post(f"{base_url}/create-student/{student_id}", json=student_data)
        if response.status_code == 200:
            st.success("Student created successfully")
        else:
            st.error("Error: Student might already exist")

elif operation == "Update Student":
    student_id = st.number_input("Enter Student ID to Update", min_value=1, step=1)
    name = st.text_input("Name (Leave empty if no change)")
    age = st.number_input("Age (Leave 0 if no change)", min_value=0, step=1)
    class_name = st.text_input("Class (Leave empty if no change)")

    if st.button("Update Student"):
        student_data = {}
        if name:
            student_data["name"] = name
        if age:
            student_data["age"] = age
        if class_name:
            student_data["Class"] = class_name

        response = requests.put(f"{base_url}/update-student/{student_id}", json=student_data)
        if response.status_code == 200:
            st.success("Student updated successfully")
        else:
            st.error("Error: Student might not exist")

elif operation == "Delete Student":
    student_id = st.number_input("Enter Student ID to Delete", min_value=1, step=1)
    if st.button("Delete Student"):
        response = requests.delete(f"{base_url}/delete-student/{student_id}")
        if response.status_code == 200:
            st.success("Student deleted successfully")
        else:
            st.error("Error: Student might not exist")
