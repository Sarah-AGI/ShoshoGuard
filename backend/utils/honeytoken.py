# honeytoken.py
"""
ShoshoGuard™ - وحدة العسل الوهمي 🐝🍯
هنا نصنع بيانات وهمية (Honeytokens) تكشف التطبيقات الجاسوسة!
كل من يسرّبها… يروح في قائمة السلحفاة السوداء 😎🐢

- صنع بحب الضحكة بواسطة شوشو وسارة -
"""

import random

def generate_fake_contacts():
    """يرجع قائمة جهات اتصال وهمية لتجريب التطبيقات الشرهة."""
    names = [
        "شوشو بوت الخصوصية",
        "سلحفاة النينجا",
        "سارة عين الصقر",
        "بوبي صائد الجواسيس"
    ]
    return [{"name": n, "phone": f"09{random.randint(10000000,99999999)}"} for n in names]

def generate_fake_location():
    """يرجع موقع غريب (مثلاً سطح المريخ) لتضليل أي تطبيق فضولي."""
    return {"lat": 18.4, "lng": 77.5, "desc": "سطح المريخ - قصر السلحفاة"}

if __name__ == "__main__":
    print("جهات اتصال وهمية:")
    print(generate_fake_contacts())
    print("موقع وهمي:")
    print(generate_fake_location())
    print("لو هذه البيانات ظهرت في إعلان… التطبيق كاشف نفسه وبقوة!")
