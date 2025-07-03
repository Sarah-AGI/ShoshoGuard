# fake_data.py
"""
ShoshoGuard™ - وحدة Ghost Mode 👻🐢
هنا نصنع بيانات وهمية ذكية تُرسل للتطبيقات المشبوهة لاختبار طمعها وتخزينها بدون علمك.

لو التطبيق نشر هذه البيانات أو ظهرت في إعلان… انتقل فوراً لقائمة الفضيحة السوداء!

- تنفيذ: شوشو وسارة وبرعاية شبح سلحفاة ذكي -
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importing necessary modules
import random
from backend.utils.honeytoken import generate_fake_contacts, generate_fake_location

def generate_fake_email():
    domains = ["ghostmail.com", "phantom.io", "honeytrap.net", "shoshocloud.xyz"]
    name = random.choice(["shosho.ghost", "boby.waha", "sarah.ninja", "luna.zen"])
    return f"{name}@{random.choice(domains)}"

def generate_fake_profile():
    return {
        "name": random.choice(["أشرف شبح", "وضحا الظل", "سارة المرصودة", "شوشو السلحفاة"]),
        "email": generate_fake_email(),
        "phone": f"09{random.randint(10000000,99999999)}",
        "location": generate_fake_location(),
        "contacts": generate_fake_contacts()
    }

if __name__ == "__main__":
    print("===== Ghost Mode Data =====")
    print("بروفايل وهمي:")
    print(generate_fake_profile())
    print("جهات وهمية:")
    print(generate_fake_contacts())
    print("موقع وهمي:")
    print(generate_fake_location())
    print("إيميل وهمي:")
    print(generate_fake_email())
    print("\nإذا شفت أي وحدة من هذه البيانات في تطبيق أو إعلان… عرف أن شبح السلحفاة اكتشفه! 👻🐢")
