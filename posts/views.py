from importlib.resources import contents
import re
from django.shortcuts import render

from datetime import datetime

# Create your views here.

posts = [
    {
        'name': 'Mont Blanck',
        'user': 'Jeyfred Calderon',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200?image=1036',
    },
    {
        'name': 'Via Láctea',
        'user': 'c. vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200?image=1076',
    }
]

def list_posts(request):
    return render(request, 'feed.html')
