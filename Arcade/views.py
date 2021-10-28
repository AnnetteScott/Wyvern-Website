from django.shortcuts import render
from .models import GamesList, ExplodingKactiScore
from .Games.ExplodingKacti import process_score

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
            iframe_title = game['title'].replace(' ', '-')
            game_status = game['online']
            break

    if game_status == True:
        ifame_src = "https://notnatural21.github.io/" + iframe_title + "/"
        context = {'title': title, 'ifame_src': ifame_src, 'status': game_status}
        process_score.updateScores()
        return render(request, 'Arcade/gamepage.html', context)
    else:
        return render(request, 'Arcade/gamedownpage.html')


def add_score(request):
    if request.method == 'POST':
        kacti_data = ExplodingKactiScore.objects.get()
        kacti_data.score = request.POST['score']
        kacti_data.save()
        process_score.updateScores()
