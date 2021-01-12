from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from . import detect_intent
import json
from django.core import serializers





@api_view(['POST'])
def collect_response(request,format=None):
        # req = request.json(force=True)
        # print(req)
        request_json=json.loads(request.body.decode('utf-8'))
        text = request_json['text']
        text_list = []
        text_list.append(text)
        result = detect_intent.detect_intent_texts("legend-tfsf", 1, text_list, "en")

        return Response({"text":result})


