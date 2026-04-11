class LevelUp():
  # class unlock
  class Unlock():
    def __init__(self,data: dict):
      self.type=data['type']
      self.name=data['name']
    def toDict(self):
      return {
        "type":self.type,
        "name":self.name
      }
  
  # class bonus
  class Bonus():
    def __init__(self,data: dict):
      self.type=data['type']
      self.amount=data['amount']
    def toDict(self):
      return {
        "type":self.type,
        "amount":self.amount
      }
  
  # constructor
  def __init__(self,json: dict):
    self.name=json['name']
    self.exp_need=json['exp_need']
    self.unlock=[]
    for i in json['unlock']:
      self.unlock.append(self.Unlock(i))
    self.bonus=[]
    for i in json['bonus']:
      self.bonus.append(self.Bonus(i))
  def toDict(self):
    return {
      "name":self.name,
      "exp_need":self.exp_need,
      "unlock":[i.toDict() for i in self.unlock],
      "bonus":[i.toDict() for i in self.bonus]
    }
  
class Farms():
  def __init__(self,json: dict):
    self.levelup=[]
    for i in json['levelup']:
      self.levelup.append(LevelUp(i))
  def toDict(self):
    return {
      "levelup":[i.toDict() for i in self.levelup]
    }