class UserFarm():
  def __init__(self,json: dict):
    # self.coin=300
    # self.exp=0
    # self.level=1
    # self.diamond=0
    # self.reputation=0
    # self.silo_max=150
    # self.barn_max=150
    for key,value in json.items():
      setattr(self,key,value)
  def renameFarm(self,name):
    self.farm_name=name
  def addCoin(self,n_coins):
    self.coin+=n_coins
  def minCoin(self,n_coins):
    self.coin-=n_coins
  def addDiamond(self,n_diamond):
    self.diamond+=n_diamond
  def minDiamond(self,n_diamond):
    self.diamond-=n_diamond
  def addLevel(self):
    self.level+=1
  def addExp(self,n_exp):
    self.exp+=n_exp
  def addReputation(self,n_reputation):
    self.reputation+=n_reputation
  def upgradeSilo(self):
    self.silo_max+=50
  def upgradeBarn(self):
    self.barn_max+=50
  
  def toDict(self):
    return {
      "farm_name":self.farm_name,
      "coin":self.coin,
      "exp":self.exp,
      "level":self.level,
      "diamond":self.diamond,
      "reputation":self.reputation,
      "silo_max":self.silo_max,
      "barn_max":self.barn_max,
    }