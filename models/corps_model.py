class Corps():
  # self.id='C001'
  # self.name='wheat'
  # self.buy=3
  # self.sell=1
  # self.reputation=0
  # self.exp=1
  # self.duration='00:02:00'
  def __init__(self,json):
    for key,value in json.items():
      setattr(self,key,value)
  def hour(self):
    return int(self.duration.split(':')[0])
  def minute(self):
    return int(self.duration.split(':')[1])
  def second(self):
    return int(self.duration.split(':')[2])