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

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'maktab_maslahatchisi_secret_key'
socketio = SocketIO(app)

# Ma'lumotlarni vaqtinchalik saqlash uchun ro'yxatlar (baza o'rnida)
videolar = [
    {"id": 1, "nomi": "1-Dars: Kirish", "url": "https://youtube.com"},
    {"id": 2, "nomi": "2-Dars: Maslahatlar", "url": "https://youtube.com"}
]
reklamalar = []
shikoyatlar = []

# --- SAHIFALAR URLLARI ---

# 1. Bosh sahifa va Videolar
@app.route('/')
def index():
    return render_template('index.html', videolar=videolar, reklamalar=reklamalar)

# 2. Onlayn Chat
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Chat xabarlarini real-time uzatish
@socketio.on('message')
def handle_message(msg):
    print('Xabar: ' + msg)
    send(msg, broadcast=True)

# 3. Reklama sahifasi
@app.route('/reklama', methods=['GET', 'POST'])
def reklama():
    if request.method == 'POST':
        nomi = request.form.get('nomi')
        link = request.form.get('link')
        reklamalar.append({"nomi": nomi, "link": link})
        flash("Reklama muvaffaqiyatli qo'shildi!")
        return redirect(url_for('index'))
    return render_template('reklama.html')

# 4. Shikoyat sahifasi
@app.route('/shikoyat', methods=['GET', 'POST'])
def shikoyat():
    if request.method == 'POST':
        ism = request.form.get('ism')
        matn = request.form.get('matn')
        shikoyatlar.append({"ism": ism, "matn": matn})
        flash("Shikoyatingiz qabul qilindi va ko'rib chiqiladi.")
        return redirect(url_for('index'))
    return render_template('shikoyat.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
