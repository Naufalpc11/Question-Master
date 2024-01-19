from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import*
import functools
import os
import sys
import json

class FullScreenApp(QWidget):
    def __init__(self, data):
        super().__init__()
    
        self.mode = "main_menu"
        self.setWindowState(Qt.WindowFullScreen)
        self.mediaPlayer = QMediaPlayer(self)
        self.mediaPlayer.mediaStatusChanged.connect(self.songFinished)
        self.addMusicToPlaylist('D:\Semester 1\PKTI nih Boss\sound\Pheme.mp3')  # Ganti dengan path lagu Anda
        self.playlist.setCurrentIndex(0)
        self.playMusic()   

        self.quiz_data = self.load_quiz_data()  # Load data from JSON
        self.current_question = 1  # Current question number
        self.score = 0 
        self.total_questions = 20 
    
        self.initUI()
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            return True  # Menghentikan aksi keyboard
        return super().eventFilter(obj, event)
   
    def load_quiz_data(self):
        
        with open('D:\Semester 1\PKTI nih Boss\Pertanyaan.json') as file:
            data = json.load(file)
        return data
    def klik(self):
        QSound.play('D:\Semester 1\PKTI nih Boss\sound\klik.wav')

    def initUI(self):
        self.setWindowTitle('YukMabar')
        self.setWindowIcon(QIcon('Gambar/Icon.jpg'))
        self.showFullScreen()

        Backrground = QPixmap('D:\Semester 1\PKTI nih Boss\Background\depan.jpg') 
        self.background_1 = QLabel(self)
        self.background_1.setPixmap(Backrground)
        self.background_1.setGeometry(0, 0, self.width(), self.height())  
        self.background_1.show()
        

        JudulRek = QPixmap('D:\Semester 1\PKTI nih Boss\Gambar\Yuk Mabar.png')
        self.judullll = QLabel(self)
        self.judullll.setPixmap(JudulRek)
        self.judullll.setAlignment(Qt.AlignCenter)
        self.judullll.show()

        self.loding = QLabel("Memuat...", self)
        self.loding.setFont(QFont("Mabook", 30))
        self.loding.setStyleSheet("color: white")
        self.loding.setGeometry(850, 800, 200, 80)
        self.loding.show()

        self.lodingnyamas = QTimer(self)
        self.lodingnyamas.setSingleShot(True)
        self.lodingnyamas.timeout.connect(self.lalala)
        self.lodingnyamas.start(4000)

        self.keluar = QPushButton('Keluar',self)
        self.keluar.setGeometry(80, 980, 300, 80)
        self.keluar.setFont(QFont('MaBook', 30))
        self.keluar.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.keluar.clicked.connect(self.klik)
        self.keluar.clicked.connect(self.keluarco)
        self.keluar.installEventFilter(self)
        self.keluar.show()
    
    def addMusicToPlaylist(self, path):
        self.playlist = QMediaPlaylist(self.mediaPlayer)
        media_url = QUrl.fromLocalFile(path)
        self.playlist.addMedia(QMediaContent(media_url))
        self.mediaPlayer.setPlaylist(self.playlist)

    def playMusic(self):
        self.mediaPlayer.play()

    def stopMusic(self):
        self.mediaPlayer.stop()

    def songFinished(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.playlist.setCurrentIndex(0)
            self.mediaPlayer.play()
    def keluarco(self):
        reply = QMessageBox.question(self, 'Peringatan',
            'Apakah Anda yakin ingin keluar dari YukMabar?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QApplication.instance().quit()

    def lalala(self):
        
        self.loding.deleteLater()
        self.lanjut = QPushButton('Mulai', self)
        self.lanjut.setGeometry(800, 800, 300, 80)
        self.lanjut.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.lanjut.setFont(QFont("MaBook", 30))
        self.lanjut.clicked.connect(self.klik)
        self.lanjut.clicked.connect(self.Menu)
        self.lanjut.installEventFilter(self)
        self.lanjut.show()

    def Menu(self):
        
        self.lanjut.hide()
        self.keluar.hide()
        self.judullll.hide()
        self.background_1.hide()

        Backrground = QPixmap('D:\Semester 1\PKTI nih Boss\Background\menu.jpg') 
        self.background_2 = QLabel(self)
        self.background_2.setPixmap(Backrground)
        self.background_2.setGeometry(0, 0, self.width(), self.height())  
        self.background_2.show()

        self.car = QLabel(self)
        oooo = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\car.png') 
        self.car.setPixmap(oooo)
        self.car.move(300, 400)
        self.car.show()
        self.animation = QPropertyAnimation(self.car, b"geometry")
        self.animation.setDuration(10000)  # Durasi animasi dalam milidetik
        self.animation.setStartValue(QRect(0, 840, 300, 109))  # Nilai awal (posisi kiri)
        self.animation.setEndValue(QRect(1900, 840, 3000, 109))
        self.animation.setLoopCount(-1)
        self.startAnimation()

        self.opolek = QLabel(self)
        ooo = QPixmap('D:\Semester 1\PKTI nih Boss\Background\p.png') 
        self.opolek.setPixmap(ooo)
        self.opolek.move(-40, 0)
        self.opolek.adjustSize()
        self.opolek.show()

        self.Judulle = QLabel('Kelas\nBerapa Kamu?', self)
        self.Judulle.setFont(QFont('MaBook', 30))
        self.Judulle.setStyleSheet("color: white")
        self.Judulle.setGeometry(50, 50, 300, 130)
        self.Judulle.adjustSize()
        self.Judulle.show()

        self.achivment = QPushButton('Achievement',self)
        self.achivment.setGeometry(50, 600, 300, 80)
        self.achivment.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.achivment.setFont(QFont('MaBook', 25))
        self.achivment.clicked.connect(self.klik)
        self.achivment.clicked.connect(self.nampilin_achievement)
        self.achivment.installEventFilter(self)
        self.achivment.show()

        self.About = QPushButton('Cara Bermain',self)
        self.About.setGeometry(50, 700, 300, 80)
        self.About.setFont(QFont('MaBook', 27))
        self.About.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.About.clicked.connect(self.klik)
        self.About.clicked.connect(self.hapus)
        self.About.installEventFilter(self)
        self.About.show()

        self.kembali = QPushButton('Kembali',self)
        self.kembali.setGeometry(50, 800, 300, 80)
        self.kembali.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.kembali.setFont(QFont('MaBook', 30))
        self.kembali.clicked.connect(self.klik)
        self.kembali.clicked.connect(self.hapus)
        self.kembali.installEventFilter(self)
        self.kembali.show()
        
        pixmap = QPixmap('D:\Semester 1\PKTI nih Boss\Gambar\Yuk Mabar.png')
        pixmap = pixmap.scaled(300, 139)
        self.lab = QLabel(self)
        self.lab.setPixmap(pixmap)
        self.lab.setGeometry(50, 900, 300, 139)
        self.lab.show()

        self.checkboxes = []

        for i in range(6):
            checkbox = QCheckBox(f'Kelas {i+1}', self)
            checkbox.setStyleSheet("font-size: 40px; color:white")
            checkbox.setFont(QFont("MaBook"))
            checkbox.setIconSize(QSize(40,40))
            checkbox.setGeometry(50, 190 + i * 60, 200, 50)
            checkbox.stateChanged.connect(self.klik)
            checkbox.stateChanged.connect(functools.partial(self.singleCheckbox, i))
            checkbox.installEventFilter(self)
            self.checkboxes.append(checkbox)
        
        for checkbox in self.checkboxes:
            checkbox.show()
    def nampilin_achievement(self):
        self.achivment.hide()
        self.About.hide()
        self.kembali.hide()
        self.lab.hide()
        self.opolek.hide()
        self.Judulle.hide()
        if self.mode == "main_menu":
            self.clearButtons()
        else:
            self.mode = "main_menu"
            for checkbox in self.checkboxes:
                checkbox.setChecked(False)
                checkbox.setEnabled(True)
            self.clearButtons()

        for checkbox in self.checkboxes:
            checkbox.setVisible(False)

        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(210, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.achievement1 = QPushButton('', self)
        self.achievement1.setGeometry(290, 150, 600, 150)
        self.achievement1.setStyleSheet("background-image: url('Widget/achievement1blm.jpg'); background-position: center; background-repeat: no-repeat;opacity: 0.1;")
        self.achievement1.setEnabled(False)
        self.achievement1.installEventFilter(self)
        self.achievement1.show()
        self.achievement2 = QPushButton('', self)
        self.achievement2.setGeometry(990, 150, 600, 150)
        self.achievement2.setStyleSheet("background-image: url('Widget/achievement2blm.jpg'); background-position: center; background-repeat: no-repeat;opacity: 0.1;")
        self.achievement2.setEnabled(False)
        self.achievement2.installEventFilter(self)
        self.achievement2.show()
        self.achievement3 = QPushButton('', self)
        self.achievement3.setGeometry(290, 330, 600, 150)
        self.achievement3.setStyleSheet("background-image: url('Widget/achievement3blm.jpg'); background-position: center; background-repeat: no-repeat;")
        self.achievement3.setEnabled(False)
        self.achievement3.installEventFilter(self)
        self.achievement3.show()
        self.achievement4 = QPushButton('', self)
        self.achievement4.setGeometry(990, 330, 600, 150)
        self.achievement4.setStyleSheet("background-image: url('Widget/achievement4blm.jpg'); background-position: center; background-repeat: no-repeat;")
        self.achievement4.setEnabled(False)
        self.achievement4.installEventFilter(self)
        self.achievement4.show()
        self.achievement5 = QPushButton('', self)
        self.achievement5.setGeometry(290, 510, 600, 150)
        self.achievement5.setStyleSheet("background-image: url('Widget/achievement5blm.jpg'); background-position: center; background-repeat: no-repeat;")
        self.achievement5.setEnabled(False)
        self.achievement5.installEventFilter(self)
        self.achievement5.show()
        self.achievement6 = QPushButton('', self)
        self.achievement6.setGeometry(990, 510, 600, 150)
        self.achievement6.setStyleSheet("background-image: url('Widget/achievement6blm.jpg'); background-position: center; background-repeat: no-repeat;")
        self.achievement6.setEnabled(False)
        self.achievement6.installEventFilter(self)
        self.achievement6.show()
        self.achievement7 = QPushButton('', self)
        self.achievement7.setGeometry(290, 690, 600, 150)
        self.achievement7.setStyleSheet("background-image: url('Widget/achievement7blm.jpg'); background-position: center; background-repeat: no-repeat;")
        self.achievement7.setEnabled(False)
        self.achievement7.installEventFilter(self)
        self.achievement7.show()
        self.achievement8 = QPushButton('', self)
        self.achievement8.setGeometry(990, 690, 600, 150)
        self.achievement8.setStyleSheet("background-image: url('Widget/achievement8blm.jpg'); background-position: center; background-repeat: no-repeat;")
        self.achievement8.setEnabled(False)
        self.achievement8.installEventFilter(self)
        self.achievement8.show()
        self.kem = QPushButton('Kembali',self)
        self.kem.setGeometry(780, 900, 300, 80)
        self.kem.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.kem.setFont(QFont('MaBook', 30))
        self.kem.clicked.connect(self.klik)
        self.kem.clicked.connect(self.menucoy)
        self.kem.installEventFilter(self)
        self.kem.show()
        file_path = 'D:\Semester 1\PKTI nih Boss\skor.json'
        total_score = 0
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as file:
                data = json.load(file)
                class_scores = ['scoresk4', 'scoresk5', 'scoresk6']  
                for class_score in class_scores:
                    if class_score in data:
                        scores = data[class_score]
                        total_score += sum(score['score'] for score in scores)
    
                    if total_score >= 100:
                        self.achievement1.setStyleSheet("background-image: url('Widget/achievement1.jpg'); background-position: center; background-repeat: no-repeat;")
                    if total_score >= 500:
                        self.achievement2.setStyleSheet("background-image: url('Widget/achievement2.jpg'); background-position: center; background-repeat: no-repeat;")
                    if total_score >= 1000:
                        self.achievement3.setStyleSheet("background-image: url('Widget/achievement3.jpg'); background-position: center; background-repeat: no-repeat;")
                    if total_score >= 2000:
                        self.achievement4.setStyleSheet("background-image: url('Widget/achievement4.jpg'); background-position: center; background-repeat: no-repeat;")
                    if total_score >= 5000:
                        self.achievement5.setStyleSheet("background-image: url('Widget/achievement5.jpg'); background-position: center; background-repeat: no-repeat;")
                    if total_score >= 10000:
                        self.achievement6.setStyleSheet("background-image: url('Widget/achievement6.jpg'); background-position: center; background-repeat: no-repeat;")
                    if total_score >= 20000:
                        self.achievement7.setStyleSheet("background-image: url('Widget/achievement7.jpg'); background-position: center; background-repeat: no-repeat;")
                    if total_score >= 50000:
                        self.achievement8.setStyleSheet("background-image: url('Widget/achievement8.jpg'); background-position: center; background-repeat: no-repeat;")
        self.totalscorelabel = QLabel(f'Poin Kamu{total_score}' ,self)
        self.totalscorelabel.show()
    
    def menucoy(self):
        self.backgroundsoal.hide()
        self.achievement1.hide()
        self.achievement2.hide()
        self.achievement3.hide()
        self.achievement4.hide()
        self.achievement5.hide()
        self.achievement6.hide()
        self.achievement7.hide()
        self.achievement8.hide()
        self.kem.hide()
        self.Menu()
    def clearButtons(self):
        buttons_to_clear = [
            'judulpelajaran1', 'judulpelajaran2', 'judulpelajaran3'
            'tem14', 'tem24', 'tem34', 'tem44', 'tem54', 'tem64', 'tem74', 'tem84', 'judulpelajaran4', 
            'tem15', 'tem25', 'tem35', 'tem45', 'tem55', 'tem65', 'tem75', 'tem85', 'judulpelajaran5',
            'tem16', 'tem26', 'tem36', 'tem46', 'tem56', 'tem66', 'tem76', 'tem86', 'judulpelajaran6',
        ]

        for btn_name in buttons_to_clear:
            button = getattr(self, btn_name, None)
            if button is not None:
                button.hide()

    def startAnimation(self):
            self.animation.start()

    def restartAnimation(self):
        if self.comings.direction() == QPropertyAnimation.Forward:
            self.comings.setDirection(QPropertyAnimation.Backward)
        else:
            self.comings.setDirection(QPropertyAnimation.Forward)
        self.comings.start()
    def functionForCheckbox1(self):
       
        self.clearButtons()
        
        self.judulpelajaran1 = QPushButton('', self)
        self.judulpelajaran1.setGeometry(750, 350, 700, 300)
        self.judulpelajaran1.setStyleSheet("background-image: url('Widget/ComingSoon.jpg'); background-position: center; background-repeat: no-repeat;")
        self.judulpelajaran1.setEnabled(False)
        self.comings = QPropertyAnimation(self.judulpelajaran1, b"geometry")
        self.comings.setDuration(1000)  
        self.comings.setStartValue(QRect(750, 350, 700, 300))
        self.comings.installEventFilter(self)
        self.comings.setEndValue(QRect(750, 450, 700, 300))
        self.comings.setDirection(QPropertyAnimation.Backward) 
        self.comings.finished.connect(self.restartAnimation)

        self.judulpelajaran1.show()
        self.restartAnimation()
        self.startAnimation()
        
    def functionForCheckbox2(self):
        self.clearButtons()
        self.judulpelajaran2 = QPushButton('', self)
        self.judulpelajaran2.setGeometry(750, 350, 700, 300)
        self.judulpelajaran2.setStyleSheet("background-image: url('Widget/ComingSoon.jpg'); background-position: center; background-repeat: no-repeat;")
        self.judulpelajaran2.setEnabled(False)
        self.comings = QPropertyAnimation(self.judulpelajaran2, b"geometry")
        self.comings.setDuration(1000)  
        self.comings.setStartValue(QRect(750, 350, 700, 300))
        self.comings.installEventFilter(self)
        self.comings.setEndValue(QRect(750, 450, 700, 300))
        self.comings.setDirection(QPropertyAnimation.Backward) 
        self.comings.finished.connect(self.restartAnimation)

        self.restartAnimation()
        self.judulpelajaran2.show()
        self.startAnimation()

    def functionForCheckbox3(self):
        self.clearButtons()
        self.judulpelajaran3 = QPushButton('', self)
        self.judulpelajaran3.setGeometry(750, 350, 700, 300)
        self.judulpelajaran3.setStyleSheet("background-image: url('Widget/ComingSoon.jpg'); background-position: center; background-repeat: no-repeat;")
        self.judulpelajaran3.setEnabled(False)
        self.comings = QPropertyAnimation(self.judulpelajaran3, b"geometry")
        self.comings.setDuration(1000)  
        self.comings.setStartValue(QRect(750, 350, 700, 300))
        self.comings.installEventFilter(self)
        self.comings.setEndValue(QRect(750, 450, 700, 300))
        self.comings.setDirection(QPropertyAnimation.Backward) 
        self.comings.finished.connect(self.restartAnimation)

        self.restartAnimation()
        self.judulpelajaran3.show()
        self.startAnimation()

    def functionForCheckbox4(self):
        self.clearButtons()

        self.tem14 = QPushButton('', self)
        self.tem14.setGeometry(850, 250, 300, 200)
        self.tem14.setStyleSheet("background-image: url('Widget/tomtem1.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem14.clicked.connect(self.st14)
        self.tem14.clicked.connect(self.klik)
        self.tem14.installEventFilter(self)
        self.tem14.show()
        self.tem24 = QPushButton('', self)
        self.tem24.setGeometry(1250, 250, 300, 200)
        self.tem24.setStyleSheet("background-image: url('Widget/tomtem2.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem24.clicked.connect(self.st24)
        self.tem24.clicked.connect(self.klik)
        self.tem24.installEventFilter(self)
        self.tem24.show()
        self.tem34 = QPushButton('', self)
        self.tem34.setGeometry(850, 500, 300, 200)
        self.tem34.setStyleSheet("background-image: url('Widget/tomtem3.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem34.clicked.connect(self.st34)
        self.tem34.clicked.connect(self.klik)
        self.tem34.installEventFilter(self)
        self.tem34.show()
        self.tem44 = QPushButton('', self)
        self.tem44.setGeometry(1250, 500, 300, 200)
        self.tem44.setStyleSheet("background-image: url('Widget/tomtem4.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem44.clicked.connect(self.st44)
        self.tem44.clicked.connect(self.klik)
        self.tem44.installEventFilter(self)
        self.tem44.show()
        self.judulpelajaran4 = QPushButton('', self)
        self.judulpelajaran4.setStyleSheet("background-image: url('Widget/Judul Pelajaran.jpg'); background-position: center; background-repeat: no-repeat;")
        self.judulpelajaran4.setGeometry(850, 800, 700, 80)
        self.judulpelajaran4.setFont(QFont('MaBook', 40))
        self.judulpelajaran4.show()
    def st14(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 120, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema1_kelas4)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema1_kelas4()
        self.p4()
    def perlihatkan_soal_tema1_kelas4(self):
        question_data = self.quiz_data["kelas"]["4"]["tema1"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema1_kelas4(self):
        correct_answer = self.quiz_data["kelas"]["4"]["tema1"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema1_kelas4()
        else:
            self.tampilkan_hasil_tema1_kelas4()
    def tampilkan_hasil_tema1_kelas4(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.k.installEventFilter(self)
        self.save_score_to_json4(self.score)
        self.k.show()
    def balik_ke_menu_coks(self):
        self.score_label.hide()
        self.k.hide()
        self.backgroundsoal.hide()
        self.Menu()
########^Tema 1 kelas 4^#######################################################
    def st24(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 120, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema2_kelas4)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema2_kelas4()
        self.p4()
    def perlihatkan_soal_tema2_kelas4(self):
        question_data = self.quiz_data["kelas"]["4"]["tema2"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema2_kelas4(self):
        correct_answer = self.quiz_data["kelas"]["4"]["tema2"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema2_kelas4()
        else:
            self.tampilkan_hasil_tema2_kelas4()
    def tampilkan_hasil_tema2_kelas4(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.k.installEventFilter(self)
        self.save_score_to_json4(self.score)
        self.k.show()
########^Tema 2 kelas 4^#######################################################
    def st34(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 120, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema3_kelas4)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema3_kelas4()
        self.p4()
    def perlihatkan_soal_tema3_kelas4(self):
        question_data = self.quiz_data["kelas"]["4"]["tema3"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema3_kelas4(self):
        correct_answer = self.quiz_data["kelas"]["4"]["tema3"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema3_kelas4()
        else:
            self.tampilkan_hasil_tema3_kelas4()
    def tampilkan_hasil_tema3_kelas4(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.k.installEventFilter(self)
        self.save_score_to_json4(self.score)
        self.k.show()
########^Tema 3 kelas 4^#######################################################
    def st44(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 120, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema4_kelas4)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema4_kelas4()
        self.p4()
    def perlihatkan_soal_tema4_kelas4(self):
        question_data = self.quiz_data["kelas"]["4"]["tema4"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema4_kelas4(self):
        correct_answer = self.quiz_data["kelas"]["4"]["tema4"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema4_kelas4()
        else:
            self.tampilkan_hasil_tema4_kelas4()
    def tampilkan_hasil_tema4_kelas4(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.k.installEventFilter(self)
        self.save_score_to_json4(self.score)
        self.k.show()
########^Tema 4 kelas 4^#######################################################
    def functionForCheckbox5(self):
        self.clearButtons()
        
        self.tem15 = QPushButton('', self)
        self.tem15.setGeometry(850, 250, 300, 200)
        self.tem15.setStyleSheet("background-image: url('Widget/tomtem1.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem15.clicked.connect(self.st15)
        self.tem15.clicked.connect(self.klik)
        self.tem15.installEventFilter(self)
        self.tem15.show()
        self.tem25 = QPushButton('', self)
        self.tem25.setGeometry(1250, 250, 300, 200)
        self.tem25.setStyleSheet("background-image: url('Widget/tomtem2.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem25.clicked.connect(self.st25)
        self.tem25.clicked.connect(self.klik)
        self.tem25.installEventFilter(self)
        self.tem25.show()
        self.tem35 = QPushButton('', self)
        self.tem35.setGeometry(850, 500, 300, 200)
        self.tem35.setStyleSheet("background-image: url('Widget/tomtem3.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem35.clicked.connect(self.st35)
        self.tem35.clicked.connect(self.klik)
        self.tem35.installEventFilter(self)
        self.tem35.show()
        self.tem45 = QPushButton('', self)
        self.tem45.setGeometry(1250, 500, 300, 200)
        self.tem45.setStyleSheet("background-image: url('Widget/tomtem4.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem45.clicked.connect(self.st45)
        self.tem45.clicked.connect(self.klik)
        self.tem45.installEventFilter(self)
        self.tem45.show()
        self.judulpelajaran5 = QPushButton('', self)
        self.judulpelajaran5.setStyleSheet("background-image: url('Widget/Judul Pelajaran.jpg'); background-position: center; background-repeat: no-repeat;")
        self.judulpelajaran5.setGeometry(850, 800, 700, 80)
        self.judulpelajaran5.setFont(QFont('MaBook', 40))
        self.judulpelajaran5.show()

        self.startAnimation()
    def st15(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 120, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema1_kelas5)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema1_kelas5()
        self.p5()
    def perlihatkan_soal_tema1_kelas5(self):
        question_data = self.quiz_data["kelas"]["5"]["tema1"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema1_kelas5(self):
        correct_answer = self.quiz_data["kelas"]["5"]["tema1"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema1_kelas5()
        else:
            self.tampilkan_hasil_tema1_kelas5()
    def tampilkan_hasil_tema1_kelas5(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.k.installEventFilter(self)
        self.save_score_to_json5(self.score)
        self.k.show()
########^Tema 1 kelas 5^#######################################################
    def st25(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 100, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema2_kelas5)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema2_kelas5()
        self.p5()
    def perlihatkan_soal_tema2_kelas5(self):
        question_data = self.quiz_data["kelas"]["5"]["tema2"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema2_kelas5(self):
        correct_answer = self.quiz_data["kelas"]["5"]["tema2"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema2_kelas5()
        else:
            self.tampilkan_hasil_tema2_kelas5()
    def tampilkan_hasil_tema2_kelas5(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.k.installEventFilter(self)
        self.save_score_to_json5(self.score)
        self.k.show()
########^Tema 2 kelas 5^#######################################################
    def st35(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 100, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema3_kelas5)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema3_kelas5()
        self.p5()
    def perlihatkan_soal_tema3_kelas5(self):
        question_data = self.quiz_data["kelas"]["5"]["tema3"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema3_kelas5(self):
        correct_answer = self.quiz_data["kelas"]["5"]["tema3"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema3_kelas5()
        else:
            self.tampilkan_hasil_tema3_kelas5()
    def tampilkan_hasil_tema3_kelas5(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.k.installEventFilter(self)
        self.save_score_to_json5(self.score)
        self.k.show()
########^Tema 3 kelas 5^#######################################################
    def st45(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 100, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema4_kelas5)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema4_kelas5()
        self.p5()
    def perlihatkan_soal_tema4_kelas5(self):
        question_data = self.quiz_data["kelas"]["5"]["tema4"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema4_kelas5(self):
        correct_answer = self.quiz_data["kelas"]["5"]["tema4"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema4_kelas5()
        else:
            self.tampilkan_hasil_tema4_kelas5()
    def tampilkan_hasil_tema4_kelas5(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.k.installEventFilter(self)
        self.save_score_to_json5(self.score)
        self.k.show()
########^Tema 4 kelas 5^#######################################################
    def functionForCheckbox6(self):
        self.clearButtons()

        self.tem16 = QPushButton('', self)
        self.tem16.setGeometry(850, 250, 300, 200)
        self.tem16.setStyleSheet("background-image: url('Widget/tomtem1.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem16.clicked.connect(self.st16)
        self.tem16.clicked.connect(self.klik)
        self.tem16.installEventFilter(self)
        self.tem16.show()
        self.tem26 = QPushButton('', self)
        self.tem26.setGeometry(1250, 250, 300, 200)
        self.tem26.setStyleSheet("background-image: url('Widget/tomtem2.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem26.clicked.connect(self.st26)
        self.tem26.clicked.connect(self.klik)
        self.tem26.installEventFilter(self)
        self.tem26.show()
        self.tem36 = QPushButton('', self)
        self.tem36.setGeometry(850, 500, 300, 200)
        self.tem36.setStyleSheet("background-image: url('Widget/tomtem3.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem36.clicked.connect(self.st36)
        self.tem36.clicked.connect(self.klik)
        self.tem36.installEventFilter(self)
        self.tem36.show()
        self.tem46 = QPushButton('', self)
        self.tem46.setGeometry(1250, 500, 300, 200)
        self.tem46.setStyleSheet("background-image: url('Widget/tomtem4.jpg'); background-position: center; background-repeat: no-repeat;")
        self.tem46.clicked.connect(self.st46)
        self.tem46.clicked.connect(self.klik)
        self.tem46.installEventFilter(self)
        self.tem46.show()
        self.judulpelajaran6 = QPushButton('', self)
        self.judulpelajaran6.setStyleSheet("background-image: url('Widget/Judul Pelajaran.jpg'); background-position: center; background-repeat: no-repeat;")
        self.judulpelajaran6.setGeometry(850, 800, 700, 80)
        self.judulpelajaran6.setFont(QFont('MaBook', 40))
        self.judulpelajaran6.show()

        self.startAnimation()
    def st16(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 100, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema1_kelas6)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema1_kelas6()
        self.p6()
    def perlihatkan_soal_tema1_kelas6(self):
        question_data = self.quiz_data["kelas"]["6"]["tema1"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema1_kelas6(self):
        correct_answer = self.quiz_data["kelas"]["6"]["tema1"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema1_kelas6()
        else:
            self.tampilkan_hasil_tema1_kelas6()
    def tampilkan_hasil_tema1_kelas6(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.save_score_to_json6(self.score)
        self.k.installEventFilter(self)
        self.k.show()
########^Tema 1 kelas 6^#######################################################
    def st26(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 100, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema2_kelas6)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema2_kelas6()
        self.p6()
    def perlihatkan_soal_tema2_kelas6(self):
        question_data = self.quiz_data["kelas"]["6"]["tema2"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema2_kelas6(self):
        correct_answer = self.quiz_data["kelas"]["6"]["tema2"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema2_kelas6()
        else:
            self.tampilkan_hasil_tema2_kelas6()
    def tampilkan_hasil_tema2_kelas6(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.save_score_to_json6(self.score)
        self.k.installEventFilter(self)
        self.k.show()
########^Tema 2 kelas 6^#######################################################
    def st36(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 100, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema3_kelas6)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema3_kelas6()
        self.p6()
    def perlihatkan_soal_tema3_kelas6(self):
        question_data = self.quiz_data["kelas"]["6"]["tema3"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema3_kelas6(self):
        correct_answer = self.quiz_data["kelas"]["6"]["tema3"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema3_kelas6()
        else:
            self.tampilkan_hasil_tema3_kelas6()
    def tampilkan_hasil_tema3_kelas6(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()

        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.save_score_to_json6(self.score)
        self.k.installEventFilter(self)
        self.k.show()
########^Tema 3 kelas 6^#######################################################
    def st46(self):
        self.backgroundsoal = QLabel(self)
        soall = QPixmap('D:\Semester 1\PKTI nih Boss\Widget\soall.png') 
        self.backgroundsoal.setPixmap(soall)
        self.backgroundsoal.move(250, 100)
        self.backgroundsoal.adjustSize()
        self.backgroundsoal.show()

        self.question_label = QLabel('Question Text', self)
        self.question_label.setGeometry(300, 200, 1300, 160) 
        self.question_label.setFont(QFont('MaBook', 30))
        
        self.question_label.setStyleSheet("color:white;")
        self.question_label.show()

        self.option_buttons = []
        option_texts = ["Option 1", "Option 2", "Option 3", "Option 4"]  
        for i in range(4):
            button = QRadioButton(option_texts[i], self)
            button.setGeometry(300, 400 + i * 100, 1300, 100)  
            button.setFont(QFont('MaBook', 25))
            button.setStyleSheet("color:white;")
            button.installEventFilter(self)
            button.show()
            self.option_buttons.append(button)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.submit_button.setGeometry(780, 900, 300, 80)
        self.submit_button.setFont(QFont('MaBook', 30)) 
        self.submit_button.clicked.connect(self.cek_jawaban_tema4_kelas6)
        self.submit_button.clicked.connect(self.klik)
        self.submit_button.installEventFilter(self)
        self.submit_button.show()

        self.current_question = 1
        self.perlihatkan_soal_tema4_kelas6()
        self.p6()
    def perlihatkan_soal_tema4_kelas6(self):
        question_data = self.quiz_data["kelas"]["6"]["tema4"]["soal" + str(self.current_question)]
        self.question_label.setText(question_data["pertanyaan"])
        options = question_data["options"]
        for i in range(len(options)):
            self.option_buttons[i].setText(options[i])
    def cek_jawaban_tema4_kelas6(self):
        correct_answer = self.quiz_data["kelas"]["6"]["tema4"]["soal" + str(self.current_question)]["jawaban"]
        selected_answer = ""
        for button in self.option_buttons:
            if button.isChecked():
                selected_answer = button.text()
                break
        if selected_answer == correct_answer:
            self.score += 5
        self.current_question += 1
        if self.current_question <= self.total_questions:
            self.perlihatkan_soal_tema4_kelas6()
        else:
            self.tampilkan_hasil_tema4_kelas6()
    def tampilkan_hasil_tema4_kelas6(self):
        self.question_label.hide()
        for button in self.option_buttons:
            button.hide()
        self.submit_button.hide()

        self.nilai = 100  
        result_message = f"Skor Kamu {self.score} dari {self.nilai}."
        self.score_label = QLabel(result_message, self)
        self.score_label.setGeometry(500, 400, 1000, 100)
        self.score_label.setFont(QFont('MaBook', 50))  
        self.score_label.setStyleSheet("color:white;")
        self.score_label.show()
        
        self.k = QPushButton('Kembali',self)
        self.k.setGeometry(780, 900, 300, 80)
        self.k.setStyleSheet("background-image: url('Widget/tombol.jpg'); background-position: center; background-repeat: no-repeat;")
        self.k.setFont(QFont('MaBook', 30))
        self.k.clicked.connect(self.balik_ke_menu_coks)
        self.k.clicked.connect(self.klik)
        self.k.installEventFilter(self)
        self.save_score_to_json6(self.score)
        self.k.show()
########^Tema 4 kelas 6^#######################################################
######NUTUPCOKS#######
    def p4(self):
        if self.mode == "main_menu":
            self.clearButtons()
        else:
            self.mode = "main_menu"
            for checkbox in self.checkboxes:
                checkbox.setChecked(False)
                checkbox.setEnabled(True)
            self.clearButtons()

        for checkbox in self.checkboxes:
            checkbox.setVisible(False)

        self.Judulle.hide()
        self.achivment.hide()
        self.About.hide()
        self.kembali.hide()
        self.lab.hide()
        self.tem14.hide()
        self.tem24.hide()
        self.tem34.hide()
        self.tem44.hide()
        self.opolek.hide()
    def p5(self):
        if self.mode == "main_menu":
            self.clearButtons()
        else:
            self.mode = "main_menu"
            for checkbox in self.checkboxes:
                checkbox.setChecked(False)
                checkbox.setEnabled(True)
            self.clearButtons()

        for checkbox in self.checkboxes:
            checkbox.setVisible(False)

        self.Judulle.hide()
        self.achivment.hide()
        self.About.hide()
        self.kembali.hide()
        self.lab.hide()
        self.tem15.hide()
        self.tem25.hide()
        self.tem35.hide()
        self.tem45.hide()
        self.opolek.hide()
    def p6(self):
        if self.mode == "main_menu":
            self.clearButtons()
        else:
            self.mode = "main_menu"
            for checkbox in self.checkboxes:
                checkbox.setChecked(False)
                checkbox.setEnabled(True)
            self.clearButtons()

        for checkbox in self.checkboxes:
            checkbox.setVisible(False)

        self.Judulle.hide()
        self.achivment.hide()
        self.About.hide()
        self.kembali.hide()
        self.lab.hide()
        self.tem16.hide()
        self.tem26.hide()
        self.tem36.hide()
        self.tem46.hide()
        self.opolek.hide()
######NUTUPCOKS#######
    def tampilkan_menu_abis_selesai_TJ(self):
        self.score_label.hide()
        self.Menu()
    def save_score_to_json4(self, score):
        file_path = 'D:\Semester 1\PKTI nih Boss\skor.json'

        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            data = {'scoresk4': [{'score': score}]}
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)  
        else:
            with open(file_path, 'r') as file:
                data = json.load(file)

            if 'scoresk4' in data:
                existing_scores = data['scoresk4']
                score_updated = False
                for existing_score in existing_scores:
                    if score > existing_score['score']:
                        existing_score['score'] = score 
                        score_updated = True
                        break

                if not score_updated:
                    data['scoresk4'].append({'score': score})
            else:
                data['scoresk4'] = [{'score': score}]

            with open(file_path, 'w') as file:
              json.dump(data, file, indent=4)

    def save_score_to_json5(self, score):
        file_path = 'D:\Semester 1\PKTI nih Boss\skor.json'

        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            data = {'scoresk5': [{'score': score}]}
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)  
        else:
            with open(file_path, 'r') as file:
                data = json.load(file)

            if 'scoresk5' in data:
                existing_scores = data['scoresk5']
                score_updated = False
                for existing_score in existing_scores:
                    if score > existing_score['score']:
                        existing_score['score'] = score 
                        score_updated = True
                        break

                if not score_updated:
                    data['scoresk5'].append({'score': score})
            else:
                data['scoresk5'] = [{'score': score}]

            with open(file_path, 'w') as file:
              json.dump(data, file, indent=4)
              
    def save_score_to_json6(self, score):
        file_path = 'D:\Semester 1\PKTI nih Boss\skor.json'

        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            data = {'scoresk6': [{'score': score}]}
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)  
        else:
            with open(file_path, 'r') as file:
                data = json.load(file)

            if 'scoresk6' in data:
                existing_scores = data['scoresk6']
                score_updated = False
                for existing_score in existing_scores:
                    if score > existing_score['score']:
                        existing_score['score'] = score 
                        score_updated = True
                        break

                if not score_updated:
                    data['scoresk6'].append({'score': score})
            else:
                data['scoresk6'] = [{'score': score}]

            with open(file_path, 'w') as file:
              json.dump(data, file, indent=4)
    def singleCheckbox(self, index, state):
        functions = [self.functionForCheckbox1, self.functionForCheckbox2, self.functionForCheckbox3,
                     self.functionForCheckbox4, self.functionForCheckbox5, self.functionForCheckbox6]

        if state == 2:
            for i, checkbox in enumerate(self.checkboxes):
                if i != index and checkbox.isChecked():
                    checkbox.setChecked(False) 
            if 0 <= index < len(functions):
                functions[index]()
        else:
            if index == 0:
                self.judulpelajaran1.hide()
            if index == 1:
                self.judulpelajaran2.hide() 
            if index == 2:
                self.judulpelajaran3.hide()
            if index == 3:
                self.tem14.hide()
                self.tem24.hide()
                self.tem34.hide()
                self.tem44.hide()
                
                self.judulpelajaran4.hide()
            if index == 4:
                self.tem15.hide()
                self.tem25.hide()
                self.tem35.hide()
                self.tem45.hide()
                
                self.judulpelajaran5.hide()
            if index == 5:
                self.tem16.hide()
                self.tem26.hide()
                self.tem36.hide()
                self.tem46.hide()
                
                self.judulpelajaran6.hide()
        if self.animation.state() == QAbstractAnimation.Running:
            return 
        else:
            self.startAnimation()
    def hapus(self):

        if self.mode == "main_menu":
            self.clearButtons()
        else:
            self.mode = "main_menu"
            for checkbox in self.checkboxes:
                checkbox.setChecked(False)
                checkbox.setEnabled(True)
            self.clearButtons()

        for checkbox in self.checkboxes:
            checkbox.setVisible(False)

        self.Judulle.hide()
        self.achivment.hide()
        self.About.hide()
        self.kembali.hide()
        self.lab.hide()
        self.initUI()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = FullScreenApp(QMainWindow)
    ex.showFullScreen()
    sys.exit(app.exec_())