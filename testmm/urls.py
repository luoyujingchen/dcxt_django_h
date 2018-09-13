from django.urls import path

from testmm.views import uploadImg

urlpatterns = [
    path('uploadImg/', uploadImg), # 新增
]