from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.core.window import Window
from translate import Translator
Window.size = (500, 600)

class MyApp(MDApp):
    def translateText(self, event):
        var1 = self.textinput.text
        translator = Translator(from_lang=self.main_button1.text,
                                to_lang=self.main_button2.text
                                )
        translation = translator.translate(var1)
        self.textinput2.text = translation

    def build(self):
        layout = MDRelativeLayout(md_bg_color=[240/255, 200/255, 200/255])
        self.titleLabel = Label(text = "Translator Application",
                                pos_hint = {"center_x": 0.5, "center_y": 0.94},
                                size_hint = (1, 1),
                                font_size = 40,
                                color = (1,0,0),
                                font_name = "Comic"
                                )
        self.textinput = TextInput(text="",
                                   pos_hint = {"center_x": 0.5, "center_y": 0.65},
                                   size_hint = (1, None),
                                   height = 150,
                                   font_size = 29,
                                   foreground_color = (0,.5,0),
                                   font_name = "Comic",
                                   hint_text = "Enter the text to be translated",
                                   #multiline = False)
                                   )

        self.textinput2 = TextInput(text="",
                                    pos_hint={"center_x": 0.5, "center_y": 0.3},
                                    size_hint=(1, None),
                                    height=150,
                                    font_size=29,
                                    foreground_color=(0, .5, 0),
                                    font_name="Comic",
                                    readonly = True,
                                    hint_text = "This will show the translated text. Do not type here"
                                    # multiline=False)
                                )


        self.translateButton = Button(text = "Translate",
                                      pos_hint = {"center_x": 0.5, "center_y": 0.10},
                                      size_hint = (.25, .1),
                                      size = (75,75),
                                      font_name = "Comic",
                                      bold = True,
                                      font_size = 24,
                                      background_color = (0, 1, 0),
                                      on_press = self.translateText
                                      )
        self.choice = ['English', 'German', 'Spanish', 'French', 'Chinese', 'Dutch', 'Swedish']
        self.dropdown1 = DropDown()
        self.dropdown2 = DropDown()
        for choice in self.choice:
            button1 = Button(text = choice, size_hint_y = None, height=30)
            button2 = Button(text = choice, size_hint_y = None, height=30)
            button1.bind(on_release = lambda button1:self.dropdown1.select(button1.text))
            button2.bind(on_release = lambda button2:self.dropdown2.select(button2.text))

            self.dropdown1.add_widget(button1)
            self.dropdown2.add_widget(button2)

        self.main_button1 = Button(text = "English",
                                   size_hint = (None, None),
                                   pos = (250,575),
                                   height = 50
                                   )
        self.main_button2 = Button(text="Dutch",
                                   size_hint=(None, None),
                                   pos=(250, 315),
                                   height=50
                                   )
        self.main_button1.bind(on_release = self.dropdown1.open)
        self.main_button2.bind(on_release = self.dropdown2.open)

        self.dropdown1.bind(on_select = lambda instance, x: setattr(self.main_button1, 'text', x))
        self.dropdown2.bind(on_select = lambda instance, x: setattr(self.main_button2, 'text', x))

        layout.add_widget(self.main_button1)
        layout.add_widget(self.main_button2)

        layout.add_widget(self.titleLabel)
        layout.add_widget(self.textinput)
        layout.add_widget(self.textinput2)
        layout.add_widget(self.translateButton)


        return layout

if __name__ == '__main__':
    app = MyApp()
    app.run()

