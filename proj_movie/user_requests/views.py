from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from user_requests.models import RequestCounter

class RequestCountAPI(APIView):
    def get(self, request):
        counter, _ = RequestCounter.objects.get_or_create(id=1)
        return Response({"requests": counter.count}, status=HTTP_200_OK)


class RequestCountResetAPI(APIView):
    def post(self, request):
        counter, _ = RequestCounter.objects.get_or_create(id=1)
        counter.count = 0
        counter.save()
        return Response({"message": "Request count reset successfully"}, status=HTTP_200_OK)
