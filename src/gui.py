import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        #--------------------------------------# Makes the Basic Grid layouts
        Layout = GridLayout(rows=2)
        TopBar = GridLayout(rows=1,cols=3,height=200,size_hint_y=None)
        MainWindow = GridLayout(rows=3,cols=2)
    #---------------------------------------# Adds the  Basic Layout
        Layout.add_widget(TopBar) #Top Bar
        Layout.add_widget(MainWindow) #Main window
        #---------------------------------------# Cre
        MenuButton = Button(text="Menu")
        ClockText = Label(text="CLOCK TEST")
        UserButton = Button(text="-USERNAME-")



        return Layout
    
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })
        return super().build_config(config)


MyApp().run()