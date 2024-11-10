from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

rooms = [
    
        {'id': 1, 'name': "let's learn python"},
        {'id': 2, 'name': "Design with me"},
        {'id': 3, 'name': "Frontend developers"},
        {'id': 4, 'name': "Backend developers"},
        
]

def about(request):
    return HttpResponse('about page')

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
    


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i  # Assign the correct room to the variable
            break  # Exit the loop once the room is found
    return render(request, 'base/room.html', {'room': room})  # Pass the room data to the template
