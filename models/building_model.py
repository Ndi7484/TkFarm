class Building():
  # class Recipe
  class Recipe():
    # class Make
    class Make():
      def __init__(self,json: dict):
        # self.id= "C001"
        # self.amount= 3
        for key,value in json.items():
          setattr(self,key,value)
      
      def toDict(self):
        return {
          "id":self.id,
          "amount":self.amount,
        }
    
    def __init__(self,json: dict):
      # self.id="B001R001"
      # self.name= "bread"
      # self.image="assets/Bakery/Bread.png"
      # self.picture= ".png"
      # self.sell= 8
      # self.buy= 10
      # self.make= []
      # self.duration="00:02:30"
      for key,value in json.items():
        setattr(self,key,value)
      self.make=[]
      for i in json['make']:
        self.make.append(self.Make(i))
    
    def toDict(self):
      return {
        "id":self.id,
        "name":self.name,
        "image":self.image,
        "picture":self.picture,
        "sell": self.sell,
        "buy": self.buy,
        "make": [i.toDict() for i in self.make],
        "duration": self.duration
      }
  
  def __init__(self,json):
    # self.id="B001",
    # self.name= "Bakery",
    # self.image="assets/Bakery/Bakery.png",
    # self.recipes=[]s
    for key,value in json.items():
      setattr(self,key,value)
    self.recipes=[]
    for i in json['recipes']:
      self.recipes.append(self.Recipe(i))
  
  def toDict(self):
    return {
      "id":self.id,
      "name": self.name,
      "image": self.image,
      "recipes": [i.toDict() for i in self.recipes]
    }
      
    