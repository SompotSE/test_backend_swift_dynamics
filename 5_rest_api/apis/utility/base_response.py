import json
from django.http import HttpResponse
from rest_framework import status

content_type = "application/json"

def success_response(result):
    jsr = JsonResponse(True, status.HTTP_200_OK, "Success", result)
    response = HttpResponse(status = status.HTTP_200_OK, content = jsr.to_json())
    response["Content-Type"] = content_type
    return response

def error_response(status_code, message, result):
    jsr = JsonResponse(False, status_code, message, result)
    response = HttpResponse(status = status_code, content = jsr.to_json())
    response["Content-Type"] = content_type
    return response

def exception_response(ex):
    jsr = JsonResponse(False, status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal Server Error", str(ex))
    response = HttpResponse(status = status.HTTP_500_INTERNAL_SERVER_ERROR, content = jsr.to_json())
    response["Content-Type"] = content_type
    return response

class JsonResponse:
    def __init__(self, is_success, status_code, message, result):
        self.is_success = is_success
        self.code = status_code
        self.message = str(message) if message is not None else None
        self.result = result
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=2)