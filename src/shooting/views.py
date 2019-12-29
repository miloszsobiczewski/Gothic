import os

from django.http import HttpResponse, Http404
from django.conf import settings

from .models import Shooting


def download(request, pk):
    file_location = Shooting.objects.get(pk=pk).confirmation.path
    file_path = os.path.join(settings.MEDIA_ROOT, file_location)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response["Content-Disposition"] = "inline; filename=" + os.path.basename(
                file_path
            )
            return response
    raise Http404
