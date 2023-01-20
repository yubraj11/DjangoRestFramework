from django.http import HttpResponse, JsonResponse


def homepage(request):
    friends = [
        'yubraj',
        'ravi',
        'raj'
    ]
    return JsonResponse(friends, safe=False)
    pass