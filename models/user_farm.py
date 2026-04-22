def from_str(x):
    assert isinstance(x, str)
    return x


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x):
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x):
    assert isinstance(x, bool)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Barn:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        amount = from_int(obj.get("amount"))
        return Barn(id, amount)

    def to_dict(self):
        result = {}
        result["id"] = from_str(self.id)
        result["amount"] = from_int(self.amount)
        return result


class Beehive:
    def __init__(self, last, amount, free):
        self.last = last
        self.amount = amount
        self.free = free

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        last = from_union([from_str, from_none], obj.get("last"))
        amount = from_union([from_int, from_none], obj.get("amount"))
        free = from_union([from_bool, from_none], obj.get("free"))
        return Beehive(last, amount, free)

    def to_dict(self):
        result = {}
        if self.last is not None:
            result["last"] = from_union([from_str, from_none], self.last)
        if self.amount is not None:
            result["amount"] = from_union([from_int, from_none], self.amount)
        if self.free is not None:
            result["free"] = from_union([from_bool, from_none], self.free)
        return result


class Recipie:
    def __init__(self, id):
        self.id = id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        return Recipie(id)

    def to_dict(self):
        result = {}
        result["id"] = from_str(self.id)
        return result


class Building:
    def __init__(self, id, recipie):
        self.id = id
        self.recipie = recipie

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        recipie = from_list(Recipie.from_dict, obj.get("recipie"))
        return Building(id, recipie)

    def to_dict(self):
        result = {}
        result["id"] = from_str(self.id)
        result["recipie"] = from_list(lambda x: to_class(Recipie, x), self.recipie)
        return result


class Bush:
    def __init__(self, id, last):
        self.id = id
        self.last = last

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        last = from_union([from_str, from_none], obj.get("last"))
        return Bush(id, last)

    def to_dict(self):
        result = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last is not None:
            result["last"] = from_union([from_str, from_none], self.last)
        return result


class Fishing:
    def __init__(self, last, free):
        self.last = last
        self.free = free

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        last = from_union([from_str, from_none], obj.get("last"))
        free = from_union([from_bool, from_none], obj.get("free"))
        return Fishing(last, free)

    def to_dict(self):
        result = {}
        if self.last is not None:
            result["last"] = from_union([from_str, from_none], self.last)
        if self.free is not None:
            result["free"] = from_union([from_bool, from_none], self.free)
        return result


class UserFarm:
    def __init__(self, username, password, farm_name, coin, exp, level, diamond, reputation, silo_max, barn_max, silo, barn, field, tree, bush, building, fishing, beehive, squirel_tree):
        self.username = username
        self.password = password
        self.farm_name = farm_name
        self.coin = coin
        self.exp = exp
        self.level = level
        self.diamond = diamond
        self.reputation = reputation
        self.silo_max = silo_max
        self.barn_max = barn_max
        self.silo = silo
        self.barn = barn
        self.field = field
        self.tree = tree
        self.bush = bush
        self.building = building
        self.fishing = fishing
        self.beehive = beehive
        self.squirel_tree = squirel_tree

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        username = from_str(obj.get("username"))
        password = from_str(obj.get("password"))
        farm_name = from_str(obj.get("farm_name"))
        coin = from_int(obj.get("coin"))
        exp = from_int(obj.get("exp"))
        level = from_int(obj.get("level"))
        diamond = from_int(obj.get("diamond"))
        reputation = from_int(obj.get("reputation"))
        silo_max = from_int(obj.get("silo_max"))
        barn_max = from_int(obj.get("barn_max"))
        silo = from_list(Barn.from_dict, obj.get("silo"))
        barn = from_list(Barn.from_dict, obj.get("barn"))
        field = from_list(Bush.from_dict, obj.get("field"))
        tree = from_list(Bush.from_dict, obj.get("tree"))
        bush = from_list(Bush.from_dict, obj.get("bush"))
        building = from_list(Building.from_dict, obj.get("building"))
        fishing = from_list(Fishing.from_dict, obj.get("fishing"))
        beehive = from_list(Beehive.from_dict, obj.get("beehive"))
        squirel_tree = from_list(Beehive.from_dict, obj.get("squirel_tree"))
        return UserFarm(username, password, farm_name, coin, exp, level, diamond, reputation, silo_max, barn_max, silo, barn, field, tree, bush, building, fishing, beehive, squirel_tree)

    def to_dict(self):
        result = {}
        result["username"] = from_str(self.username)
        result["password"] = from_str(self.password)
        result["farm_name"] = from_str(self.farm_name)
        result["coin"] = from_int(self.coin)
        result["exp"] = from_int(self.exp)
        result["level"] = from_int(self.level)
        result["diamond"] = from_int(self.diamond)
        result["reputation"] = from_int(self.reputation)
        result["silo_max"] = from_int(self.silo_max)
        result["barn_max"] = from_int(self.barn_max)
        result["silo"] = from_list(lambda x: to_class(Barn, x), self.silo)
        result["barn"] = from_list(lambda x: to_class(Barn, x), self.barn)
        result["field"] = from_list(lambda x: to_class(Bush, x), self.field)
        result["tree"] = from_list(lambda x: to_class(Bush, x), self.tree)
        result["bush"] = from_list(lambda x: to_class(Bush, x), self.bush)
        result["building"] = from_list(lambda x: to_class(Building, x), self.building)
        result["fishing"] = from_list(lambda x: to_class(Fishing, x), self.fishing)
        result["beehive"] = from_list(lambda x: to_class(Beehive, x), self.beehive)
        result["squirel_tree"] = from_list(lambda x: to_class(Beehive, x), self.squirel_tree)
        return result


def user_farm_from_dict(s):
    return UserFarm.from_dict(s)


def user_farm_to_dict(x):
    return to_class(UserFarm, x)