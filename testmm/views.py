from django.shortcuts import render

# Create your views here.
from testmm.models import ImgTest


def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = ImgTest(img_url=request.FILES.get('img'))
        img.save()
    return render(request, 'imgupload.html')