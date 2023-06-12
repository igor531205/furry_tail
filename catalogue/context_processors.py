from catalogue.models import Favorites


def favorites(request):
    user = request.user
    return {'favorites': Favorites.objects.filter(user=user) if user.is_authenticated else []}
