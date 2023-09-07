
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from datetime import datetime
from screens import Main_Screen, Hangman, Market
from widgets import GameButton, ChooseCategory,Carousel_Item, Carousel_P, WordList
from db_manage import DB_Manager
from animations import Animate
# from kivy.animation import Animate
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.clock import Clock
from kivy.core.window import Window

import random

class EnebiApp(MDApp):
    
    DB = DB_Manager()
    last_id = DB.get_last_id()
    
    animations = Animate

    Show_translation = True
    Voice_on = True
    # db files
    b = DB.get_balance()


    balance_str = ObjectProperty(str(b))
    current_phrases_info = {"ყველა":DB.get_current()}#{
       #f"ახალი სიტყვები":[{'geo': "გამარჯdasdობა", 'n':5,"en":"hi"},{'geo': "გამარჯობა",'n':5, "en":"hello"},{'geo': "გამარჯdasdობა", 'n':5,"en":"hi"},{'geo': "გამარჯობა",'n':5, "en":"hello"}]}
        #"მისალმება":[{'geo': "გამარჯობა",'n':5, "en":"hi"},{'geo': "გამარჯობა",'n':5, "en":"hello"}],
        #"დათანხმება":[{'geo':"დათანხმება",'n':5, "en":"aha"}, {'geo':"დიახ მართალია", 'n':5,"en":"Yes, that's correct"  }]}

    get_familiar = DB.get_familiar(last_id)
    category_names = [x for x in current_phrases_info ]

    def buy(self, quantity):
        
        should = quantity * 5
        
        if int(self.balance_str) >= should:
            new = self.DB.add_new(self.last_id, quantity)
            for words in new:

                self.current_phrases_info['ყველა'].append(words)
                self.hangman.queue['current'].append(words)

            self.carousel_dropdown.add()
            self.balance(-should)
        else:
            self.animations.no(self.main_screen.balance)
           

    def hangman_words(self):
        self.get_familiar
        return self.get_familiar#random.choice(self.get_familiar)
        """
        pirveli modis n=5
        mere n = 4
        mere n = 3
        
        """


        pass

    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "100" 
        self.sm = ScreenManager()
        self.main_screen = Main_Screen(name="main")
        self.carousel_popup = Carousel_P()    

        self.market = Market()

        self.hangman = Hangman(name="hangman")
        self.dropdown()
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.hangman)


        def menu(window,key,*largs):
            
            if key == 27:
                if self.bb_counter == 1:
                    self.stop()
                else:
                    self.sm.current="main"
                    self.main_screen.switch.switch_tab("listview")                
                    self.bb_counter +=1
                    Clock.schedule_interval(lambda x:self.reset_counter(), 1)
                return True
        Window.bind(on_keyboard=menu)
        return self.sm

    

    time_old = None
    sc_m = 0
    def scrolling_points(self):
        
        time_now = datetime.now().second

        try:
            delta = time_now - self.time_old

            if delta > 1:
                self.sc_m+=1
                balance = int(self.balance_str)
                if self.sc_m % 5 ==0:
                    balance +=1
                    self.animations.grow(self.main_screen.balance)
                    
                self.DB.update_balance(balance)
                self.balance_str = str(balance)
                balance_label = self.main_screen.balance
                
                # self.animations.glow(self.main_screen.header.gold)
            # else:
            #     print(':shsmsumsu')
            self.time_old = time_now
        except Exception as e:
            # else:
            self.time_old = time_now
            print(e)



    def remove_from_current(self, word):
        id = word["id"]
        for i in self.current_phrases_info["ყველა"]:
            if i["id"] ==  id:
                i["current"] = 0
        
        self.DB.remove_current(int(id))
        





        # remove from carousel and listview
        for slide in self.main_screen.carousel.slides:
            
            try:
                slide_en = slide.label.text.split(" - ")[0]
            
            except:
                slide_en = current = slide.label.text.split(" - ")[0]

            if slide_en == word["en"]:
                self.main_screen.carousel.remove_widget(slide)

        for list_ in self.main_screen.listview.scroll.children:
            try:
                slide_en = list_.label.text.split(" - ")[0]
            
            except:
                slide_en = list_.label.text.split(" - ")[0]

            if slide_en == word["en"]:
                self.main_screen.listview.scroll.remove_widget(list_)
                

    def add_to_current(self, word):
        print(word)
    
    def balance(self,balance):
        if int(balance) > 0:
            pass
            # self.animations.glow(self.hangman.header.gold)
            # self.animations.grow(self.hangman.header.gold)
        self.balance_str = str(int(self.balance_str) + int(balance))
        self.DB.update_balance(self.balance_str)
        
    def switch(self):
        if self.main_screen.switch.current == "carousel_view":
            self.main_screen.switch.current = "listview"
            # self.main_screen.switch_button.icon = "view-carousel-outline"
        else:
            self.main_screen.switch.current = "carousel_view"
            
            # self.main_screen.switch_button.icon = "format-list-bulleted"

    # DROPDOWN STUFF
    def dropdown(self):        
        main_scroll = self.main_screen.switch.listview.scroll

        main_dropdown_button = self.main_screen.dropdown_key

        # self.category_dropdown = ChooseCategory(main_scroll, main_dropdown_button,WordList)
        
        
        self.carousel_dropdown = ChooseCategory(self.main_screen.switch.carousel_view.carousel, main_dropdown_button,Carousel_Item)
        
    
    def show_translation(self):
        title = "ყველა"#self.main_screen.dropdown_key.text
        current = self.main_screen.carousel.current_slide.label.text
        

        try:
            current = current.split(" - ")[0]
            
        except:
            current = current.split(" - ")[0]
           
        for i in self.current_phrases_info[title]:
            if i["en"] == current:
                index = self.main_screen.carousel.index


        if self.carousel_dropdown.show_translation:
            self.carousel_dropdown.change()
            for i in self.main_screen.carousel.slides:                
                i.show_translation.icon ="eye-off-outline"
            self.carousel_dropdown.show_translation=False
        else:
            self.carousel_dropdown.change()
            for i in self.main_screen.carousel.slides:                
                i.show_translation.icon ="eye-outline"
            self.carousel_dropdown.show_translation=True
        
       
       

    def voice_on_off(self):
        if self.Voice_on==False:
            self.Voice_on=True
            for i in self.main_screen.carousel.slides:
                        
                i.voice_button.icon ="volume-high"
        else:
            self.Voice_on=False
            for i in self.main_screen.carousel.slides:
                        
                i.voice_button.icon ="volume-off"


        print(self.Voice_on)

    def open_carousel(self, widget):
        # category = self.main_screen.dropdown_key.text
        carousel = self.main_screen.carousel

        word = widget.label.text.split(" - ")[0]
        index = None
        for i in self.current_phrases_info["ყველა"]:
            if i["en"] == word:
                index = self.current_phrases_info["ყველა"].index(i)
                
        self.main_screen.switch.switch_tab("carousel_view")
        carousel.index=index
        # # self.voice(carousel.current_slide)
        # # self.carousel_popup.open()
        # carousel.clear_widgets()
        # for word in  self.current_phrases_info[category]:
        #     carousel.add_widget(Carousel_Item(word["geo"] + " - " + word['en']))
        # self.main_screen.dropdown_key.text = category
        # carousel.index =  index

        
    def voice(self,widget):

        text = widget.label.text.split(" - ")[0]


        if self.Voice_on:
            print(text)
        else:
            pass

    bb_counter = 0
    def reset_counter(self):
        self.bb_counter = 0

    
            
    

if __name__ == "__main__":
    EnebiApp().run()