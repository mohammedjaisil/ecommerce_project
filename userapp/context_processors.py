from accounts.models import *


def checkid(request):
    if 'user_id' in request.session:
        logi = request.session.get('user_id')
        if Accounts.objects.filter(username = logi):
            user = Accounts.objects.get(username = logi)
        else:
            user = None
        return {
            'user' : user
        }
    else:
        return { 'user' : None}
        
