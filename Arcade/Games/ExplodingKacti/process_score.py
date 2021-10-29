from ...models import ExplodingKactiScore

def updateScores():
    data = list(ExplodingKactiScore.objects.values().order_by('-score'))        
    if len(data) > 10:
        data_length = len(data)
        for index in range(10, data_length):
            obj_id = data[index]['id']
            ExplodingKactiScore.objects.filter(pk=obj_id).delete()

    




