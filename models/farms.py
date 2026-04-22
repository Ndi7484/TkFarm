def from_str(x):
    assert isinstance(x, str)
    return x


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Bonus:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        amount = from_int(obj.get("amount"))
        return Bonus(type, amount)

    def to_dict(self):
        result = {}
        result["type"] = from_str(self.type)
        result["amount"] = from_int(self.amount)
        return result


class Unlock:
    def __init__(self, id):
        self.id = id

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        return Unlock(id)

    def to_dict(self):
        result = {}
        result["id"] = from_str(self.id)
        return result


class Levelup:
    def __init__(self, name, exp_need, unlock, bonus):
        self.name = name
        self.exp_need = exp_need
        self.unlock = unlock
        self.bonus = bonus

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        exp_need = from_int(obj.get("exp_need"))
        unlock = from_list(Unlock.from_dict, obj.get("unlock"))
        bonus = from_list(Bonus.from_dict, obj.get("bonus"))
        return Levelup(name, exp_need, unlock, bonus)

    def to_dict(self):
        result = {}
        result["name"] = from_str(self.name)
        result["exp_need"] = from_int(self.exp_need)
        result["unlock"] = from_list(lambda x: to_class(Unlock, x), self.unlock)
        result["bonus"] = from_list(lambda x: to_class(Bonus, x), self.bonus)
        return result


class Farms:
    def __init__(self, levelup):
        self.levelup = levelup

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        levelup = from_list(Levelup.from_dict, obj.get("levelup"))
        return Farms(levelup)

    def to_dict(self):
        result = {}
        result["levelup"] = from_list(lambda x: to_class(Levelup, x), self.levelup)
        return result


def farms_from_dict(s):
    return Farms.from_dict(s)


def farms_to_dict(x):
    return to_class(Farms, x)