from django.shortcuts import render, redirect
from .models import Student

def student_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Student.objects.create(name=name)
        return redirect("student")

    students = Student.objects.all()
    return render(request, "student.html", {"students": students})
