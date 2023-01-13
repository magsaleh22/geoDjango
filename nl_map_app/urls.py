from django.contrib import admin
from django.urls import  path
from nl_map_app import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    # path('', views.home),
    path('register/',views.UserCreate.as_view(),name="register"),
    path('login/',views.LoginView.as_view()),
    path('user/',views.UserView.as_view()),
    path('token/',TokenObtainPairView.as_view(),name = "token_obtain_view"),
    path('token/refresh/', TokenRefreshView.as_view(),name = "token_refresh_view"),
    path('municipalities/', views.MunicipalitiesListGenerics.as_view(),name= 'mncplties'),
    path('municipalities/<int:pk>', views.MunicipalitiesListGenericsDetail.as_view()),
    path('filter/', views.SpatialDataViewSet.as_view()),
    path('municipalitieslocation/', views.MunicipalitiesListGenericsGeoJSON.as_view()),
]



# urlpatterns = format_suffix_patterns(urlpatterns)

