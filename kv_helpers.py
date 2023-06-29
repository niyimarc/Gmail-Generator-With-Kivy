screen_helper= """
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: "vertical"
                    MDTopAppBar:
                        title: "Generate Gmail Address"
                        elevation: 4
                        pos_hint: {"top": 1}
                        
                    MDBottomNavigation:
                        #panel_color: "#eeeaea"
                        selected_color_background: "orange"
                        text_color_active: "lightgrey"
      
                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Gmail Generator'
                            icon: 'gmail'
                            spacing: "20dp"
                            
                            MDBoxLayout:
                                orientation: "horizontal" 
                                size_hint: (.9,None)
                                pos_hint: {'center_x': 0.5, 'center_y': 0.75} 
                                spacing: "10dp"
                                
                                MDTextField:
                                    id: email_input
                                    hint_text: "Paste Only Gmail address"
                                    mode: "fill"
                                    helper_text: "Paste Youtube Video Link"
                                    pos_hint: {'center_y': 0.95}                                          
                                    multiline: False
                      
                                    
                                MDRaisedButton:
                                    id: generate_gmail
                                    text: "Generate"
                                    pos_hint: {'center_x': 0.86, 'center_y': 0.95}
                                    on_release: 
                                        app.getEmail(self)  # Call the function when the button is released
                                    disabled: not email_input.text or not email_input.text.endswith(("@gmail.com"))
                                    
                            MDBoxLayout:
                                orientation: "horizontal"
                                id: results 
                                size_hint: (.9,None)
                                pos_hint: {'center_x': 0.5, 'center_y': 20} 
                                spacing: "10dp"
                                MDTextField:
                                    id: output
                                    text: ''
                                    size_hint_x: .5
                                    hint_text: "Generated Results"
                                    max_height: "250dp"
                                    mode: "fill"
                                    fill_color: 0, 0, 0, .4
                                    multiline: True
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    
                                MDRaisedButton:
                                    id: copy_text
                                    text: "Copy"
                                    pos_hint: {'center_x': 0.5,}
                                    on_release: 
                                        app.copy_text()  # Call the function when the button is released
                                    disabled: not output.text
"""