from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django import forms
from django.http import HttpResponseRedirect
from django.contrib import messages
from garrett.models import *

class userForm(forms.Form):
    account = forms.CharField(label = '',
                              widget = forms.TextInput(attrs={'placeholder':'Account',
                                                              'class':'form-control'}))
    password = forms.CharField(label = '',
                               widget = forms.PasswordInput(attrs={'placeholder':'Password',
                                                                   'class':'form-control'}))

class searchForm(forms.Form):
    srch = forms.CharField(label = '',
                             widget = forms.TextInput(attrs={'class':'form-control'}))


def index(request):
    if request.method == 'POST':
        uf1 = userForm(request.POST)
        if uf1.is_valid():
            account = uf1.cleaned_data['account']
            password = uf1.cleaned_data['password']
            index.user = users.objects.filter(name=account, passwrd=password)
            if index.user:
                return HttpResponseRedirect('/garrett/pageSinger/')
            else:
                messages.warning(request, 'informal error')
                return HttpResponseRedirect('/garrett/#signin')
    else:
        uf1 = userForm()
    return render(request, 'index.html',{'uf1':uf1})


def page404(request):
    if request.method == 'POST':
        sr = searchForm(request.POST)
        if sr.is_valid():
            want = sr.cleaned_data['srch']
            want = want.title()
            player = authors.objects.filter(name=want)
            singleSong = songs.objects.filter(songName=want)
            if player:
                return HttpResponseRedirect('/garrett/pageSinger/%s'\
                                            %player[0].singerID)
            elif singleSong:
                return HttpResponseRedirect('/garrett/song/%s'\
                                            %singleSong[0].songID)
            else:
                return HttpResponseRedirect('/garrett/404')
    else:
        sr = searchForm()
    contents = {'search': sr, 'user': index.user[0].name}
    return render(request, '404.html', contents)


def signUp(request):
    if request.method == 'POST':
        uf2 = userForm(request.POST)
        if uf2.is_valid():
            account = uf2.cleaned_data['account']
            password = uf2.cleaned_data['password']
            user = users.objects.filter(name=account)
            if user:
                messages.warning(request, 'used account')
            else:
                user = users()
                user.name = account
                user.passwrd = password
                user.save()
                messages.success(request, 'new account has been created!')
                return HttpResponseRedirect('/garrett/#signin')
    else:
        uf2 = userForm()
    return render(request, 'signUp.html', {'uf2':uf2})



def pageSinger(request):
    singers = authors.objects.all()
    if request.method == 'POST':
        sr = searchForm(request.POST)
        if sr.is_valid():
            want = sr.cleaned_data['srch']
            want = want.title()
            player = authors.objects.filter(name=want)
            singleSong = songs.objects.filter(songName=want)
            if player:
                return HttpResponseRedirect('/garrett/pageSinger/%s'\
                                            %player[0].singerID)
            elif singleSong:
                return HttpResponseRedirect('/garrett/song/%s'\
                                            %singleSong[0].songID)
            else:
                return HttpResponseRedirect('/garrett/404')
    else:
        sr = searchForm()
    contents = {'search': sr, 'singers': singers, 'user':index.user[0].name}
    return render(request, 'pageSinger.html', contents)
    
    

def singerSong(request, singer_name):
    author = authors.objects.get(singerID=singer_name)
    melodies = songs.objects.filter(singerID=singer_name)
    if request.method == 'POST':
        sr = searchForm(request.POST)
        if sr.is_valid():
            want = sr.cleaned_data['srch']
            want = want.title()
            player = authors.objects.filter(name=want)
            singleSong = songs.objects.filter(songName=want)
            if player:
                return HttpResponseRedirect('/garrett/pageSinger/%s'\
                                            %player[0].singerID)
            elif singleSong:
                return HttpResponseRedirect('/garrett/song/%s'\
                                            %singleSong[0].songID)
            else:
                return HttpResponseRedirect('/garrett/404')
    else:
        sr = searchForm()
    contents = {'author': author, 'songs': melodies, 'user': index.user[0].name,
                'search':sr}
    return render(request, 'authorSong.html', contents)


def singleSong(request, song_id):
    melody = songs.objects.get(pk=song_id)
    author = authors.objects.get(singerID=melody.singerID)
    comments = commentPost.objects.filter(songID=song_id)

    if request.method == 'POST':
        sr = searchForm(request.POST)
        if sr.is_valid():
            want = sr.cleaned_data['srch']
            want = want.title()
            player = authors.objects.filter(name=want)
            singleSong = songs.objects.filter(songName=want)
            if player:
                return HttpResponseRedirect('/garrett/pageSinger/%s'\
                                            %player[0].singerID)
            elif singleSong:
                return HttpResponseRedirect('/garrett/song/%s'\
                                            %singleSong[0].songID)
            else:
                return HttpResponseRedirect('/garrett/404')
        else:
            commentPost(songID=song_id, account=index.user[0].name,
                    body=request.POST.get('commentpost'),
                    timestamp=datetime.now()).save()
            return HttpResponseRedirect('/garrett/song/%s'%song_id)
    else:
        sr = searchForm()
        
    contents = {'user': index.user[0].name, 'melody': melody, 'author': author,
                'comments': comments, 'search': sr}
    return render(request, 'singleSong.html', contents)


def allSong(request):
    melodies = songs.objects.all()
    if request.method == 'POST':
        sr = searchForm(request.POST)
        if sr.is_valid():
            want = sr.cleaned_data['srch']
            want = want.title()
            player = authors.objects.filter(name=want)
            singleSong = songs.objects.filter(songName=want)
            if player:
                return HttpResponseRedirect('/garrett/pageSinger/%s'\
                                            %player[0].singerID)
            elif singleSong:
                return HttpResponseRedirect('/garrett/song/%s'\
                                            %singleSong[0].songID)
            else:
                return HttpResponseRedirect('/garrett/404')
    else:
        sr = searchForm()
    contents = {'melodies': melodies, 'user': index.user[0].name, 'search': sr}
    return render(request, 'allSong.html', contents)
