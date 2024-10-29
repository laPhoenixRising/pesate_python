from django.http import HttpResponse

from .models import Weigh

def index(request):
    latest_weighs = Weigh.objects.order_by("-created_on")[:5]
    list = [f"{weigh.value} {weigh.created_on}" for weigh in latest_weighs]
    output = "<br>".join(list)
    return HttpResponse(output)
