import os
from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response  
from .serializers import *  
from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt

def home(request): 
    return render(request, 'home.html' )

@method_decorator(csrf_exempt, name='dispatch')
class HandleFileUpload(APIView): 
    def post(self, request): 
        try: 
            data = request.data   
            serializers = FileListSerializer(data = data)  
            if serializers.is_valid(): 
                serializers.save() 
                return Response({'status':200,'message':'Files uploaded successfully.','data':serializers.data})  
            return Response({'status':400,'message':'Something went wrong.','data':serializers.errors})


        except Exception as e: 
            print(e)  
            return Response({'status':500, 'message':'Internal Server Error', 'error': str(e)})



