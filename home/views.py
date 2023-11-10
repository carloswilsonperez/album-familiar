import os
from django.shortcuts import render, redirect
from family_album import settings


def clean_file_name(file_name): 
    return file_name.replace('\n', '')

# Create your views here.
def home(request):
    return render(request, 'home/index.html', context={ 'image': 'home/img/gallery/20230301-113253.jpg', 'page': 'home' })

# ========================================================================================

# Create your views here.
def about(request):
    return render(request, 'home/about.html', context={ 'page': 'about' })

# ========================================================================================

def gallery(request):
    with open(os.path.join(os.path.dirname(__file__), 'file_names.txt'), 'r') as f:
        lines = f.readlines()
        image_list = list(map(clean_file_name, lines))

    image_list.sort()
    return render(request, 'home/gallery.html', context={ 'image_names': image_list, 'page': 'gallery'})

# ========================================================================================

def family(request):
    if request.method == 'POST':
        yearId = request.POST.get('yearId')
        fileNames = f'file_names{yearId}.txt'
        templateName = f'home/{yearId}.html'
        viewName = f'pictures{yearId}'
        
        with open(os.path.join(os.path.dirname(__file__), fileNames), 'r') as f:
            lines = f.readlines()
            image_list = list(map(clean_file_name, lines))
        
        
        return render(request, 'home/family.html', context={ 'image_names': image_list, 'yearId': yearId }) # will make a get request on the class_students view 
    
    with open(os.path.join(os.path.dirname(__file__), 'family_names.txt'), 'r') as f:
        lines = f.readlines()
        image_list = list(map(clean_file_name, lines))

    image_list.sort()
    return render(request, 'home/family.html', context={ 'image_names': image_list })

# ========================================================================================

def contact(request):
    return render(request, 'home/contact.html', context={ 'page': 'contact' })

# ========================================================================================

def pictures2004(request):
    with open(os.path.join(os.path.dirname(__file__), 'file_names2004.txt'), 'r') as f:
        lines = f.readlines()
        image_list = list(map(clean_file_name, lines))

    image_list.sort()
    return render(request, 'home/2004.html', context={ 'image_names': image_list })

# ========================================================================================

def pictures2005(request):
    with open(os.path.join(os.path.dirname(__file__), 'file_names2005.txt'), 'r') as f:
        lines = f.readlines()
        image_list = list(map(clean_file_name, lines))

    image_list.sort()
    return render(request, 'home/2005.html', context={ 'image_names': image_list })

# ========================================================================================
