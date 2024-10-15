from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Lead
from .serializers import LeadSerializer

# Lead Views
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]  

class LeadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  


class LeadListView(APIView):
    @method_decorator(cache_page(60 * 15))  
    def get(self, request, *args, **kwargs):
        leads = Lead.objects.all()
        serialized_data = LeadSerializer(leads, many=True).data
        return Response({"leads": serialized_data})
