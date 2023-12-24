import flet as ft

def main(page: ft.Page):
    def swap_theme_color(self):
        print(self.control.text)
        if self == 1:
            page.theme = ft.Theme(color_scheme_seed=ft.colors.RED)
        else:
            page.theme = ft.Theme(color_scheme_seed=ft.colors.BLUE)
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=swap_theme_color
                    ),
                ]
            ),
        ],
    )
    page.add(ft.Text("Body!"))

ft.app(target=main)