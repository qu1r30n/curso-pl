from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'titulo': 'Mont Blanc',
        'usuario': {
            'nombre': 'Yésica Cortés',
            'imagen': 'https://picsum.photos/60/60/?image=1027'
        },
        'hora': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'foto': 'https://picsum.photos/800/600?image=1036',
    },
    
    {
        'titulo': 'QU1R30N',
        'usuario': {
            'nombre': 'QUIREON',
            'imagen': 'https://scontent.fmex10-2.fna.fbcdn.net/v/t1.0-9/60711010_2041531622635374_8482051606299279360_n.jpg?_nc_cat=111&_nc_ht=scontent.fmex10-2.fna&oh=0589735df37fb41a0cd8ae0f7e646e95&oe=5D5D1C12'
        },
        'hora': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'foto': 'https://scontent.fmex10-2.fna.fbcdn.net/v/t1.0-9/56580456_1979830398805497_2283758562255568896_n.jpg?_nc_cat=100&_nc_ht=scontent.fmex10-2.fna&oh=f3ad6f517f5cfe23555d754b3853173a&oe=5D9BF638',
    },

]

# Create your views here.
def lista_posts(request):
    """lista existe post"""
    return render(request,"feed.html", {"posts": posts})