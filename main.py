from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup

from datetime import datetime



Builder.load_file('imageholder.kv')
Builder.load_file('memelayout.kv')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)



class ImageHolder(FloatLayout):
    img_source = StringProperty('assets/loadimage.png')

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file",
                            title_align='center',
                            title_color=[1.0, 1.0, 1.0, 1.0],
                            content=content,
                            size_hint=(0.9, 0.9)
                            )
        self._popup.open()
    
    def load(self, path, filename):
        print(filename)
        self.img_source = filename[0]
        self.dismiss_popup()
    
    def open_img(self):
        self.show_load()

class MemeLayout(BoxLayout):
    pass

class RootWidget(BoxLayout):
    def new(self):
        ml = MemeLayout()
        self.container.clear_widgets()
        self.container.add_widget(ml)

    def save(self):
        self.container.children[0].img1.remove_widget(self.container.children[0].img1.btn)
        self.container.children[0].img2.remove_widget(self.container.children[0].img2.btn)
        self.children[1].export_to_png(f"meme-{datetime.now()}.png")
        self.container.clear_widgets()
        self.container.add_widget(Label(text='Image saved successfull.'))

class MemeApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    app = MemeApp()
    app.run()