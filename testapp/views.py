from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication

from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegistrationAPI(APIView):
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            users = serializer.save()
            token = get_tokens_for_user(users)
            # return render(request, 'app/login.html')
            return Response({"token": token, "msg": "Registration successfully"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPI(APIView):
    # renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # username = serializer.data.get('username')
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            # user = authenticate(email=email, password=password) or authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                # return redirect('/testapp/api/v1/home/')
                return Response({"token": token, "msg": "Login Success"},
                                status=status.HTTP_200_OK)
            else:
                return Response({"error": {"non_field_errors":
                                           ['email or password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        # request.session.clear()
        request.user.auth_token.delete()
        logout(request)
        return redirect('/testapp/login')
        # return Response('User Logged out successfully')
        

def Logout(request):
    request.session.clear()
    return redirect('login')


class UserChangePasswordAPI(APIView):
    # renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data,
                                                  context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({"msg": "Password change Successfully"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class Posts(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        Serializer = PostsSerializer(data = request.data)
        
        if Post.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This Post already exists')
  
        if Serializer.is_valid():
            Serializer.save()
            return Response({"msg":"data added successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
    def get(self,request):
        try:
            get_data = Post.objects.all()
            Serializer = PostsSerializer(get_data, many=True)
            return Response(Serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            get_data = Post.objects.filter(id=pk)
            get_data.delete()
            return Response({"msg":"Post successfully deleted"}, status=status.HTTP_200_OK)        
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk):
        try:
            item = Post.objects.get(pk=pk)
            Serializer = PostsSerializer(instance=item, data=request.data)
        
            if Post.objects.filter(**request.data).exists():
                raise serializers.ValidationError('This Post already exists')
    
            if Serializer.is_valid():
                Serializer.save()
                return Response(Serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class PostByIdAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,pk):
        try:
            item = Post.objects.get(pk=pk)
            Serializer= PostsSerializer(item)
            return Response(Serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            item = User.objects.get(pk=pk)
            Serializer = RegistrationSerializer(item)
            return Response(Serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg":"Internal server error {}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

            

            




            
        

    # def update_items(request, pk):
        
    # def get(self,request,pk):
    #     try:
    #         if request.query_params:
    #             get_data = Post.objects.filter(**request.query_param.dict())
    #         else:   
    #             get_data = Post.objects.all()
    #         if get_data:
    #             data = PostsSerializer(get_data)
    #             return Response(data)
    #     except Exception as e:
    #         return Response({"msg":"Internal server error {}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # @login_required
# def home(request):
#     return render(request, 'app/home.html')


# def signup(request):
#     return render(request, 'app/signup.html')

# def login(request):
#     return render(request, 'app/login.html')

# def userlogout(request):
#     return render(request, 'app/logout.html')



