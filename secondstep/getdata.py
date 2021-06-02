from .models import Object


def objectMatcher(eng):
    totalObjects = Object.objects.all()
    for target in totalObjects:
        if eng not in target.title_eng:
            print("pass : " + eng + '!=' + target.title_eng)
            continue
        return target

    return "Not in database : " + eng
