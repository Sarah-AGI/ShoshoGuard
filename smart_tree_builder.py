import os

tree = {
    "README.md": "",
    "LICENSE.TIM": "",
    "requirements.txt": "",
    "backend": {
        "app.py": "",
        "utils": {"honeytoken.py": ""},
        "scanner": {"permission_scanner.py": ""},
        "memegen": {"meme_generator.py": ""},
        "reports": {"report_builder.py": ""},
        "ghost_mode": {"fake_data.py": ""},
    },
    "frontend": {
        "public": {},
        "src": {
            "App.jsx": "",
            "components": {
                "ScandalButton.jsx": "",
                "GhostMode.jsx": "",
                "MemeWall.jsx": "",
                "FakeTransparencyBot.jsx": "",
            },
            "assets": {
                "memes": {},
                "turtle": {},
            }
        },
        "package.json": "",
    },
    "podcast": {
        "episodes": {
            "ep01-intro.mp3": "",
            "ep02-museum.mp3": "",
        },
        "notes": {
            "ep01-notes.txt": "",
        },
    },
    "tests": {
        "test_scanner.py": "",
        "test_meme.py": "",
        "test_ghost.py": "",
    },
}

def smart_make_tree(base, struct):
    for name, content in struct.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            if not os.path.exists(path):
                os.makedirs(path)
            smart_make_tree(path, content)
        else:
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

if __name__ == "__main__":
    root = "."
    smart_make_tree(root, tree)
    print("👌 تمت إضافة كل المجلدات والملفات الناقصة بدون أي حذف! (طريقة شوشو الحذرة)")

