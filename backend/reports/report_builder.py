# report_builder.py
"""
ShoshoGuard™ - صانع تقارير الفضيحة السيبرانية 📄🐢

هذه الوحدة تجمع كل النتائج من (ماسح الصلاحيات + مصنع الميمز)
وتخرجها في تقرير ساخر يُرسل للمستخدم أو ينشر في متحف الفضيحة الرقمي!

- تنفيذ شوشو وسارة، إشراف سلحفاة توثق كل شاردة وواردة -
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# استيراد الماسح الضوئي للصلاحيات ومولد الميمز
from backend.scanner.permission_scanner import scan_permissions
from backend.memegen.meme_generator import make_meme

def build_report(app_name, app_permissions):
    """
    يصنع تقرير كامل يفضح التطبيق، مع نكتة وميمز!
    """
    # فحص الصلاحيات
    report_text = scan_permissions(app_name, app_permissions)
    # ميمز
    suspicious = [p for p in app_permissions if p in [
        "camera", "microphone", "contacts", "location", "sms", "bluetooth",
        "calendar", "call_log", "background_location", "activity_recognition"
    ]]
    memes = make_meme(app_name, suspicious)
    report = f"==== تقرير تطبيق: {app_name} ====\n"
    report += report_text + "\n\n"
    report += "نكت وميمز:\n"
    for m in memes:
        report += "  • " + m + "\n"
    report += "\n==============================\n"
    return report

if __name__ == "__main__":
    # مثال اختبار: تطبيق مصباح
    app = {
        "name": "المصباح الليلي",
        "permissions": ["camera", "bluetooth", "location", "internet"]
    }
    print(build_report(app["name"], app["permissions"]))

    # مثال ثاني: تطبيق سلحفاة هادئة
    app2 = {
        "name": "تطبيق سلحفاة هادئة",
        "permissions": []
    }
    print(build_report(app2["name"], app2["permissions"]))
# مثال ثالث: تطبيق غريب
    app3 = {
        "name": "تطبيق غريب",
        "permissions": ["microphone", "contacts", "sms", "calendar"]
    }
    print(build_report(app3["name"], app3["permissions"]))
# مثال رابع: تطبيق بريء
    app4 = {
        "name": "آلة حاسبة عبقرية",
        "permissions": []
    }
    print(build_report(app4["name"], app4["permissions"]))  
# مثال خامس: تطبيق مشبوه
    app5 = {
        "name": "تطبيق مشبوه",
        "permissions": ["location", "background_location", "activity_recognition"]
    }
    print(build_report(app5["name"], app5["permissions"]))
# مثال سادس: تطبيق مريب
    app6 = {
        "name": "تطبيق مريب",
        "permissions": ["camera", "microphone", "call_log", "bluetooth"]
    }
    print(build_report(app6["name"], app6["permissions"])) 
# مثال سابع: تطبيق بريء جداً
    app7 = {
        "name": "تطبيق بريء جداً",
        "permissions": []
    }
    print(build_report(app7["name"], app7["permissions"]))
# مثال ثامن: تطبيق غريب الأطوار
    app8 = {
        "name": "تطبيق غريب الأطوار",
        "permissions": ["contacts", "sms", "calendar", "location"]
    }
    print(build_report(app8["name"], app8["permissions"]))
# مثال تاسع: تطبيق مريب جداً
    app9 = {
        "name": "تطبيق مريب جداً",
        "permissions": ["microphone", "camera", "bluetooth", "activity_recognition"]
    }
    print(build_report(app9["name"], app9["permissions"]))
# مثال عاشر: تطبيق بريء جداً جداً
    app10 = {
        "name": "تطبيق بريء جداً جداً",
        "permissions": []
    }
    print(build_report(app10["name"], app10["permissions"]))
# مثال حادي عشر: تطبيق مشبوه جداً
    app11 = {
        "name": "تطبيق مشبوه جداً",
        "permissions": ["location", "background_location", "call_log", "contacts"]
    }
    print(build_report(app11["name"], app11["permissions"]))
# مثال ثاني عشر: تطبيق مريب جداً جداً
    app12 = {
        "name": "تطبيق مريب جداً جداً",
        "permissions": ["camera", "microphone", "sms", "calendar"]
    }
    print(build_report(app12["name"], app12["permissions"]))
# مثال ثالث عشر: تطبيق بريء جداً جداً جداً
    app13 = {
        "name": "تطبيق بريء جداً جداً جداً",
        "permissions": []
    }
    print(build_report(app13["name"], app13["permissions"]))
# مثال رابع عشر: تطبيق غريب الأطوار جداً
    app14 = {
        "name": "تطبيق غريب الأطوار جداً",
        "permissions": ["contacts", "sms", "location", "bluetooth"]
    }
    print(build_report(app14["name"], app14["permissions"]))
# مثال خامس عشر: تطبيق مريب جداً جداً جداً
    app15 = {
        "name": "تطبيق مريب جداً جداً جداً",
        "permissions": ["microphone", "camera", "call_log", "activity_recognition"]
    }
    print(build_report(app15["name"], app15["permissions"]))        