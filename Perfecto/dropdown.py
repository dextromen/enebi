 # Widget:
            #     size_hint:1,None
            #     height:dp(10)
            
            # BoxLayout:
            #     size_hint:0.95,None
            #     pos_hint:{"center_x":.5, "center_y":.5}
            #     height:dp(40)
            #     spacing:dp(10)
            #     Button:
            #         text:"სწავლის რეჟიმი"
            #         font_size:sp(16)
            #         markup:True
            #         on_release:app.switch()#app.market.open()
            #         disabled:True if len(scroll.children) <1 else False
            #         size_hint:0.5,1
            #         height:dp(40)
            #         background_normal:''
            #         background_color:0,0,1,1
            #         pos_hint:{"center_x":.5,"center_y":.5}
            #         font_name:"BPG2.ttf"

            #     GameButton:
            #         text:"თამაშის დაწყება"
            #         on_release:app.root.current='hangman'
            #         font_size:sp(16)
            #         markup:True
            #         on_release:app.switch()#app.market.open()
            #         size_hint:0.5,1
            #         height:dp(40)
            #         background_normal:''
            #         background_color:0,0,1,1
            #         pos_hint:{"center_x":.5,"center_y":.5}
                    # font_name:"BPG2.ttf"
                    # font_name:"BPG2.ttf"                
                    # font_size:sp(18)
                    # size_hint:.5,1
                    # # width:dp(320)
                    # pos_hint:{"center_x":.5,"center_y":.5}
                
                # MDFloatingActionButton:
                #     size_hint:1,1
                #     # text:"+"#"[u]დაამატე ახალი სიტყვები"
                #     font_size:sp(34)
                #     on_release:app.market.open()
                #     # size_hint:0.2,None
                #     icon:"volume-high"
                #     theme_icon_color: "Custom"
                #     icon_color: 1,1,1,1
                #     # height:dp(40)
                #     # background_normal:''
                #     # background_color:0,0,1,1
                #     pos_hint:{"center_y":.5}
                #     # font_name:"BPG2.ttf"

            # MDBoxLayout:
            #     size_hint:.8,None
            #     md_bg_color:1,1,1,0.2
            #     width:dp(250)
            #     height:dp(30)
            #     pos_hint:{"center_y":.525,"center_x":.5}
            #     DropDown_Button:
            #         size_hint:0.2,1
            #         on_release:app.category_dropdown.category_load_prev()
            #         MDIconButton:
            #             icon:"arrow-left-bold"
            #             line_color:1,0,0,1
            #             theme_icon_color: "Custom"
            #             icon_color:0,0,0,0.5
            #             # icon_size:dp(30)
            #             pos_hint:{"center_y":.525,"center_x":.5}
            #             on_release:app.category_dropdown.category_load_prev()
            #             # background_normal:"images/arrow_left.png"
            #     DropDown_Open_Button:
            #         id:dropdown_key
            #         text:'ყველა'#app.category_names[0]
            #         font_size:sp(13)
            #         on_release:app.category_dropdown.open(self)
            #         size_hint:.6,1
            #         color:0,0,0,1
            #         font_name:"DejaVuSans.ttf"
            #         pos_hint:{"center_x":.5}
            #     DropDown_Button:
            #         size_hint:0.2,1
            #         on_release:app.category_dropdown.category_load_prev()
            #         MDIconButton:
            #             icon:"arrow-right-bold"
            #             line_color:1,0,0,1
            #             theme_icon_color: "Custom"
            #             icon_color:0,0,0,0.5
            #             # icon_size:dp(30)
            #             pos_hint:{"center_y":.525,"center_x":.7}
            #             on_release:app.category_dropdown.category_load_next()
        
            



            # MDGridLayout:
                
            #     radius:[16]
            #     id:yz
            #     size_hint_x:1
            #     pos_hint:{"center_x":.5,"center_y":.5}
            #     md_bg_color:1,1,1,0
            #     # radius:[16,16,5,5]
            #     cols:1
            #     # padding:[dp(0),dp(10),0,0]
            #     # spacing:dp(10)

                
                # MDFloatLayout:
                #     md_bg_color:1,1,1,0.2
                #     radius:[16,16,0,0]
                #     padding:[0,dp(150)]
                #     pos_hint:{"center_x":.5,"center_y":.5}
                #     size_hint:0.8,None
                #     height:dp(40)
                #     EffectWidget:
                #         effecs: ew.PixelateEffect(pixel_size=20),ew.FXAAEffect(),ew.ScanlinesEffect()
                #         pos_hint:{"center_x":.5,"center_y":.5}
                #     Label:
                #         text:"სამეცადინო სივრცე"
                #         pos_hint:{"center_x":.5,"center_y":.5}
                #         font_size:sp(14)
                #         font_name:"BPG2.ttf"
                #         color:1,1,1,1
                #     MDIconButton:
                #         id:switch_button
                #         size_hint:0.2,1
                #         pos_hint:{"center_x":.90,"center_y":.5}
                #         on_release:app.switch()
                #         icon:"view-carousel-outline"







# padding:[dp(520)]
                        # MDBoxLayout:
                        #     size_hint:.8,None
                        #     md_bg_color:1,1,1,0.2
                        #     width:dp(250)
                        #     height:dp(30)
                        #     pos_hint:{"center_y":.525,"center_x":.5}
                        #     DropDown_Button:
                        #         size_hint:0.2,1
                        #         on_release:app.category_dropdown.category_load_prev()
                        #         MDIconButton:
                        #             icon:"arrow-left-bold"
                        #             line_color:1,0,0,1
                        #             theme_icon_color: "Custom"
                        #             icon_color:0,0,0,0.5
                        #             # icon_size:dp(30)
                        #             pos_hint:{"center_y":.525,"center_x":.5}
                        #             on_release:app.category_dropdown.category_load_prev()
                        #             # background_normal:"images/arrow_left.png"
                        #     DropDown_Open_Button:
                        #         id:dropdown_key
                        #         text:'ყველა'#app.category_names[0]
                        #         font_size:sp(13)
                        #         on_release:app.category_dropdown.open(self)
                        #         size_hint:.6,1
                        #         color:0,0,0,1
                        #         font_name:"DejaVuSans.ttf"
                        #         pos_hint:{"center_x":.5}
                        #     DropDown_Button:
                        #         size_hint:0.2,1
                        #         on_release:app.category_dropdown.category_load_prev()
                        #         MDIconButton:
                        #             icon:"arrow-right-bold"
                        #             line_color:1,0,0,1
                        #             theme_icon_color: "Custom"
                        #             icon_color:0,0,0,0.5
                        #             # icon_size:dp(30)
                        #             pos_hint:{"center_y":.525,"center_x":.7}
                        #             on_release:app.category_dropdown.category_load_next()
                        # Widget:
                        #     size_hint:1,None
                        #     height:dp(1)
                        
                        # MDBoxLayout:
                        #     # md_bg_color:1,1,1,0.4
                        #     pos_hint:{"center_y":.5}
                            # MDIconButton:
                            #     size_hint:0.1,None
                            #     height:dp(10)
                            #     pos_hint:{"center_y":.5}
                            #     # width:dp(5)
                            #     theme_icon_color: "Custom"
                            #     icon_color:1,1,1,0.5
                            #     icon:"arrow-left"
                            #     on_release:carousel.load_previous()