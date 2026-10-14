from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import WorkoutSerializers

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_workout_view(request):
     serializers = WorkoutSerializers(data=request.data)

     try:
          if serializers.is_valid():
               serializers.save(user=request.user)

               return Response(
                    {
                         "message" : "Record is successfully created.",
                    },
                    status= status.HTTP_201_CREATED
               )
          return Response(
               serializers.errors,
               status=status.HTTP_400_BAD_REQUEST
          )
     except Exception as e:
          print(e)
          return Response(
               {
                    "message" : "Internal Server Error",
               },
               status=status.HTTP_500_INTERNAL_SERVER_ERROR
          )
