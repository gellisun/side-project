from django.shortcuts import render, redirect 
from .models import Gallery, Exhibition
from .forms import ExhibitionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def galleries_index(request):
    galleries = Gallery.objects.all()
    return render(request, 'galleries/galleries_index.html', {
        'galleries': galleries
    })

def galleries_detail(request, gallery_id):
    gallery = Gallery.objects.get(id=gallery_id)
    exhibition_form = ExhibitionForm()
    return render(request, 'galleries/galleries_detail.html', { 'gallery': gallery, 'exhibition_form': exhibition_form })

@login_required
def exhibition_create(request, gallery_id):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            new_exhibition = form.save(commit=False)
            new_exhibition.gallery_id = gallery_id
            new_exhibition.user = request.user
            new_exhibition.save()
        else:
            print(form.errors)
    return redirect('galleries_detail', gallery_id=gallery_id)

def save_exhibition(request, exhibition_id):
    try:
        exhibition = Exhibition.objects.get(id=exhibition_id)
        exhibition.user_favourite = True
        exhibition.save()
        return JsonResponse({"success": True})
    except Exhibition.DoesNotExist:
        return JsonResponse({"success": False})
    
def exhibitions_saved(request):
    user = request.user
    saved_exhibitions = Exhibition.objects.filter(user=user, user_favourite=True)
    
    return render(request, 'exhibitions/exhibitions_saved.html', {'saved_exhibitions': saved_exhibitions})