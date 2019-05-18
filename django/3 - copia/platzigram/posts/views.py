from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'titulo': 'Mont Blanc',
        'usuario': {
            'nombre': 'Yesica Cortes',
            'imagen': 'https://picsum.photos/60/60/?image=1027'
        },
        'hora': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'foto': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'titulo': 'QUIREON',
        'usuario': {
            'nombre': 'QU1R30N',
            'imagen': 'https://scontent.fmex10-2.fna.fbcdn.net/v/t1.0-9/60711010_2041531622635374_8482051606299279360_n.jpg?_nc_cat=111&_nc_ht=scontent.fmex10-2.fna&oh=0589735df37fb41a0cd8ae0f7e646e95&oe=5D5D1C12'
        },
        'hora': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'foto': 'https://scontent.fmex10-2.fna.fbcdn.net/v/t1.0-9/60711010_2041531622635374_8482051606299279360_n.jpg?_nc_cat=111&_nc_ht=scontent.fmex10-2.fna&oh=0589735df37fb41a0cd8ae0f7e646e95&oe=5D5D1C12',
    },
    
]



# Create your views here.
def lista_posts(request):
    return render(request,'feed.html',{'posts':posts})