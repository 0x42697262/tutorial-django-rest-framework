from rest_framework.response            import Response
from rest_framework.decorators          import api_view
from ch1.models                         import TestCases, StringInputs

from .serializers                       import TestCasesSerializer, StringInputsSerializer

@api_view(['GET'])
def get_test_cases(request):
    test_case   = TestCases.objects.all()
    serializer  = TestCasesSerializer(test_case, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_test_cases(request):
    serializer  = TestCasesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_strings(request):
    strings     = StringInputs.objects.all()
    serializer  = StringInputsSerializer(strings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_strings(request):
    serializer  = StringInputsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

