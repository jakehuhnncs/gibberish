from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

from . import security

@csrf_exempt
def webhook(request):
    if security.secIP == False:
        return HttpResponseForbidden('Permission denied.')
    elif security.secSIG == 'forbidden':
         return HttpResponseForbidden('Permission denied.')
    elif security.secSIG == 'servererror':
        return HttpResponseServerError('Operation not supported.', status=501)
    else:
        return HttpResponse('pong')
