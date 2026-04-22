from datetime import datetime
import dateutil.parser


def from_str(x):
    assert isinstance(x, str)
    return x


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x):
    return dateutil.parser.parse(x)


def from_bool(x):
    assert isinstance(x, bool)
    return x


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Corp:
    def __init__(self, id, name, buy, sell, reputation, exp, duration, image, field, tree, bush):
        self.id = id
        self.name = name
        self.buy = buy
        self.sell = sell
        self.reputation = reputation
        self.exp = exp
        self.duration = duration
        self.image = image
        self.field = field
        self.tree = tree
        self.bush = bush

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        buy = from_int(obj.get("buy"))
        sell = from_int(obj.get("sell"))
        reputation = from_int(obj.get("reputation"))
        exp = from_int(obj.get("exp"))
        duration = from_datetime(obj.get("duration"))
        image = from_str(obj.get("image"))
        field = from_bool(obj.get("field"))
        tree = from_bool(obj.get("tree"))
        bush = from_bool(obj.get("bush"))
        return Corp(id, name, buy, sell, reputation, exp, duration, image, field, tree, bush)

    def to_dict(self):
        result = {}
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        result["buy"] = from_int(self.buy)
        result["sell"] = from_int(self.sell)
        result["reputation"] = from_int(self.reputation)
        result["exp"] = from_int(self.exp)
        result["duration"] = self.duration.isoformat()
        result["image"] = from_str(self.image)
        result["field"] = from_bool(self.field)
        result["tree"] = from_bool(self.tree)
        result["bush"] = from_bool(self.bush)
        return result


def corp_from_dict(s):
    return Corp.from_dict(s)


def corp_to_dict(x):
    return to_class(Corp, x)