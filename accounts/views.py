from accounts import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignupSerializer

@api_view(['POST'])
def signup_view(request):
    """User Accounts creation"""

    serializer = UserSignupSerializer(data=request.data)

    try:
        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "message"   : "User registered successfully",
                    "username"  : user.username
                },
                status = status.HTTP_201_CREATED
            )

    except Exception as e:
        print(e)
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
        
# @api_view(['POST'])
# def login_view(request):
#     """User Login"""
#     serializer = UserLoginSerializer(data=request.data)

#     try:
#         if serializer.is_valid():
#             user = serializer.validated_data['user']

#             return Response(
#                 {
#                     "message"   : "Successfully Logged In.",
#                     "username"  : user.username
#                 },
#                 status=status.HTTP_200_OK
#             )

#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
#     except Exception as e:
#         print(e)
#         return Response(
#             {
#                 "message" : "Internal Server Error."
#             },
#             status=status.HTTP_500_INTERNAL_SERVER_ERROR
#         )
