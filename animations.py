from kivy.animation import Animation
from kivy.clock import Clock


class Animate:


    def no( widget):
        x,y = widget.pos
        width, height = widget.size
        dur = 0.1
        incr = 7
        anim = Animation(x = x+incr, duration = dur-.05) 
        anim += Animation(x=x-incr, duration = dur-.05)
        anim += Animation(x = x+incr, duration = dur-.03) 
        anim += Animation(x=x-incr, duration = dur-.02)
        anim+=Animation(x=x,  duration = dur)

        anim.start(widget)

    def yes(self,widget):
        x,y = widget.pos
        width,height = widget.size
        # width = widget.font_size_
        dur = 0.1
        incr = 10
        anim = Animation(y = y+incr, duration = dur) 
        anim += Animation(y=y-incr, duration = dur)
        anim+=Animation(y=y,  duration = dur)
        
        anim.start(widget)

    def glow(widget):
        source1 = "images/gold_no_glow.png"
        source2 = "images/gold_purple_glow.png"

        def so(dt):
            widget.source = source1
        widget.source = source2
        Clock.schedule_once(so, 0.5)

    def grow(widget):
        x,y = widget.pos
        width,height = widget.size_hint
        # width = widget.font_size_
        dur = 0.1
        incr = 0.8
        anim = Animation(size_hint_y = height+incr, duration = dur) 
        anim += Animation(size_hint_y = height, duration = dur)
        # anim+=Animation(y=y,  duration = dur)
        
        anim.start(widget)

    def glow_3x(widget):
        Clock.schedule_interval(Animate.glow(widget), .5)
        # Clock.schedule_once(x.stop(), 1.2)
        
