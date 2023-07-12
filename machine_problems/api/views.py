from rest_framework.response            import Response
from rest_framework.decorators          import APIView, api_view
from rest_framework                     import status

from ch1.models                         import TestCases, StringInputs

from .serializers                       import TestCasesSerializer, StringInputsSerializer

class Cases(APIView):
    """
    List all test cases or create a new test case.
    """
    def get(self, request, format=None):
        cases = TestCases.objects.all()
        serializer = TestCasesSerializer(cases, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer  = TestCasesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class Strings(APIView):
    """
    List all strings or create a new string.
    """
    def get(self, request, format=None):
        strings     = StringInputs.objects.all()
        serializer  = StringInputsSerializer(strings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer  = StringInputsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


