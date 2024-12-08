import sys

from PyQt6.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt


class Project(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.v = []
        self.f = 0
        self.basket = QWidget()
        self.tab1_layout = QVBoxLayout()

    def initUI(self):
        self.setGeometry(0, 0, 450, 450)
        self.setWindowTitle('Бургер кинг')

        self.layout = QVBoxLayout()

        self.btn = QPushButton('Сделать заказ', self)
        self.btn.setStyleSheet("font-size: 50px")

        self.layout.addWidget(self.btn)
        self.btn.resize(450, 450)

        self.btn.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        self.btn.deleteLater()
        self.btn.setEnabled(False)

        self.tabs = QTabWidget()


        self.burger = QTabWidget()
        self.tab_burger_layout = QVBoxLayout()

        self.tabs.addTab(self.burger, "Бургеры")
        self.burger.setLayout(self.tab_burger_layout)

        self.beef = QWidget()
        self.tab_beef_layout = QVBoxLayout()
        self.tab_beef_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.burger.addTab(self.beef, "Говядина")
        self.beef.setLayout(self.tab_beef_layout)

        self.object_beef_1 = QPushButton("Ангус Сибирский")
        self.tab_beef_layout.addWidget(self.object_beef_1)

        self.object_beef_1.clicked.connect(self.Beef1)
        self.object_beef_1.clicked.connect(self.Basket)

        self.object_beef_2 = QPushButton("Острый Ангус Сибирский")
        self.tab_beef_layout.addWidget(self.object_beef_2)

        self.object_beef_2.clicked.connect(self.Beef2)
        self.object_beef_2.clicked.connect(self.Basket)

        self.object_beef_3 = QPushButton("Ангус Сибирский Двойной")
        self.tab_beef_layout.addWidget(self.object_beef_3)

        self.object_beef_3.clicked.connect(self.Beef3)
        self.object_beef_3.clicked.connect(self.Basket)

        self.object_beef_4 = QPushButton("Ангус Пармеджано")
        self.tab_beef_layout.addWidget(self.object_beef_4)

        self.object_beef_4.clicked.connect(self.Beef4)
        self.object_beef_4.clicked.connect(self.Basket)

        self.object_beef_5 = QPushButton("Ангус Пармеджано Двойной")
        self.tab_beef_layout.addWidget(self.object_beef_5)

        self.object_beef_5.clicked.connect(self.Beef5)
        self.object_beef_5.clicked.connect(self.Basket)

        self.object_beef_6 = QPushButton("Воппер Сибирский")
        self.tab_beef_layout.addWidget(self.object_beef_6)

        self.object_beef_6.clicked.connect(self.Beef6)
        self.object_beef_6.clicked.connect(self.Basket)

        self.object_beef_7 = QPushButton("Острый Воппер Сибирский")
        self.tab_beef_layout.addWidget(self.object_beef_7)

        self.object_beef_7.clicked.connect(self.Beef7)
        self.object_beef_7.clicked.connect(self.Basket)

        self.object_beef_8 = QPushButton("Воппер Сибирский Двойной")
        self.tab_beef_layout.addWidget(self.object_beef_8)

        self.object_beef_8.clicked.connect(self.Beef8)
        self.object_beef_8.clicked.connect(self.Basket)

        self.object_beef_9 = QPushButton("Острый Воппер Сибирский Двойной")
        self.tab_beef_layout.addWidget(self.object_beef_9)

        self.object_beef_9.clicked.connect(self.Beef9)
        self.object_beef_9.clicked.connect(self.Basket)

        self.object_beef_10 = QPushButton("Ангус Сибирский Двойной")
        self.tab_beef_layout.addWidget(self.object_beef_10)

        self.object_beef_10.clicked.connect(self.Beef10)
        self.object_beef_10.clicked.connect(self.Basket)

        self.object_beef_11 = QPushButton("Острый Ангус Сибирский Двойной")
        self.tab_beef_layout.addWidget(self.object_beef_11)

        self.object_beef_11.clicked.connect(self.Beef11)
        self.object_beef_11.clicked.connect(self.Basket)

        self.object_beef_12 = QPushButton("Острый Двойной Воппер С Сыром")
        self.tab_beef_layout.addWidget(self.object_beef_12)

        self.object_beef_12.clicked.connect(self.Beef12)
        self.object_beef_12.clicked.connect(self.Basket)

        self.object_beef_13 = QPushButton("Двойной Воппер")
        self.tab_beef_layout.addWidget(self.object_beef_13)

        self.object_beef_13.clicked.connect(self.Beef13)
        self.object_beef_13.clicked.connect(self.Basket)

        self.object_beef_14 = QPushButton("Двойной Чизбургер Фреш")
        self.tab_beef_layout.addWidget(self.object_beef_14)

        self.object_beef_14.clicked.connect(self.Beef14)
        self.object_beef_14.clicked.connect(self.Basket)

        self.object_beef_15 = QPushButton("Тройной Воппер")
        self.tab_beef_layout.addWidget(self.object_beef_15)

        self.object_beef_15.clicked.connect(self.Beef15)
        self.object_beef_15.clicked.connect(self.Basket)

        self.object_beef_16 = QPushButton("Чизбургер Фреш")
        self.tab_beef_layout.addWidget(self.object_beef_16)

        self.object_beef_16.clicked.connect(self.Beef16)
        self.object_beef_16.clicked.connect(self.Basket)

        self.object_beef_17 = QPushButton("Острый Гамбургер Фреш")
        self.tab_beef_layout.addWidget(self.object_beef_17)

        self.object_beef_17.clicked.connect(self.Beef17)
        self.object_beef_17.clicked.connect(self.Basket)

        self.object_beef_18 = QPushButton("Острый Чизбургер Фреш")
        self.tab_beef_layout.addWidget(self.object_beef_18)

        self.object_beef_18.clicked.connect(self.Beef18)
        self.object_beef_18.clicked.connect(self.Basket)

        self.object_beef_19 = QPushButton("Гамбургер Фреш")
        self.tab_beef_layout.addWidget(self.object_beef_19)

        self.object_beef_19.clicked.connect(self.Beef19)
        self.object_beef_19.clicked.connect(self.Basket)

        self.object_beef_20 = QPushButton("Тройной Чизбургер Фреш")
        self.tab_beef_layout.addWidget(self.object_beef_20)

        self.object_beef_20.clicked.connect(self.Beef20)
        self.object_beef_20.clicked.connect(self.Basket)

        self.object_beef_21 = QPushButton("Острый Тройной Чизбургер Фреш")
        self.tab_beef_layout.addWidget(self.object_beef_21)

        self.object_beef_21.clicked.connect(self.Beef21)
        self.object_beef_21.clicked.connect(self.Basket)

        self.object_beef_22 = QPushButton("Воппер Джуниор")
        self.tab_beef_layout.addWidget(self.object_beef_22)

        self.object_beef_22.clicked.connect(self.Beef22)
        self.object_beef_22.clicked.connect(self.Basket)

        self.object_beef_23 = QPushButton("Чизбургер")
        self.tab_beef_layout.addWidget(self.object_beef_23)

        self.object_beef_23.clicked.connect(self.Beef23)
        self.object_beef_23.clicked.connect(self.Basket)

        self.object_beef_24 = QPushButton("Гамбургер")
        self.tab_beef_layout.addWidget(self.object_beef_24)

        self.object_beef_24.clicked.connect(self.Beef24)
        self.object_beef_24.clicked.connect(self.Basket)

        self.object_beef_25 = QPushButton("Гранд Чиз")
        self.tab_beef_layout.addWidget(self.object_beef_25)

        self.object_beef_25.clicked.connect(self.Beef25)
        self.object_beef_25.clicked.connect(self.Basket)


        self.chicken = QWidget()
        self.tab_chicken_layout = QVBoxLayout()
        self.tab_chicken_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.burger.addTab(self.chicken, "Курица")
        self.chicken.setLayout(self.tab_chicken_layout)

        self.object_chicken_1 = QPushButton("Сибирский Чикен")
        self.tab_chicken_layout.addWidget(self.object_chicken_1)

        self.object_chicken_1.clicked.connect(self.Chicken1)
        self.object_chicken_1.clicked.connect(self.Basket)

        self.object_chicken_2 = QPushButton("Острый Сибирский Чикен")
        self.tab_chicken_layout.addWidget(self.object_chicken_2)

        self.object_chicken_2.clicked.connect(self.Chicken2)
        self.object_chicken_2.clicked.connect(self.Basket)

        self.object_chicken_3 = QPushButton("Чикенбургер")
        self.tab_chicken_layout.addWidget(self.object_chicken_3)

        self.object_chicken_3.clicked.connect(self.Chicken3)
        self.object_chicken_3.clicked.connect(self.Basket)

        self.object_chicken_4 = QPushButton("Острый Чикенбургер")
        self.tab_chicken_layout.addWidget(self.object_chicken_4)

        self.object_chicken_4.clicked.connect(self.Chicken4)
        self.object_chicken_4.clicked.connect(self.Basket)

        self.object_chicken_5 = QPushButton("Чикен Тар-Тар")
        self.tab_chicken_layout.addWidget(self.object_chicken_5)

        self.object_chicken_5.clicked.connect(self.Chicken5)
        self.object_chicken_5.clicked.connect(self.Basket)

        self.object_chicken_6 = QPushButton("Острый Чикен Тар-Тар")
        self.tab_chicken_layout.addWidget(self.object_chicken_6)

        self.object_chicken_6.clicked.connect(self.Chicken6)
        self.object_chicken_6.clicked.connect(self.Basket)

        self.object_chicken_7 = QPushButton("Цезарь Кинг")
        self.tab_chicken_layout.addWidget(self.object_chicken_7)

        self.object_chicken_7.clicked.connect(self.Chicken7)
        self.object_chicken_7.clicked.connect(self.Basket)


        self.fish = QWidget()
        self.tab_fish_layout = QVBoxLayout()
        self.tab_fish_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.burger.addTab(self.fish, "Рыба")
        self.fish.setLayout(self.tab_fish_layout)

        self.object_fish_1 = QPushButton("Фиш Бургер")
        self.tab_fish_layout.addWidget(self.object_fish_1)

        self.object_fish_1.clicked.connect(self.Fish1)
        self.object_fish_1.clicked.connect(self.Basket)

        self.object_fish_2 = QPushButton("Фиш Бургер Двойной")
        self.tab_fish_layout.addWidget(self.object_fish_2)

        self.object_fish_2.clicked.connect(self.Fish2)
        self.object_fish_2.clicked.connect(self.Basket)


        self.acute = QWidget()
        self.tab_acute_layout = QVBoxLayout()
        self.tab_acute_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.burger.addTab(self.acute, "Острое")
        self.acute.setLayout(self.tab_acute_layout)

        self.object_acute_1 = QPushButton("Острый Ангус Сибирский")
        self.tab_acute_layout.addWidget(self.object_acute_1)

        self.object_acute_1.clicked.connect(self.Acute1)
        self.object_acute_1.clicked.connect(self.Basket)

        self.object_acute_2 = QPushButton("Острый Ангус Сибирский Двойной")
        self.tab_acute_layout.addWidget(self.object_acute_2)

        self.object_acute_2.clicked.connect(self.Acute2)
        self.object_acute_2.clicked.connect(self.Basket)

        self.object_acute_3 = QPushButton("Острый Ангус Пармеджано")
        self.tab_acute_layout.addWidget(self.object_acute_3)

        self.object_acute_3.clicked.connect(self.Acute3)
        self.object_acute_3.clicked.connect(self.Basket)

        self.object_acute_4 = QPushButton("Острый Ангус Пармеджано Двойной")
        self.tab_acute_layout.addWidget(self.object_acute_4)

        self.object_acute_4.clicked.connect(self.Acute4)
        self.object_acute_4.clicked.connect(self.Basket)

        self.object_acute_5 = QPushButton("Острый Воппер Сибирский")
        self.tab_acute_layout.addWidget(self.object_acute_5)

        self.object_acute_5.clicked.connect(self.Acute5)
        self.object_acute_5.clicked.connect(self.Basket)

        self.object_acute_6 = QPushButton("Острый Воппер Сибирский Двойной")
        self.tab_acute_layout.addWidget(self.object_acute_6)

        self.object_acute_6.clicked.connect(self.Acute6)
        self.object_acute_6.clicked.connect(self.Basket)

        self.object_acute_7 = QPushButton("Острый Воппер С Сыром")
        self.tab_acute_layout.addWidget(self.object_acute_7)

        self.object_acute_7.clicked.connect(self.Acute7)
        self.object_acute_7.clicked.connect(self.Basket)

        self.object_acute_8 = QPushButton("Острый Воппер")
        self.tab_acute_layout.addWidget(self.object_acute_8)

        self.object_acute_8.clicked.connect(self.Acute8)
        self.object_acute_8.clicked.connect(self.Basket)

        self.object_acute_9 = QPushButton("Острый Двойной Воппер С Сыром")
        self.tab_acute_layout.addWidget(self.object_acute_9)

        self.object_acute_9.clicked.connect(self.Acute9)
        self.object_acute_9.clicked.connect(self.Basket)

        self.object_acute_10 = QPushButton("Острый Воппер Джуниор")
        self.tab_acute_layout.addWidget(self.object_acute_10)

        self.object_acute_10.clicked.connect(self.Acute10)
        self.object_acute_10.clicked.connect(self.Basket)

        self.object_acute_11 = QPushButton("Острый Чизбургер Фреш")
        self.tab_acute_layout.addWidget(self.object_acute_11)

        self.object_acute_11.clicked.connect(self.Acute11)
        self.object_acute_11.clicked.connect(self.Basket)

        self.object_acute_12 = QPushButton("Острый Тройной Чизбургер Фреш")
        self.tab_acute_layout.addWidget(self.object_acute_12)

        self.object_acute_12.clicked.connect(self.Acute12)
        self.object_acute_12.clicked.connect(self.Basket)

        self.object_acute_13 = QPushButton("Острый Гамбургер Фреш")
        self.tab_acute_layout.addWidget(self.object_acute_13)

        self.object_acute_13.clicked.connect(self.Acute13)
        self.object_acute_13.clicked.connect(self.Basket)

        self.object_acute_14 = QPushButton("Острый Сибирский Чикен")
        self.tab_acute_layout.addWidget(self.object_acute_14)

        self.object_acute_14.clicked.connect(self.Acute14)
        self.object_acute_14.clicked.connect(self.Basket)

        self.object_acute_15 = QPushButton("Острый Чикен Тар-Тар")
        self.tab_acute_layout.addWidget(self.object_acute_15)

        self.object_acute_15.clicked.connect(self.Acute15)
        self.object_acute_15.clicked.connect(self.Basket)

        self.object_acute_16 = QPushButton("Острый Чикенбургер")
        self.tab_acute_layout.addWidget(self.object_acute_16)

        self.object_acute_16.clicked.connect(self.Acute16)
        self.object_acute_16.clicked.connect(self.Basket)

        self.object_acute_17 = QPushButton("Острый Фиш Бургер")
        self.tab_acute_layout.addWidget(self.object_acute_17)

        self.object_acute_17.clicked.connect(self.Acute17)
        self.object_acute_17.clicked.connect(self.Basket)

        self.object_acute_18 = QPushButton("Острый Цезарь Кинг")
        self.tab_acute_layout.addWidget(self.object_acute_18)

        self.object_acute_18.clicked.connect(self.Acute18)
        self.object_acute_18.clicked.connect(self.Basket)


        self.rolls = QWidget()
        self.tab_rolls_layout = QVBoxLayout()
        self.tab_rolls_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tabs.addTab(self.rolls, "Роллы")
        self.rolls.setLayout(self.tab_rolls_layout)

        self.object_rolls_1 = QPushButton("Сибирский Чикен Ролл")
        self.tab_rolls_layout.addWidget(self.object_rolls_1)

        self.object_rolls_1.clicked.connect(self.Rolls1)
        self.object_rolls_1.clicked.connect(self.Basket)

        self.object_rolls_2 = QPushButton("Острый Сибирский Чикен Ролл")
        self.tab_rolls_layout.addWidget(self.object_rolls_2)

        self.object_rolls_2.clicked.connect(self.Rolls2)
        self.object_rolls_2.clicked.connect(self.Basket)

        self.object_rolls_3 = QPushButton("Сибирский Шримп Ролл")
        self.tab_rolls_layout.addWidget(self.object_rolls_3)

        self.object_rolls_3.clicked.connect(self.Rolls3)
        self.object_rolls_3.clicked.connect(self.Basket)

        self.object_rolls_4 = QPushButton("Острый Сибирский Шримп Ролл")
        self.tab_rolls_layout.addWidget(self.object_rolls_4)

        self.object_rolls_4.clicked.connect(self.Rolls4)
        self.object_rolls_4.clicked.connect(self.Basket)

        self.object_rolls_5 = QPushButton("Шримп Ролл")
        self.tab_rolls_layout.addWidget(self.object_rolls_5)

        self.object_rolls_5.clicked.connect(self.Rolls5)
        self.object_rolls_5.clicked.connect(self.Basket)

        self.object_rolls_6 = QPushButton("Острый Шримп Ролл")
        self.tab_rolls_layout.addWidget(self.object_rolls_6)

        self.object_rolls_6.clicked.connect(self.Rolls6)
        self.object_rolls_6.clicked.connect(self.Basket)

        self.object_rolls_7 = QPushButton("Цезарь Ролл Со Стрипсами")
        self.tab_rolls_layout.addWidget(self.object_rolls_7)

        self.object_rolls_7.clicked.connect(self.Rolls7)
        self.object_rolls_7.clicked.connect(self.Basket)

        self.object_rolls_8 = QPushButton("Острый Цезарь Ролл Со Стрипсами")
        self.tab_rolls_layout.addWidget(self.object_rolls_8)

        self.object_rolls_8.clicked.connect(self.Rolls8)
        self.object_rolls_8.clicked.connect(self.Basket)

        self.object_rolls_9 = QPushButton("Воппер Ролл")
        self.tab_rolls_layout.addWidget(self.object_rolls_9)

        self.object_rolls_9.clicked.connect(self.Rolls9)
        self.object_rolls_9.clicked.connect(self.Basket)

        self.object_rolls_10 = QPushButton("Острый Воппер Ролл")
        self.tab_rolls_layout.addWidget(self.object_rolls_10)

        self.object_rolls_10.clicked.connect(self.Rolls10)
        self.object_rolls_10.clicked.connect(self.Basket)

        self.object_rolls_11 = QPushButton("Фиш Ролл")
        self.tab_rolls_layout.addWidget(self.object_rolls_11)

        self.object_rolls_11.clicked.connect(self.Rolls11)
        self.object_rolls_11.clicked.connect(self.Basket)


        self.snacks = QTabWidget()
        self.tab_snacks_layout = QVBoxLayout()

        self.tabs.addTab(self.snacks, "Закуски")
        self.snacks.setLayout(self.tab_snacks_layout)


        self.big_snacks = QWidget()
        self.tab_big_snacks_layout = QVBoxLayout()
        self.tab_big_snacks_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.snacks.addTab(self.big_snacks, "Большой")
        self.big_snacks.setLayout(self.tab_big_snacks_layout)

        self.object_big_snacks_1 = QPushButton("Большой Кинг Фри")
        self.tab_big_snacks_layout.addWidget(self.object_big_snacks_1)

        self.object_big_snacks_1.clicked.connect(self.Big_snacks1)
        self.object_big_snacks_1.clicked.connect(self.Basket)

        self.object_big_snacks_2 = QPushButton("Большой Роял Фри")
        self.tab_big_snacks_layout.addWidget(self.object_big_snacks_2)

        self.object_big_snacks_2.clicked.connect(self.Big_snacks2)
        self.object_big_snacks_2.clicked.connect(self.Basket)

        self.object_big_snacks_3 = QPushButton("Большой Картофель Деревенский")
        self.tab_big_snacks_layout.addWidget(self.object_big_snacks_3)

        self.object_big_snacks_3.clicked.connect(self.Big_snacks3)
        self.object_big_snacks_3.clicked.connect(self.Basket)

        self.object_big_snacks_4 = QPushButton("Наггетсы (12 штук)")
        self.tab_big_snacks_layout.addWidget(self.object_big_snacks_4)

        self.object_big_snacks_4.clicked.connect(self.Big_snacks4)
        self.object_big_snacks_4.clicked.connect(self.Basket)

        self.object_big_snacks_5 = QPushButton("Креветки (9 штук)")
        self.tab_big_snacks_layout.addWidget(self.object_big_snacks_5)

        self.object_big_snacks_5.clicked.connect(self.Big_snacks5)
        self.object_big_snacks_5.clicked.connect(self.Basket)

        self.object_big_snacks_6 = QPushButton("Крылышки (9 штук)")
        self.tab_big_snacks_layout.addWidget(self.object_big_snacks_6)

        self.object_big_snacks_6.clicked.connect(self.Big_snacks6)
        self.object_big_snacks_6.clicked.connect(self.Basket)

        self.object_big_snacks_7 = QPushButton("Сырные Медальоны (9 штук)")
        self.tab_big_snacks_layout.addWidget(self.object_big_snacks_7)

        self.object_big_snacks_7.clicked.connect(self.Big_snacks7)
        self.object_big_snacks_7.clicked.connect(self.Basket)

        self.object_big_snacks_8 = QPushButton("Луковые Кольца (9 штук)")
        self.tab_big_snacks_layout.addWidget(self.object_big_snacks_8)

        self.object_big_snacks_8.clicked.connect(self.Big_snacks8)
        self.object_big_snacks_8.clicked.connect(self.Basket)

        self.object_big_snacks_9 = QPushButton("Стрипсы (9 штук)")
        self.tab_big_snacks_layout.addWidget(self.object_big_snacks_9)

        self.object_big_snacks_9.clicked.connect(self.Big_snacks9)
        self.object_big_snacks_9.clicked.connect(self.Basket)


        self.mid_snacks = QWidget()
        self.tab_mid_snacks_layout = QVBoxLayout()
        self.tab_mid_snacks_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.snacks.addTab(self.mid_snacks, "Средний")
        self.mid_snacks.setLayout(self.tab_mid_snacks_layout)

        self.object_mid_snacks_1 = QPushButton("Средний Кинг Фри")
        self.tab_mid_snacks_layout.addWidget(self.object_mid_snacks_1)

        self.object_mid_snacks_1.clicked.connect(self.Mid_snacks1)
        self.object_mid_snacks_1.clicked.connect(self.Basket)

        self.object_mid_snacks_2 = QPushButton("Средний Роял Фри")
        self.tab_mid_snacks_layout.addWidget(self.object_mid_snacks_2)

        self.object_mid_snacks_2.clicked.connect(self.Mid_snacks2)
        self.object_mid_snacks_2.clicked.connect(self.Basket)

        self.object_mid_snacks_3 = QPushButton("Средний Картофель Деревенский")
        self.tab_mid_snacks_layout.addWidget(self.object_mid_snacks_3)

        self.object_mid_snacks_3.clicked.connect(self.Mid_snacks3)
        self.object_mid_snacks_3.clicked.connect(self.Basket)

        self.object_mid_snacks_4 = QPushButton("Наггетсы (9 штук)")
        self.tab_mid_snacks_layout.addWidget(self.object_mid_snacks_4)

        self.object_mid_snacks_4.clicked.connect(self.Mid_snacks4)
        self.object_mid_snacks_4.clicked.connect(self.Basket)

        self.object_mid_snacks_5 = QPushButton("Креветки (6 штук)")
        self.tab_mid_snacks_layout.addWidget(self.object_mid_snacks_5)

        self.object_mid_snacks_5.clicked.connect(self.Mid_snacks5)
        self.object_mid_snacks_5.clicked.connect(self.Basket)

        self.object_mid_snacks_6 = QPushButton("Крылышки (6 штук)")
        self.tab_mid_snacks_layout.addWidget(self.object_mid_snacks_6)

        self.object_mid_snacks_6.clicked.connect(self.Mid_snacks6)
        self.object_mid_snacks_6.clicked.connect(self.Basket)

        self.object_mid_snacks_7 = QPushButton("Сырные Медальоны (6 штук)")
        self.tab_mid_snacks_layout.addWidget(self.object_mid_snacks_7)

        self.object_mid_snacks_7.clicked.connect(self.Mid_snacks7)
        self.object_mid_snacks_7.clicked.connect(self.Basket)

        self.object_mid_snacks_8 = QPushButton("Луковые Кольца (6 штук)")
        self.tab_mid_snacks_layout.addWidget(self.object_mid_snacks_8)

        self.object_mid_snacks_8.clicked.connect(self.Mid_snacks8)
        self.object_mid_snacks_8.clicked.connect(self.Basket)

        self.object_mid_snacks_9 = QPushButton("Стрипсы (6 штук)")
        self.tab_mid_snacks_layout.addWidget(self.object_mid_snacks_9)

        self.object_mid_snacks_9.clicked.connect(self.Mid_snacks9)
        self.object_mid_snacks_9.clicked.connect(self.Basket)


        self.small_snacks = QWidget()
        self.tab_small_snacks_layout = QVBoxLayout()
        self.tab_small_snacks_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.snacks.addTab(self.small_snacks, "Малый")
        self.small_snacks.setLayout(self.tab_small_snacks_layout)

        self.object_small_snacks_1 = QPushButton("Малый Кинг Фри")
        self.tab_small_snacks_layout.addWidget(self.object_small_snacks_1)

        self.object_small_snacks_1.clicked.connect(self.Small_snacks1)
        self.object_small_snacks_1.clicked.connect(self.Basket)

        self.object_small_snacks_2 = QPushButton("Малый Роял Фри")
        self.tab_small_snacks_layout.addWidget(self.object_small_snacks_2)

        self.object_small_snacks_2.clicked.connect(self.Small_snacks2)
        self.object_small_snacks_2.clicked.connect(self.Basket)

        self.object_small_snacks_3 = QPushButton("Малый Картофель Деревенский")
        self.tab_small_snacks_layout.addWidget(self.object_small_snacks_3)

        self.object_small_snacks_3.clicked.connect(self.Small_snacks3)
        self.object_small_snacks_3.clicked.connect(self.Basket)

        self.object_small_snacks_4 = QPushButton("Наггетсы (6 штуки)")
        self.tab_small_snacks_layout.addWidget(self.object_small_snacks_4)

        self.object_small_snacks_4.clicked.connect(self.Small_snacks4)
        self.object_small_snacks_4.clicked.connect(self.Basket)

        self.object_small_snacks_5 = QPushButton("Креветки (3 штуки)")
        self.tab_small_snacks_layout.addWidget(self.object_small_snacks_5)

        self.object_small_snacks_5.clicked.connect(self.Small_snacks5)
        self.object_small_snacks_5.clicked.connect(self.Basket)

        self.object_small_snacks_6 = QPushButton("Крылышки (3 штуки)")
        self.tab_small_snacks_layout.addWidget(self.object_small_snacks_6)

        self.object_small_snacks_6.clicked.connect(self.Small_snacks6)
        self.object_small_snacks_6.clicked.connect(self.Basket)

        self.object_small_snacks_7 = QPushButton("Сырные Медальоны (3 штуки)")
        self.tab_small_snacks_layout.addWidget(self.object_small_snacks_7)

        self.object_small_snacks_7.clicked.connect(self.Small_snacks7)
        self.object_small_snacks_7.clicked.connect(self.Basket)

        self.object_small_snacks_8 = QPushButton("Луковые Кольца (3 штуки)")
        self.tab_small_snacks_layout.addWidget(self.object_small_snacks_8)

        self.object_small_snacks_8.clicked.connect(self.Small_snacks8)
        self.object_small_snacks_8.clicked.connect(self.Basket)

        self.object_small_snacks_9 = QPushButton("Стрипсы (3 штуки)")
        self.tab_small_snacks_layout.addWidget(self.object_small_snacks_9)

        self.object_small_snacks_9.clicked.connect(self.Small_snacks9)
        self.object_small_snacks_9.clicked.connect(self.Basket)


        self.drinks = QTabWidget()
        self.tab_drinks_layout = QVBoxLayout()

        self.tabs.addTab(self.drinks, "Напитки")
        self.drinks.setLayout(self.tab_drinks_layout)


        self.big_drinks = QWidget()
        self.tab_big_drinks_layout = QVBoxLayout()
        self.tab_big_drinks_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.drinks.addTab(self.big_drinks, "Большой")
        self.big_drinks.setLayout(self.tab_big_drinks_layout)

        self.object_big_drinks_1 = QPushButton("Большой Стакан Колы")
        self.tab_big_drinks_layout.addWidget(self.object_big_drinks_1)

        self.object_big_drinks_1.clicked.connect(self.Big_drinks1)
        self.object_big_drinks_1.clicked.connect(self.Basket)

        self.object_big_drinks_2 = QPushButton("Большой Стакан Пепси")
        self.tab_big_drinks_layout.addWidget(self.object_big_drinks_2)

        self.object_big_drinks_2.clicked.connect(self.Big_drinks2)
        self.object_big_drinks_2.clicked.connect(self.Basket)

        self.object_big_drinks_3 = QPushButton("Большой Стакан Фанты")
        self.tab_big_drinks_layout.addWidget(self.object_big_drinks_3)

        self.object_big_drinks_3.clicked.connect(self.Big_drinks3)
        self.object_big_drinks_3.clicked.connect(self.Basket)

        self.object_big_drinks_4 = QPushButton("Большой Стакан Спрайта")
        self.tab_big_drinks_layout.addWidget(self.object_big_drinks_4)

        self.object_big_drinks_4.clicked.connect(self.Big_drinks4)
        self.object_big_drinks_4.clicked.connect(self.Basket)

        self.object_big_drinks_5 = QPushButton("Большой Стакан Липтона")
        self.tab_big_drinks_layout.addWidget(self.object_big_drinks_5)

        self.object_big_drinks_5.clicked.connect(self.Big_drinks5)
        self.object_big_drinks_5.clicked.connect(self.Basket)

        self.object_big_drinks_6 = QPushButton("Большой Стакан Шоколадного Шейка")
        self.tab_big_drinks_layout.addWidget(self.object_big_drinks_6)

        self.object_big_drinks_6.clicked.connect(self.Big_drinks6)
        self.object_big_drinks_6.clicked.connect(self.Basket)

        self.object_big_drinks_7 = QPushButton("Большой Стакан Клубничного Шейка")
        self.tab_big_drinks_layout.addWidget(self.object_big_drinks_7)

        self.object_big_drinks_7.clicked.connect(self.Big_drinks7)
        self.object_big_drinks_7.clicked.connect(self.Basket)

        self.object_big_drinks_8 = QPushButton("Большой Стакан Ванильного Шейка")
        self.tab_big_drinks_layout.addWidget(self.object_big_drinks_8)

        self.object_big_drinks_8.clicked.connect(self.Big_drinks8)
        self.object_big_drinks_8.clicked.connect(self.Basket)


        self.mid_drinks = QWidget()
        self.tab_mid_drinks_layout = QVBoxLayout()
        self.tab_mid_drinks_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.drinks.addTab(self.mid_drinks, "Средний")
        self.mid_drinks.setLayout(self.tab_mid_drinks_layout)

        self.object_mid_drinks_1 = QPushButton("Средний Стакан Колы")
        self.tab_mid_drinks_layout.addWidget(self.object_mid_drinks_1)

        self.object_mid_drinks_1.clicked.connect(self.Mid_drinks1)
        self.object_mid_drinks_1.clicked.connect(self.Basket)

        self.object_mid_drinks_2 = QPushButton("Средний Стакан Пепси")
        self.tab_mid_drinks_layout.addWidget(self.object_mid_drinks_2)

        self.object_mid_drinks_2.clicked.connect(self.Mid_drinks2)
        self.object_mid_drinks_2.clicked.connect(self.Basket)

        self.object_mid_drinks_3 = QPushButton("Средний Стакан Фанты")
        self.tab_mid_drinks_layout.addWidget(self.object_mid_drinks_3)

        self.object_mid_drinks_3.clicked.connect(self.Mid_drinks3)
        self.object_mid_drinks_3.clicked.connect(self.Basket)

        self.object_mid_drinks_4 = QPushButton("Средний Стакан Спрайта")
        self.tab_mid_drinks_layout.addWidget(self.object_mid_drinks_4)

        self.object_mid_drinks_4.clicked.connect(self.Mid_drinks4)
        self.object_mid_drinks_4.clicked.connect(self.Basket)

        self.object_mid_drinks_5 = QPushButton("Средний Стакан Липтона")
        self.tab_mid_drinks_layout.addWidget(self.object_mid_drinks_5)

        self.object_mid_drinks_5.clicked.connect(self.Mid_drinks5)
        self.object_mid_drinks_5.clicked.connect(self.Basket)

        self.object_mid_drinks_6 = QPushButton("Средний Стакан Шоколадного Шейка")
        self.tab_mid_drinks_layout.addWidget(self.object_mid_drinks_6)

        self.object_mid_drinks_6.clicked.connect(self.Mid_drinks6)
        self.object_mid_drinks_6.clicked.connect(self.Basket)

        self.object_mid_drinks_7 = QPushButton("Средний Стакан Клубничного Шейка")
        self.tab_mid_drinks_layout.addWidget(self.object_mid_drinks_7)

        self.object_mid_drinks_7.clicked.connect(self.Mid_drinks7)
        self.object_mid_drinks_7.clicked.connect(self.Basket)

        self.object_mid_drinks_8 = QPushButton("Средний Стакан Ванильного Шейка")
        self.tab_mid_drinks_layout.addWidget(self.object_mid_drinks_8)

        self.object_mid_drinks_8.clicked.connect(self.Mid_drinks8)
        self.object_mid_drinks_8.clicked.connect(self.Basket)


        self.small_drinks = QWidget()
        self.tab_small_drinks_layout = QVBoxLayout()
        self.tab_small_drinks_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.drinks.addTab(self.small_drinks, "Маленький")
        self.small_drinks.setLayout(self.tab_small_drinks_layout)

        self.object_small_drinks_1 = QPushButton("Малый Стакан Колы")
        self.tab_small_drinks_layout.addWidget(self.object_small_drinks_1)

        self.object_small_drinks_1.clicked.connect(self.Small_drinks1)
        self.object_small_drinks_1.clicked.connect(self.Basket)

        self.object_small_drinks_2 = QPushButton("Малый Стакан Пепси")
        self.tab_small_drinks_layout.addWidget(self.object_small_drinks_2)

        self.object_small_drinks_2.clicked.connect(self.Small_drinks2)
        self.object_small_drinks_2.clicked.connect(self.Basket)

        self.object_small_drinks_3 = QPushButton("Малый Стакан Фанты")
        self.tab_small_drinks_layout.addWidget(self.object_small_drinks_3)

        self.object_small_drinks_3.clicked.connect(self.Small_drinks3)
        self.object_small_drinks_3.clicked.connect(self.Basket)

        self.object_small_drinks_4 = QPushButton("Малый Стакан Спрайта")
        self.tab_small_drinks_layout.addWidget(self.object_small_drinks_4)

        self.object_small_drinks_4.clicked.connect(self.Small_drinks4)
        self.object_small_drinks_4.clicked.connect(self.Basket)

        self.object_small_drinks_5 = QPushButton("Малый Стакан Липтона")
        self.tab_small_drinks_layout.addWidget(self.object_small_drinks_5)

        self.object_small_drinks_5.clicked.connect(self.Small_drinks5)
        self.object_small_drinks_5.clicked.connect(self.Basket)

        self.object_small_drinks_6 = QPushButton("Малый Стакан Шоколадного Шейка")
        self.tab_small_drinks_layout.addWidget(self.object_small_drinks_6)

        self.object_small_drinks_6.clicked.connect(self.Small_drinks6)
        self.object_small_drinks_6.clicked.connect(self.Basket)

        self.object_small_drinks_7 = QPushButton("Малый Стакан Клубничного Шейка")
        self.tab_small_drinks_layout.addWidget(self.object_small_drinks_7)

        self.object_small_drinks_7.clicked.connect(self.Small_drinks7)
        self.object_small_drinks_7.clicked.connect(self.Basket)

        self.object_small_drinks_8 = QPushButton("Малый Стакан Ванильного Шейка")
        self.tab_small_drinks_layout.addWidget(self.object_small_drinks_8)

        self.object_small_drinks_8.clicked.connect(self.Small_drinks8)
        self.object_small_drinks_8.clicked.connect(self.Basket)


        self.desserts = QWidget()
        self.tab_desserts_layout = QVBoxLayout()

        self.tabs.addTab(self.desserts, "Дессерты")
        self.desserts.setLayout(self.tab_desserts_layout)
        self.tab_desserts_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.object_desserts_1 = QPushButton("Айс Твист Шоколадный")
        self.tab_desserts_layout.addWidget(self.object_desserts_1)

        self.object_desserts_1.clicked.connect(self.Desserts1)
        self.object_desserts_1.clicked.connect(self.Basket)

        self.object_desserts_2 = QPushButton("Айс Твист Клубничный")
        self.tab_desserts_layout.addWidget(self.object_desserts_2)

        self.object_desserts_2.clicked.connect(self.Desserts2)
        self.object_desserts_2.clicked.connect(self.Basket)

        self.object_desserts_3 = QPushButton("Сандэй Шоколадный")
        self.tab_desserts_layout.addWidget(self.object_desserts_3)

        self.object_desserts_3.clicked.connect(self.Desserts3)
        self.object_desserts_3.clicked.connect(self.Basket)

        self.object_desserts_4 = QPushButton("Сандэй Клубничный")
        self.tab_desserts_layout.addWidget(self.object_desserts_4)

        self.object_desserts_4.clicked.connect(self.Desserts4)
        self.object_desserts_4.clicked.connect(self.Basket)

        self.object_desserts_5 = QPushButton("Горячий Брауни")
        self.tab_desserts_layout.addWidget(self.object_desserts_5)

        self.object_desserts_5.clicked.connect(self.Desserts5)
        self.object_desserts_5.clicked.connect(self.Basket)

        self.object_desserts_6 = QPushButton("Горячий Брауни С Мороженным")
        self.tab_desserts_layout.addWidget(self.object_desserts_6)

        self.object_desserts_6.clicked.connect(self.Desserts6)
        self.object_desserts_6.clicked.connect(self.Basket)

        self.object_desserts_7 = QPushButton("Пирожок С Вишней")
        self.tab_desserts_layout.addWidget(self.object_desserts_7)

        self.object_desserts_7.clicked.connect(self.Desserts7)
        self.object_desserts_7.clicked.connect(self.Basket)

        self.object_desserts_8 = QPushButton("Рожок")
        self.tab_desserts_layout.addWidget(self.object_desserts_8)

        self.object_desserts_8.clicked.connect(self.Desserts8)
        self.object_desserts_8.clicked.connect(self.Basket)


        self.btn1 = QPushButton("Оплатить", self)
        self.tab1_layout.addWidget(self.btn1)
        self.tab1_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.btn1.clicked.connect(self.open_second_form)


        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.tabs)
        self.setLayout(self.main_layout)

    def Beef1(self):
        self.v.append("Ангус Сибирский")
        self.f += 459

    def Beef2(self):
        self.v.append("Острый Ангус Сибирский")
        self.f += 469

    def Beef3(self):
        self.v.append("Ангус Сибирский Двойной")
        self.f += 619

    def Beef4(self):
        self.v.append("Ангус Пармеджано")
        self.f += 399

    def Beef5(self):
        self.v.append("Ангус Пармеджано Двойной")
        self.f += 549

    def Beef6(self):
        self.v.append("Воппер Сибирский")
        self.f += 339

    def Beef7(self):
        self.v.append("Острый Воппер Сибирский")
        self.f += 349

    def Beef8(self):
        self.v.append("Воппер Сибирский Двойной")
        self.f += 459

    def Beef9(self):
        self.v.append("Острый Воппер Сибирский Двойной")
        self.f += 469

    def Beef10(self):
        self.v.append("Ангус Сибирский Двойной")
        self.f += 619

    def Beef11(self):
        self.v.append("Острый Ангус Сибирский Двойной")
        self.f += 629

    def Beef12(self):
        self.v.append("Острый Двойной Воппер С Сыром")
        self.f += 469

    def Beef13(self):
        self.v.append("Двойной Воппер")
        self.f += 354

    def Beef14(self):
        self.v.append("Двойной Чизбургер Фреш")
        self.f += 269

    def Beef15(self):
        self.v.append("Тройной Воппер")
        self.f += 409

    def Beef16(self):
        self.v.append("Чизбургер Фреш")
        self.f += 339

    def Beef17(self):
        self.v.append("Острый Гамбургер Фреш")
        self.f += 244

    def Beef18(self):
        self.v.append("Острый Чизбургер Фреш")
        self.f += 269

    def Beef19(self):
        self.v.append("Гамбургер Фреш")
        self.f += 259

    def Beef20(self):
        self.v.append("Тройной Чизбургер Фреш")
        self.f += 309

    def Beef21(self):
        self.v.append("Острый Тройной Чизбургер Фреш")
        self.f += 409

    def Beef22(self):
        self.v.append("Воппер Джуниор")
        self.f += 134

    def Beef23(self):
        self.v.append("Чизбургер")
        self.f += 99

    def Beef24(self):
        self.v.append("Гамбургер")
        self.f += 94

    def Beef25(self):
        self.v.append("Гранд Чиз")
        self.f += 234

    def Chicken1(self):
        self.v.append("Сибирский Чикен")
        self.f += 339

    def Chicken2(self):
        self.v.append("Острый Сибирский Чикен")
        self.f += 349

    def Chicken3(self):
        self.v.append("Чикенбургер")
        self.f += 94

    def Chicken4(self):
        self.v.append("Острый Чикенбургер")
        self.f += 104

    def Chicken5(self):
        self.v.append("Чикен Тар-Тар")
        self.f += 209

    def Chicken6(self):
        self.v.append("Острый Чикен Тар-Тар")
        self.f += 219

    def Chicken7(self):
        self.v.append("Цезарь Кинг")
        self.f += 134

    def Fish1(self):
        self.v.append("Фиш Бургер")
        self.f += 184

    def Fish2(self):
        self.v.append("Фиш Бургер Двойной")
        self.f += 219

    def Acute1(self):
        self.v.append("Острый Ангус Сибирский")
        self.f += 469

    def Acute2(self):
        self.v.append("Острый Ангус Сибирский Двойной")
        self.f += 629

    def Acute3(self):
        self.v.append("Острый Ангус Пармеджано")
        self.f += 409

    def Acute4(self):
        self.v.append("Острый Ангус Пармеджано Двойной")
        self.f += 559

    def Acute5(self):
        self.v.append("Острый Воппер Сибирский")
        self.f += 349

    def Acute6(self):
        self.v.append("Острый Воппер Сибирский Двойной")
        self.f += 469

    def Acute7(self):
        self.v.append("Острый Воппер С Сыром")
        self.f += 314

    def Acute8(self):
        self.v.append("Острый Воппер")
        self.f += 294

    def Acute9(self):
        self.v.append("Острый Двойной Воппер С Сыром")
        self.f += 399

    def Acute10(self):
        self.v.append("Острый Воппер Джуниор")
        self.f += 144

    def Acute11(self):
        self.v.append("Острый Чизбургер Фреш")
        self.f += 184

    def Acute12(self):
        self.v.append("Острый Тройной Чизбургер Фреш")
        self.f += 229

    def Acute13(self):
        self.v.append("Острый Гамбургер Фреш")
        self.f += 194

    def Acute14(self):
        self.v.append("Острый Сибирский Чикен")
        self.f += 349

    def Acute15(self):
        self.v.append("Острый Чикен Тар-Тар")
        self.f += 219

    def Acute16(self):
        self.v.append("Острый Чикенбургер")
        self.f += 104

    def Acute17(self):
        self.v.append("Острый Фиш Бургер")
        self.f += 194

    def Acute18(self):
        self.v.append("Острый Цезарь Кинг")
        self.f += 144

    def Rolls1(self):
        self.v.append("Сибирский Чикен Ролл")
        self.f += 399

    def Rolls2(self):
        self.v.append("Острый Сибирский Чикен Ролл")
        self.f += 339

    def Rolls3(self):
        self.v.append("Сибирский Шримп Ролл")
        self.f += 384

    def Rolls4(self):
        self.v.append("Острый Сибирский Шримп Ролл")
        self.f += 394

    def Rolls5(self):
        self.v.append("Шримп Ролл")
        self.f += 329

    def Rolls6(self):
        self.v.append("Острый Шримп Ролл")
        self.f += 339

    def Rolls7(self):
        self.v.append("Цезарь Ролл Со Стрипсами")
        self.f += 259

    def Rolls8(self):
        self.v.append("Острый Цезарь Ролл Со Стрипсами")
        self.f += 269

    def Rolls9(self):
        self.v.append("Воппер Ролл")
        self.f += 274

    def Rolls10(self):
        self.v.append("Острый Воппер Ролл")
        self.f += 284

    def Rolls11(self):
        self.v.append("Фиш Ролл")
        self.f += 199

    def Big_snacks1(self):
        self.v.append("Большой Кинг Фри")
        self.f += 139

    def Big_snacks2(self):
        self.v.append("Большой Роял Фри")
        self.f += 249

    def Big_snacks3(self):
        self.v.append("Большой Картофель Деревенский")
        self.f += 164

    def Big_snacks4(self):
        self.v.append("Наггетсы (12 штук)")
        self.f += 204

    def Big_snacks5(self):
        self.v.append("Креветки (12 штук)")
        self.f += 719

    def Big_snacks6(self):
        self.v.append("Крылышки (12 штук)")
        self.f += 519

    def Big_snacks7(self):
        self.v.append("Сырные Медальоны (12 штук)")
        self.f += 249

    def Big_snacks8(self):
        self.v.append("Луковые Кольца (12 штук)")
        self.f += 229

    def Big_snacks9(self):
        self.v.append("Стрипсы (12 штук)")
        self.f += 529

    def Mid_snacks1(self):
        self.v.append("Средний Кинг Фри")
        self.f += 109

    def Mid_snacks2(self):
        self.v.append("Средний Роял Фри")
        self.f += 224

    def Mid_snacks3(self):
        self.v.append("Средний Картофель Деревенский")
        self.f += 154

    def Mid_snacks4(self):
        self.v.append("Наггетсы (9 штук)")
        self.f += 169

    def Mid_snacks5(self):
        self.v.append("Креветки (9 штук)")
        self.f += 569

    def Mid_snacks6(self):
        self.v.append("Крылышки (9 штук)")
        self.f += 449

    def Mid_snacks7(self):
        self.v.append("Сырные Медальоны (9 штук)")
        self.f += 219

    def Mid_snacks8(self):
        self.v.append("Луковые Кольца (9 штук)")
        self.f += 209

    def Mid_snacks9(self):
        self.v.append("Стрипсы (9 штук)")
        self.f += 454

    def Small_snacks1(self):
        self.v.append("Малый Кинг Фри")
        self.f += 94

    def Small_snacks2(self):
        self.v.append("Малый Роял Фри")
        self.f += 204

    def Small_snacks3(self):
        self.v.append("Малый Картофель Деревенский")
        self.f += 199

    def Small_snacks4(self):
        self.v.append("Наггетсы (6 штук)")
        self.f += 114

    def Small_snacks5(self):
        self.v.append("Креветки (6 штук)")
        self.f += 399

    def Small_snacks6(self):
        self.v.append("Крылышки (6 штук)")
        self.f += 329

    def Small_snacks7(self):
        self.v.append("Сырные Медальоны (6 штук)")
        self.f += 144

    def Small_snacks8(self):
        self.v.append("Луковые Кольца (6 штук)")
        self.f += 114

    def Small_snacks9(self):
        self.v.append("Стрипсы (6 штук)")
        self.f += 389

    def Big_drinks1(self):
        self.v.append("Большой Стакан Колы")
        self.f += 199

    def Big_drinks2(self):
        self.v.append("Большой Стакан Пепси")
        self.f += 199

    def Big_drinks3(self):
        self.v.append("Большой Стакан Фанты")
        self.f += 199

    def Big_drinks4(self):
        self.v.append("Большой Стакан Спрайта")
        self.f += 199

    def Big_drinks5(self):
        self.v.append("Большой Стакан Липтона")
        self.f += 199

    def Big_drinks6(self):
        self.v.append("Большой Стакан Шоколадного Шейка")
        self.f += 174

    def Big_drinks7(self):
        self.v.append("Большой Стакан Клубничного Шейка")
        self.f += 174

    def Big_drinks8(self):
        self.v.append("Большой Стакан Ванильного Шейка")
        self.f += 174

    def Mid_drinks1(self):
        self.v.append("Средний Стакан Колы")
        self.f += 159

    def Mid_drinks2(self):
        self.v.append("Средний Стакан Пепси")
        self.f += 159

    def Mid_drinks3(self):
        self.v.append("Средний Стакан Фанты")
        self.f += 159

    def Mid_drinks4(self):
        self.v.append("Средний Стакан Спрайта")
        self.f += 159

    def Mid_drinks5(self):
        self.v.append("Средний Стакан Липтона")
        self.f += 159

    def Mid_drinks6(self):
        self.v.append("Средний Стакан Шоколадного Шейка")
        self.f += 154

    def Mid_drinks7(self):
        self.v.append("Средний Стакан Клубничного Шейка")
        self.f += 154

    def Mid_drinks8(self):
        self.v.append("Средний Стакан Ванильного Шейка")
        self.f += 154

    def Small_drinks1(self):
        self.v.append("Малый Стакан Колы")
        self.f += 129

    def Small_drinks2(self):
        self.v.append("Малый Стакан Пепси")
        self.f += 129

    def Small_drinks3(self):
        self.v.append("Малый Стакан Фанты")
        self.f += 129

    def Small_drinks4(self):
        self.v.append("Малый Стакан Спрайта")
        self.f += 129

    def Small_drinks5(self):
        self.v.append("Малый Стакан Липтона")
        self.f += 129

    def Small_drinks6(self):
        self.v.append("Малый Стакан Шоколадного Шейка")
        self.f += 144

    def Small_drinks7(self):
        self.v.append("Малый Стакан Клубничного Шейка")
        self.f += 144

    def Small_drinks8(self):
        self.v.append("Малый Стакан Ванильного Шейка")
        self.f += 144

    def Desserts1(self):
        self.v.append("Айс Твист Шоколадный")
        self.f += 179

    def Desserts2(self):
        self.v.append("Айс Твист Клубничный")
        self.f += 179

    def Desserts3(self):
        self.v.append("Сандэй Шоколадный")
        self.f += 134

    def Desserts4(self):
        self.v.append("Сандэй Клубничный")
        self.f += 134

    def Desserts5(self):
        self.v.append("Горячий Брауни")
        self.f += 129

    def Desserts6(self):
        self.v.append("Горячий Брауни С Мороженным")
        self.f += 165

    def Desserts7(self):
        self.v.append("Пирожок С Вишней")
        self.f += 109

    def Desserts8(self):
        self.v.append("Рожок")
        self.f += 49

    def Basket(self):
        self.tabs.addTab(self.basket, "Корзина")
        self.basket.setLayout(self.tab1_layout)

        for i in self.v:
            self.eats = QPushButton(i)
            self.tab1_layout.addWidget(self.eats)
        self.v.clear()

        self.btn20 = QLabel(f'Итого: {self.f}')
        self.tab1_layout.addWidget(self.btn20)

    def open_second_form(self):
        self.second_form = SecondForm()
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1450, 850)
        self.setWindowTitle('Бургер кинг')

        self.layout1 = QVBoxLayout()

        self.btn3 = QPushButton('Спасибо за покупку', self)
        self.btn3.setStyleSheet("font-size: 50px")

        self.layout1.addWidget(self.btn3)
        self.btn3.resize(1450, 850)

        self.btn3.clicked.connect(QApplication.instance().quit)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
