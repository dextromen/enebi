from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import sp, dp

from kivy.app import App

class Header(MDBoxLayout):
    balance = ObjectProperty()
    #font_size_ = ObjectProperty(16)
    gold = ObjectProperty()




class Hangman_key(Button):
    pass

class GameButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class VoiceButton(MDIconButton):
    pass

class Carousel_P(Popup):
    dropdown_key = ObjectProperty()


class ChooseCategory(DropDown):
    def __init__(self,scroll, button, word_list_widget, **kwargs):
        super().__init__(**kwargs)
        """add phrases, scroll widget, main button widget and word list widget"""
        self.current_phrases_info = App.get_running_app().current_phrases_info
        self.category_names = [x for x in self.current_phrases_info ]
        self.current_category = self.category_names[0]

        self.show_translation = True

        for i in self.category_names:
            but = DropDown_Open_Button(text=i,size_hint_y=None, height=40, font_name="DejaVuSans.ttf")
            but.bind(on_release= lambda but:self.select(but.text))
            self.add_widget(but)
    
        self.scroll = scroll
        self.main_button = button
        self.list_item = word_list_widget
        self.add()


    def change_translation(self):
        if self.show_translation:
            self.show_translation = False
            self.change()
            # self.add()
        else:
            self.show_translation = True
            self.add()

    def change(self):
        app = App.get_running_app()
        
        
        # for word in  self.current_phrases_info[self.current_category]:
        #     index = self.current_phrases_info[self.current_category].index(word)

        for a in app.main_screen.carousel.slides:
            index = app.main_screen.carousel.slides.index(a)
            
            word = self.current_phrases_info['ყველა'][index]

            if self.show_translation:
                a.label.text =  word['en'] #+ " - " + word["geo"] 
                #self.show_translation=False
            else:
                a.label.text =  word['en'] + " - " + word["geo"] 
                #self.show_translation=True
              
               

    def category_load_next(self):
        button = self.main_button
        index = self.category_names.index(button.text)
        
        try:
            self.current_category = self.category_names[index+1]
            button.text = self.category_names[index +1]
            self.add()
        except IndexError:
            self.current_category = self.category_names[0]
            button.text = self.category_names[0]
            self.add()



    def category_load_prev(self):
        button = self.main_button
        index = self.category_names.index(button.text)
        try:
            self.current_category = self.category_names[index-1]
            button.text = self.category_names[index -1]
            self.add()
            
        except IndexError:
            pass
    

    
    def add(self):
        # if App.get_running_app().main_screen.switch.current == "carousel_view":
        #     # print("dada")
        carousel = App.get_running_app().main_screen.carousel
        listview = App.get_running_app().main_screen.listview.scroll
        
        for word in  self.current_phrases_info[self.current_category]:
                
            car = Carousel_Item( word['en'] + " - " + word["geo"] )
            list_ = WordList( word['en'] + " - " + word["geo"] )
            carousel.add_widget(car)
            listview.add_widget(list_)
        # if len(carousel.slides) !=0:
        #     listview.clear_widgets()
        #     print("upsie")
        # else:                
        #     self.scroll.clear_widgets()
        #     for word in  self.current_phrases_info[self.current_category]:
            
        #         self.scroll.add_widget(self.list_item( word['en'] + " - " + word["geo"] ))
           


    def select(self,instance):
        self.current_category = instance
        self.main_button.text = instance
        self.add()
        self.dismiss()

class Carousel_Item(ButtonBehavior,MDFloatLayout):
    def __init__(self, text,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint=.99,0.98
        self.pos_hint={"center_y":.5,"center_x":.5}
        self.label = MDLabel()
        self.radius=[6]
        self.md_bg_color=1,1,1,.9
        self.label.text=text
        self.label.size=self.label.texture_size
        self.label.text_size=self.size[0],None
        self.label.halign= 'center'
        # self.padding=[20]
        self.label.color = 0,0,0,1
        # self.label.outline_color = 0,0,0,1
        # self.label.outline_width = 0.1
        self.label.font_size = sp(24)
        self.label.font_name = "DejaVuSans.ttf"
        self.add_widget(self.label)
    
    def on_release(self):
        App.get_running_app().voice(self)



class DropDown_Button(ButtonBehavior,BoxLayout):
    pass

class Hangman_Win(Popup):
    def __init__(self, hangman,**kwargs):
        super().__init__(**kwargs)
        self.hangman = hangman
    
    def restart(self):
        self.hangman.on_pre_enter()





class Reklama(Popup):
    def __init__(self, hangman,**kwargs):
        super().__init__(**kwargs)
        self.hangman = hangman
        
    
    def close(self):
        self.hangman.lose_popup.open()

class Hangman_Lose(Popup):

    correct = ObjectProperty(None)
    nawer = ObjectProperty('None')
    def __init__(self, hangman,**kwargs):
        super().__init__(**kwargs)
        self.hangman = hangman
        self.correct = hangman.word
        self.nawer = f'swori iyo {hangman.word}'
    
    def restart(self):
        self.hangman.on_pre_enter()



class DropDown_Open_Button(Button):
    pass



class WordList(MDCard):
    def __init__(self, text,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = MDLabel(text=text,color=(0,0,0,1))
        self.label.font_name = "DejaVuSans.ttf"
        self.label.halign="center"
        
        # self.label.size = self.label.texture_size
        # self.label.text_size=self.size
        self.label.font_size = sp(16)
        voice = VoiceButton()
        self.md_bg_color=1,1,1,1
        self.add_widget(self.label)
        # self.add_widget(voice)
    

