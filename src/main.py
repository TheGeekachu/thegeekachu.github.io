import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "TheGeekachu | Geeky Engineering Enthusiast"
    page.background_color = "#000000"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO

    ACCENT = "#f25f3a"
    ACCENT_DIM = "#1a0f0a"
    SURFACE = "#0b0b0c"
    TEXT = "#f4f4f6"
    MUTED = "#83838c"
    BORDER = "#1f1f23"

    def create_uniform_border(color_hex, width=1):
        side = ft.BorderSide(width, color_hex)
        return ft.Border(left=side, top=side, right=side, bottom=side)

    section_anchors = {}
    nav_links = {}

    def on_nav_click(e):
        target_section = e.control.content.value
        for text, container in nav_links.items():
            container.bgcolor = "transparent"
            container.border = create_uniform_border("transparent")
            container.content.color = MUTED
        e.control.bgcolor = ACCENT_DIM
        e.control.border = create_uniform_border(ACCENT)
        e.control.content.color = TEXT
        page.update()
        if target_section in section_anchors:
            page.scroll_to(key=section_anchors[target_section], duration=600, curve=ft.AnimationCurve.EASE_OUT)

    def create_nav_link(text, is_active=False):
        link_container = ft.Container(
            content=ft.Text(text, size=14, color=TEXT if is_active else MUTED, weight=ft.FontWeight.W_500),
            padding=ft.Padding(left=16, top=8, right=16, bottom=8),
            border_radius=20,
            bgcolor=ACCENT_DIM if is_active else "transparent",
            border=create_uniform_border(ACCENT) if is_active else create_uniform_border("transparent"),
            animate=ft.Animation(200, ft.AnimationCurve.EASE),
            on_click=on_nav_click,
            on_hover=lambda e: setattr(e.control, "bgcolor", SURFACE) if e.control.content.color == MUTED else None or page.update()
        )
        nav_links[text] = link_container
        return link_container

    logo = ft.Row(
        controls=[
            ft.Container(width=12, height=12, bgcolor=ACCENT, border_radius=3),
            ft.Text("thegeekachu", size=18, color=TEXT, weight=ft.FontWeight.BOLD)
        ],
        spacing=8
    )

    nav_bar = ft.Row(
        controls=[
            logo,
            ft.Row(
                controls=[
                    create_nav_link("Projects", is_active=True),
                    create_nav_link("Stack"),
                    ft.Container(
                        content=ft.Text("Contact", size=14, color=MUTED, weight=ft.FontWeight.W_500),
                        padding=ft.Padding(left=16, top=8, right=16, bottom=8),
                        border_radius=20,
                        url="mailto:vijayakasee@gmail.com",
                        on_hover=lambda e: setattr(e.control, "bgcolor", SURFACE) if e.data == "true" else setattr(e.control, "bgcolor", "transparent") or page.update()
                    )
                ],
                spacing=8
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    badge = ft.Container(
        content=ft.Text("Available for anything tech-related!", size=12, color=ACCENT, weight=ft.FontWeight.W_600),
        bgcolor=ACCENT_DIM,
        padding=ft.Padding(left=12, top=4, right=12, bottom=4),
        border_radius=100,
        border=create_uniform_border("rgba(242, 95, 58, 0.2)")
    )

    hero_heading = ft.Text(
        value="Aerospace, robotics, software, and anything engineering-related.",
        size=44,
        color=TEXT,
        weight=ft.FontWeight.BOLD,
        selectable=True
    )

    hero_paragraph = ft.Text(
        value="I'm a 13-year-old member of Hack Club who likes to code, build, design, hack, and anything engineering related. This website is a collage of some of my projects, experiences, and more.",
        size=18,
        color=MUTED,
        selectable=True
    )

    hero_section = ft.Column(
        controls=[badge, hero_heading, hero_paragraph],
        spacing=20
    )

    def create_section_title(title_text):
        return ft.Row(
            controls=[
                ft.Text(title_text.upper(), size=12, color=MUTED, weight=ft.FontWeight.W_600),
                ft.Container(expand=True, height=1, bgcolor=BORDER)
            ],
            spacing=12
        )

    def create_project_card(index_str, title, description, daurl):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(f"{index_str} // {title}", size=18, color=TEXT, weight=ft.FontWeight.W_600),
                    ft.Text(description, size=14, color=MUTED),
                ],
                spacing=8,
            ),
            bgcolor=SURFACE,
            border=create_uniform_border(BORDER),
            padding=30,
            border_radius=12,
            expand=True,
            animate=ft.Animation(200, ft.AnimationCurve.EASE),
            url = daurl,
            on_hover=lambda e: (
                setattr(e.control, "border", create_uniform_border(ACCENT)) if e.data == "true" 
                else setattr(e.control, "border", create_uniform_border(BORDER)), 
                e.control.update()
            )
        )

    projects_grid = ft.ResponsiveRow(
        controls=[
            ft.Column([create_project_card("01", "KnowNow", "An AI browser extension to instantly research anything that catches your fancy.", "https://github.com/TheGeekachu/know-now")], col={"sm": 12, "md": 6}),
            ft.Column([create_project_card("02", "TurboNinja", "A quick side-scrolling, relaxing platformer made in vanilla Python with Pygame.", "https://github.com/TheGeekachu/TurboNinja")], col={"sm": 12, "md": 6}),
            ft.Column([create_project_card("03", "Hadley D114", "a 4 inch Newtonian telescope capable of seeing Jupiter and it's moons.", "https://github.com/TheGeekachu")], col={"sm": 12, "md": 6}),
            ft.Column([create_project_card("04", "Terra 5", "A custom-built RC car capable of up to 50mph, and burning the plastic it's 3D-printed from.", "https://github.com/TheGeekachu")], col={"sm": 12, "md": 6}),
            ft.Column([create_project_card("05", "Assistocrat", "An AI-powered 3D model gen for your CAD projects, currently powered by GPT-OSS-4", "https://github.com/TheGeekachu/Assistocrat")], col={"sm": 12, "md": 6}),
            ft.Column([create_project_card("06", "TheGeekachuDev", "This website, built in Python with Flet, pain, and a whole lot of effort.", "https://github.com/TheGeekachu")], col={"sm": 12, "md": 6}),
        ],
        spacing=20
    )

    def create_skill_tag(tech_name):
        return ft.Container(
            content=ft.Text(tech_name, size=14, color=TEXT, weight=ft.FontWeight.W_500),
            bgcolor=SURFACE,
            border=create_uniform_border(BORDER),
            padding=ft.Padding(left=16, top=8, right=16, bottom=8),
            border_radius=12
        )

    skills_row = ft.Row(
        controls=[
            create_skill_tag("HTML / JS / CSS"),
            create_skill_tag("Arduino / C / C++"),
            create_skill_tag("Python / Flet / Reflex"),
            create_skill_tag("Linux Kernels"),
            create_skill_tag("Onshape / KiCAD"),
            create_skill_tag("Supabase / SQL")
        ],
        wrap=True,
        spacing=10
    )

    footer = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("© 2026 TheGeekachuDev. Engineered with raw code.", size=14, color=MUTED),
                ft.Row(
                    controls=[
                        ft.TextButton("GitHub", style=ft.ButtonStyle(color=TEXT), url="https://github.com"),
                        ft.TextButton("LinkedIn", style=ft.ButtonStyle(color=TEXT), url="https://linkedin.com"),
                        ft.TextButton("Email", style=ft.ButtonStyle(color=TEXT), url="mailto:vijayakasee@gmail.com")
                    ],
                    spacing=10
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        border=ft.Border(top=ft.BorderSide(1, BORDER)),
        padding=ft.Padding(top=40, bottom=0, left=0, right=0)
    )

    projects_anchor = ft.Column(controls=[create_section_title("My Featured Projects"), projects_grid], spacing=20)
    stack_anchor = ft.Column(controls=[create_section_title("A Very Geeky Stack"), skills_row], spacing=20)

    section_anchors["Projects"] = projects_anchor.key
    section_anchors["Stack"] = stack_anchor.key

    content_wrapper = ft.Column(
        controls=[
            nav_bar,
            ft.Container(height=40),
            hero_section,
            ft.Container(height=40),
            projects_anchor,
            ft.Container(height=40),
            stack_anchor,
            ft.Container(height=60),
            footer
        ],
        spacing=20,
        expand=True
    )

    main_layout = ft.Container(
        content=content_wrapper,
        width=850,
        margin=ft.Margin(left=24, top=60, right=24, bottom=60),
        alignment=ft.Alignment(0, 0),
        expand=True
    )

    page.add(ft.Row([main_layout], alignment=ft.MainAxisAlignment.CENTER, expand=True))

if __name__ == "__main__":
    ft.app(target=main)
