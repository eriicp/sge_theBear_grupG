from fastapi import APIRouter, HTTPException
from .models import Employee  # Assuming you have an Employee model defined in models.py

router = APIRouter()

# Sample in-memory storage for employees
employees = []

@router.post("/empleats/", response_model=Employee)
def create_employee(employee: Employee):
    employees.append(employee)
    return employee

@router.get("/empleats/{employee_id}", response_model=Employee)
def read_employee(employee_id: int):
    if employee_id < 0 or employee_id >= len(employees):
        raise HTTPException(status_code=404, detail="Employee not found")
    return employees[employee_id]

@router.put("/empleats/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: Employee):
    if employee_id < 0 or employee_id >= len(employees):
        raise HTTPException(status_code=404, detail="Employee not found")
    employees[employee_id] = employee
    return employee

@router.delete("/empleats/{employee_id}")
def delete_employee(employee_id: int):
    if employee_id < 0 or employee_id >= len(employees):
        raise HTTPException(status_code=404, detail="Employee not found")
    employees.pop(employee_id)
    return {"detail": "Employee deleted"}