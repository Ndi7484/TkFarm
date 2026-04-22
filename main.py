import json
from models.farms import farms_from_dict, farms_to_dict
from models.user_farm import user_farm_from_dict, user_farm_to_dict
from tkinter import *
class MyApp():
  def __init__(self,farms: dict,user_farm: dict):
    self.farms=farms_from_dict(farms)
    self.user_farm=user_farm_from_dict(user_farm)
  
  def baseWindow(self, **params):
    tk = Tk()
    tk.title(params.get('title','Unknown'))
    tk.geometry(params.get('geometry','450x350'))
    tk.configure(bg=params.get('bg','black'))
    return tk
    
  def showMainMenu(self, tk):
    label = Label(tk, text='Main Menu', bg='black', fg='white', font=('Arial', 20))
    label.pack(padx=10, pady=10)
  
  def run(self):
    tk = self.baseWindow(
      title = "My Farm Main Menu",
      geometry = "450x350",
      bg = "black"
    )
    self.showMainMenu(tk)
    
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