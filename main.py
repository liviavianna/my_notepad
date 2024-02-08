import flet as ft
import tkinter.filedialog


def main(page: ft.Page):
    page.title = 'Your own notes app'
    page.scroll = True
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = True
    page.theme_mode = 'light'
    page.bgcolor = '#ff99c8'
    page.update()
    
    def save_file(e):
        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                text_to_save = text_input.value
                file.write(text_to_save)

    page.appbar = ft.AppBar(
        title=ft.Text("Livia's Notepad"),
        center_title=True,
        bgcolor='#fcf6bd'
    )

    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor='#fcf6bd',
            mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                          ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Save"),
                        leading=ft.Icon(ft.icons.SAVE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}),
                        on_click=save_file
                    )
                ]
            ),
        ]
    )
    text_input = ft.TextField(
            multiline = True,
            border_width = 0,
            autofocus= True
        )    
    page.add(ft.Row([menubar]), text_input)
ft.app(target=main)
