
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from client.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def user_list(request):
    #     if request.method == 'GET':
    #         users = User.objects.all()
    #         serializer = UserSerializer(users, many=True)
    #         return JsonResponse(serializer.data, safe=False)
    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = UserSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, safe=False, status=201)
    #         return JsonResponse(serializer.errors, status=400)
