from django.urls        import path
from .                  import views

urlpatterns = [
        path('',            views.get_test_cases),
        path('add_test/',   views.add_test_cases),
        path('strings/',    views.get_strings),
        path('add_string/', views.add_strings),

]
