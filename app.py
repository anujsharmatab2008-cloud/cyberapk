import flet as ft

# --- COMPLETE COMPREHENSIVE INTEGRATED DATABASE ---
GLOBAL_DATABASE = [
    # --- BUDGET CHAMPIONS & RECENT MID-RANGERS (₹14k - ₹20k) ---
    {"name": "OnePlus Nord CE 6 Lite 5G", "brand": "OnePlus", "price": 18999, "ram": 6, "storage": 128, "cpu": "Dimensity 7400 Apex", "battery": 7000},
    {"name": "POCO M8 5G", "brand": "Poco", "price": 17999, "ram": 6, "storage": 128, "cpu": "Snapdragon 6 Gen 3", "battery": 5520},
    {"name": "Moto G96 5G", "brand": "Motorola", "price": 17999, "ram": 8, "storage": 128, "cpu": "Snapdragon 7s Gen 2", "battery": 5500},
    {"name": "Vivo T4X 5G", "brand": "Vivo", "price": 16999, "ram": 6, "storage": 128, "cpu": "Dimensity 7300", "battery": 6500},
    {"name": "Realme P4x 5G", "brand": "Realme", "price": 15999, "ram": 6, "storage": 128, "cpu": "Dimensity 7400 Ultra", "battery": 7000},
    {"name": "Realme P3 5G", "brand": "Realme", "price": 15999, "ram": 6, "storage": 128, "cpu": "Snapdragon 6 Gen 4", "battery": 6000},
    {"name": "Samsung Galaxy F36 5G", "brand": "Samsung", "price": 17999, "ram": 6, "storage": 128, "cpu": "Exynos 1380", "battery": 6000},
    {"name": "POCO X7 5G", "brand": "Poco", "price": 16999, "ram": 8, "storage": 128, "cpu": "Dimensity 7300", "battery": 5500},
    {"name": "CMF by Nothing Phone 2 Pro", "brand": "Nothing", "price": 17999, "ram": 8, "storage": 128, "cpu": "Dimensity 7400", "battery": 5000},
    {"name": "iQOO Z10x 5G", "brand": "iQOO", "price": 14998, "ram": 6, "storage": 128, "cpu": "Dimensity 7300", "battery": 6500},
    {"name": "Motorola Moto G86 Power 5G", "brand": "Motorola", "price": 17500, "ram": 8, "storage": 128, "cpu": "Dimensity 7400", "battery": 6720},
    {"name": "iQOO Z9x 5G", "brand": "iQOO", "price": 17499, "ram": 8, "storage": 128, "cpu": "Snapdragon 6 Gen 1", "battery": 6000},
    {"name": "iQOO Z9 5G", "brand": "iQOO", "price": 19999, "ram": 8, "storage": 128, "cpu": "Dimensity 7200", "battery": 5000},
    {"name": "Samsung Galaxy M35 5G", "brand": "Samsung", "price": 19999, "ram": 8, "storage": 128, "cpu": "Exynos 1380", "battery": 6000},
    {"name": "Motorola G64 5G", "brand": "Motorola", "price": 15999, "ram": 8, "storage": 128, "cpu": "Dimensity 7025", "battery": 6000},
    {"name": "Realme P1 5G", "brand": "Realme", "price": 15999, "ram": 6, "storage": 128, "cpu": "Dimensity 7050", "battery": 5000},
    {"name": "Realme Narzo 70 Pro", "brand": "Realme", "price": 18999, "ram": 8, "storage": 128, "cpu": "Dimensity 7050", "battery": 5000},
    {"name": "Xiaomi Redmi Note 13 5G", "brand": "Xiaomi", "price": 16999, "ram": 6, "storage": 128, "cpu": "Dimensity 6080", "battery": 5000},
    {"name": "Xiaomi Redmi Note 14 5G", "brand": "Xiaomi", "price": 19999, "ram": 8, "storage": 128, "cpu": "Dimensity 7025 Ultra", "battery": 5110},
    {"name": "POCO X6 Neo 5G", "brand": "Poco", "price": 15999, "ram": 8, "storage": 128, "cpu": "Dimensity 6080", "battery": 5000},
    {"name": "OPPO K14x 5G", "brand": "OPPO", "price": 14749, "ram": 6, "storage": 128, "cpu": "Dimensity 6300", "battery": 6500},
    {"name": "Vivo T3x 5G", "brand": "Vivo", "price": 16499, "ram": 8, "storage": 128, "cpu": "Snapdragon 6 Gen 1", "battery": 6000},
    {"name": "Lava Agni 2 5G", "brand": "Lava", "price": 17999, "ram": 8, "storage": 256, "cpu": "Dimensity 7050", "battery": 4700},

    # --- APPLE PREMIUM ECOSYSTEM ---
    {"name": "Apple iPhone 17 Pro Max", "brand": "Apple", "price": 149900, "ram": 12, "storage": 256, "cpu": "A19 Pro", "battery": 4832},
    {"name": "Apple iPhone 17 Pro", "brand": "Apple", "price": 129900, "ram": 12, "storage": 128, "cpu": "A19 Pro", "battery": 4200},
    {"name": "Apple iPhone 17 Standard", "brand": "Apple", "price": 79900, "ram": 8, "storage": 128, "cpu": "A19", "battery": 4000},
    {"name": "Apple iPhone 16 Pro Max", "brand": "Apple", "price": 139900, "ram": 8, "storage": 256, "cpu": "A18 Pro", "battery": 4685},
    {"name": "Apple iPhone 16 Standard", "brand": "Apple", "price": 69900, "ram": 8, "storage": 128, "cpu": "A18", "battery": 3561},
    {"name": "Apple iPhone 15 Pro Max", "brand": "Apple", "price": 124900, "ram": 8, "storage": 256, "cpu": "A17 Pro", "battery": 4441},
    {"name": "Apple iPhone 15 Standard", "brand": "Apple", "price": 59900, "ram": 6, "storage": 128, "cpu": "A16 Bionic", "battery": 3349},
    {"name": "Apple iPhone SE 4 (AI Edition)", "brand": "Apple", "price": 49900, "ram": 8, "storage": 128, "cpu": "A18", "battery": 3200},

    # --- SAMSUNG ULTRA FLAGSHIP & HIGH TIERS ---
    {"name": "Samsung Galaxy S26 Ultra", "brand": "Samsung", "price": 121998, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 5000},
    {"name": "Samsung Galaxy S26 Plus", "brand": "Samsung", "price": 84999, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 4900},
    {"name": "Samsung Galaxy S25 Ultra", "brand": "Samsung", "price": 104400, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 5000},
    {"name": "Samsung Galaxy S24 Ultra", "brand": "Samsung", "price": 99999, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Gen 3", "battery": 5000},
    {"name": "Samsung Galaxy S24 FE", "brand": "Samsung", "price": 54999, "ram": 8, "storage": 128, "cpu": "Exynos 2400e", "battery": 4700},
    {"name": "Samsung Galaxy A57 5G", "brand": "Samsung", "price": 38999, "ram": 8, "storage": 128, "cpu": "Exynos 1580", "battery": 5000},
    {"name": "Samsung Galaxy A37 5G", "brand": "Samsung", "price": 27999, "ram": 8, "storage": 128, "cpu": "Exynos 1480", "battery": 5000},
    {"name": "Samsung Galaxy M55 5G", "brand": "Samsung", "price": 24999, "ram": 8, "storage": 128, "cpu": "Snapdragon 7 Gen 1", "battery": 5000},

    # --- ONEPLUS HIGH PERFORMANCE ---
    {"name": "OnePlus 15 Pro", "brand": "OnePlus", "price": 79999, "ram": 16, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 6500},
    {"name": "OnePlus 13 Standard", "brand": "OnePlus", "price": 69999, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Elite", "battery": 6000},
    {"name": "OnePlus 13R 5G", "brand": "OnePlus", "price": 42999, "ram": 12, "storage": 256, "cpu": "Snapdragon 8 Gen 3", "battery": 6000},
    {"name": "OnePlus 12R", "brand": "OnePlus", "price": 37999, "ram": 8, "storage": 128, "cpu": "Snapdragon 8 Gen 2", "battery": 5500},
    {"name": "OnePlus Nord 6 5G", "brand": "OnePlus", "price": 42999, "ram": 8, "storage": 256, "cpu": "Snapdragon 8s Gen 4", "battery": 9000},
    {"name": "OnePlus Nord CE 4 5G", "brand": "OnePlus", "price": 23499, "ram": 8, "storage": 128, "cpu": "Snapdragon 7 Gen 3", "battery": 5500},

    # --- ADVANCED POWER MID-RANGERS (₹20k - ₹120k) ---
    {"name": "Xiaomi 17 Ultra", "brand": "Xiaomi", "price": 119999, "ram": 16, "storage": 512, "cpu": "Snapdragon 8 Elite", "battery": 5500},
    {"name": "Xiaomi Redmi Note 15 Pro+", "brand": "Xiaomi", "price": 33999, "ram": 12, "storage": 256, "cpu": "Dimensity 7500 Ultra", "battery": 5500},
    {"name": "POCO F6 5G", "brand": "Poco", "price": 29999, "ram": 8, "storage": 256, "cpu": "Snapdragon 8s Gen 3", "battery": 5000},
    {"name": "POCO X6 Pro 5G", "brand": "Poco", "price": 22499, "ram": 8, "storage": 256, "cpu": "Dimensity 8300 Ultra", "battery": 5000},
    {"name": "Realme GT 6T 5G", "brand": "Realme", "price": 29999, "ram": 8, "storage": 128, "cpu": "Snapdragon 7+ Gen 3", "battery": 5500},
    {"name": "Motorola Edge 50 Pro", "brand": "Motorola", "price": 29999, "ram": 8, "storage": 256, "strong": "Snapdragon 7 Gen 3", "battery": 4500},
    {"name": "Motorola Edge 50 Fusion", "brand": "Motorola", "price": 21999, "ram": 8, "storage": 128, "cpu": "Snapdragon 7s Gen 2", "battery": 5000},
    {"name": "iQOO Neo 11 Pro", "brand": "iQOO", "price": 36999, "ram": 8, "storage": 256, "cpu": "Snapdragon 8 Gen 4", "battery": 7500},
    {"name": "Vivo V40 Pro 5G", "brand": "Vivo", "price": 49999, "ram": 8, "storage": 256, "cpu": "Dimensity 9200+", "battery": 5500},
    {"name": "OPPO Reno 12 Pro 5G", "brand": "OPPO", "price": 34999, "ram": 12, "storage": 256, "cpu": "Dimensity 7300 Energy", "battery": 5000},
    {"name": "Google Pixel 9 Pro XL", "brand": "Google", "price": 89999, "ram": 16, "storage": 128, "cpu": "Tensor G4", "battery": 5060},
    {"name": "Nothing Phone (2a) Plus", "brand": "Nothing", "price": 27999, "ram": 8, "storage": 256, "cpu": "Dimensity 7350 Pro", "battery": 5000}
]

def main(page: ft.Page):
    page.title = "CYBER AGGREGATOR AI"
    page.bgcolor = "#0A0F14"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "adaptive"
    page.padding = 15

    selected_to_compare = []

    def sync_budget(e):
        budget_text.value = f"Max Budget: ₹{int(budget_slider.value):,}"
        page.update()
        filter_data()

    def filter_data(e=None):
        query = search_input.value.lower().strip()
        max_budget = int(budget_slider.value)
        selected_processor = processor_dropdown.value
        
        product_list.controls.clear()
        for p in GLOBAL_DATABASE:
            if p["price"] > max_budget:
                continue
            if selected_processor and selected_processor != "All Processors":
                if selected_processor.lower() == "apple" and "a1" not in p["cpu"].lower():
                    continue
                elif selected_processor.lower() != "apple" and selected_processor.lower() not in p["cpu"].lower():
                    continue
            if query and query not in p["name"].lower() and query not in p["brand"].lower():
                continue
            
            # Use closures to uniquely freeze current items inside dynamic checkboxes
            def make_change_closure(prod=p):
                return lambda e: handle_checkbox(e, prod)

            product_list.controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(p["name"], weight="bold", color="#FFFFFF", size=13),
                            ft.Text(f"₹{p['price']:,} | Core: {p['cpu']}", color="#888888", size=11),
                        ], expand=True),
                        ft.Checkbox(on_change=make_change_closure())
                    ]),
                    padding=10, bgcolor="#121B22", border_radius=8, margin=ft.margin.only(bottom=4)
                )
            )
        page.update()

    def handle_checkbox(e, prod):
        if e.control.value:
            if prod not in selected_to_compare:
                selected_to_compare.append(prod)
        else:
            if prod in selected_to_compare:
                selected_to_compare.remove(prod)
        update_matrix()

    def update_matrix():
        matrix_list.controls.clear()
        if not selected_to_compare:
            matrix_list.controls.append(ft.Text("// No nodes mapped...", color="#666666", font_family="Courier"))
        else:
            for p in selected_to_compare[:3]:
                matrix_list.controls.append(
                    ft.Text(f"• {p['name']} (₹{p['price']:,} | {p['ram']}GB RAM | {p['battery']}mAh)", size=12, color="#00E5FF")
                )
        page.update()

    def run_verdict(e):
        if len(selected_to_compare) < 2:
            verdict_box.value = "[ERROR] Select at least 2 devices to map values."
            winner_banner.text = "🏆 AI WINNER: SELECTION ERROR"
            winner_banner.text_color = "#FF3333"
            page.update()
            return
            
        verdict_box.value = "Analyzing data layers..."
        page.update()
        
        winner = selected_to_compare[0]
        for c in selected_to_compare:
            if c["ram"] > winner["ram"]:
                winner = c
            elif c["ram"] == winner["ram"]:
                if c["price"] < winner["price"] and c["battery"] >= winner["battery"]:
                    winner = c
                
        winner_banner.text = f"🏆 WINNER: {winner['name'].upper()}"
        winner_banner.text_color = "#00FF66"
        verdict_box.value = f"[ANALYSIS SUCCESSFUL]\nRecommended asset: {winner['name']}.\nIt features an optimized {winner['cpu']} chip layout, {winner['ram']} GB memory system, and a balanced battery power map for its retail range."
        page.update()

    # Layout Elements Components
    title = ft.Text("CYBER AGGREGATOR Mobile", size=22, weight="bold", color="#00FF66")
    search_input = ft.TextField(hint_text="Type hardware keyword...", border_color="#00E5FF", on_change=filter_data)
    
    processor_dropdown = ft.Dropdown(
        value="All Processors",
        options=[
            ft.dropdown.Option("All Processors"),
            ft.dropdown.Option("Snapdragon"),
            ft.dropdown.Option("Dimensity"),
            ft.dropdown.Option("Apple"),
            ft.dropdown.Option("Tensor"),
            ft.dropdown.Option("Exynos")
        ],
        border_color="#00E5FF",
        on_change=filter_data
    )
    
    budget_text = ft.Text("Max Budget: ₹1,50,000", weight="bold", color="#FFFFFF")
    budget_slider = ft.Slider(min=10000, max=150000, value=150000, divisions=140, on_change=sync_budget)
    
    product_list = ft.Column()
    matrix_list = ft.Column([ft.Text("// No nodes mapped...", color="#666666", font_family="Courier")])
    
    winner_banner = ft.Text("🏆 AI WINNER: AWAITING SELECTION...", weight="bold", color="#888888")
    verdict_box = ft.Text("// Standing by...", color="#00FF66", font_family="Courier")

    page.add(
        title,
        ft.Container(content=ft.Column([search_input, processor_dropdown, budget_text, budget_slider]), padding=12, bgcolor="#121B22", border_radius=8),
        ft.Text("Available Models Cluster:", weight="bold", size=14, color="#00E5FF"),
        product_list,
        ft.Divider(color="#00E5FF"),
        ft.Text("Live Benchmarking Nodes:", weight="bold", size=14, color="#00E5FF"),
        ft.Container(content=matrix_list, padding=10, bgcolor="#0A0F14", border_radius=8),
        ft.Container(content=winner_banner, padding=12, bgcolor="#1A2630", border_radius=8, alignment=ft.alignment.center),
        ft.ElevatedButton("RUN INTELLECT VERDICT ⚡", bgcolor="#00FF66", color="#0A0F14", on_click=run_verdict, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6))),
        ft.Container(content=verdict_box, padding=10, bgcolor="#0A0F14", border_radius=8)
    )

    filter_data()

ft.app(target=main)
