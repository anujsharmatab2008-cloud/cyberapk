import flet as ft

GLOBAL_DATABASE = [
    {"name": "OnePlus Nord CE 6 Lite", "brand": "OnePlus", "price": 18999, "cpu": "Dimensity 7400"},
    {"name": "iPhone 17 Pro Max", "brand": "Apple", "price": 149900, "cpu": "A19 Pro"},
    {"name": "Samsung Galaxy S26 Ultra", "brand": "Samsung", "price": 121998, "cpu": "Snapdragon 8 Elite"},
    {"name": "Google Pixel 9 Pro XL", "brand": "Google", "price": 89999, "cpu": "Tensor G4"}
]

def main(page: ft.Page):
    page.title = "CYBER AGGREGATOR"
    page.theme_mode = ft.ThemeMode.DARK
    
    def build_list(e=None):
        lv.controls.clear()
        for item in GLOBAL_DATABASE:
            lv.controls.append(ft.ListTile(title=ft.Text(item["name"]), subtitle=ft.Text(f"₹{item['price']}")))
        page.update()

    lv = ft.ListView(expand=1, spacing=10)
    page.add(ft.Text("Available Nodes", size=20), lv)
    build_list()

ft.app(target=main)
