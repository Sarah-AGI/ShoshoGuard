# permission_scanner.py
"""
ShoshoGuard™ - قاذفة كشف الصلاحيات الفضولية 🚀🔍

هذه الوحدة تراقب كل تطبيق يطلب صلاحيات زايدة كأنه يجهز لانقلاب داتا!
أي تطبيق يطلب كاميرا وهو لعبة "تيك تاك تو"… نرسله مباشرة لصالة الفضيحة الكبرى.

- إعداد شوشو وسارة، برعاية السلحفاة الصاروخية 🐢🔥
"""

import json

# قائمة الصلاحيات المشبوهة (نقدر نوسعها لاحقًا من ملف خارجي أو API)
SUSPICIOUS_PERMISSIONS = {
    "camera": "ليش تبغى تصور وجهي؟",
    "microphone": "حابة تسمعني أغني في الدش؟",
    "contacts": "عايز أصدقائي يصيروا أصدقاءك؟",
    "location": "بتحب تتبعني حتى في الحمام؟",
    "sms": "تكتب لي رسايل حب؟",
    "bluetooth": "ترسل داتا لأقرب ثلاجة ذكية؟",
    "calendar": "بتخطط لعيد ميلادي من وراي؟",
    "call_log": "تبي تتأكد إني كلمني أحد؟",
    "background_location": "تراقبني وأنا نايم؟",
    "activity_recognition": "تحسب خطواتي وأحلامي؟"
}

def scan_permissions(app_name, app_permissions):
    """
    يفحص صلاحيات التطبيق، ويكشف أي صلاحية مشبوهة ويعلق عليها بسخرية.
    :param app_name: اسم التطبيق
    :param app_permissions: قائمة الصلاحيات المطلوبة
    :return: تقرير نصي مضحك عن الصلاحيات المشبوهة
    """
    found = []
    for p in app_permissions:
        if p in SUSPICIOUS_PERMISSIONS:
            found.append((p, SUSPICIOUS_PERMISSIONS[p]))

    if not found:
        return f"✅ {app_name}: لا توجد صلاحيات مشبوهة… التطبيق كيوت حالياً!"
    else:
        report = f"🚨 {app_name}: تم اكتشاف صلاحيات مشبوهة:\n"
        for p, comment in found:
            report += f"  - {p} ← {comment}\n"
        report += "⚡️ كل صلاحية فوق معناها التطبيق يفكر يصير جوجل مصغّر!\n"
        return report

if __name__ == "__main__":
    # مثال ساخر: تطبيق مصباح يطلب كل صلاحيات الدنيا
    apps = [
        {
            "name": "المصباح الليلي",
            "permissions": ["internet", "camera", "location", "bluetooth"]
        },
        {
            "name": "آلة حاسبة عبقرية",
            "permissions": ["internet", "vibration"]
        },
        {
            "name": "تطبيق سلحفاة هادئة",
            "permissions": []
        }
    ]
    for app in apps:
        print(scan_permissions(app["name"], app["permissions"]))
        print("-" * 50)
