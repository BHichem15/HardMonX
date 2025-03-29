# Colors
COLOR_BACKGROUND = "#F7F7F7"  
COLOR_FOREGROUND = "#2E2E2E"  
COLOR_ACCENT = "#4A90E2"       
COLOR_BUTTON_BG = "#EAEAEA"  
COLOR_BUTTON_FG = "#333333"   
COLOR_LABEL_BG = "#FFFFFF"  
COLOR_ENTRY_BG = "#F0F0F0"    

# Fonts (Reduced Sizes)
FONT_TITLE = ("Broadway", 10, "bold")  
FONT_DATA = ("Britannic", 7)          
FONT_LABEL = ("Britannic", 7, "bold") 
FONT_BUTTON = ("Century", 7, "bold")  

# Styles (Reduced Padding)
title_style = {
    "font": FONT_TITLE,
    "fg": COLOR_FOREGROUND,
    "bg": COLOR_BACKGROUND,
    "padx": 5,
    "pady": 5
}

data_style = {
    "font": FONT_DATA,
    "fg": COLOR_FOREGROUND,
    "bg": COLOR_LABEL_BG,
    "padx": 5,
    "pady": 3
}

label_style = {
    "font": FONT_LABEL,
    "fg": COLOR_FOREGROUND,
    "bg": COLOR_BACKGROUND,
    "padx": 2,
    "pady": 2
}

button_style = {
    "font": FONT_BUTTON,
    "fg": COLOR_BUTTON_FG,
    "bg": COLOR_BUTTON_BG,
    "activebackground": COLOR_ACCENT,
    "activeforeground": COLOR_FOREGROUND,
    "relief": "flat",
    "borderwidth": 0,
    "padx": 7,
    "pady": 3
}

frame_style = {
    "bg": COLOR_BACKGROUND,
    "padx": 5,
    "pady": 5
}
