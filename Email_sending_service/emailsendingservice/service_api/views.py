from django.db import connections
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from model_repository.models import VwEmailSender
from service_api.repository import ServiceRepository
import json

from django.core import serializers
# Create your views here.
def email_info(request):
    service_repository = ServiceRepository(connections["postsql"].cursor())
    serialized = service_repository.read_email_info()
    json.loads(serialized)
    return JsonResponse(serialized, safe=False)


@require_POST
@csrf_exempt
def send_email(request):
    content = get_content(request)
    service_repository = ServiceRepository(connections["postsql"].cursor())
    raw_id = service_repository.save_email_raw_data(content)
    result = {"raw_id": raw_id}
    return JsonResponse(result)

def get_content(request):
    body = request.body.decode("utf-8")
    return body