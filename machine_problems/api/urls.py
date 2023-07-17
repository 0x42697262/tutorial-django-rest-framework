from rest_framework.urlpatterns import format_suffix_patterns
from django.urls        import path
from .                  import views

urlpatterns = [
        path('',            views.Cases.as_view()),
        path('strings/',    views.Strings.as_view()),

]
