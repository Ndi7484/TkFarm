from datetime import datetime
import dateutil.parser


def from_str(x):
    assert isinstance(x, str)
    return x


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x):
    return dateutil.parser.parse(x)


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Make:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        amount = from_int(obj.get("amount"))
        return Make(id, amount)

    def to_dict(self):
        result = {}
        result["id"] = from_str(self.id)
        result["amount"] = from_int(self.amount)
        return result


class Recipe:
    def __init__(self, id, name, image, sell, buy, make, duration):
        self.id = id
        self.name = name
        self.image = image
        self.sell = sell
        self.buy = buy
        self.make = make
        self.duration = duration

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        image = from_str(obj.get("image"))
        sell = from_int(obj.get("sell"))
        buy = from_int(obj.get("buy"))
        make = from_list(Make.from_dict, obj.get("make"))
        duration = from_datetime(obj.get("duration"))
        return Recipe(id, name, image, sell, buy, make, duration)

    def to_dict(self):
        result = {}
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        result["image"] = from_str(self.image)
        result["sell"] = from_int(self.sell)
        result["buy"] = from_int(self.buy)
        result["make"] = from_list(lambda x: to_class(Make, x), self.make)
        result["duration"] = self.duration.isoformat()
        return result


class Building:
    def __init__(self, id, name, image, buy, recipes):
        self.id = id
        self.name = name
        self.image = image
        self.buy = buy
        self.recipes = recipes

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        image = from_str(obj.get("image"))
        buy = from_int(obj.get("buy"))
        recipes = from_list(Recipe.from_dict, obj.get("recipes"))
        return Building(id, name, image, buy, recipes)

    def to_dict(self):
        result = {}
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        result["image"] = from_str(self.image)
        result["buy"] = from_int(self.buy)
        result["recipes"] = from_list(lambda x: to_class(Recipe, x), self.recipes)
        return result


def building_from_dict(s):
    return Building.from_dict(s)


def building_to_dict(x):
    return to_class(Building, x)