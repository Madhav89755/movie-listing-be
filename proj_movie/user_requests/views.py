from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from user_requests.models import RequestCounter
from drf_yasg.utils import swagger_auto_schema

class RequestCountAPI(APIView):
    @swagger_auto_schema(
        operation_description="This feature returns you the total count \
            of Request done to the server till date.",
        operation_id="Request Count",
        tags=['Request Count']
    )
    def get(self, request):
        counter, _ = RequestCounter.objects.get_or_create(id=1)
        return Response({"requests": counter.count}, status=HTTP_200_OK)


class RequestCountResetAPI(APIView):
    @swagger_auto_schema(
        operation_description="This feature resets the count of the request made to server.",
        operation_id="Request Count Reset",
        tags=['Request Count']
    )
    def post(self, request):
        counter, _ = RequestCounter.objects.get_or_create(id=1)
        counter.count = 0
        counter.save()
        return Response({"message": "Request count reset successfully"}, status=HTTP_200_OK)
