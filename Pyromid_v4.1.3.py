from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFrame, QGridLayout, QFormLayout, QLabel, QTextBrowser, QSizePolicy, QLayout, QHBoxLayout, QPushButton, QToolButton, QRadioButton, QLineEdit, QFileDialog, QProgressDialog
from PyQt5.QtCore import Qt, QSize, QCoreApplication, QMetaObject, QTimer, pyqtSignal, QThread
from PyQt5.QtGui import QFont, QIcon, QTextDocument, QTextCursor, QPixmap, QTextOption, QFileOpenEvent
import os
import sys
from cryptofuzz import Convertor, Ethereum, Tron, Dash, Litecoin
from random import choice
currentDir = os.path.dirname(__file__)
rcFilePath = os.path.join(currentDir, 'media_rc.py')
if os.path.exists(rcFilePath):
    import media_rc
    import base64
app = QApplication([])
conv = Convertor()
eth = Ethereum()
trx = Tron()
dash = Dash()
ltc = Litecoin()

class StyleBoard:
    
    def __init__(self = None):
        super().__init__()
        styles = {
            'label_3': {
                'css': 'background-color: #4f8c4b; color: white; border: 1px solid #4f8c4b; border-top-left-radius: 6px; border-bottom-left-radius: 6px;' },
            'label': {
                'css': 'background-color: #5a5a5a; color: white; border: 1px solid #5a5a5a; border-top-left-radius: 6px; border-bottom-left-radius: 6px;' },
            'textBrowser': {
                'css': 'border: 1px solid #40af50; border-radius: 6px; color: #52ff52;  background-color: rgb(17, 50, 31);' },
            'label_value': {
                'css': 'border: 1px solid #4f8c4b; border-left: 6px solid #4f8c4b; border-top-right-radius: 6px; border-bottom-right-radius: 6px; background-color: white; padding-right: 9px;' },
            'label_gen': {
                'css': 'border: 1px solid #a84845; border-left: 6px solid #a84845; border-top-right-radius: 6px; border-bottom-right-radius: 6px; background-color: white; margin-right: 3px; color: #a84845;' },
            'label_7': {
                'css': 'background-color: #a84845; color: white; border: 1px solid #a84845; border-top-left-radius: 6px; border-bottom-left-radius: 6px;' },
            'label_6': {
                'css': 'background-color: #a84845; color: white; border: 1px solid #a84845; border-top-left-radius: 6px; border-bottom-left-radius: 6px;' },
            'label_check': {
                'css': 'border: 1px solid #a84845; border-left: 6px solid #a84845; border-top-right-radius: 6px; border-bottom-right-radius: 6px; background-color: white; padding-right: 9px; color: #a84845;' },
            'label_value_found': {
                'css': 'border: 1px solid #5a5a5a; border-left: 6px solid #5a5a5a; border-top-right-radius: 6px; border-bottom-right-radius: 6px; background-color: white; margin-right: 3px;' } }
        css = {
            'LineFile': 'border: 1px  solid #5a5a5a; border-left: 6px solid #5a5a5a; border-top-right-radius: 6px; border-bottom-right-radius: 6px; background-color: white; margin-right: 3px;',
            'toolButton': 'border: 1px solid #545454;border-radius: 6px; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.522727 rgba(255, 255, 255, 255), stop:0.954545 rgba(225, 225, 225, 255));' }
        self.label_value_found = styles['label_value_found']['css']
        self.label_gen = styles['label_gen']['css']
        self.label_value = styles['label_value']['css']
        self.textBrowser = styles['textBrowser']['css']
        self.label_3 = styles['label_3']['css']
        self.label = styles['label']['css']
        self.label_check = styles['label_check']['css']
        self.label_7 = styles['label_7']['css']
        self.label_6 = styles['label_6']['css']
        self.LineFile = str(css['LineFile'])
        self.toolButton = str(css['toolButton'])

    __classcell__ = None


class FileReader(QThread):
    data_read = pyqtSignal(list)
    progress = pyqtSignal(int)
    
    def __init__(self = None, filename = None):
        super().__init__()
        self.filename = filename

    
    def run(self):
        pass
    # WARNING: Decompyle incomplete

    __classcell__ = None


