from django.shortcuts import render
from .forms import UploadForm
from .models import UploadImage
from .models import Image

def index(request):
    params = {
        'title': '画像のアップロード',
        'upload_form': UploadForm(),
        'id': None,
    }

    if (request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            params['id'] = upload_image.id

    return render(request, 'upload_app/index.html', params)

# def home(request):
#     return render(request, 'upload_app/home.html', {})

# def image_list(request):
from PIL import Image

def home(request):
    images = UploadImage.objects.all()
    # for image in images:
    #     img = Image.open(image.image.url)
    #     width, height = img.size
    #     aspect_ratio = height / width
    #     new_width = 400  # The width that you want
    #     new_height = int(new_width * aspect_ratio)
    #     img = img.resize((new_width, new_height))
    #     img.save(image.image.url)
    return render(request, 'upload_app/home.html', {'images': images})

def link(request):
   return render(request, 'upload_app/link.html', {}) 
