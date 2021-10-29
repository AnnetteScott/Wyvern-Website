from django.shortcuts import render
from .models import GamesList, ExplodingKactiScore
from django.http import HttpResponse
from .Games.ExplodingKacti import process_score

games_dict = {'Exploding Kacti': ExplodingKactiScore}





# Create your views here.
def home(request):
    games_list_dict = list(GamesList.objects.values())
    context = {'games_list': games_list_dict}
    return render(request, 'Arcade/home.html', context)

def gamePage(request, gameurl):
    games_list_dict = list(GamesList.objects.values())
    title = None
    for game in games_list_dict:
        url = ''
        if game['url'] == '' or game['url'] == 'null':
            url = (game['title'].replace(' ', '-')).lower()

        if game['url'] == gameurl or url == gameurl:
            title = game['title']
            game_status = game['online']
            break

    if game_status == True:
        context = {'title': title, 'status': game_status}
        
        if title == 'Exploding Kacti':  
            data = list(ExplodingKactiScore.objects.values().order_by('-score'))
            process_score.updateScores(data)
            context['high_scores'] = data
            
        return render(request, title + '.html', context)
    else:
        return render(request, 'Arcade/gamedownpage.html')


def add_score(request):
    if request.method == 'POST':
        ExplodingKactiScore.objects.create(score=request.POST['score'], name=request.POST['name'])
        process_score.updateScores()
        return HttpResponse('success')
    return HttpResponse('error')
