from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View abc"""

    def get(self, request, format=None):
        """
        Return a list of APIView feature
        request: contain detail of request
        format: add format

        """
        an_apiview=[
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Dajango View',
            'Give you the most control over your application logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
