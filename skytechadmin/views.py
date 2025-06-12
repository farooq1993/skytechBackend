from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status
from .models import *
from .serializers import *


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username, email=email,password=password)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return redirect('registration')
    return render(request, 'registration.html')


class GetallServices(APIView):
    def get(self, request):
        try:
            all_services = Subservicename.objects.all()
            serializer = SubserviceSerializer(all_services, many=True)
            return Response({'data':serializer.data}, status=status.HTTP_200_OK)
        except Subservicename.DoesNotExist:
            return Response({'error':serializer.errors}, status=status.HTTP_404_NOT_FOUND)

class Itservices(APIView):
    """
    Showing here only IT services 
    """
    def get(self, request):
        category = request.GET.get("category", "IT services")
        services = Subservicename.objects.filter(main_service_name__main_service_name=category)
        serializer = SubserviceSerializer(services, many=True)
        return Response(serializer.data)

class ServiceById(APIView):
    """
    Using this api we will get single service
    """
    def get(self, request, id):
        record = Subservicename.objects.get(id=id)
        serializer = SubserviceSerializer(record)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
class SubserviceData(APIView):
    def get(self, request,id):
        try:
            servcie_data = Subservicename.objects.get(id=id)
            serializer = SubserviceSerializer(servcie_data)
            return Response({'data':serializer.data}, status=status.HTTP_200_OK)
        except Subservicename.DoesNotExist:
            return Response({'error':serializer.errors}, status=status.HTTP_204_NO_CONTENT)
    
class Enquiries(APIView):
    def post(self, request):
        data = request.data
        serializer = EnquiriesSerializer(data=data)
        if serializer.is_valid():
            enquiry = serializer.save()

            # Prepare email content
            subject = f"New Enquiry from {enquiry.first_name} {enquiry.last_name}"
            message = (
                f"Name: {enquiry.first_name} {enquiry.last_name}\n"
                f"Email: {enquiry.email}\n"
                f"Phone: {enquiry.phone}\n"
                f"Company: {enquiry.company_name}\n"
                f"Title: {enquiry.title}\n"
                f"Message:\n{enquiry.message}"
            )
            recipient_list = ['farooqaziz1993@gmail.com'] #info@skytechme.com

            # Send email
            send_mail(
                subject,
                message,
                'farooqaziz1993@gmail.com',
                recipient_list,
                fail_silently=False,
            )

            return Response({'message': 'Enquiry submitted and email sent.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)