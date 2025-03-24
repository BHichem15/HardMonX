# Colors
COLOR_BACKGROUND = "#F7F7F7"  # خلفية فاتحة
COLOR_FOREGROUND = "#2E2E2E"  # نص داكن
COLOR_ACCENT = "#4A90E2"       # لون بارز أزرق هادئ
COLOR_BUTTON_BG = "#EAEAEA"    # لون أزرار فاتح
COLOR_BUTTON_FG = "#333333"    # نص الأزرار داكن قليلاً
COLOR_LABEL_BG = "#FFFFFF"     # خلفية التسمية بيضاء تمامًا
COLOR_ENTRY_BG = "#F0F0F0"     # خلفية حقول الإدخال رمادية خفيفة


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