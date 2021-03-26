from PyQt5 import QtCore, QtGui, QtWidgets
from SBot import SupremeBot
import time

class Ui_MainWindow(object):

    def save_func(self):
            self.Dict = {
            "User_Profile":self.Gogle_Chrome_Path_field.toPlainText(),
            "product": [self.P1_Name.toPlainText(),self.P2_Name.toPlainText(),self.P3_Name.toPlainText(),self.P4_Name.toPlainText(),self.P5_Name.toPlainText(),self.P6_Name.toPlainText()],
            "color" : [self.P1_Color.toPlainText(), self.P2_Color.toPlainText(),self.P3_Color.toPlainText(),self.P4_Color.toPlainText(),self.P5_Color.toPlainText(),self.P6_Color.toPlainText()],
            "size" : [self.P1_Size.toPlainText(),self.P2_Size.toPlainText(),self.P3_Size.toPlainText(),self.P4_Size.toPlainText(),self.P5_Size.toPlainText(),self.P6_Size.toPlainText()],
            "category": [self.P1_cat.currentText(), self.P2_cat.currentText(),self.P3_cat.currentText(),self.P4_cat.currentText(),self.P5_cat.currentText(),self.P6_cat.currentText()],
            "fullname" : self.Full_Name_field.toPlainText(),
            "email" : self.Email_field.toPlainText(),
            "tel" : self.Tel_field.toPlainText(),
            "address" : self.Adress_Field.toPlainText(),
            "city" : self.City_field.toPlainText(),
            "zip" : self.Post_Code_field.toPlainText(),
            "country" : "POLAND",
            #"card" : "CRE",
            "number" : self.Credit_Card_Number_field.toPlainText(),
            "month" : self.month_field.currentText(),
            "year" : self.Year_field.currentText(),
            "ccv" : self.CCV_field.toPlainText(),
            }

            self.checkoutTime = int(self.Checkout_deley_field.toPlainText())
            self.BetweenItems = int(self.Betwee_Products_deley_field.toPlainText())
            self.BeforeBasket = int(self.BeforeBasket_Site_deley_field.toPlainText())
            self.RefreshPage = int(self.Refresh_every_field.toPlainText())
            self.MaxNumberOfRefresh = int(self.Number_of_refresh_field.toPlainText())


    def drop_func(self):
            how_many_items = 0
            for i in range(0,6):
                if self.Dict["category"][i] in "None":
                    break
                how_many_items+=1


            bot = SupremeBot(**self.Dict)
            bot.init_browser()
            found_product = False
            counter = 1
            start = time.time()


            while not found_product and counter < self.MaxNumberOfRefresh:
                found_product = bot.find_product(0)
                counter +=1
                time.sleep(self.RefreshPage)
            bot.visit_site(0)
            time.sleep(self.BetweenItems)
            if how_many_items is not 1:
                for i in range(1,how_many_items):
                    try:
                        bot.find_product(i)
                        time.sleep(self.BetweenItems)
                        bot.visit_site(i)
                    except Exception:
                        pass
            time.sleep(self.BeforeBasket)
            bot.checkout_fun(self.checkoutTime)
            end = time.time()
            print(end - start)





    def setupUi(self, MainWindow):
        #MainWindow.setWindowIcon(QtGui.QIcon('Icon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 479)
        MainWindow.setStyleSheet("")

        self.Dict = {}

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Profil_Chrome = QtWidgets.QGroupBox(self.centralwidget)
        self.Profil_Chrome.setGeometry(QtCore.QRect(0, 0, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Profil_Chrome.setFont(font)
        self.Profil_Chrome.setObjectName("Profil_Chrome")
        self.Gogle_Chrome_Path_field = QtWidgets.QTextEdit(self.Profil_Chrome)
        self.Gogle_Chrome_Path_field.setGeometry(QtCore.QRect(20, 20, 431, 31))
        self.Gogle_Chrome_Path_field.setObjectName("Gogle_Chrome_Path_field")
        self.Dane = QtWidgets.QGroupBox(self.centralwidget)
        self.Dane.setGeometry(QtCore.QRect(0, 70, 461, 381))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dane.setFont(font)
        self.Dane.setObjectName("Dane")
        self.Full_Name_field = QtWidgets.QTextEdit(self.Dane)
        self.Full_Name_field.setGeometry(QtCore.QRect(30, 40, 161, 31))
        self.Full_Name_field.setObjectName("Full_Name_field")
        self.label = QtWidgets.QLabel(self.Dane)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.label.setObjectName("label")
        self.Email_field = QtWidgets.QTextEdit(self.Dane)
        self.Email_field.setGeometry(QtCore.QRect(30, 100, 161, 31))
        self.Email_field.setObjectName("Email_field")
        self.label_2 = QtWidgets.QLabel(self.Dane)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.Tel_field = QtWidgets.QTextEdit(self.Dane)
        self.Tel_field.setGeometry(QtCore.QRect(30, 160, 161, 31))
        self.Tel_field.setObjectName("Tel_field")
        self.label_3 = QtWidgets.QLabel(self.Dane)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 47, 13))
        self.label_3.setObjectName("label_3")
        self.Adress_Field = QtWidgets.QTextEdit(self.Dane)
        self.Adress_Field.setGeometry(QtCore.QRect(30, 220, 161, 31))
        self.Adress_Field.setObjectName("Adress_Field")
        self.label_4 = QtWidgets.QLabel(self.Dane)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.Dane)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 47, 13))
        self.label_6.setObjectName("label_6")
        self.Post_Code_field = QtWidgets.QTextEdit(self.Dane)
        self.Post_Code_field.setGeometry(QtCore.QRect(30, 340, 81, 31))
        self.Post_Code_field.setObjectName("Post_Code_field")
        self.label_5 = QtWidgets.QLabel(self.Dane)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 61, 16))
        self.label_5.setObjectName("label_5")
        self.City_field = QtWidgets.QTextEdit(self.Dane)
        self.City_field.setGeometry(QtCore.QRect(30, 280, 161, 31))
        self.City_field.setObjectName("City_field")
        self.Credit_Card_Number_field = QtWidgets.QTextEdit(self.Dane)
        self.Credit_Card_Number_field.setGeometry(QtCore.QRect(240, 40, 161, 31))
        self.Credit_Card_Number_field.setObjectName("Credit_Card_Number_field")
        self.label_7 = QtWidgets.QLabel(self.Dane)
        self.label_7.setGeometry(QtCore.QRect(240, 20, 141, 16))
        self.label_7.setObjectName("label_7")
        self.month_field = QtWidgets.QComboBox(self.Dane)
        self.month_field.setGeometry(QtCore.QRect(240, 100, 51, 31))
        self.month_field.setObjectName("month_field")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.month_field.addItem("")
        self.Year_field = QtWidgets.QComboBox(self.Dane)
        self.Year_field.setGeometry(QtCore.QRect(300, 100, 51, 31))
        self.Year_field.setObjectName("Year_field")
        self.Year_field.addItem("")
        self.Year_field.addItem("")
        self.Year_field.addItem("")
        self.Year_field.addItem("")
        self.Year_field.addItem("")
        self.Year_field.addItem("")
        self.Year_field.addItem("")
        self.Year_field.addItem("")
        self.Year_field.addItem("")
        self.Year_field.addItem("")
        self.CCV_field = QtWidgets.QTextEdit(self.Dane)
        self.CCV_field.setGeometry(QtCore.QRect(360, 100, 41, 31))
        self.CCV_field.setObjectName("CCV_field")
        self.label_8 = QtWidgets.QLabel(self.Dane)
        self.label_8.setGeometry(QtCore.QRect(240, 140, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Dane)
        self.label_9.setGeometry(QtCore.QRect(300, 140, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Dane)
        self.label_10.setGeometry(QtCore.QRect(360, 140, 47, 13))
        self.label_10.setObjectName("label_10")
        self.Products = QtWidgets.QGroupBox(self.centralwidget)
        self.Products.setGeometry(QtCore.QRect(460, 0, 521, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Products.setFont(font)
        self.Products.setObjectName("Products")
        self.P1_cat = QtWidgets.QComboBox(self.Products)
        self.P1_cat.setGeometry(QtCore.QRect(20, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P1_cat.setFont(font)
        self.P1_cat.setObjectName("P1_cat")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.P1_cat.addItem("")
        self.label_11 = QtWidgets.QLabel(self.Products)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Products)
        self.label_12.setGeometry(QtCore.QRect(140, 30, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.P1_Name = QtWidgets.QTextEdit(self.Products)
        self.P1_Name.setGeometry(QtCore.QRect(140, 50, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P1_Name.setFont(font)
        self.P1_Name.setObjectName("P1_Name")
        self.label_13 = QtWidgets.QLabel(self.Products)
        self.label_13.setGeometry(QtCore.QRect(340, 30, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.P1_Size = QtWidgets.QTextEdit(self.Products)
        self.P1_Size.setGeometry(QtCore.QRect(340, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P1_Size.setFont(font)
        self.P1_Size.setObjectName("P1_Size")
        self.P1_Color = QtWidgets.QTextEdit(self.Products)
        self.P1_Color.setGeometry(QtCore.QRect(450, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P1_Color.setFont(font)
        self.P1_Color.setObjectName("P1_Color")
        self.label_14 = QtWidgets.QLabel(self.Products)
        self.label_14.setGeometry(QtCore.QRect(450, 30, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.P2_Size = QtWidgets.QTextEdit(self.Products)
        self.P2_Size.setGeometry(QtCore.QRect(340, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P2_Size.setFont(font)
        self.P2_Size.setObjectName("P2_Size")
        self.P2_cat = QtWidgets.QComboBox(self.Products)
        self.P2_cat.setGeometry(QtCore.QRect(20, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P2_cat.setFont(font)
        self.P2_cat.setObjectName("P2_cat")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_cat.addItem("")
        self.P2_Color = QtWidgets.QTextEdit(self.Products)
        self.P2_Color.setGeometry(QtCore.QRect(450, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P2_Color.setFont(font)
        self.P2_Color.setObjectName("P2_Color")
        self.P2_Name = QtWidgets.QTextEdit(self.Products)
        self.P2_Name.setGeometry(QtCore.QRect(140, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P2_Name.setFont(font)
        self.P2_Name.setObjectName("P2_Name")
        self.P3_Size = QtWidgets.QTextEdit(self.Products)
        self.P3_Size.setGeometry(QtCore.QRect(340, 110, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P3_Size.setFont(font)
        self.P3_Size.setObjectName("P3_Size")
        self.P3_cat = QtWidgets.QComboBox(self.Products)
        self.P3_cat.setGeometry(QtCore.QRect(20, 110, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P3_cat.setFont(font)
        self.P3_cat.setObjectName("P3_cat")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_cat.addItem("")
        self.P3_Color = QtWidgets.QTextEdit(self.Products)
        self.P3_Color.setGeometry(QtCore.QRect(450, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P3_Color.setFont(font)
        self.P3_Color.setObjectName("P3_Color")
        self.P3_Name = QtWidgets.QTextEdit(self.Products)
        self.P3_Name.setGeometry(QtCore.QRect(140, 110, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P3_Name.setFont(font)
        self.P3_Name.setObjectName("P3_Name")
        self.P4_Name = QtWidgets.QTextEdit(self.Products)
        self.P4_Name.setGeometry(QtCore.QRect(140, 140, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P4_Name.setFont(font)
        self.P4_Name.setObjectName("P4_Name")
        self.P5_Color = QtWidgets.QTextEdit(self.Products)
        self.P5_Color.setGeometry(QtCore.QRect(450, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P5_Color.setFont(font)
        self.P5_Color.setObjectName("P5_Color")
        self.P4_Size = QtWidgets.QTextEdit(self.Products)
        self.P4_Size.setGeometry(QtCore.QRect(340, 140, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P4_Size.setFont(font)
        self.P4_Size.setObjectName("P4_Size")
        self.P5_cat = QtWidgets.QComboBox(self.Products)
        self.P5_cat.setGeometry(QtCore.QRect(20, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P5_cat.setFont(font)
        self.P5_cat.setObjectName("P5_cat")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P5_cat.addItem("")
        self.P6_Color = QtWidgets.QTextEdit(self.Products)
        self.P6_Color.setGeometry(QtCore.QRect(450, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P6_Color.setFont(font)
        self.P6_Color.setObjectName("P6_Color")
        self.P4_Color = QtWidgets.QTextEdit(self.Products)
        self.P4_Color.setGeometry(QtCore.QRect(450, 140, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P4_Color.setFont(font)
        self.P4_Color.setObjectName("P4_Color")
        self.P5_Size = QtWidgets.QTextEdit(self.Products)
        self.P5_Size.setGeometry(QtCore.QRect(340, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P5_Size.setFont(font)
        self.P5_Size.setObjectName("P5_Size")
        self.P6_Name = QtWidgets.QTextEdit(self.Products)
        self.P6_Name.setGeometry(QtCore.QRect(140, 200, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P6_Name.setFont(font)
        self.P6_Name.setObjectName("P6_Name")
        self.P4_cat = QtWidgets.QComboBox(self.Products)
        self.P4_cat.setGeometry(QtCore.QRect(20, 140, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P4_cat.setFont(font)
        self.P4_cat.setObjectName("P4_cat")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P4_cat.addItem("")
        self.P5_Name = QtWidgets.QTextEdit(self.Products)
        self.P5_Name.setGeometry(QtCore.QRect(140, 170, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P5_Name.setFont(font)
        self.P5_Name.setObjectName("P5_Name")
        self.P6_Size = QtWidgets.QTextEdit(self.Products)
        self.P6_Size.setGeometry(QtCore.QRect(340, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P6_Size.setFont(font)
        self.P6_Size.setObjectName("P6_Size")
        self.P6_cat = QtWidgets.QComboBox(self.Products)
        self.P6_cat.setGeometry(QtCore.QRect(20, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.P6_cat.setFont(font)
        self.P6_cat.setObjectName("P6_cat")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.P6_cat.addItem("")
        self.Deley_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Deley_box.setGeometry(QtCore.QRect(460, 250, 131, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Deley_box.setFont(font)
        self.Deley_box.setObjectName("Deley_box")
        self.label_15 = QtWidgets.QLabel(self.Deley_box)
        self.label_15.setGeometry(QtCore.QRect(30, 30, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.Checkout_deley_field = QtWidgets.QTextEdit(self.Deley_box)
        self.Checkout_deley_field.setGeometry(QtCore.QRect(30, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Checkout_deley_field.setFont(font)
        self.Checkout_deley_field.setObjectName("Checkout_deley_field")
        self.Betwee_Products_deley_field = QtWidgets.QTextEdit(self.Deley_box)
        self.Betwee_Products_deley_field.setGeometry(QtCore.QRect(30, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Betwee_Products_deley_field.setFont(font)
        self.Betwee_Products_deley_field.setObjectName("Betwee_Products_deley_field")
        self.label_16 = QtWidgets.QLabel(self.Deley_box)
        self.label_16.setGeometry(QtCore.QRect(30, 80, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.BeforeBasket_Site_deley_field = QtWidgets.QTextEdit(self.Deley_box)
        self.BeforeBasket_Site_deley_field.setGeometry(QtCore.QRect(30, 150, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.BeforeBasket_Site_deley_field.setFont(font)
        self.BeforeBasket_Site_deley_field.setObjectName("BeforeBasket_Site_deley_field")
        self.label_17 = QtWidgets.QLabel(self.Deley_box)
        self.label_17.setGeometry(QtCore.QRect(30, 130, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.Drop_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Drop_Button.setGeometry(QtCore.QRect(810, 380, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Drop_Button.setFont(font)
        self.Drop_Button.setObjectName("Drop_Button")
        self.Settings_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Settings_box.setGeometry(QtCore.QRect(590, 250, 211, 80))
        self.Settings_box.setObjectName("Settings_box")
        self.Refresh_every_field = QtWidgets.QTextEdit(self.Settings_box)
        self.Refresh_every_field.setGeometry(QtCore.QRect(20, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Refresh_every_field.setFont(font)
        self.Refresh_every_field.setObjectName("Refresh_every_field")
        self.label_24 = QtWidgets.QLabel(self.Settings_box)
        self.label_24.setGeometry(QtCore.QRect(20, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.Settings_box)
        self.label_25.setGeometry(QtCore.QRect(110, 30, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.Number_of_refresh_field = QtWidgets.QTextEdit(self.Settings_box)
        self.Number_of_refresh_field.setGeometry(QtCore.QRect(110, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Number_of_refresh_field.setFont(font)
        self.Number_of_refresh_field.setObjectName("Number_of_refresh_field")
        self.SAVE_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SAVE_Button.setGeometry(QtCore.QRect(630, 380, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SAVE_Button.setFont(font)
        self.SAVE_Button.setObjectName("SAVE_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KroboCop"))
        self.Profil_Chrome.setTitle(_translate("MainWindow", "Profil Chrome"))
        self.Gogle_Chrome_Path_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Dane.setTitle(_translate("MainWindow", "Dane"))
        self.Full_Name_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.25pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Full Name"))
        self.Email_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.25pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.Tel_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.25pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Adress"))
        self.Adress_Field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.25pt;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Tel"))
        self.label_6.setText(_translate("MainWindow", "City"))
        self.Post_Code_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.25pt;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Post Code"))
        self.City_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.25pt;\"><br /></p></body></html>"))
        self.Credit_Card_Number_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.25pt;\"><br /></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Credit Card Number"))
        self.month_field.setItemText(0, _translate("MainWindow", "01"))
        self.month_field.setItemText(1, _translate("MainWindow", "02"))
        self.month_field.setItemText(2, _translate("MainWindow", "03"))
        self.month_field.setItemText(3, _translate("MainWindow", "04"))
        self.month_field.setItemText(4, _translate("MainWindow", "05"))
        self.month_field.setItemText(5, _translate("MainWindow", "06"))
        self.month_field.setItemText(6, _translate("MainWindow", "07"))
        self.month_field.setItemText(7, _translate("MainWindow", "08"))
        self.month_field.setItemText(8, _translate("MainWindow", "09"))
        self.month_field.setItemText(9, _translate("MainWindow", "10"))
        self.month_field.setItemText(10, _translate("MainWindow", "11"))
        self.month_field.setItemText(11, _translate("MainWindow", "12"))
        self.Year_field.setItemText(0, _translate("MainWindow", "2021"))
        self.Year_field.setItemText(1, _translate("MainWindow", "2022"))
        self.Year_field.setItemText(2, _translate("MainWindow", "2023"))
        self.Year_field.setItemText(3, _translate("MainWindow", "2024"))
        self.Year_field.setItemText(4, _translate("MainWindow", "2025"))
        self.Year_field.setItemText(5, _translate("MainWindow", "2026"))
        self.Year_field.setItemText(6, _translate("MainWindow", "2027"))
        self.Year_field.setItemText(7, _translate("MainWindow", "2028"))
        self.Year_field.setItemText(8, _translate("MainWindow", "2029"))
        self.Year_field.setItemText(9, _translate("MainWindow", "2030"))
        self.CCV_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.25pt;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Month"))
        self.label_9.setText(_translate("MainWindow", "Year"))
        self.label_10.setText(_translate("MainWindow", "CCV"))
        self.Products.setTitle(_translate("MainWindow", "Basket"))
        self.P1_cat.setItemText(0, _translate("MainWindow", "None"))
        self.P1_cat.setItemText(1, _translate("MainWindow", "jackets"))
        self.P1_cat.setItemText(2, _translate("MainWindow", "shirts"))
        self.P1_cat.setItemText(3, _translate("MainWindow", "tops/sweaters"))
        self.P1_cat.setItemText(4, _translate("MainWindow", "pants"))
        self.P1_cat.setItemText(5, _translate("MainWindow", "shorts"))
        self.P1_cat.setItemText(6, _translate("MainWindow", "t-shirts"))
        self.P1_cat.setItemText(7, _translate("MainWindow", "hats"))
        self.P1_cat.setItemText(8, _translate("MainWindow", "bags"))
        self.P1_cat.setItemText(9, _translate("MainWindow", "accessories"))
        self.P1_cat.setItemText(10, _translate("MainWindow", "shoes"))
        self.P1_cat.setItemText(11, _translate("MainWindow", "skate"))
        self.label_11.setText(_translate("MainWindow", "Category"))
        self.label_12.setText(_translate("MainWindow", "Name"))
        self.P1_Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Size"))
        self.P1_Size.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P1_Color.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Color"))
        self.P2_Size.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P2_cat.setItemText(0, _translate("MainWindow", "None"))
        self.P2_cat.setItemText(1, _translate("MainWindow", "jackets"))
        self.P2_cat.setItemText(2, _translate("MainWindow", "shirts"))
        self.P2_cat.setItemText(3, _translate("MainWindow", "tops/sweaters"))
        self.P2_cat.setItemText(4, _translate("MainWindow", "pants"))
        self.P2_cat.setItemText(5, _translate("MainWindow", "shorts"))
        self.P2_cat.setItemText(6, _translate("MainWindow", "t-shirts"))
        self.P2_cat.setItemText(7, _translate("MainWindow", "hats"))
        self.P2_cat.setItemText(8, _translate("MainWindow", "bags"))
        self.P2_cat.setItemText(9, _translate("MainWindow", "accessories"))
        self.P2_cat.setItemText(10, _translate("MainWindow", "shoes"))
        self.P2_cat.setItemText(11, _translate("MainWindow", "skate"))
        self.P2_Color.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P2_Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P3_Size.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P3_cat.setItemText(0, _translate("MainWindow", "None"))
        self.P3_cat.setItemText(1, _translate("MainWindow", "jackets"))
        self.P3_cat.setItemText(2, _translate("MainWindow", "shirts"))
        self.P3_cat.setItemText(3, _translate("MainWindow", "tops/sweaters"))
        self.P3_cat.setItemText(4, _translate("MainWindow", "pants"))
        self.P3_cat.setItemText(5, _translate("MainWindow", "shorts"))
        self.P3_cat.setItemText(6, _translate("MainWindow", "t-shirts"))
        self.P3_cat.setItemText(7, _translate("MainWindow", "hats"))
        self.P3_cat.setItemText(8, _translate("MainWindow", "bags"))
        self.P3_cat.setItemText(9, _translate("MainWindow", "accessories"))
        self.P3_cat.setItemText(10, _translate("MainWindow", "shoes"))
        self.P3_cat.setItemText(11, _translate("MainWindow", "skate"))
        self.P3_Color.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P3_Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P4_Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P5_Color.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P4_Size.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P5_cat.setItemText(0, _translate("MainWindow", "None"))
        self.P5_cat.setItemText(1, _translate("MainWindow", "jackets"))
        self.P5_cat.setItemText(2, _translate("MainWindow", "shirts"))
        self.P5_cat.setItemText(3, _translate("MainWindow", "tops/sweaters"))
        self.P5_cat.setItemText(4, _translate("MainWindow", "pants"))
        self.P5_cat.setItemText(5, _translate("MainWindow", "shorts"))
        self.P5_cat.setItemText(6, _translate("MainWindow", "t-shirts"))
        self.P5_cat.setItemText(7, _translate("MainWindow", "hats"))
        self.P5_cat.setItemText(8, _translate("MainWindow", "bags"))
        self.P5_cat.setItemText(9, _translate("MainWindow", "accessories"))
        self.P5_cat.setItemText(10, _translate("MainWindow", "shoes"))
        self.P5_cat.setItemText(11, _translate("MainWindow", "skate"))
        self.P6_Color.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P4_Color.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P5_Size.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P6_Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P4_cat.setItemText(0, _translate("MainWindow", "None"))
        self.P4_cat.setItemText(1, _translate("MainWindow", "jackets"))
        self.P4_cat.setItemText(2, _translate("MainWindow", "shirts"))
        self.P4_cat.setItemText(3, _translate("MainWindow", "tops/sweaters"))
        self.P4_cat.setItemText(4, _translate("MainWindow", "pants"))
        self.P4_cat.setItemText(5, _translate("MainWindow", "shorts"))
        self.P4_cat.setItemText(6, _translate("MainWindow", "t-shirts"))
        self.P4_cat.setItemText(7, _translate("MainWindow", "hats"))
        self.P4_cat.setItemText(8, _translate("MainWindow", "bags"))
        self.P4_cat.setItemText(9, _translate("MainWindow", "accessories"))
        self.P4_cat.setItemText(10, _translate("MainWindow", "shoes"))
        self.P4_cat.setItemText(11, _translate("MainWindow", "skate"))
        self.P5_Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P6_Size.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.P6_cat.setItemText(0, _translate("MainWindow", "None"))
        self.P6_cat.setItemText(1, _translate("MainWindow", "jackets"))
        self.P6_cat.setItemText(2, _translate("MainWindow", "shirts"))
        self.P6_cat.setItemText(3, _translate("MainWindow", "tops/sweaters"))
        self.P6_cat.setItemText(4, _translate("MainWindow", "pants"))
        self.P6_cat.setItemText(5, _translate("MainWindow", "shorts"))
        self.P6_cat.setItemText(6, _translate("MainWindow", "t-shirts"))
        self.P6_cat.setItemText(7, _translate("MainWindow", "hats"))
        self.P6_cat.setItemText(8, _translate("MainWindow", "bags"))
        self.P6_cat.setItemText(9, _translate("MainWindow", "accessories"))
        self.P6_cat.setItemText(10, _translate("MainWindow", "shoes"))
        self.P6_cat.setItemText(11, _translate("MainWindow", "skate"))
        self.Deley_box.setTitle(_translate("MainWindow", "Deley"))
        self.label_15.setText(_translate("MainWindow", "Checkout"))
        self.Checkout_deley_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.Betwee_Products_deley_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "Between products"))
        self.BeforeBasket_Site_deley_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "Before Basket Site"))
        self.Drop_Button.setText(_translate("MainWindow", "DROP!!!"))
        self.Settings_box.setTitle(_translate("MainWindow", "Settings"))
        self.Refresh_every_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "Refresh every"))
        self.label_25.setText(_translate("MainWindow", "Numberof Refresh "))
        self.Number_of_refresh_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.SAVE_Button.setText(_translate("MainWindow", "SAVE"))

        #przyciski save i drop
        self.SAVE_Button.clicked.connect(self.save_func)
        self.Drop_Button.clicked.connect(self.drop_func)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
