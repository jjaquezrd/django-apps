from . import models

def get_logo(request):
    logo=models.AppSetting.objects.first()
    title=models.AppSetting.objects.first()
    data={
    #    'logo':logo.image_tag,
        'title': title.title
    }
    return data 
    