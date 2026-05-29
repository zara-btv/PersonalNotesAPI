
from django.urls import path,include

from Note.views import RegisterUserView,ChangGenericAPIView,CreateGenericAPIView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("notes/<id>", ChangGenericAPIView.as_view(), name="crud"),
    path("notes/", CreateGenericAPIView.as_view(), name="create"),
]
