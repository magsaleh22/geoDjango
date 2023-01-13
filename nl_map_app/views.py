# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Municipalities, User
from .serializers import UserSerializer
from .serializers import MunicipilitiesSerializer
from .serializers import MunicipilitiesLocationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework_gis.filters import InBBoxFilter
# from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
import jwt, datetime
from django.urls import reverse
from django.http import  HttpResponseRedirect

# from django.http  import HttpResponse 




class MunicipalitiesListGenerics(generics.ListCreateAPIView):
    """
    DRF this handles GeoJSON input/output files, not our "municipalities_nl.geojson" file 
    for now it works for posting single feature per POST request.
    next step is to handle a list of objects via get_serializer()
    
    for now the assignment asks CRUD using this django-restframework only
    """
    queryset = Municipalities.objects.all()
    serializer_class = MunicipilitiesSerializer


class MunicipalitiesListGenericsDetail(generics.RetrieveAPIView,
                                       generics.UpdateAPIView,
                                       generics.DestroyAPIView):
    
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Municipalities.objects.all()
    serializer_class = MunicipilitiesSerializer
   

class CustomResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
class SpatialDataViewSet(ListAPIView):
    queryset = Municipalities.objects.all()
    serializer_class = MunicipilitiesLocationSerializer
    bbox_filter_field = 'location'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True # Optional
    pagination_class = CustomResultsSetPagination
    


class MunicipalitiesListGenericsGeoJSON(generics.ListCreateAPIView):
    """
    - implemented with GeoFeatureModelSerializer
    - accepts GeoJSON file (features only)
    - handling an input collection be can done later 

    """
    queryset = Municipalities.objects.all()
    serializer_class = MunicipilitiesLocationSerializer
    
    
# implemented to create register view, issue with creating extended AbstractUser       
class UserCreate(generics.CreateAPIView):
    queryset =User.objects.all()
    serializer_class =UserSerializer
    permission_classes = (AllowAny,)
    
    
class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Wrong password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            'iat': datetime.datetime.utcnow()
        }
        
        # encoded token
        encoded = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
  
        response.set_cookie(key='jwt', value=encoded,httponly=True)
        
        response.data = {
            'jwt':encoded
        }
        
        
        return response
    
    
class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user =User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        
   
        # return Response(serializer.data)
        return HttpResponseRedirect(reverse("mncplties"))