import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Order


@csrf_exempt
def order(request):
    data = json.loads(str(request.body, encoding='utf-8'))

    response = HttpResponse(content='OK!', status=200,
                            content_type='text/plain')

    total_price = 0
    for food in data['foods']:
        total_price += food['price'] * food['amount']

    if request.user.is_authenticated():
        o = Order(restaurant=data['restaurant_name'],
                  user_id=request.user.pk,
                  foods=data['foods'],
                  total_price=total_price)
    else:
        o = Order(restaurant=data['restaurant_name'],
                  foods=data['foods'],
                  total_price=total_price)

    o.save()

    return response
