class Corps():
  def __init__(self,json):
    # self.id='C001'
    # self.name='wheat'
    # self.buy=3
    # self.sell=1
    # self.reputation=0
    # self.exp=1
    # self.duration='00:02:00'
    # self.image='assets/ACorps/Wheat.png'
    # self.field=True
    # self.tree=False
    # self.bush=False
    for key,value in json.items():
      setattr(self,key,value)
  def hour(self):
    return int(self.duration.split(':')[0])
  def minute(self):
    return int(self.duration.split(':')[1])
  def second(self):
    return int(self.duration.split(':')[2])
  
  def toDict(self):
    return {
      "id":self.id,
      "name":self.name,
      "buy":self.buy,
      "sell":self.sell,
      "reputation":self.reputation,
      "exp":self.exp,
      "duration":self.duration,
      "image":self.image,
      "field":self.field,
      "tree":self.tree,
      "bush":self.bush
    }