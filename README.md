# 🏫 MAKTAB-MASLAHATCHISI

Maktab o'quvchilari, ota-onalar va o'qituvchilarga ta'lim jarayonida maslahat va yordam beruvchi platforma.

## 🚀 Loyiha haqida
Bu loyiha maktab tizimidagi foydalanuvchilarga to'g'ri yo'nalish ko'rsatish va muammolarni hal qilishga yordam berish uchun yaratilgan.

## ✨ Imkoniyatlari
* 💬 Onlayn maslahat olish tizimi
* 📚 Foydali o'quv materiallari bazasi
* 🎯 Kasbga yo'naltirish testlari

# Maslahatchi va Ota-ona suhbatini yuklash funksiyasi
def get_parent_chat(user):
    # Agar so'rov yuborgan foydalanuvchi o'quvchi bo'lsa, xabarlarni bermaydi
    if user.role == 'student':
        return "Xatolik: Sizda bu suhbatni ko'rish huquqi yo'q!"

    # Faqat maslahatchi yoki tegishli ota-onaga ruxsat beriladi
    return fetch_messages_from_db(room_type='parent_counselor')
