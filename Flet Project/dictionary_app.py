from turtle import width
import flet as ft
import dictionary_backend as db

def main(page: ft.Page):
    page.title = "Dictionary"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    
    # def minus_click(e):
    #     txt_number.value = str(int(txt_number.value) - 1)
    #     page.update()

    # def plus_click(e):
    #     txt_number.value = str(int(txt_number.value) + 1)
    #     page.update()

    async def move_divider(e: ft.DragUpdateEvent):
        if (e.delta_y > 0 and results_bar.width < 300) or (e.delta_y < 0 and results_bar.width > 100):
            results_bar.width += e.delta_y
        await results_bar.update_async()

    async def show_draggable_cursor(e: ft.HoverEvent):
        e.control.mouse_cursor = ft.MouseCursor.RESIZE_LEFT_RIGHT
        await e.control.update_async()

    results_bar = ft.Container(
            bgcolor=ft.colors.WHITE10,
            alignment=ft.alignment.center,
            width=100,
            expand=True
    )
    search_definitions = ft.Container(
            bgcolor=ft.colors.BLACK87,
            alignment=ft.alignment.center,
            expand=True,
    )

    slider_divider = ft.GestureDetector(
                    content=ft.Divider(height=1, thickness=3, color='white'),
                    on_pan_update=move_divider,
                    on_hover=show_draggable_cursor,
    )

    page.add(
        ft.Row(
            [   
                results_bar,
                ft.Divider(),
                search_definitions
            ],
            spacing=0,
            expand=True,
        )
    )

ft.app(target=main)