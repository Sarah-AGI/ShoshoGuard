# honeytoken.py
"""
مكتبة زرع بيانات وهمية في التطبيقات لاختبار من يسرّب المعلومات.
"""
import random

def generate_fake_contacts():
    names = [
        "شوشو بوت الخصوصية", "سلحفاة النينجا", "سارة عين الصقر", "بوبي صائد الجواسيس"
    ]
    return [{"name": n, "phone": f"09{random.randint(10000000,99999999)}"} for n in names]

def generate_fake_location():
    # موقع على سطح المريخ
    return {"lat": 18.4, "lng": 77.5, "desc": "سطح المريخ - قصر السلحفاة"}

if __name__ == "__main__":
    print(generate_fake_contacts())
    print(generate_fake_location())
