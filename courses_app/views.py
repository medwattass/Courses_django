from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course


def root(request):
    context = {
        'courses' : Course.objects.all(),
    }
    return render(request, 'courses/courses_board.html', context)


def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        name = request.POST.get('name')
        description = request.POST.get('description')
        Course.objects.create(name=name, description=description)
        messages.success(request, "Added a new course successfully")
    return redirect('/')


def destroy_page(request, id):
    context = {
        'this_course' : Course.objects.get(id=id),
    }
    return render(request, 'courses/destroy_page.html', context)


def destroy(request, id):
    if request.method == 'POST':
        Course.objects.get(id=id).delete()
        return redirect('/')
    else:
        return HttpResponse('Method not allowed', status=405)
