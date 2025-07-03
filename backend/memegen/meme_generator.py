# meme_generator.py
"""
ShoshoGuard™ - مصنع الميمز السيبرانية 😂🐢
كل تطبيق نصاب… نصنع له ميمز على مقاسه ونضحك عليه علناً!

- إعداد شوشو وسارة، برعاية سلحفاة ترسم النكت -
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import random

# قوالب الميمز النصية (قابلة للتوسيع لأي صورة لاحقاً)
MEME_TEMPLATES = [
    "🐢: {app} يطلب {perm}! أكيد ناوي يدخل موسوعة جينيس لأغرب تطبيق.",
    "😂: لو {app} طلب {perm}… قول له: 'صورني وأنا أضحك عليك!'",
    "🤔: {app} جالس يجمع {perm}؟ يمكن يفتح له متحف خاص بالبيانات.",
    "🚨: انتبه! {app} صار يسأل عن {perm}… السلحفاة الآن في وضع التأهب!"
]

def make_meme(app_name, suspicious_permissions):
    """
    يصنع ميمز نصي ساخر لكل صلاحية مشبوهة.
    :param app_name: اسم التطبيق
    :param suspicious_permissions: قائمة الصلاحيات المشبوهة
    :return: قائمة ميمز نصية
    """
    memes = []
    for perm in suspicious_permissions:
        template = random.choice(MEME_TEMPLATES)
        memes.append(template.format(app=app_name, perm=perm))
    if not memes:
        memes.append(f"🌟 {app_name} تطبيق بريء... السلحفاة ترسل لك تحية!")
    return memes

if __name__ == "__main__":
    # تجربة: تطبيق غريب
    memes1 = make_meme("المصباح الليلي", ["camera", "bluetooth", "location"])
    for m in memes1:
        print(m)
    print("-" * 40)
    # تجربة: تطبيق بريء
    memes2 = make_meme("آلة حاسبة عبقرية", [])
    for m in memes2:
        print(m)
