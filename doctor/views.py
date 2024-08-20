from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor
from .serializers import Doctorserializer


@api_view(['GET', 'POST'])
def doctor(request):
    if request.method == 'GET':
        objs = Doctor.objects.all()
        serializer = Doctorserializer(objs, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = Doctorserializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

