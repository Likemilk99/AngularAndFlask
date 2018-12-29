from ..models import Hero

class HeroService():
    def list():
        list = []
        list.append(Hero(0, "one"))
        list.append(Hero(1, "two"))
        return list