from ...models import ExplodingKactiScore

def updateScores(data):        
    if len(data) > 10:
        data_length = len(data)
        for index in range(10, data_length):
            obj_id = data[index]['id']
            ExplodingKactiScore.objects.filter(pk=obj_id).delete()

    




