import flet as ft
from datetime import datetime

def main(page : ft.Page):
    page.title= "Мое первое приложение"
    greeting_text= ft.Text(value= 'Hello world!', color= ft.Colors.GREEN)
    button_name=ft.Text(value = "Изменение темы :")
    page.theme_mode = ft.ThemeMode.LIGHT
    theme_status= ft.Text(value= 'Светлая')
    
    # greeting_text.value= 'Привет'
    # greeting_text.color= ft.Colors.GREEN

    def on_button_click(_):
        # print(name_input.value)
        name=name_input.value.strip()

        timestamp=datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f' {timestamp} - Hello {name}'
            greeting_text.color=None
            name_input.value=None
        else:
            greeting_text.value= 'Введите корректное имя'
            greeting_text.color=ft.Colors.RED

        page.update()

    def button_sun(_):
        if page.theme_mode == ft.ThemeMode.LIGHT :
           page.theme_mode = ft.ThemeMode.DARK
           theme_status.value= "Темная"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_status.value= "Светлая"

        page.update()

    name_input= ft.TextField(label ='Введите имя', on_submit= on_button_click)

    button_text=ft.TextButton(text='send',on_click=on_button_click)
    button_elevated=ft.ElevatedButton(text='send',on_click=on_button_click)
    button_icon_send=ft.IconButton(ft.Icons.SEND, on_click=on_button_click)
    button_icon_sun=ft.IconButton(ft.Icons.BRIGHTNESS_7, on_click=button_sun)


    page.add(greeting_text, name_input,button_text, button_elevated,button_icon_send)
    page.add(ft.Row([button_icon_sun,button_name ,theme_status]))

ft.app(target=main)


 