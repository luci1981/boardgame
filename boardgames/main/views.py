from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html', {'message':'Hi, there!'})

def formular(request):
    return render(request, "main/formular.html")

def formular_submit(request):
    return render(request, "main/raspunsformular.html",
                  {'name':request.POST['nume'],'prenume':request.POST['prenume'],
                   'trimite':request.POST['trimite']})