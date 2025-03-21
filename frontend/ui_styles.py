# Colors
COLOR_BACKGROUND = "#2E3440"  
COLOR_FOREGROUND = "#D8DEE9"  
COLOR_ACCENT = "#5E81AC"      
COLOR_BUTTON_BG = "#434C5E"    
COLOR_BUTTON_FG = "#ECEFF4"    
COLOR_LABEL_BG = "#3B4252"     
COLOR_ENTRY_BG = "#4C566A"     

# Fonts
FONT_TITLE = ("Broadway", 12, "bold")  # title font
FONT_DATA = ("Britannic", 8)           # Data font
FONT_LABEL = ("Britannic", 8, "bold")  # Label font
FONT_BUTTON = ("Century", 8, "bold") # button font

# Styles
title_style = {
    "font": FONT_TITLE,
    "fg": COLOR_FOREGROUND,
    "bg": COLOR_BACKGROUND,
    "padx": 10,
    "pady": 10
}

data_style = {
    "font": FONT_DATA,
    "fg": COLOR_FOREGROUND,
    "bg": COLOR_LABEL_BG,
    "padx": 10,
    "pady": 5
}

label_style = {
    "font": FONT_LABEL,
    "fg": COLOR_FOREGROUND,
    "bg": COLOR_BACKGROUND,
    "padx": 4,
    "pady": 4
}

button_style = {
    "font": FONT_BUTTON,
    "fg": COLOR_BUTTON_FG,
    "bg": COLOR_BUTTON_BG,
    "activebackground": COLOR_ACCENT,
    "activeforeground": COLOR_FOREGROUND,
    "relief": "flat",
    "borderwidth": 0,
    "padx": 10,
    "pady": 5
}

frame_style = {
    "bg": COLOR_BACKGROUND,
    "padx": 10,
    "pady": 10
}