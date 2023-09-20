from django.shortcuts import render, redirect 
from .models import Gallery, Exhibition
from .forms import ExhibitionForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def galleries_index(request):
    galleries = Gallery.objects.all()
    return render(request, 'galleries/galleries_index.html', {
        'galleries': galleries
    })

def galleries_detail(request, gallery_id):
    gallery = Gallery.objects.get(id=gallery_id)
    exhibition_form = ExhibitionForm()
    return render(request, 'galleries/galleries_detail.html', { 'gallery': gallery, 'exhibition_form': exhibition_form })

def exhibition_create(request, gallery_id):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        print('1')
        if form.is_valid():
            print('2')
            new_exhibition = form.save(commit=False)
            print('3')
            new_exhibition.gallery_id = gallery_id
            print('4')
            new_exhibition.save()
            print('5')
        else:
            print(form.errors)
    return redirect('galleries_detail', gallery_id=gallery_id)