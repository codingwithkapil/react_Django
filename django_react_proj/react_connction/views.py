from django.shortcuts import render

# Create your views here.

import os
import logging
index_file_path = os.path.join(settings.react_app, 'build', 'index.html')
...
def react(request):
    try:
        with open(index_file_path) as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        logging.exception('Production build of app not found'
