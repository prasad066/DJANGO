from django.http import HttpResponse
import json
from django.http import JsonResponse
from pathlib import Path
from django.shortcuts import render
def sample(request):
    return HttpResponse("DJAGO...")
def addition(request,a,b):
    return HttpResponse(f'sum of {a} and {b} is {a+b}')
def subtraction(request):
    a=int(request.GET.get('a'))
    b=int(request.GET.get('b'))
    return HttpResponse(f'difference of {a} and {b} is {a-b}')
def mul(request):
    return render(request,"first_app/mul.html")
def mulres(request):
    num1=int(request.GET.get('num1'))
    num2=int(request.GET.get('num2'))
    return HttpResponse(f'product of {num1} and {num2} is {num1*num2}')
def employees(request):
    file_path = Path(__file__).resolve().parent / "data" / "employees.json"
    with open(file_path, encoding="utf-8") as file:
        employees = json.load(file)
    return render(request,"first_app/emp.html",{'employees':employees})
def addemp(request):
    return render(request,'first_app/addemp.html')
def newemp(request):
    if request.method == "POST":
        data = json.loads(request.body)

        file_path = Path(__file__).resolve().parent / "data" / "employees.json"

        with open(file_path, "r", encoding="utf-8") as file:
            employees = json.load(file)

        new_employee = {
            "id": int(data["id"]),
            "name": data["name"],
            "department": data["department"]
        }

        employees.append(new_employee)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(employees, file, indent=4)

        return JsonResponse({
            "message": "Employee added successfully",
            "employee": new_employee
        })

    return JsonResponse({"error": "Only POST method allowed"}, status=405)
    