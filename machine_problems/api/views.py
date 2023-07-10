from rest_framework.response                import Response
from rest_framework.decorators              import api_view


@api_view(['GET'])
def get_test_cases(request):
    test_case   = {
            1: "aabb",
            2: "baabb",
            3: "aababb",
            4: "a",
            5: "b",
            }
    return Response(test_case)
