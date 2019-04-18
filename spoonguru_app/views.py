from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import json

from .models import ContactRequest

# Create your views here.
@csrf_exempt
def new_contact_request(request):
    if request.method == 'POST':
        req_dict = json.loads(request.body)
        cr = ContactRequest(first_name=req_dict['firstName'], last_name=req_dict['lastName'], email=req_dict['email'], message=req_dict['message'])
        try:
            cr.clean_fields()
            cr.save()
            data = json.dumps({'message': "Created successfully!"})
            response = HttpResponse(data, content_type='application/json', status=201)
        except ValidationError as err:
            data = json.dumps({'message': "Failed to validate!", 'error': err.message_dict})
            response = HttpResponse(data, content_type='application/json', status=500)
        except ValueError as err:
            data = json.dumps({'message': "Failed to save!", 'error': err})
            response = HttpResponse(data, content_type='application/json', status=500)
        response["Access-Control-Allow-Origin"] = "localhost:8000, localhost:8080"
        return response
    else:
        raise Http404("Page not found")