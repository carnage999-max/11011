from django.shortcuts import render, redirect
from django.contrib import messages

def HomePage(request):
    return render(request, "main/index.html")

def gpaHome(request):
    if request.method == "POST":
        num_courses = int(request.POST.get('num_courses'))
        request.session['num_courses'] = num_courses
        return redirect("gpa")
    return render(request, "main/gpa/gpahome.html")

def semester_gpa(request):
    num_courses = request.session.get('num_courses')
    course_grades = list()
    course_names = []
    gpa = 0
    total_units = 0
    total_grade_points = 0
    if request.method == "POST":
        for i in range(num_courses):
            course_name = request.POST.get(f'course_name_{i}')
            course_names.append(course_name)
            course_grade = request.POST.get(f'course_grade_{i}')
            units = int(request.POST.get(f'units_{i}'))
            total_units += units
            grade_points = get_grade_points(course_grade) * units
            total_grade_points += grade_points
            course_grades.append((course_grade, units, grade_points))
        messages.success(request, "GPA calculated successully")
        gpa = round(total_grade_points / total_units, 2)
        print(course_grades)
    context = {
        "val": range(num_courses), "course_grades":course_grades, 
        "gpa":gpa, "course_names":course_names,
        "total_units":total_units,
    }
    return render(request, "main/gpa/semestergpa.html", context)

def get_grade_points(grade):
    grade_points = {
        'A':5.0,
        'B':4.0,
        'C':3.0,
        'D':2.0,
        'E':1.0,
        'F':0.0,
    }
    return grade_points.get(grade, 0.0)
