# freebackend-demo/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloView(APIView):
    def post(self, request, format=None):
        name = request.data.get('name', 'Ospite')
        message = f"Ciao {name}, ho ricevuto la tua richiesta e questa è la mia risposta"
        return Response({"message": message}, status=status.HTTP_200_OK)
