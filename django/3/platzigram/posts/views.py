from django.http import HttpResponse
from datetime import datetime
posts = [{
    'usuario':'QU1R30N',
    'nombre':'victor hugo quintanilla',
    'hora': datetime.now().strftime("%b %dth , %Y - %H:%M hrs"),
    'imagen':'https://scontent.fmex10-2.fna.fbcdn.net/v/t1.0-9/56580456_1979830398805497_2283758562255568896_n.jpg?_nc_cat=100&_nc_ht=scontent.fmex10-2.fna&oh=f3ad6f517f5cfe23555d754b3853173a&oe=5D9BF638',
    
}]

# Create your views here.
def lista_posts(request):
    """lista existe post"""
    contenido=[]
    for post in posts:
        contenido.append("""
        <p><strong>{usuario}</strong></p>
        <p><small>{nombre}-<i>{hora}</i></small></p>
        <figure><img src="{imagen}"/></figure>
        """.format(**post))
    return HttpResponse("<br>".join(contenido))