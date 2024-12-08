from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import graphene
from .models import *
from app_dtos.app import EmploymentInputObject, EmploymentObject
from appBuilders.appBuilders import EmploymentBuilders



@csrf_exempt
def execute_code(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data
            data = json.loads(request.body)
            temperature = data.get('temperature')
            humidity = data.get('humidity')

            # Print the temperature and humidity to the console
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity} %")

            # Save data to the Weather model
            if temperature is not None and humidity is not None:
                Weather.objects.create(
                    temperature=int(temperature),  # Ensure it's stored as an integer
                    humidity=int(humidity)         # Ensure it's stored as an integer
                )
                return JsonResponse({'status': 'success', 'message': 'Data received and stored successfully'}, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid data type'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Weather
from .serializer import WeatherSerializer
# import pandas as pd
from rest_framework.views import APIView
from .serializer import FileSerializer
from .models import Files

from rest_framework.parsers import FileUploadParser
@api_view(['GET'])
def hourly_average_summary(request):
    data = Weather.objects.all().order_by('created_at')
    serializer = WeatherSerializer(data, many=True)
    df = pd.DataFrame(serializer.data) # type: ignore
    df['created_at'] = pd.to_datetime(df['created_at'])
    df.set_index('created_at', inplace=True)
    df_resampled = df.resample('10T').agg({
        'temperature': 'mean',
        'humidity': 'mean'
    }).reset_index()
    df_resampled.fillna(0, inplace=True)  # Replace NaN values with 0
    
    df_resampled.replace([float('inf'), float('-inf')], 0, inplace=True)  # Replace infinite values with 0
    
    # Delete rows where either 'Temperature Average' or 'Humidity Average' is 0
    df_resampled = df_resampled[(df_resampled['temperature'] != 0) & (df_resampled['humidity'] != 0)]
    df_resampled.replace([float('inf'), float('-inf')], 0, inplace=True)  # Replace infinite values with 0
    df_resampled.columns = ['Date', 'Temperature Average', 'Humidity Average']
    response_data = df_resampled.to_dict(orient='records')
    return Response(response_data)



@api_view(['GET'])
def current_weather(request):
    try:
        # Retrieve the latest weather record
        latest_weather = Weather.objects.latest('created_at')
        
        # Serialize the latest weather record
        serializer = WeatherSerializer(latest_weather)
        
        # Return the serialized data
        return Response(serializer.data)
    
    except Weather.DoesNotExist:
        # If no weather data is available, return an empty response or an error message
        return Response({"error": "No weather data available."}, status=404)
    

################file upload##############
# class FileUploadView(APIView):
    
#     @staticmethod
#     def post(request):
#         data = request.FILES.get("file")
        
#         if data:
#             file = Files.objects.create(file=data)
#             return Response({"error": False, "data": file.file})
#         return Response({"error": True,})
    
#     @staticmethod
#     def get(request):
#         data = Files.objects.all()
#         return Response(FileSerializer(instance=data, many=True).data)
    
    


class FileUploadView(APIView):
    
    def post(self, request):
        file = request.FILES.get("file")
        
        if file:
            try:
                # Assuming `Files` model has a `file` field that is a `FileField`
                saved_file = Files.objects.create(file=file)
                return Response({"error": False, "data": FileSerializer(saved_file).data})
            except Exception as e:
                return Response({"error": True, "message": str(e)})
            
        return Response({"error": True, "message": "No file uploaded."})
    
    def get(self, request):
        try:
            data = Files.objects.all()
            return Response(FileSerializer(instance=data, many=True).data)
        except Exception as e:
            return Response({"error": True, "message": str(e)})
    
    
# class CreateEmploymentMutation(graphene.Mutation):
    
#     class Arguments:
#         input = EmploymentInputObject(required=True)
        
#     data = graphene.Field(EmploymentObject)
    
#     def mutate(self, info, input):
#         new_employment, create = Employment.objects.update_or_create(
#             job_title = input.job_title,
#             employ_status = input.employ_status,
#             details_month = input.details_month,
#             employ_name = input.employ_name,
            
#         defaults={
#             'is_active': True
#         }
#         )
#         return EmploymentBuilders.get_employment_data(id=new_employment.unique_id)



class CreateEmploymentMutation(graphene.Mutation):
    class Arguments:
        input = EmploymentInputObject(required=True)
        
    data = graphene.Field(EmploymentObject)
    success=graphene.Boolean()
    
    @classmethod
    def mutate(cls,root, info, input):
        # Create a new employment record
        new_employment = Employment.objects.create(
            job_title=input.job_title,
            employ_status=input.employ_status,
            details_month=input.details_month,
            employ_name=input.employ_name
        )
    
        return CreateEmploymentMutation(data=new_employment,success=True)
    