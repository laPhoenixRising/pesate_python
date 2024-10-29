from django.http import HttpResponse

from .models import Weigh

def index(request):
    latest_value_list = Weigh.objects.order_by("-created_on")[:5]
    
    output = ", ".join([f"{q.value} {q.created_on}" for q in latest_value_list])

    return HttpResponse(output)
