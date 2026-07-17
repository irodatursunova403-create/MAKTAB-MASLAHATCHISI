# app.py yoki controllers/chat.py fayliga joylang

def get_parent_chat(user, room_id):
    # 1. Foydalanuvchi tizimga kirganini tekshirish
    if not user:
        return "Xatolik: Avval tizimga kiring!"
        
    # 2. O'quvchi bu chatga kirmoqchi bo'lsa, qat'iyan rad etish
    if user.role == 'student':
        return "Xatolik: Sizda bu suhbatni ko'rish huquqi yo'q!"
    
    # 3. Faqat maslahatchi yoki tegishli ota-onaga ma'lumotlarni qaytarish
    # Bu yerda bazadan faqat shu ota-ona va maslahatchi chati yuklanadi
    return fetch_messages_from_db(room_id=room_id)
