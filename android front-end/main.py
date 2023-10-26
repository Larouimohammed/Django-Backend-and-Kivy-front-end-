import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


headers = {'Accept': 'application/json'}

class AndroidApp(App):
    def build(self):
     return MyRoot()

class MyRoot(BoxLayout):
   def __init__(self, **kwargs):
      super(MyRoot,self).__init__()
   def list(self):
        response = requests.get('http://127.0.0.1:8000/boutique',headers=headers).json()
        list =[]
        for name in response.split(","):
               #remove all special character from name
               new = "".join(filter(str.isalnum, name))
               print(new)
               
               #print(f"type: {str(line)}")
               list.append(new)

        self.data = list
        self.random_lable.text =str(self.data)
            
        


   
if __name__ == '__main__':
    
    
    androidApp = AndroidApp()  
    androidApp.run()
    
