import json
from models.farms_model import Farms
from models.user_farm_model import UserFarm
from tkinter import *
class MyApp():
  def __init__(self,farms: dict,user_farm: dict):
    self.farms=Farms(farms)
    self.user_farm=UserFarm(user_farm)
  
  # show showMainMenu(self)
  def run(self):
    tk=Tk()
    tk.title("My Farm Main Menu")
    tk.geometry("450x350")
    tk.configure(bg='black')
    label=Label(tk,text='Main Menu', bg='green', fg='white', font=('Arial',20))
    label.pack(padx=10,pady=10)
    
    tk.mainloop()
  
  # basic operation
  def get_level(self):
    return self.user_farm.level

if __name__ == "__main__":
    with open('data/farms.json','r') as farm_file:
        farms_data = json.load(farm_file)
    with open('data/user_farm.json','r') as user_farm_file:
        user_farm_data = json.load(user_farm_file)
    app = MyApp(farms_data, user_farm_data)
    app.run()