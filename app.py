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
chat_xabarlari = [] # Xabarlarni vaqtinchalik saqlash uchun

# Kelgusida foydalanuvchi huquqlarini tekshirish funksiyasi
def get_parent_chat(user, room_id):
    if not user:
        return "Xatolik: Avval tizimga kiring!"
    if user.role == 'student':
        return "Xatolik: Sizda bu suhbatni ko'rish huquqi yo'q!"
    return chat_xabarlari

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
    chat_xabarlari.append(msg)
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
