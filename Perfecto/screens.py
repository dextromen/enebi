from kivy.uix.screenmanager import Screen
from widgets import Hangman_key, Hangman_Lose, Hangman_Win, Reklama
from kivy.properties import ObjectProperty, StringProperty
import random
from kivy.app import App
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
from kivy.core.window import Window



class Main_Screen(Screen):
    dropdown_key = ObjectProperty(None)
    header = ObjectProperty()

   
class Market(Popup):
    pass

class Hangman(Screen):
    display = ObjectProperty()
    button_area = ObjectProperty()
    score = ObjectProperty()
    sityva = StringProperty('')
    n=ObjectProperty(None)
    header = ObjectProperty()
    word = StringProperty('')
    qartuli = StringProperty('')

    def __init__(self,**kw):
        super().__init__(**kw)
        self.words = App.get_running_app().hangman_words()
        alphabet = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,4,4'.split(',')
        row1 = "q,w,e,r,t,y,u,i,o,p".split(',')
        row2 = 'a,s,d,f,g,h,j,k,l'.split(',')
        row3 ='@,z,x,c,v,b,n,m,@'.split(',')

        self.queue = {"current":[], "old":[]}
        for word in self.words:
            if word["current"] == 1:
                self.queue["current"].append(word)
            else:
                self.queue['old'].append(word)
        

        self.win_popup=Hangman_Win(self)
        self.lose_popup=Hangman_Lose(self)
        self.reklama = Reklama(self)
        self.first = True
        self.current_word = None
        self.box1 = MDBoxLayout()
        self.box2 = MDBoxLayout()
        self.box3 = MDBoxLayout(pos_hint={"center_x":0.5})
        for i in row1:
            key = Hangman_key(text=i.upper())
            
            self.box1.add_widget(key)
        for i in row2:
            key = Hangman_key(text=i.upper())
            
            self.box2.add_widget(key)
        for i in row3:
            key = Hangman_key(text=i.upper())
            
            self.box3.add_widget(key)
        self.button_area.add_widget(self.box1)
        self.button_area.add_widget(self.box2)
        self.button_area.add_widget(self.box3)
    
        for i in self.box3.children:
        
            if i.text == '@':
                i.width=dp(20)
                i.color = 0,0,0,0
                i.background_normal = ''
                i.background_color = (0,0,0,0)
                i.disabled=True

    
    
   

    def on_pre_enter(self):
        self._defisiani = ''
        self.sityva = ''
        self.add_word()
        
        for button in self.box1.children:
            if button.disabled:
                button.disabled = False
        for button in self.box2.children:
            if button.disabled:
                button.disabled = False
        for button in self.box3.children:
            if button.disabled:
                button.disabled = False


    
    
    def sortify(self,queue):
        return queue["mistake"]

    def add_word(self):
        self.first = True
        if len(self.queue["current"]) > 0:
            self.current_word = random.choice(self.queue["current"])
            index = self.queue["current"].index(self.current_word)
            self.queue["current"].pop(index)
        else:
            self.queue['old'].sort(key=self.sortify)
            self.current_word = self.queue['old'][-1]
            self.queue['old'].pop(-1)

        self.n = str( self.current_word['n'])
        self.qartuli =  self.current_word['geo']
        self.word =  self.current_word['en'].lower()
        exclude = [" ", "!", '.', "  ", "/", '[', ']', ',']
        for i in range(len(self.word)):

            if self.word[i] not in exclude:
                self.sityva+="-"
                
            else:
                self.sityva+=" "

    def update_mistakes(self, n):
        updated_mistake = self.current_word["mistake"] + n
        App.get_running_app().DB.change_mistake(self.current_word["id"], updated_mistake)


    def win(self):
        App.get_running_app().balance(self.n)
        self.win_popup.open()
        if int(self.n) == 5:
            App.get_running_app().remove_from_current(self.current_word)
            n = self.current_word["n"]
            if n > 3:
                n-=1
                App.get_running_app().DB.change_n(self.current_word["id"],n)
            self.update_mistakes(-5)


            
        elif int(self.n) > 0:

            n = 5 - int(self.n)
            self.update_mistakes(n)
            
            



    def lose(self): 
        App.get_running_app().add_to_current(self.current_word)
        self.update_mistakes(5)

        if self.first:
            self.reklama.open()
            self.first = False
        else:
            self.lose_popup.open()
        self.lose_popup.correct = self.current_word["geo"] + " - " + self.current_word["en"]
        


    def chance(self):
        
        self.n =1

        
    def guess(self, button):
        letter = button.text.lower()
        
        if letter == "@":
            pass

        else:
            button.disabled = True


            sityva = list(self.sityva)

            
            if letter in self.word:
                for w in range(len(sityva)):

                    if self.word[w] == letter:
                        sityva[w] = letter
                    self.sityva = "".join(sityva)  
                    
                        

            else:

                self.n = int(self.n)-1
                if int(self.n) < 3:
                    App.get_running_app().add_to_current(self.current_word)
                    
                    if int(self.n) == 0:
                        self.lose()
                    


        if not "-" in self.sityva:
            
            self.win()

