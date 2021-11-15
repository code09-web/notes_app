from django.shortcuts import render

def notes_page(request):
    return render(request,'UI/notes.html')

def login(request):
        return render(request,'UI/login.html')

def create_notes(request):
    return render(request,'UI/create_notes.html')

def singup(request):
    return render(request,'UI/singup.html')

def details(request):
    return render(request,'UI/details_page.html')