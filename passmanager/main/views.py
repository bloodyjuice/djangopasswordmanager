from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Passes
from .forms import PassForm
from time import time


def index(request):
    form = PassForm
    context = {
        'form': form
    }

    passes = Passes.objects.all()
    print(len(passes))
    for a in range(len(passes)):
        passes[a].password = decrypt(passes[a].password)

    for b in range(len(passes)):
        passes[b].login = decrypt(passes[b].login)

    return render(request, 'main/index.html', {'title': 'Password Manager!', 'passes': passes})


def delete(request, id):
    try:
        passw = Passes.objects.get(id=id)
        passw.delete()
        return HttpResponseRedirect("/")
    except Passes.DoesNotExist:
        return HttpResponseNotFound("<h2>Pass not found</h2>")


def edit(request, id):
    try:
        passw = Passes.objects.get(id=id)

        if request.method == "POST":
            passw.title = request.POST.get("title")
            passw.login = request.POST.get("login")
            passw.password = mycrypt(request.POST.get("password"))
            passw.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"passw": passw})
    except Passes.DoesNotExist:
        return HttpResponseNotFound("<h2>Pass not found</h2>")


def mycrypt(password):
    key = int(str(time())[-3:-1])
    en = ''

    for symb in password:
        en += chr(ord(symb) + key)
    en = en + str(key)
    return en


def decrypt(password):
    decoded = ''
    key = int(password[-2:])
    print(chr(ord(password[0]) - key))
    for symb in password[:-2]:
        ff = chr(ord(symb) - key)
        decoded += ff
    print(decoded)
    return decoded


def edits(request):
    error = ''
    if request.method == 'POST':
        form = PassForm(request.POST)
        print(form.instance.password)
        if form.is_valid():
            form.instance.login = mycrypt(form.data['login'])
            form.instance.password = mycrypt(form.data['password'])
            form.save()
            return redirect('main')
        else:
            error = 'Форма недействительна'

    form = PassForm
    context = {
        'form': form
    }
    return render(request, 'main/edits.html', context)