from django.shortcuts import render

def home(request):
    context = {
        'name': 'Tom Leo',
    }
    return render(request, 'blog/index.html', context)
