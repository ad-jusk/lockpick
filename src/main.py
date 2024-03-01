from kivy.app import App
from kivy.lang import Builder

class LockpickApp(App):
    
    def build(self):
        return Builder.load_file("./design/main.kv")

if __name__ == "__main__":
    LockpickApp().run()