from django.shortcuts import render

def student_profile(request):
    student = None

    if request.method == "POST":
        student = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'course': request.POST.get('course')
        }

    return render(request, 'profile.html', {'student': student})