class Ui_Error(QWidget):
    
    def __init__(self = None):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(409, 204)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName('gridLayout')
        self.frame = QFrame(self)
        self.frame.setMinimumSize(QSize(391, 186))
        self.frame.setMaximumSize(QSize(391, 186))
        self.frame.setStyleSheet('border: 2px solid #bf4a4c;\nborder-radius: 12px;\nbackground-color: white;')
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName('frame')
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName('gridLayout_3')
        self.labelIcon = QLabel(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelIcon.sizePolicy().hasHeightForWidth())
        self.labelIcon.setSizePolicy(sizePolicy)
        self.labelIcon.setMinimumSize(QSize(120, 110))
        self.labelIcon.setMaximumSize(QSize(120, 110))
        self.labelIcon.setStyleSheet('border:none; border-radius: none;padding: 10px; margin: 5px; ')
        self.labelIcon.setText('')
        self.labelIcon.setPixmap(QPixmap(':/media/media/error.png'))
        self.labelIcon.setScaledContents(True)
        self.labelIcon.setObjectName('labelIcon')
        self.gridLayout_3.addWidget(self.labelIcon, 0, 0, 1, 1)
        self.textBrowser = QTextBrowser(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QSize(243, 109))
        self.textBrowser.setMaximumSize(QSize(243, 109))
        font = QFont()
        font.setFamily('Tahoma')
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet('border: none; border-radius: none; padding: 10px; margin: 5px; \ncolor: rgb(117, 41, 42);letter-spacing: 1px;')
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName('textBrowser')
        self.gridLayout_3.addWidget(self.textBrowser, 0, 1, 1, 2)
        self.Button_Close = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Close.sizePolicy().hasHeightForWidth())
        self.Button_Close.setSizePolicy(sizePolicy)
        self.Button_Close.setMinimumSize(QSize(148, 45))
        self.Button_Close.setMaximumSize(QSize(150, 16777215))
        self.Button_Close.setStyleSheet('border: 1px solid #cacaca;\nborder-radius: 6px;\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.727273, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(239, 239, 239, 255));\npadding: 10px;\nmargin: 5px')
        icon = QIcon()
        icon.addPixmap(QPixmap(':/media/media/cross.png'), QIcon.Normal, QIcon.On)
        self.Button_Close.setIcon(icon)
        self.Button_Close.setIconSize(QSize(18, 18))
        self.Button_Close.setObjectName('Button_Close')
        self.gridLayout_3.addWidget(self.Button_Close, 1, 0, 1, 2)
        self.Button_OK = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_OK.sizePolicy().hasHeightForWidth())
        self.Button_OK.setSizePolicy(sizePolicy)
        self.Button_OK.setMinimumSize(QSize(215, 45))
        self.Button_OK.setStyleSheet('border: 1px solid #cacaca;\nborder-radius: 6px;\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.727273, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(239, 239, 239, 255));\npadding: 10px;\nmargin: 5px')
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(':/media/media/tick.png'), QIcon.Normal, QIcon.On)
        self.Button_OK.setIcon(icon1)
        self.Button_OK.setIconSize(QSize(22, 22))
        self.Button_OK.setObjectName('Button_OK')
        self.gridLayout_3.addWidget(self.Button_OK, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.Button_Close.clicked.connect(self.close)
        self.Button_OK.clicked.connect(self.close)
        self.setWindowTitle('ERROR')
        self.labelIcon.setText('')
        self.Button_Close.setText('Close')
        self.Button_OK.setText('Ok')
        QMetaObject.connectSlotsByName(self)

    __classcell__ = None


class Ui_VertMain(QWidget):
    z = pyqtSignal(int)
    logger = pyqtSignal(str)
    importValue = pyqtSignal(int)
    
    def __init__(self = None):
        super(self.__class__, self).__init__()
        self.error = Ui_Error()
        self.progressDialog = None
        self.scan = False
        self.index_forceStop = False
        self.resize(419, 860)
        self.styles = StyleBoard()
        self.z = 0
        self.importValue = 0
        self.checked = 0
        self.found = 0
        self.total_num = 0
        self.targetList = []
        self.FilePath = None
        self.FileReader = None
        self.indexFile = False
        self.setMinimumSize(QSize(419, 860))
        self.gridLayout_6 = QGridLayout(self)
        self.gridLayout_6.setObjectName('gridLayout_6')
        self.Frame_Footer = QFrame(self)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_Footer.sizePolicy().hasHeightForWidth())
        self.Frame_Footer.setSizePolicy(sizePolicy)
        self.Frame_Footer.setMinimumSize(QSize(0, 40))
        self.Frame_Footer.setMaximumSize(QSize(16777215, 120))
        self.Frame_Footer.setFrameShape(QFrame.StyledPanel)
        self.Frame_Footer.setFrameShadow(QFrame.Raised)
        self.Frame_Footer.setObjectName('Frame_Footer')
        self.gridLayout_8 = QGridLayout(self.Frame_Footer)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName('gridLayout_8')
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.button_close = QPushButton(self.Frame_Footer)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setMaximumSize(QSize(16777215, 50))
        icon = QIcon()
        icon.addPixmap(QPixmap(':/media/media/cross.png'), QIcon.Normal, QIcon.On)
        self.button_close.setIcon(icon)
        self.button_close.setObjectName('button_close')
        self.horizontalLayout.addWidget(self.button_close)
        self.button_forcestop = QPushButton(self.Frame_Footer)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_forcestop.sizePolicy().hasHeightForWidth())
        self.button_forcestop.setSizePolicy(sizePolicy)
        self.button_forcestop.setMaximumSize(QSize(16777215, 50))
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(':/media/media/link_break.png'), QIcon.Normal, QIcon.On)
        self.button_forcestop.setIcon(icon1)
        self.button_forcestop.setIconSize(QSize(19, 19))
        self.button_forcestop.setObjectName('button_forcestop')
        self.horizontalLayout.addWidget(self.button_forcestop)
        self.button_start = QPushButton(self.Frame_Footer)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy)
        self.button_start.setMaximumSize(QSize(16777215, 50))
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(':/media/media/update.png'), QIcon.Normal, QIcon.On)
        self.button_start.setIcon(icon2)
        self.button_start.setIconSize(QSize(20, 20))
        self.button_start.setObjectName('button_start')
        self.horizontalLayout.addWidget(self.button_start)
        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.Frame_Footer, 3, 0, 1, 1)
        self.Frame_textBrowser = QFrame(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_textBrowser.sizePolicy().hasHeightForWidth())
        self.Frame_textBrowser.setSizePolicy(sizePolicy)
        self.Frame_textBrowser.setMinimumSize(QSize(0, 430))
        self.Frame_textBrowser.setMaximumSize(QSize(16777215, 1200))
        self.Frame_textBrowser.setFrameShape(QFrame.StyledPanel)
        self.Frame_textBrowser.setFrameShadow(QFrame.Raised)
        self.Frame_textBrowser.setObjectName('Frame_textBrowser')
        self.gridLayout_5 = QGridLayout(self.Frame_textBrowser)
        self.gridLayout_5.setObjectName('gridLayout_5')
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_9.setObjectName('gridLayout_9')
        self.textBrowser = QTextBrowser(self.Frame_textBrowser)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QSize(0, 400))
        self.textBrowser.setMaximumSize(QSize(16777215, 1200))
        self.textBrowser.setStyleSheet(self.styles.textBrowser)
        self.textBrowser.setObjectName('textBrowser')
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gridLayout_9.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_9, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.Frame_textBrowser, 2, 0, 1, 1)
        self.Frame_Header = QFrame(self)
        self.Frame_Header.setMinimumSize(QSize(360, 320))
        self.Frame_Header.setMaximumSize(QSize(16777215, 380))
        self.Frame_Header.setFrameShape(QFrame.StyledPanel)
        self.Frame_Header.setFrameShadow(QFrame.Raised)
        self.Frame_Header.setObjectName('Frame_Header')
        self.gridLayout_2 = QGridLayout(self.Frame_Header)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName('gridLayout_2')
        self.line = QFrame(self.Frame_Header)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName('line')
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        self.Layout_Radio = QGridLayout()
        self.Layout_Radio.setObjectName('Layout_Radio')
        self.radioButton_eth = QRadioButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_eth.sizePolicy().hasHeightForWidth())
        self.radioButton_eth.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.radioButton_eth.setFont(font)
        self.radioButton_eth.setObjectName('radioButton_eth')
        self.Layout_Radio.addWidget(self.radioButton_eth, 0, 1, 1, 1)
        self.radioButton_btc = QRadioButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_btc.sizePolicy().hasHeightForWidth())
        self.radioButton_btc.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.radioButton_btc.setFont(font)
        self.radioButton_btc.setWhatsThis('')
        self.radioButton_btc.setObjectName('radioButton_btc')
        self.Layout_Radio.addWidget(self.radioButton_btc, 0, 0, 1, 1)
        self.radioButton_trx = QRadioButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_trx.sizePolicy().hasHeightForWidth())
        self.radioButton_trx.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.radioButton_trx.setFont(font)
        self.radioButton_trx.setObjectName('radioButton_trx')
        self.Layout_Radio.addWidget(self.radioButton_trx, 0, 2, 1, 1)
        self.radioButton_ltc = QRadioButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_ltc.sizePolicy().hasHeightForWidth())
        self.radioButton_ltc.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.radioButton_ltc.setFont(font)
        self.radioButton_ltc.setObjectName('radioButton_ltc')
        self.Layout_Radio.addWidget(self.radioButton_ltc, 1, 0, 1, 1)
        self.radioButton_bnb = QRadioButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_bnb.sizePolicy().hasHeightForWidth())
        self.radioButton_bnb.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.radioButton_bnb.setFont(font)
        self.radioButton_bnb.setObjectName('radioButton_bnb')
        self.Layout_Radio.addWidget(self.radioButton_bnb, 1, 1, 1, 1)
        self.radioButton_dash = QRadioButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_dash.sizePolicy().hasHeightForWidth())
        self.radioButton_dash.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.radioButton_dash.setFont(font)
        self.radioButton_dash.setObjectName('radioButton_dash')
        self.Layout_Radio.addWidget(self.radioButton_dash, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.Layout_Radio, 1, 0, 1, 1)
        self.Layout_Gen_Chk = QGridLayout()
        self.Layout_Gen_Chk.setContentsMargins(3, 6, 3, 6)
        self.Layout_Gen_Chk.setSpacing(0)
        self.Layout_Gen_Chk.setObjectName('Layout_Gen_Chk')
        self.Label_Check_Value = QLabel(self.Frame_Header)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.Label_Check_Value.setFont(font)
        self.Label_Check_Value.setStyleSheet(self.styles.label_gen)
        self.Label_Check_Value.setIndent(3)
        self.Label_Check_Value.setObjectName('Label_Check_Value')
        self.Layout_Gen_Chk.addWidget(self.Label_Check_Value, 0, 1, 1, 1)
        self.Label_Import = QLabel(self.Frame_Header)
        font = QFont()
        font.setFamily('Verdana')
        self.Label_Import.setFont(font)
        self.Label_Import.setStyleSheet(self.styles.label_7)
        self.Label_Import.setObjectName('Label_Import')
        self.Layout_Gen_Chk.addWidget(self.Label_Import, 0, 2, 1, 1)
        self.Label_Check = QLabel(self.Frame_Header)
        font = QFont()
        font.setFamily('Verdana')
        self.Label_Check.setFont(font)
        self.Label_Check.setStyleSheet(self.styles.label_6)
        self.Label_Check.setObjectName('Label_Check')
        self.Layout_Gen_Chk.addWidget(self.Label_Check, 0, 0, 1, 1)
        self.Label_Import_Value = QLabel(self.Frame_Header)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.Label_Import_Value.setFont(font)
        self.Label_Import_Value.setStyleSheet(self.styles.label_check)
        self.Label_Import_Value.setIndent(3)
        self.Label_Import_Value.setObjectName('Label_Import_Value')
        self.Layout_Gen_Chk.addWidget(self.Label_Import_Value, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.Layout_Gen_Chk, 4, 0, 1, 1)
        self.Layout_Header_Buttons = QGridLayout()
        self.Layout_Header_Buttons.setContentsMargins(3, 3, 3, 3)
        self.Layout_Header_Buttons.setSpacing(3)
        self.Layout_Header_Buttons.setObjectName('Layout_Header_Buttons')
        self.TButton_ltc = QToolButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TButton_ltc.sizePolicy().hasHeightForWidth())
        self.TButton_ltc.setSizePolicy(sizePolicy)
        self.TButton_ltc.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(8)
        self.TButton_ltc.setFont(font)
        self.TButton_ltc.setText('')
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(':/crypto/media/crypto/__ltc__.png'), QIcon.Normal, QIcon.On)
        self.TButton_ltc.setIcon(icon3)
        self.TButton_ltc.setIconSize(QSize(53, 53))
        self.TButton_ltc.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.TButton_ltc.setAutoRaise(False)
        self.TButton_ltc.setArrowType(Qt.NoArrow)
        self.TButton_ltc.setObjectName('TButton_ltc')
        self.Layout_Header_Buttons.addWidget(self.TButton_ltc, 1, 0, 1, 1)
        self.TButton_btc = QToolButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TButton_btc.sizePolicy().hasHeightForWidth())
        self.TButton_btc.setSizePolicy(sizePolicy)
        self.TButton_btc.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(8)
        self.TButton_btc.setFont(font)
        self.TButton_btc.setText('')
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(':/crypto/media/crypto/__btc__.png'), QIcon.Normal, QIcon.On)
        self.TButton_btc.setIcon(icon4)
        self.TButton_btc.setIconSize(QSize(53, 53))
        self.TButton_btc.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.TButton_btc.setAutoRaise(False)
        self.TButton_btc.setArrowType(Qt.NoArrow)
        self.TButton_btc.setObjectName('TButton_btc')
        self.Layout_Header_Buttons.addWidget(self.TButton_btc, 0, 0, 1, 1)
        self.TButton_eth = QToolButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TButton_eth.sizePolicy().hasHeightForWidth())
        self.TButton_eth.setSizePolicy(sizePolicy)
        self.TButton_eth.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(8)
        self.TButton_eth.setFont(font)
        self.TButton_eth.setText('')
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(':/crypto/media/crypto/__eth__.png'), QIcon.Normal, QIcon.On)
        self.TButton_eth.setIcon(icon5)
        self.TButton_eth.setIconSize(QSize(53, 53))
        self.TButton_eth.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.TButton_eth.setAutoRaise(False)
        self.TButton_eth.setArrowType(Qt.NoArrow)
        self.TButton_eth.setObjectName('TButton_eth')
        self.Layout_Header_Buttons.addWidget(self.TButton_eth, 0, 1, 1, 1)
        self.TButton_trx = QToolButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TButton_trx.sizePolicy().hasHeightForWidth())
        self.TButton_trx.setSizePolicy(sizePolicy)
        self.TButton_trx.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(8)
        self.TButton_trx.setFont(font)
        self.TButton_trx.setText('')
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(':/crypto/media/crypto/__trx__.png'), QIcon.Normal, QIcon.On)
        self.TButton_trx.setIcon(icon6)
        self.TButton_trx.setIconSize(QSize(53, 53))
        self.TButton_trx.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.TButton_trx.setAutoRaise(False)
        self.TButton_trx.setArrowType(Qt.NoArrow)
        self.TButton_trx.setObjectName('TButton_trx')
        self.Layout_Header_Buttons.addWidget(self.TButton_trx, 0, 2, 1, 1)
        self.TButton_bnb = QToolButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TButton_bnb.sizePolicy().hasHeightForWidth())
        self.TButton_bnb.setSizePolicy(sizePolicy)
        self.TButton_bnb.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(8)
        self.TButton_bnb.setFont(font)
        self.TButton_bnb.setText('')
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(':/crypto/media/crypto/__bnb__.png'), QIcon.Normal, QIcon.On)
        self.TButton_bnb.setIcon(icon7)
        self.TButton_bnb.setIconSize(QSize(53, 53))
        self.TButton_bnb.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.TButton_bnb.setAutoRaise(False)
        self.TButton_bnb.setArrowType(Qt.NoArrow)
        self.TButton_bnb.setObjectName('TButton_bnb')
        self.Layout_Header_Buttons.addWidget(self.TButton_bnb, 1, 1, 1, 1)
        self.TButton_dash = QToolButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TButton_dash.sizePolicy().hasHeightForWidth())
        self.TButton_dash.setSizePolicy(sizePolicy)
        self.TButton_dash.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(8)
        self.TButton_dash.setFont(font)
        self.TButton_dash.setText('')
        icon8 = QIcon()
        icon8.addPixmap(QPixmap(':/crypto/media/crypto/__dash__.png'), QIcon.Normal, QIcon.On)
        self.TButton_dash.setIcon(icon8)
        self.TButton_dash.setIconSize(QSize(53, 53))
        self.TButton_dash.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.TButton_dash.setAutoRaise(False)
        self.TButton_dash.setArrowType(Qt.NoArrow)
        self.TButton_dash.setObjectName('TButton_dash')
        self.Layout_Header_Buttons.addWidget(self.TButton_dash, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.Layout_Header_Buttons, 0, 0, 1, 1)
        self.Layout_Counter = QGridLayout()
        self.Layout_Counter.setContentsMargins(3, 6, 3, 6)
        self.Layout_Counter.setSpacing(0)
        self.Layout_Counter.setObjectName('Layout_Counter')
        self.Label_Value_TotalValue = QLabel(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_Value_TotalValue.sizePolicy().hasHeightForWidth())
        self.Label_Value_TotalValue.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.Label_Value_TotalValue.setFont(font)
        self.Label_Value_TotalValue.setStyleSheet(self.styles.label_value)
        self.Label_Value_TotalValue.setIndent(3)
        self.Label_Value_TotalValue.setObjectName('Label_Value_TotalValue')
        self.Layout_Counter.addWidget(self.Label_Value_TotalValue, 0, 4, 1, 1)
        self.label_3 = QLabel(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(self.styles.label_3)
        self.label_3.setObjectName('label_3')
        self.Layout_Counter.addWidget(self.label_3, 0, 3, 1, 1)
        self.label = QLabel(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        self.label.setFont(font)
        self.label.setStyleSheet(self.styles.label)
        self.label.setObjectName('label')
        self.Layout_Counter.addWidget(self.label, 0, 0, 1, 1)
        self.Label_Value_Found = QLabel(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_Value_Found.sizePolicy().hasHeightForWidth())
        self.Label_Value_Found.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily('Verdana')
        font.setPointSize(9)
        self.Label_Value_Found.setFont(font)
        self.Label_Value_Found.setStyleSheet(self.styles.label_value_found)
        self.Label_Value_Found.setInputMethodHints(Qt.ImhDigitsOnly)
        self.Label_Value_Found.setIndent(3)
        self.Label_Value_Found.setTextInteractionFlags(Qt.NoTextInteraction)
        self.Label_Value_Found.setObjectName('Label_Value_Found')
        self.Layout_Counter.addWidget(self.Label_Value_Found, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.Layout_Counter, 3, 0, 1, 1)
        self.Layout_Target_File = QGridLayout()
        self.Layout_Target_File.setHorizontalSpacing(0)
        self.Layout_Target_File.setVerticalSpacing(3)
        self.Layout_Target_File.setObjectName('Layout_Target_File')
        self.Label_TargetLine = QLabel(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_TargetLine.sizePolicy().hasHeightForWidth())
        self.Label_TargetLine.setSizePolicy(sizePolicy)
        self.Label_TargetLine.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setFamily('Verdana')
        self.Label_TargetLine.setFont(font)
        self.Label_TargetLine.setStyleSheet(self.styles.label)
        self.Label_TargetLine.setObjectName('Label_TargetLine')
        self.Layout_Target_File.addWidget(self.Label_TargetLine, 1, 0, 1, 1)
        self.Line_File = QLineEdit(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Line_File.sizePolicy().hasHeightForWidth())
        self.Line_File.setSizePolicy(sizePolicy)
        self.Line_File.setMinimumSize(QSize(250, 35))
        self.Line_File.setStyleSheet(self.styles.LineFile)
        self.Line_File.setInputMask('')
        self.Line_File.setText('')
        self.Line_File.setFrame(True)
        self.Line_File.setObjectName('Line_File')
        self.Layout_Target_File.addWidget(self.Line_File, 1, 2, 1, 1)
        self.toolButton = QToolButton(self.Frame_Header)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QSize(42, 35))
        self.toolButton.setStyleSheet(self.styles.toolButton)
        self.toolButton.setObjectName('toolButton')
        self.Layout_Target_File.addWidget(self.toolButton, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.Layout_Target_File, 6, 0, 1, 1)
        self.line_2 = QFrame(self.Frame_Header)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName('line_2')
        self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 1)
        self.gridLayout_6.addWidget(self.Frame_Header, 0, 0, 1, 1)
        self.Frame_Footer_Copyright = QFrame(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_Footer_Copyright.sizePolicy().hasHeightForWidth())
        self.Frame_Footer_Copyright.setSizePolicy(sizePolicy)
        self.Frame_Footer_Copyright.setFrameShape(QFrame.StyledPanel)
        self.Frame_Footer_Copyright.setFrameShadow(QFrame.Raised)
        self.Frame_Footer_Copyright.setObjectName('Frame_Footer_Copyright')
        self.gridLayout_11 = QGridLayout(self.Frame_Footer_Copyright)
        self.gridLayout_11.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_11.setSpacing(3)
        self.gridLayout_11.setObjectName('gridLayout_11')
        self.formLayout = QFormLayout()
        self.formLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.formLayout.setContentsMargins(3, 3, 3, 3)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName('formLayout')
        self.label_4 = QLabel(self.Frame_Footer_Copyright)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet('color: rgb(127, 127, 127);')
        self.label_4.setObjectName('label_4')
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)
        self.label_2 = QLabel(self.Frame_Footer_Copyright)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('color: rgb(122, 122, 122);')
        self.label_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_2.setObjectName('label_2')
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_2)
        self.gridLayout_11.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.Frame_Footer_Copyright, 4, 0, 1, 1)
        self.Line_File.setReadOnly(True)
        self.retranslateUi(self)
        self.TButton_btc.clicked['bool'].connect(self.radioButton_btc.toggle)
        self.TButton_eth.clicked['bool'].connect(self.radioButton_eth.toggle)
        self.TButton_trx.clicked['bool'].connect(self.radioButton_trx.toggle)
        self.TButton_ltc.clicked['bool'].connect(self.radioButton_ltc.toggle)
        self.TButton_bnb.clicked['bool'].connect(self.radioButton_bnb.toggle)
        self.TButton_dash.clicked['bool'].connect(self.radioButton_dash.toggle)
        QMetaObject.connectSlotsByName(self)
        self.logger.connect(self.Logs)
        None((lambda : self.OnCoinSelect('eth')))
        None((lambda : self.OnCoinSelect('btc')))
        None((lambda : self.OnCoinSelect('trx')))
        None((lambda : self.OnCoinSelect('ltc')))
        None((lambda : self.OnCoinSelect('bnb')))
        None((lambda : self.OnCoinSelect('dash')))
        None((lambda : self.OnCoinSelect('btc')))
        None((lambda : self.OnCoinSelect('eth')))
        None((lambda : self.OnCoinSelect('trx')))
        None((lambda : self.OnCoinSelect('ltc')))
        None((lambda : self.OnCoinSelect('bnb')))
        None((lambda : self.OnCoinSelect('dash')))
        self.index_eth = False
        self.index_btc = True
        self.index_trx = False
        self.index_ltc = False
        self.index_bnb = False
        self.index_dash = False
        self.words = [
            'abandon',
            'ability',
            'able',
            'about',
            'above',
            'absent',
            'absorb',
            'abstract',
            'absurd',
            'abuse',
            'access',
            'accident',
            'account',
            'accuse',
            'achieve',
            'acid',
            'acoustic',
            'acquire',
            'across',
            'act',
            'action',
            'actor',
            'actress',
            'actual',
            'adapt',
            'add',
            'addict',
            'address',
            'adjust',
            'admit',
            'adult',
            'advance',
            'advice',
            'aerobic',
            'affair',
            'afford',
            'afraid',
            'again',
            'age',
            'agent',
            'agree',
            'ahead',
            'aim',
            'air',
            'airport',
            'aisle',
            'alarm',
            'album',
            'alcohol',
            'alert',
            'alien',
            'all',
            'alley',
            'allow',
            'almost',
            'alone',
            'alpha',
            'already',
            'also',
            'alter',
            'always',
            'amateur',
            'amazing',
            'among',
            'amount',
            'amused',
            'analyst',
            'anchor',
            'ancient',
            'anger',
            'angle',
            'angry',
            'animal',
            'ankle',
            'announce',
            'annual',
            'another',
            'answer',
            'antenna',
            'antique',
            'anxiety',
            'any',
            'apart',
            'apology',
            'appear',
            'apple',
            'approve',
            'april',
            'arch',
            'arctic',
            'area',
            'arena',
            'argue',
            'arm',
            'armed',
            'armor',
            'army',
            'around',
            'arrange',
            'arrest',
            'arrive',
            'arrow',
            'art',
            'artefact',
            'artist',
            'artwork',
            'ask',
            'aspect',
            'assault',
            'asset',
            'assist',
            'assume',
            'asthma',
            'athlete',
            'atom',
            'attack',
            'attend',
            'attitude',
            'attract',
            'auction',
            'audit',
            'august',
            'aunt',
            'author',
            'auto',
            'autumn',
            'average',
            'avocado',
            'avoid',
            'awake',
            'aware',
            'away',
            'awesome',
            'awful',
            'awkward',
            'axis',
            'baby',
            'bachelor',
            'bacon',
            'badge',
            'bag',
            'balance',
            'balcony',
            'ball',
            'bamboo',
            'banana',
            'banner',
            'bar',
            'barely',
            'bargain',
            'barrel',
            'base',
            'basic',
            'basket',
            'battle',
            'beach',
            'bean',
            'beauty',
            'because',
            'become',
            'beef',
            'before',
            'begin',
            'behave',
            'behind',
            'believe',
            'below',
            'belt',
            'bench',
            'benefit',
            'best',
            'betray',
            'better',
            'between',
            'beyond',
            'bicycle',
            'bid',
            'bike',
            'bind',
            'biology',
            'bird',
            'birth',
            'bitter',
            'black',
            'blade',
            'blame',
            'blanket',
            'blast',
            'bleak',
            'bless',
            'blind',
            'blood',
            'blossom',
            'blouse',
            'blue',
            'blur',
            'blush',
            'board',
            'boat',
            'body',
            'boil',
            'bomb',
            'bone',
            'bonus',
            'book',
            'boost',
            'border',
            'boring',
            'borrow',
            'boss',
            'bottom',
            'bounce',
            'box',
            'boy',
            'bracket',
            'brain',
            'brand',
            'brass',
            'brave',
            'bread',
            'breeze',
            'brick',
            'bridge',
            'brief',
            'bright',
            'bring',
            'brisk',
            'broccoli',
            'broken',
            'bronze',
            'broom',
            'brother',
            'brown',
            'brush',
            'bubble',
            'buddy',
            'budget',
            'buffalo',
            'build',
            'bulb',
            'bulk',
            'bullet',
            'bundle',
            'bunker',
            'burden',
            'burger',
            'burst',
            'bus',
            'business',
            'busy',
            'butter',
            'buyer',
            'buzz',
            'cabbage',
            'cabin',
            'cable',
            'cactus',
            'cage',
            'cake',
            'call',
            'calm',
            'camera',
            'camp',
            'can',
            'canal',
            'cancel',
            'candy',
            'cannon',
            'canoe',
            'canvas',
            'canyon',
            'capable',
            'capital',
            'captain',
            'car',
            'carbon',
            'card',
            'cargo',
            'carpet',
            'carry',
            'cart',
            'case',
            'cash',
            'casino',
            'castle',
            'casual',
            'cat',
            'catalog',
            'catch',
            'category',
            'cattle',
            'caught',
            'cause',
            'caution',
            'cave',
            'ceiling',
            'celery',
            'cement',
            'census',
            'century',
            'cereal',
            'certain',
            'chair',
            'chalk',
            'champion',
            'change',
            'chaos',
            'chapter',
            'charge',
            'chase',
            'chat',
            'cheap',
            'check',
            'cheese',
            'chef',
            'cherry',
            'chest',
            'chicken',
            'chief',
            'child',
            'chimney',
            'choice',
            'choose',
            'chronic',
            'chuckle',
            'chunk',
            'churn',
            'cigar',
            'cinnamon',
            'circle',
            'citizen',
            'city',
            'civil',
            'claim',
            'clap',
            'clarify',
            'claw',
            'clay',
            'clean',
            'clerk',
            'clever',
            'click',
            'client',
            'cliff',
            'climb',
            'clinic',
            'clip',
            'clock',
            'clog',
            'close',
            'cloth',
            'cloud',
            'clown',
            'club',
            'clump',
            'cluster',
            'clutch',
            'coach',
            'coast',
            'coconut',
            'code',
            'coffee',
            'coil',
            'coin',
            'collect',
            'color',
            'column',
            'combine',
            'come',
            'comfort',
            'comic',
            'common',
            'company',
            'concert',
            'conduct',
            'confirm',
            'congress',
            'connect',
            'consider',
            'control',
            'convince',
            'cook',
            'cool',
            'copper',
            'copy',
            'coral',
            'core',
            'corn',
            'correct',
            'cost',
            'cotton',
            'couch',
            'country',
            'couple',
            'course',
            'cousin',
            'cover',
            'coyote',
            'crack',
            'cradle',
            'craft',
            'cram',
            'crane',
            'crash',
            'crater',
            'crawl',
            'crazy',
            'cream',
            'credit',
            'creek',
            'crew',
            'cricket',
            'crime',
            'crisp',
            'critic',
            'crop',
            'cross',
            'crouch',
            'crowd',
            'crucial',
            'cruel',
            'cruise',
            'crumble',
            'crunch',
            'crush',
            'cry',
            'crystal',
            'cube',
            'culture',
            'cup',
            'cupboard',
            'curious',
            'current',
            'curtain',
            'curve',
            'cushion',
            'custom',
            'cute',
            'cycle',
            'dad',
            'damage',
            'damp',
            'dance',
            'danger',
            'daring',
            'dash',
            'daughter',
            'dawn',
            'day',
            'deal',
            'debate',
            'debris',
            'decade',
            'december',
            'decide',
            'decline',
            'decorate',
            'decrease',
            'deer',
            'defense',
            'define',
            'defy',
            'degree',
            'delay',
            'deliver',
            'demand',
            'demise',
            'denial',
            'dentist',
            'deny',
            'depart',
            'depend',
            'deposit',
            'depth',
            'deputy',
            'derive',
            'describe',
            'desert',
            'design',
            'desk',
            'despair',
            'destroy',
            'detail',
            'detect',
            'develop',
            'device',
            'devote',
            'diagram',
            'dial',
            'diamond',
            'diary',
            'dice',
            'diesel',
            'diet',
            'differ',
            'digital',
            'dignity',
            'dilemma',
            'dinner',
            'dinosaur',
            'direct',
            'dirt',
            'disagree',
            'discover',
            'disease',
            'dish',
            'dismiss',
            'disorder',
            'display',
            'distance',
            'divert',
            'divide',
            'divorce',
            'dizzy',
            'doctor',
            'document',
            'dog',
            'doll',
            'dolphin',
            'domain',
            'donate',
            'donkey',
            'donor',
            'door',
            'dose',
            'double',
            'dove',
            'draft',
            'dragon',
            'drama',
            'drastic',
            'draw',
            'dream',
            'dress',
            'drift',
            'drill',
            'drink',
            'drip',
            'drive',
            'drop',
            'drum',
            'dry',
            'duck',
            'dumb',
            'dune',
            'during',
            'dust',
            'dutch',
            'duty',
            'dwarf',
            'dynamic',
            'eager',
            'eagle',
            'early',
            'earn',
            'earth',
            'easily',
            'east',
            'easy',
            'echo',
            'ecology',
            'economy',
            'edge',
            'edit',
            'educate',
            'effort',
            'egg',
            'eight',
            'either',
            'elbow',
            'elder',
            'electric',
            'elegant',
            'element',
            'elephant',
            'elevator',
            'elite',
            'else',
            'embark',
            'embody',
            'embrace',
            'emerge',
            'emotion',
            'employ',
            'empower',
            'empty',
            'enable',
            'enact',
            'end',
            'endless',
            'endorse',
            'enemy',
            'energy',
            'enforce',
            'engage',
            'engine',
            'enhance',
            'enjoy',
            'enlist',
            'enough',
            'enrich',
            'enroll',
            'ensure',
            'enter',
            'entire',
            'entry',
            'envelope',
            'episode',
            'equal',
            'equip',
            'era',
            'erase',
            'erode',
            'erosion',
            'error',
            'erupt',
            'escape',
            'essay',
            'essence',
            'estate',
            'eternal',
            'ethics',
            'evidence',
            'evil',
            'evoke',
            'evolve',
            'exact',
            'example',
            'excess',
            'exchange',
            'excite',
            'exclude',
            'excuse',
            'execute',
            'exercise',
            'exhaust',
            'exhibit',
            'exile',
            'exist',
            'exit',
            'exotic',
            'expand',
            'expect',
            'expire',
            'explain',
            'expose',
            'express',
            'extend',
            'extra',
            'eye',
            'eyebrow',
            'fabric',
            'face',
            'faculty',
            'fade',
            'faint',
            'faith',
            'fall',
            'false',
            'fame',
            'family',
            'famous',
            'fan',
            'fancy',
            'fantasy',
            'farm',
            'fashion',
            'fat',
            'fatal',
            'father',
            'fatigue',
            'fault',
            'favorite',
            'feature',
            'february',
            'federal',
            'fee',
            'feed',
            'feel',
            'female',
            'fence',
            'festival',
            'fetch',
            'fever',
            'few',
            'fiber',
            'fiction',
            'field',
            'figure',
            'file',
            'film',
            'filter',
            'final',
            'find',
            'fine',
            'finger',
            'finish',
            'fire',
            'firm',
            'first',
            'fiscal',
            'fish',
            'fit',
            'fitness',
            'fix',
            'flag',
            'flame',
            'flash',
            'flat',
            'flavor',
            'flee',
            'flight',
            'flip',
            'float',
            'flock',
            'floor',
            'flower',
            'fluid',
            'flush',
            'fly',
            'foam',
            'focus',
            'fog',
            'foil',
            'fold',
            'follow',
            'food',
            'foot',
            'force',
            'forest',
            'forget',
            'fork',
            'fortune',
            'forum',
            'forward',
            'fossil',
            'foster',
            'found',
            'fox',
            'fragile',
            'frame',
            'frequent',
            'fresh',
            'friend',
            'fringe',
            'frog',
            'front',
            'frost',
            'frown',
            'frozen',
            'fruit',
            'fuel',
            'fun',
            'funny',
            'furnace',
            'fury',
            'future',
            'gadget',
            'gain',
            'galaxy',
            'gallery',
            'game',
            'gap',
            'garage',
            'garbage',
            'garden',
            'garlic',
            'garment',
            'gas',
            'gasp',
            'gate',
            'gather',
            'gauge',
            'gaze',
            'general',
            'genius',
            'genre',
            'gentle',
            'genuine',
            'gesture',
            'ghost',
            'giant',
            'gift',
            'giggle',
            'ginger',
            'giraffe',
            'girl',
            'give',
            'glad',
            'glance',
            'glare',
            'glass',
            'glide',
            'glimpse',
            'globe',
            'gloom',
            'glory',
            'glove',
            'glow',
            'glue',
            'goat',
            'goddess',
            'gold',
            'good',
            'goose',
            'gorilla',
            'gospel',
            'gossip',
            'govern',
            'gown',
            'grab',
            'grace',
            'grain',
            'grant',
            'grape',
            'grass',
            'gravity',
            'great',
            'green',
            'grid',
            'grief',
            'grit',
            'grocery',
            'group',
            'grow',
            'grunt',
            'guard',
            'guess',
            'guide',
            'guilt',
            'guitar',
            'gun',
            'gym',
            'habit',
            'hair',
            'half',
            'hammer',
            'hamster',
            'hand',
            'happy',
            'harbor',
            'hard',
            'harsh',
            'harvest',
            'hat',
            'have',
            'hawk',
            'hazard',
            'head',
            'health',
            'heart',
            'heavy',
            'hedgehog',
            'height',
            'hello',
            'helmet',
            'help',
            'hen',
            'hero',
            'hidden',
            'high',
            'hill',
            'hint',
            'hip',
            'hire',
            'history',
            'hobby',
            'hockey',
            'hold',
            'hole',
            'holiday',
            'hollow',
            'home',
            'honey',
            'hood',
            'hope',
            'horn',
            'horror',
            'horse',
            'hospital',
            'host',
            'hotel',
            'hour',
            'hover',
            'hub',
            'huge',
            'human',
            'humble',
            'humor',
            'hundred',
            'hungry',
            'hunt',
            'hurdle',
            'hurry',
            'hurt',
            'husband',
            'hybrid',
            'ice',
            'icon',
            'idea',
            'identify',
            'idle',
            'ignore',
            'ill',
            'illegal',
            'illness',
            'image',
            'imitate',
            'immense',
            'immune',
            'impact',
            'impose',
            'improve',
            'impulse',
            'inch',
            'include',
            'income',
            'increase',
            'index',
            'indicate',
            'indoor',
            'industry',
            'infant',
            'inflict',
            'inform',
            'inhale',
            'inherit',
            'initial',
            'inject',
            'injury',
            'inmate',
            'inner',
            'innocent',
            'input',
            'inquiry',
            'insane',
            'insect',
            'inside',
            'inspire',
            'install',
            'intact',
            'interest',
            'into',
            'invest',
            'invite',
            'involve',
            'iron',
            'island',
            'isolate',
            'issue',
            'item',
            'ivory',
            'jacket',
            'jaguar',
            'jar',
            'jazz',
            'jealous',
            'jeans',
            'jelly',
            'jewel',
            'job',
            'join',
            'joke',
            'journey',
            'joy',
            'judge',
            'juice',
            'jump',
            'jungle',
            'junior',
            'junk',
            'just',
            'kangaroo',
            'keen',
            'keep',
            'ketchup',
            'key',
            'kick',
            'kid',
            'kidney',
            'kind',
            'kingdom',
            'kiss',
            'kit',
            'kitchen',
            'kite',
            'kitten',
            'kiwi',
            'knee',
            'knife',
            'knock',
            'know',
            'lab',
            'label',
            'labor',
            'ladder',
            'lady',
            'lake',
            'lamp',
            'language',
            'laptop',
            'large',
            'later',
            'latin',
            'laugh',
            'laundry',
            'lava',
            'law',
            'lawn',
            'lawsuit',
            'layer',
            'lazy',
            'leader',
            'leaf',
            'learn',
            'leave',
            'lecture',
            'left',
            'leg',
            'legal',
            'legend',
            'leisure',
            'lemon',
            'lend',
            'length',
            'lens',
            'leopard',
            'lesson',
            'letter',
            'level',
            'liar',
            'liberty',
            'library',
            'license',
            'life',
            'lift',
            'light',
            'like',
            'limb',
            'limit',
            'link',
            'lion',
            'liquid',
            'list',
            'little',
            'live',
            'lizard',
            'load',
            'loan',
            'lobster',
            'local',
            'lock',
            'logic',
            'lonely',
            'long',
            'loop',
            'lottery',
            'loud',
            'lounge',
            'love',
            'loyal',
            'lucky',
            'luggage',
            'lumber',
            'lunar',
            'lunch',
            'luxury',
            'lyrics',
            'machine',
            'mad',
            'magic',
            'magnet',
            'maid',
            'mail',
            'main',
            'major',
            'make',
            'mammal',
            'man',
            'manage',
            'mandate',
            'mango',
            'mansion',
            'manual',
            'maple',
            'marble',
            'march',
            'margin',
            'marine',
            'market',
            'marriage',
            'mask',
            'mass',
            'master',
            'match',
            'material',
            'math',
            'matrix',
            'matter',
            'maximum',
            'maze',
            'meadow',
            'mean',
            'measure',
            'meat',
            'mechanic',
            'medal',
            'media',
            'melody',
            'melt',
            'member',
            'memory',
            'mention',
            'menu',
            'mercy',
            'merge',
            'merit',
            'merry',
            'mesh',
            'message',
            'metal',
            'method',
            'middle',
            'midnight',
            'milk',
            'million',
            'mimic',
            'mind',
            'minimum',
            'minor',
            'minute',
            'miracle',
            'mirror',
            'misery',
            'miss',
            'mistake',
            'mix',
            'mixed',
            'mixture',
            'mobile',
            'model',
            'modify',
            'mom',
            'moment',
            'monitor',
            'monkey',
            'monster',
            'month',
            'moon',
            'moral',
            'more',
            'morning',
            'mosquito',
            'mother',
            'motion',
            'motor',
            'mountain',
            'mouse',
            'move',
            'movie',
            'much',
            'muffin',
            'mule',
            'multiply',
            'muscle',
            'museum',
            'mushroom',
            'music',
            'must',
            'mutual',
            'myself',
            'mystery',
            'myth',
            'naive',
            'name',
            'napkin',
            'narrow',
            'nasty',
            'nation',
            'nature',
            'near',
            'neck',
            'need',
            'negative',
            'neglect',
            'neither',
            'nephew',
            'nerve',
            'nest',
            'net',
            'network',
            'neutral',
            'never',
            'news',
            'next',
            'nice',
            'night',
            'noble',
            'noise',
            'nominee',
            'noodle',
            'normal',
            'north',
            'nose',
            'notable',
            'note',
            'nothing',
            'notice',
            'novel',
            'now',
            'nuclear',
            'number',
            'nurse',
            'nut',
            'oak',
            'obey',
            'object',
            'oblige',
            'obscure',
            'observe',
            'obtain',
            'obvious',
            'occur',
            'ocean',
            'october',
            'odor',
            'off',
            'offer',
            'office',
            'often',
            'oil',
            'okay',
            'old',
            'olive',
            'olympic',
            'omit',
            'once',
            'one',
            'onion',
            'online',
            'only',
            'open',
            'opera',
            'opinion',
            'oppose',
            'option',
            'orange',
            'orbit',
            'orchard',
            'order',
            'ordinary',
            'organ',
            'orient',
            'original',
            'orphan',
            'ostrich',
            'other',
            'outdoor',
            'outer',
            'output',
            'outside',
            'oval',
            'oven',
            'over',
            'own',
            'owner',
            'oxygen',
            'oyster',
            'ozone',
            'pact',
            'paddle',
            'page',
            'pair',
            'palace',
            'palm',
            'panda',
            'panel',
            'panic',
            'panther',
            'paper',
            'parade',
            'parent',
            'park',
            'parrot',
            'party',
            'pass',
            'patch',
            'path',
            'patient',
            'patrol',
            'pattern',
            'pause',
            'pave',
            'payment',
            'peace',
            'peanut',
            'pear',
            'peasant',
            'pelican',
            'pen',
            'penalty',
            'pencil',
            'people',
            'pepper',
            'perfect',
            'permit',
            'person',
            'pet',
            'phone',
            'photo',
            'phrase',
            'physical',
            'piano',
            'picnic',
            'picture',
            'piece',
            'pig',
            'pigeon',
            'pill',
            'pilot',
            'pink',
            'pioneer',
            'pipe',
            'pistol',
            'pitch',
            'pizza',
            'place',
            'planet',
            'plastic',
            'plate',
            'play',
            'please',
            'pledge',
            'pluck',
            'plug',
            'plunge',
            'poem',
            'poet',
            'point',
            'polar',
            'pole',
            'police',
            'pond',
            'pony',
            'pool',
            'popular',
            'portion',
            'position',
            'possible',
            'post',
            'potato',
            'pottery',
            'poverty',
            'powder',
            'power',
            'practice',
            'praise',
            'predict',
            'prefer',
            'prepare',
            'present',
            'pretty',
            'prevent',
            'price',
            'pride',
            'primary',
            'print',
            'priority',
            'prison',
            'private',
            'prize',
            'problem',
            'process',
            'produce',
            'profit',
            'program',
            'project',
            'promote',
            'proof',
            'property',
            'prosper',
            'protect',
            'proud',
            'provide',
            'public',
            'pudding',
            'pull',
            'pulp',
            'pulse',
            'pumpkin',
            'punch',
            'pupil',
            'puppy',
            'purchase',
            'purity',
            'purpose',
            'purse',
            'push',
            'put',
            'puzzle',
            'pyramid',
            'quality',
            'quantum',
            'quarter',
            'question',
            'quick',
            'quit',
            'quiz',
            'quote',
            'rabbit',
            'raccoon',
            'race',
            'rack',
            'radar',
            'radio',
            'rail',
            'rain',
            'raise',
            'rally',
            'ramp',
            'ranch',
            'random',
            'range',
            'rapid',
            'rare',
            'rate',
            'rather',
            'raven',
            'raw',
            'razor',
            'ready',
            'real',
            'reason',
            'rebel',
            'rebuild',
            'recall',
            'receive',
            'recipe',
            'record',
            'recycle',
            'reduce',
            'reflect',
            'reform',
            'refuse',
            'region',
            'regret',
            'regular',
            'reject',
            'relax',
            'release',
            'relief',
            'rely',
            'remain',
            'remember',
            'remind',
            'remove',
            'render',
            'renew',
            'rent',
            'reopen',
            'repair',
            'repeat',
            'replace',
            'report',
            'require',
            'rescue',
            'resemble',
            'resist',
            'resource',
            'response',
            'result',
            'retire',
            'retreat',
            'return',
            'reunion',
            'reveal',
            'review',
            'reward',
            'rhythm',
            'rib',
            'ribbon',
            'rice',
            'rich',
            'ride',
            'ridge',
            'rifle',
            'right',
            'rigid',
            'ring',
            'riot',
            'ripple',
            'risk',
            'ritual',
            'rival',
            'river',
            'road',
            'roast',
            'robot',
            'robust',
            'rocket',
            'romance',
            'roof',
            'rookie',
            'room',
            'rose',
            'rotate',
            'rough',
            'round',
            'route',
            'royal',
            'rubber',
            'rude',
            'rug',
            'rule',
            'run',
            'runway',
            'rural',
            'sad',
            'saddle',
            'sadness',
            'safe',
            'sail',
            'salad',
            'salmon',
            'salon',
            'salt',
            'salute',
            'same',
            'sample',
            'sand',
            'satisfy',
            'satoshi',
            'sauce',
            'sausage',
            'save',
            'say',
            'scale',
            'scan',
            'scare',
            'scatter',
            'scene',
            'scheme',
            'school',
            'science',
            'scissors',
            'scorpion',
            'scout',
            'scrap',
            'screen',
            'script',
            'scrub',
            'sea',
            'search',
            'season',
            'seat',
            'second',
            'secret',
            'section',
            'security',
            'seed',
            'seek',
            'segment',
            'select',
            'sell',
            'seminar',
            'senior',
            'sense',
            'sentence',
            'series',
            'service',
            'session',
            'settle',
            'setup',
            'seven',
            'shadow',
            'shaft',
            'shallow',
            'share',
            'shed',
            'shell',
            'sheriff',
            'shield',
            'shift',
            'shine',
            'ship',
            'shiver',
            'shock',
            'shoe',
            'shoot',
            'shop',
            'short',
            'shoulder',
            'shove',
            'shrimp',
            'shrug',
            'shuffle',
            'shy',
            'sibling',
            'sick',
            'side',
            'siege',
            'sight',
            'sign',
            'silent',
            'silk',
            'silly',
            'silver',
            'similar',
            'simple',
            'since',
            'sing',
            'siren',
            'sister',
            'situate',
            'six',
            'size',
            'skate',
            'sketch',
            'ski',
            'skill',
            'skin',
            'skirt',
            'skull',
            'slab',
            'slam',
            'sleep',
            'slender',
            'slice',
            'slide',
            'slight',
            'slim',
            'slogan',
            'slot',
            'slow',
            'slush',
            'small',
            'smart',
            'smile',
            'smoke',
            'smooth',
            'snack',
            'snake',
            'snap',
            'sniff',
            'snow',
            'soap',
            'soccer',
            'social',
            'sock',
            'soda',
            'soft',
            'solar',
            'soldier',
            'solid',
            'solution',
            'solve',
            'someone',
            'song',
            'soon',
            'sorry',
            'sort',
            'soul',
            'sound',
            'soup',
            'source',
            'south',
            'space',
            'spare',
            'spatial',
            'spawn',
            'speak',
            'special',
            'speed',
            'spell',
            'spend',
            'sphere',
            'spice',
            'spider',
            'spike',
            'spin',
            'spirit',
            'split',
            'spoil',
            'sponsor',
            'spoon',
            'sport',
            'spot',
            'spray',
            'spread',
            'spring',
            'spy',
            'square',
            'squeeze',
            'squirrel',
            'stable',
            'stadium',
            'staff',
            'stage',
            'stairs',
            'stamp',
            'stand',
            'start',
            'state',
            'stay',
            'steak',
            'steel',
            'stem',
            'step',
            'stereo',
            'stick',
            'still',
            'sting',
            'stock',
            'stomach',
            'stone',
            'stool',
            'story',
            'stove',
            'strategy',
            'street',
            'strike',
            'strong',
            'struggle',
            'student',
            'stuff',
            'stumble',
            'style',
            'subject',
            'submit',
            'subway',
            'success',
            'such',
            'sudden',
            'suffer',
            'sugar',
            'suggest',
            'suit',
            'summer',
            'sun',
            'sunny',
            'sunset',
            'super',
            'supply',
            'supreme',
            'sure',
            'surface',
            'surge',
            'surprise',
            'surround',
            'survey',
            'suspect',
            'sustain',
            'swallow',
            'swamp',
            'swap',
            'swarm',
            'swear',
            'sweet',
            'swift',
            'swim',
            'swing',
            'switch',
            'sword',
            'symbol',
            'symptom',
            'syrup',
            'system',
            'table',
            'tackle',
            'tag',
            'tail',
            'talent',
            'talk',
            'tank',
            'tape',
            'target',
            'task',
            'taste',
            'tattoo',
            'taxi',
            'teach',
            'team',
            'tell',
            'ten',
            'tenant',
            'tennis',
            'tent',
            'term',
            'test',
            'text',
            'thank',
            'that',
            'theme',
            'then',
            'theory',
            'there',
            'they',
            'thing',
            'this',
            'thought',
            'three',
            'thrive',
            'throw',
            'thumb',
            'thunder',
            'ticket',
            'tide',
            'tiger',
            'tilt',
            'timber',
            'time',
            'tiny',
            'tip',
            'tired',
            'tissue',
            'title',
            'toast',
            'tobacco',
            'today',
            'toddler',
            'toe',
            'together',
            'toilet',
            'token',
            'tomato',
            'tomorrow',
            'tone',
            'tongue',
            'tonight',
            'tool',
            'tooth',
            'top',
            'topic',
            'topple',
            'torch',
            'tornado',
            'tortoise',
            'toss',
            'total',
            'tourist',
            'toward',
            'tower',
            'town',
            'toy',
            'track',
            'trade',
            'traffic',
            'tragic',
            'train',
            'transfer',
            'trap',
            'trash',
            'travel',
            'tray',
            'treat',
            'tree',
            'trend',
            'trial',
            'tribe',
            'trick',
            'trigger',
            'trim',
            'trip',
            'trophy',
            'trouble',
            'truck',
            'true',
            'truly',
            'trumpet',
            'trust',
            'truth',
            'try',
            'tube',
            'tuition',
            'tumble',
            'tuna',
            'tunnel',
            'turkey',
            'turn',
            'turtle',
            'twelve',
            'twenty',
            'twice',
            'twin',
            'twist',
            'two',
            'type',
            'typical',
            'ugly',
            'umbrella',
            'unable',
            'unaware',
            'uncle',
            'uncover',
            'under',
            'undo',
            'unfair',
            'unfold',
            'unhappy',
            'uniform',
            'unique',
            'unit',
            'universe',
            'unknown',
            'unlock',
            'until',
            'unusual',
            'unveil',
            'update',
            'upgrade',
            'uphold',
            'upon',
            'upper',
            'upset',
            'urban',
            'urge',
            'usage',
            'use',
            'used',
            'useful',
            'useless',
            'usual',
            'utility',
            'vacant',
            'vacuum',
            'vague',
            'valid',
            'valley',
            'valve',
            'van',
            'vanish',
            'vapor',
            'various',
            'vast',
            'vault',
            'vehicle',
            'velvet',
            'vendor',
            'venture',
            'venue',
            'verb',
            'verify',
            'version',
            'very',
            'vessel',
            'veteran',
            'viable',
            'vibrant',
            'vicious',
            'victory',
            'video',
            'view',
            'village',
            'vintage',
            'violin',
            'virtual',
            'virus',
            'visa',
            'visit',
            'visual',
            'vital',
            'vivid',
            'vocal',
            'voice',
            'void',
            'volcano',
            'volume',
            'vote',
            'voyage',
            'wage',
            'wagon',
            'wait',
            'walk',
            'wall',
            'walnut',
            'want',
            'warfare',
            'warm',
            'warrior',
            'wash',
            'wasp',
            'waste',
            'water',
            'wave',
            'way',
            'wealth',
            'weapon',
            'wear',
            'weasel',
            'weather',
            'web',
            'wedding',
            'weekend',
            'weird',
            'welcome',
            'west',
            'wet',
            'whale',
            'what',
            'wheat',
            'wheel',
            'when',
            'where',
            'whip',
            'whisper',
            'wide',
            'width',
            'wife',
            'wild',
            'will',
            'win',
            'window',
            'wine',
            'wing',
            'wink',
            'winner',
            'winter',
            'wire',
            'wisdom',
            'wise',
            'wish',
            'witness',
            'wolf',
            'woman',
            'wonder',
            'wood',
            'wool',
            'word',
            'work',
            'world',
            'worry',
            'worth',
            'wrap',
            'wreck',
            'wrestle',
            'wrist',
            'write',
            'wrong',
            'yard',
            'year',
            'yellow',
            'you',
            'young',
            'youth',
            'zebra',
            'zero',
            'zone',
            'zoo']
        self.generator = {
            'btc': self.GenBitcoin,
            'eth': self.GenEthereum,
            'ltc': self.GenLitecoin,
            'trx': self.GenTron,
            'bnb': self.GenEthereum,
            'dash': self.GenDash }
        self.timers = { }
        self.defaultCoin = 'btc'
        self.set_default_coin(self.defaultCoin)
        self.button_start.clicked.connect(self.getStartMain)
        self.button_forcestop.clicked.connect(self.getStopMain)
        self.button_close.clicked[bool].connect(self.close)
        self.toolButton.clicked.connect(self.OnOpenFile)

    
    def retranslateUi(self, QWidget):
        _translate = QCoreApplication.translate
        self.setWindowTitle('Pyromid Hunter 4.1.3 - Mmdrza.Com')
        self.setWindowIcon(QIcon(':/media/media/logo.png'))
        self.button_close.setText(_translate('Form', 'Close'))
        self.button_forcestop.setText(_translate('Form', 'Force Stop'))
        self.button_start.setText(_translate('Form', 'Start'))
        self.radioButton_eth.setToolTip(_translate('Form', 'Ethereum ( CTRL + E )'))
        self.radioButton_eth.setText(_translate('Form', 'Ethereum'))
        self.radioButton_eth.setShortcut(_translate('Form', 'Ctrl+E'))
        self.radioButton_btc.setToolTip(_translate('Form', 'Bitcoin Mode ( CTRL + B )'))
        self.radioButton_btc.setText(_translate('Form', 'Bitcoin'))
        self.radioButton_btc.setShortcut(_translate('Form', 'Ctrl+B'))
        self.radioButton_trx.setToolTip(_translate('Form', 'Tron ( CTRL + T )'))
        self.radioButton_trx.setText(_translate('Form', 'Tron'))
        self.radioButton_trx.setShortcut(_translate('Form', 'Ctrl+T'))
        self.radioButton_ltc.setToolTip(_translate('Form', 'Litecoin ( CTRL + L )'))
        self.radioButton_ltc.setText(_translate('Form', 'Litecoin'))
        self.radioButton_ltc.setShortcut(_translate('Form', 'Ctrl+L'))
        self.radioButton_bnb.setToolTip(_translate('Form', 'BNB ( CTRL + SHIFT + B )'))
        self.radioButton_bnb.setText(_translate('Form', 'BNB'))
        self.radioButton_bnb.setShortcut(_translate('Form', 'Ctrl+Shift+B'))
        self.radioButton_dash.setToolTip(_translate('Form', 'DASH ( CTRL + D )'))
        self.radioButton_dash.setText(_translate('Form', 'DASH'))
        self.radioButton_dash.setShortcut(_translate('Form', 'Ctrl+D'))
        self.Label_Check_Value.setText(_translate('Form', '0'))
        self.Label_Import.setText(_translate('Form', '   Import : '))
        self.Label_Check.setText(_translate('Form', '   Check :'))
        self.Label_Import_Value.setText(_translate('Form', '0'))
        self.Label_Value_TotalValue.setText(_translate('Form', '0'))
        self.label_3.setText(_translate('Form', '   Value $ :'))
        self.label.setText(_translate('Form', '   Found : '))
        self.Label_Value_Found.setText(_translate('Form', '0'))
        self.Label_TargetLine.setText(_translate('Form', 'Target File'))
        self.Line_File.setPlaceholderText(_translate('Form', "Target's Address File ( .txt )"))
        self.toolButton.setText(_translate('Form', '...'))
        self.label_4.setText(_translate('Form', 'Programmer & Owner :'))
        self.label_2.setText(_translate('Form', 'M M D R Z A . C O M'))

    
    def OnOpenFile(self):
        fileDial = QFileDialog(self)
        (filePath, _) = fileDial.getOpenFileName(self, 'Select Target Text File', '', 'Text Files (*.txt)')
        if filePath:
            self.FilePath = filePath
            self.Line_File.setText(filePath)
            self.LOGGER(f'''File : {filePath}''')
            self.indexFile = True
            self.progressDialog = QProgressDialog('Loading File...', 'Cancel', 0, 100, self)
            self.progressDialog.setWindowModality(Qt.WindowModal)
            self.progressDialog.setAutoClose(True)
            self.progressDialog.show()
            self.FileReader = FileReader(filePath)
            self.FileReader.data_read.connect(self.OnRead)
            self.FileReader.progress.connect(self.progressDialog.setValue)
            self.FileReader.finished.connect(self.progressDialog.close)
            self.FileReader.start()
        else:
            self.indexFile = False
            return None

    
    def OnRead(self, lines):
        self.importValue = len(lines)
        self.LOGGER(f'''Total Target Import : {format(self.importValue, ',')}''')
        self.targetList = lines
        self.Label_Import_Value.setText(f'''{format(self.importValue, ',')}''')

    
    def getStartMain(self):
        if not self.indexFile:
            self.OnError('No Target Address File Imported (.txt). Needed Load a Text File First.')
            return None
        for coin, index in None.generator.items():
            if getattr(self, f'''index_{coin}''', False):
                self.timers[coin] = QTimer(self)
                self.timers[coin].timeout.connect(index)
                self.timers[coin].start(1)
                self.scan = True
                self.button_start.setEnabled(False)
            
            return None

    
    def getStopMain(self):
        for timer in self.timers.values():
            timer.stop()
        self.scan = False
        self.button_start.setEnabled(True)

    
    def LOGGER(self, msgContent):
        self.logger.emit(f'''{msgContent}''')

    
    def Logs(self, msgContent):
        courser = self.textBrowser.textCursor()
    # WARNING: Decompyle incomplete

    
    def set_default_coin(self, coin):
        self.defaultCoin = coin
        if self.scan:
            self.getStopMain()
        setattr(self, f'''index_{coin}''', True)
        self.OnCoinSelect(self.defaultCoin)

    
    def OnCoinSelect(self, coin_name):
        if self.scan:
            self.getStopMain()
            self.scan = False
        for coin in ('eth', 'btc', 'trx', 'ltc', 'bnb', 'dash'):
            getattr(self, f'''radioButton_{coin}''').setChecked(False)
            getattr(self, f'''TButton_{coin}''').setChecked(False)
        getattr(self, f'''radioButton_{coin_name}''').setChecked(True)
        getattr(self, f'''TButton_{coin_name}''').setChecked(True)
        for coin in ('eth', 'btc', 'trx', 'ltc', 'bnb', 'dash'):
            setattr(self, f'''index_{coin.lower()}''', coin_name.lower() == coin.lower())
        if coin_name == 'eth':
            coin_name = 'Ethereum'
        elif coin_name == 'btc':
            coin_name = 'Bitcoin'
        elif coin_name == 'trx':
            coin_name = 'Tron'
        elif coin_name == 'ltc':
            coin_name = 'Litecoin'
        elif coin_name == 'bnb':
            coin_name = 'Binance'
        elif coin_name == 'dash':
            coin_name = 'Dash'
        self.textBrowser.setText(f'''Coin Selected :<font color=green> {coin_name}</font>''')

    
    def GenMnemonic(self = None, size = None):
        words_list = []
        for _ in range(size):
            words_list.append(choice(self.words))
        return ' '.join(words_list)

    
    def checkAddrFile(self, address):
        if address in self.targetList:
            return True
        return None

    
    def writerFile(self, addr, pvk, mnemonic, coin):
        content = f'''Address: {addr}\nPRIVATE: {pvk}\nMNEMONIC: {mnemonic}\n'''
        fileName_ = f'''MatchData_{coin.upper()}.txt'''
    # WARNING: Decompyle incomplete

    
    def OnError(self, ErrorMassage):
        self.error.textBrowser.setHtml(f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li {{ white-space: pre-wrap; }}\n</style></head><body style=" font-family:\'Tahoma\'; font-size:9pt; font-weight:400; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{ErrorMassage}</p></body></html>''')
        self.error.show()

    
    def GenBitcoin(self):
        if not self.indexFile:
            self.OnError('No Target Address File Imported (.txt). Needed Load a Text File First.')
            return None
        _mnemonic_ = None.GenMnemonic(12)
        priv = conv.mne_to_hex(_mnemonic_)
        caddr = conv.mne_to_addr(_mnemonic_, True, **('compress',))
        uaddr = conv.mne_to_addr(_mnemonic_, False, **('compress',))
        self.z += 1
        self.Label_Check_Value.setText(f'''{self.z}''')
        if self.checkAddrFile(caddr):
            self.writerFile(caddr, priv, _mnemonic_, 'btc')
            self.found += 1
            self.Label_Value_Found.setText(f'''{self.found}''')
        addrShow = f'''{caddr[0:4]}...{caddr[-5:]}'''
        sizeAddr = len(addrShow) + 1
        formatted_text = f'''<pre>{addrShow.ljust(sizeAddr)} MNEMONIC: {_mnemonic_}</pre>'''
        self.LOGGER(formatted_text)

    
    def GenEthereum(self):
        if not self.indexFile:
            self.OnError('No Target Address File Imported (.txt). Needed Load a Text File First.')
            return None
        _mnemonic_ = None.GenMnemonic(12)
        hexString = conv.mne_to_hex(_mnemonic_)
        addr = eth.hex_addr(hexString)
        self.z += 1
        self.Label_Check_Value.setText(f'''{self.z}''')
        addrShow = f'''{addr[0:4]}...{addr[-5:]}'''
        if self.checkAddrFile(addr):
            self.writerFile(addr, hexString, _mnemonic_, 'eth')
            self.found += 1
            self.Label_Value_Found.setText(f'''{self.found}''')
        sizeAddr = len(addrShow) + 1
        formatted_text = f'''<pre>{addrShow.ljust(sizeAddr)} MNEMONIC: {_mnemonic_}</pre>'''
        self.LOGGER(formatted_text)

    
    def GenTron(self):
        if not self.indexFile:
            self.OnError('No Target Address File Imported (.txt). Needed Load a Text File First.')
            return None
        _mnemonic_ = None.GenMnemonic(12)
        hexString = conv.mne_to_hex(_mnemonic_)
        addr = trx.hex_addr(hexString)
        self.z += 1
        self.Label_Check_Value.setText(f'''{self.z}''')
        addrShow = f'''{addr[0:4]}...{addr[-5:]}'''
        if self.checkAddrFile(addr):
            self.writerFile(addr, hexString, _mnemonic_, 'trx')
            self.found += 1
            self.Label_Value_Found.setText(f'''{self.found}''')
        sizeAddr = len(addrShow) + 1
        formatted_text = f'''<pre>{addrShow.ljust(sizeAddr)} MNEMONIC: {_mnemonic_}</pre>'''
        self.LOGGER(formatted_text)

    
    def GenLitecoin(self):
        if not self.indexFile:
            self.OnError('No Target Address File Imported (.txt). Needed Load a Text File First.')
            return None
        _mnemonic_ = None.GenMnemonic(12)
        hexString = conv.mne_to_hex(_mnemonic_)
        addr = ltc.hex_addr(hexString)
        self.z += 1
        self.Label_Check_Value.setText(f'''{self.z}''')
        addrShow = f'''{addr[0:4]}...{addr[-5:]}'''
        if self.checkAddrFile(addr):
            self.writerFile(addr, hexString, _mnemonic_, 'ltc')
            self.found += 1
            self.Label_Value_Found.setText(f'''{self.found}''')
        sizeAddr = len(addrShow) + 1
        formatted_text = f'''<pre>{addrShow.ljust(sizeAddr)} MNEMONIC: {_mnemonic_}</pre>'''
        self.LOGGER(formatted_text)

    
    def GenDash(self):
        if not self.indexFile:
            self.OnError('No Target Address File Imported (.txt). Needed Load a Text File First.')
            return None
        _mnemonic_ = None.GenMnemonic(12)
        hexString = conv.mne_to_hex(_mnemonic_)
        addr = dash.hex_addr(hexString)
        self.z += 1
        self.Label_Check_Value.setText(f'''{self.z}''')
        addrShow = f'''{addr[0:4]}...{addr[-5:]}'''
        if self.checkAddrFile(addr):
            self.writerFile(addr, hexString, _mnemonic_, 'dash')
            self.found += 1
            self.Label_Value_Found.setText(f'''{self.found}''')
        sizeAddr = len(addrShow) + 1
        formatted_text = f'''<pre>{addrShow.ljust(sizeAddr)} MNEMONIC: {_mnemonic_}</pre>'''
        self.LOGGER(formatted_text)

    __classcell__ = None

if __name__ == '__main__':
    hIui = Ui_VertMain()
    hIui.show()
    sys.exit(app.exec_())
