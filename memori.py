#HUBUNGKAN MODUL PYQT5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QButtonGroup, QGroupBox, QRadioButton, QPushButton)
from random import shuffle, randint

#OBJEK JENDELA DAN APLIKASI
APLIKASI = QApplication([])
JENDELA = QWidget()
JENDELA.setFixedSize(200, 250)

#OBJEK WIDGET
SOAL = QLabel('Berapa Tinggi Kura Kura?')
R_BTN1 = QRadioButton('170cm')
R_BTN2 = QRadioButton('70cm')
R_BTN3 = QRadioButton('100cm')
R_BTN4 = QRadioButton('10cm')
GRUP_R_BTN = QGroupBox('Pilihan Jawaban')
TOMBOL = QPushButton('Jawab!')
GRUP_HASIL = QGroupBox('Hasilnya!!!')
BENARSALAH = QLabel('Benar /  Salah')
JAWABAN_BENAR = QLabel('Ini Jawaban Benarnya')

#GRUP TATA LETAK GRUP_HASIL
garis_v_grup_hasil = QVBoxLayout()
garis_v_grup_hasil.addWidget(BENARSALAH)
garis_v_grup_hasil.addWidget(JAWABAN_BENAR, alignment=Qt.AlignHCenter)
GRUP_HASIL.setLayout(garis_v_grup_hasil)

#TATA LETAK GRUP_R_BTN
garis_v_grup_rbtn = QVBoxLayout()
garis_h1_grup_rbtn = QHBoxLayout()
garis_h2_grup_rbtn = QHBoxLayout()
garis_h1_grup_rbtn.addWidget(R_BTN1)
garis_h1_grup_rbtn.addWidget(R_BTN2)
garis_h2_grup_rbtn.addWidget(R_BTN3)
garis_h2_grup_rbtn.addWidget(R_BTN4)
garis_v_grup_rbtn.addLayout(garis_h1_grup_rbtn)
garis_v_grup_rbtn.addLayout(garis_h2_grup_rbtn)
GRUP_R_BTN.setLayout(garis_v_grup_rbtn)

#TATA LETAK JENDELA
garis_v_jendela = QVBoxLayout()
garis_v_jendela.addWidget(SOAL, alignment=Qt.AlignHCenter)
garis_v_jendela.addWidget(GRUP_R_BTN)
garis_v_jendela.addWidget(GRUP_HASIL)
garis_v_jendela.addWidget(TOMBOL)
JENDELA.setLayout(garis_v_jendela)

#KELOMPOKKAN TOMBOL RADIO
kelompok_radio = QButtonGroup()
kelompok_radio.addButton(R_BTN1)
kelompok_radio.addButton(R_BTN2)
kelompok_radio.addButton(R_BTN3)
kelompok_radio.addButton(R_BTN4)

#MEMBUAT KELAS PERTANYAAN
class Question:
    def __init__(self, soal, benar, salah1, salah2, salah3):
        self.soal = soal
        self.benar = benar
        self.salah1 = salah1
        self.salah2 = salah2
        self.salah3 = salah3

#MEMBUAT OBJEK SOAL
LIST_SOAL = list()

LIST_SOAL.append(Question('HARI INI SAYA PAKAI BAJU WARNA?', 'BIRU', 'HITAM', 'PINK', 'HIJAU'))
LIST_SOAL.append(Question('HARI INI SAYA MAKAN?', 'NASI', 'KENTANG', 'RENDANG', 'GORENGAN'))
LIST_SOAL.append(Question('HARI INI SAYA MINUM?', 'SODA', 'AIR', 'WATER', 'DARAH'))
LIST_SOAL.append(Question('HARI INI SAYA MAIN?', 'LAPTOP', 'HP', 'IPAD', 'PS'))
LIST_SOAL.append(Question('HARI INI SAYA OLAHRAGA?', 'BERENANG', 'LARI', 'JOGGING', 'FUTSAL'))

JENDELA.total_soal = 0
JENDELA.total_benar = 0
JENDELA.total_salah = 0
#EVENT HANDLING
def show_result():
    GRUP_R_BTN.hide()
    GRUP_HASIL.show()
    TOMBOL.setText('SOAL BERIKUTNYA')

def show_question():
    GRUP_R_BTN.show()
    GRUP_HASIL.hide()
    TOMBOL.setText('JAWAB')
    #MERESET TOMBOL RADIO
    kelompok_radio.setExclusive(False)
    R_BTN1.setChecked(False)
    R_BTN2.setChecked(False)
    R_BTN3.setChecked(False)
    R_BTN4.setChecked(False)
    kelompok_radio.setExclusive(True)

def klik_ok():
    if TOMBOL.text() == 'JAWAB':
        #
        check_answer()
    else:
        #
        next_question()

LIST_RADIO = [R_BTN1, R_BTN2, R_BTN3, R_BTN4]
def ask(objek_soal):
    shuffle(LIST_RADIO) #MENGACAK ISI DARI LIST_RADIO
    LIST_RADIO[0].setText(objek_soal.benar)
    LIST_RADIO[1].setText(objek_soal.salah1)
    LIST_RADIO[2].setText(objek_soal.salah2)
    LIST_RADIO[3].setText(objek_soal.salah3)
    SOAL.setText(objek_soal.soal)
    JAWABAN_BENAR.setText(objek_soal.benar)
    show_question()

def check_answer():
    if LIST_RADIO[0].isChecked():
        BENARSALAH.setText('BENAR')
        JENDELA.total_benar += 1
    else:
        BENARSALAH.setText('SALAH')
        JENDELA.total_salah += 1
    show_result()
    print('================')
    print('TOTAL BENAR =', JENDELA.total_benar)
    print('TOTAL SALAH =', JENDELA.total_salah)
    print('PERSENTASE =', (JENDELA.total_benar / JENDELA.total_soal) * 100, '%')
    print('================')

JENDELA.index_saat_ini = -1
def next_question():
    JENDELA.index_saat_ini += 1
    if JENDELA.index_saat_ini == len(LIST_SOAL):
        JENDELA.index_saat_ini = 0
    ask(LIST_SOAL[JENDELA.index_saat_ini])

def next_question():
    JENDELA.total_soal += 1
    print('================')
    print('TOTAL SOAL =', JENDELA.total_soal)
    print('================')
    index_saat_ini = randint(0, len(LIST_SOAL)-1)
    ask(LIST_SOAL[index_saat_ini])
    
next_question()

TOMBOL.clicked.connect(klik_ok)

#TAMPILKAN JENDELA DAN JALANKAN APLIKASI
JENDELA.show()
APLIKASI.exec_()
