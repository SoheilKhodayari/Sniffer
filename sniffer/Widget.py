#urllib2.open ... baraye login be ye safeii  >> supremely fundamental
#QGroupBOX for layouts perfect  >> better than splitter since it has some hard codes
#QList for input TOlist <<not neccessary really

from BeautifulSoup import *
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QApplication, QSplitter, QLabel, QVBoxLayout
from PyQt4 import QtGui,QtCore
import sys
from scrper_complex import *
from EmailLogic import *
from urllib2 import urlopen

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class CheckableComboBox(QtGui.QComboBox):
    def __init__(self):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QtGui.QStandardItemModel(self))

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)


class WIDGET(QtGui.QWidget):

    def __init__(self,layout):
        super(WIDGET, self).__init__()
        self.layout=layout
        self.initUI()
    def initUI(self):
        self.setLayout(self.layout)
        self.show()


class MyWidget(QWidget):
    sounds= { "Pulse A" : 1,
              "Cool": 2,
              "CloudNine": 3,
              "GreenPlace": 4,
              "darkclouds": 5 }
    def __init__( self, parent=None  ):
        super(MyWidget, self).__init__(parent)
        self.__soundType= self.sounds["darkclouds"]
        self.__pSound=False
        self.InsideSound=True
        self.initUI()
        self.setMinimumWidth(600)
        self.setMinimumHeight(600)


    def initUI(self):
        self.Emails=EmailScraper() #list of emails
        #self.email=emailSender()
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)



        #Crawler Section:-------------------------------------------
        URLlabel=QtGui.QLabel('<b> URl :<b>')
        self.Num=QtGui.QLabel()

        self.leURL = QtGui.QLineEdit()
        self.AddB=QtGui.QPushButton('Add URL')
        self.leURL.setText('http://localhost:8000/login')
        self.EnterBt=QtGui.QPushButton('Crawl',self)
        self.EnterBt.resize(self.EnterBt.sizeHint())
        self.teCrawl=QtGui.QTextEdit()

        self.connect(self.EnterBt, QtCore.SIGNAL("clicked()"),self.button_click)
        self.connect(self.AddB,QtCore.SIGNAL("clicked()"),self.OnClicked)

        layoutCr = QtGui.QFormLayout()
        hboxC=QtGui.QHBoxLayout()
        hboxC.addWidget(self.leURL)
        hboxC.addWidget(self.AddB)
        hboxC.setSpacing(5)
        layoutCr.addWidget(URLlabel)
        #layout.addWidget(self.le)
        layoutCr.addItem(hboxC)
        layoutCr.addWidget(self.EnterBt)
        layoutCr.addWidget(self.teCrawl)
        layoutCr.addWidget(self.Num)
        layoutCr.setSpacing(5)
        vbox00=QtGui.QVBoxLayout()
        vbox00.addItem(layoutCr)
        
        #--------------------------------------------------------------EmailUI

        self.senderLabel=QtGui.QLabel('<b>Senders Specifications:<b>')
        self.FreeLable=QtGui.QLabel('',self)

        self.loginbtn =QtGui.QPushButton('Login',self)
        self.loginbtn.clicked.connect(self.CreateSender)

        self.le1=QtGui.QLineEdit()
        self.btn1 = QtGui.QPushButton('Username', self)
        self.btn1.clicked.connect(self.showDialog1)

        self.le2=QtGui.QLineEdit()
        self.le2.setEchoMode(QtGui.QLineEdit.Password)
        self.btn2=QtGui.QPushButton('Password',self)
        self.btn2.clicked.connect(self.showDialog2)
        self.le3=QtGui.QLineEdit()
        self.le3.setText('smtp.live.com')
        #self.le3.setEchoMode(QtGui.QLineEdit.Password)
        #self.btn3 = QtGui.QPushButton('SMTP Server', self)
        #self.btn3.clicked.connect(self.showDialog3)
        
        self.combo3 = QtGui.QComboBox(self)  
        
        self.combo3.setFixedSize(80,23)
        self.combo3.addItem("Live")  #587
        self.combo3.addItem("Yahoo") # 465 
        self.combo3.addItem("Gmail") #465
        
       
        

        self.combo3.activated[str].connect(self.onActivatedServer)     

        self.le4=QtGui.QLineEdit()
        self.le4.setText('587')
        #self.btn4 = QtGui.QPushButton('Port', self)
        #self.btn4.clicked.connect(self.showDialog4)
        self.combo4 = QtGui.QComboBox(self)
        self.combo4.addItem("Live Port")
        self.combo4.addItem("Yahoo Port")
        self.combo4.addItem("Gmail Port")
        self.combo4.setFixedSize(80,23)
        
        self.combo4.activated[str].connect(self.onActivatedPort)   


        #layouts
        hbox1=QtGui.QHBoxLayout()
        hbox1.addWidget(self.btn1)
        hbox1.addWidget(self.le1)
        hbox1.setSpacing(5)

        hbox2=QtGui.QHBoxLayout()
        hbox2.addWidget(self.btn2)
        hbox2.addWidget(self.le2)
        hbox2.setSpacing(5)

        hbox3=QtGui.QHBoxLayout()
        hbox3.addWidget(self.combo3)
        hbox3.addWidget(self.le3)
        hbox3.setSpacing(5)

        hbox4=QtGui.QHBoxLayout()
        hbox4.addWidget(self.combo4)
        hbox4.addWidget(self.le4)
        hbox4.setSpacing(5)


        lb=QtGui.QFormLayout()
        lb.addWidget(self.senderLabel)
        lb.addWidget(self.FreeLable)


        lb.addItem(hbox1)
        lb.addItem(hbox2)
        lb.addItem(hbox3)
        lb.addItem(hbox4)
        lb.addWidget(self.loginbtn)
        lb.setSpacing(12)
        vbox=QtGui.QVBoxLayout()

        vbox.addItem(lb)
        #----------------------------------- SendMail
        
        
        
        self.SendButton=QtGui.QPushButton('Send NOW')
        self.SendButton.clicked.connect(self.Send)
        self.status=QtGui.QLabel()

        self.lblSubject=QtGui.QLabel('Subject:')
        self.leSubject=QtGui.QLineEdit()
        self.leSubject.setText(" None ")
        self.btnSubject=QtGui.QPushButton("Add Subject")
        self.btnSubject.clicked.connect(self.AddSubject)

        self.labelbody=QtGui.QLabel('Body ')
        self.body=QtGui.QTextEdit()
        #self.body.setStyleSheet('color: red')
        col = QtGui.QColor(0, 0, 0) 
        self.colbtn = QtGui.QPushButton('Color', self)
        self.colbtn.setSizePolicy(QtGui.QSizePolicy.Fixed,
            QtGui.QSizePolicy.Fixed)
        self.colbtn.clicked.connect(self.showcolDialog)
        self.body.setStyleSheet('color: {0}'.format(col.name()))
        
        self.btnfont = QtGui.QPushButton('Font / Size', self)
        self.btnfont.setSizePolicy(QtGui.QSizePolicy.Fixed,
            QtGui.QSizePolicy.Fixed)
        self.btnfont.clicked.connect(self.showfontDialog)
        
        
        
        self.addbodybtn=QtGui.QPushButton('Add Body')  
        self.addbodybtn.setSizePolicy(QtGui.QSizePolicy.Fixed,
            QtGui.QSizePolicy.Fixed)
        self.addbodybtn.clicked.connect(self.Addbody)

        # self.attach
        self.lblAttach=QtGui.QLabel('Sticky:  ')
        self.btnAttach=QtGui.QPushButton('Attach')
        self.btnAttach.clicked.connect(self.openfile)
        self.leAttach=QtGui.QLineEdit()
        self.leAttach.setText('None')
        #self.To
        self.lblTo = QtGui.QLabel("To:        ", self)
        self.leTo=QtGui.QLineEdit()


        #self.combo = QtGui.QComboBox(self)
        self.combo= QtGui.QToolButton(self)
        self.combo.setFixedSize(80,23)
        self.combo.triggered.connect(self.onActivated)
        self.combo.setText('MaiL To ')
        #self.combo = CheckableComboBox()
        #self.combo.update()
        #self.combo.setEditable(True)
        #self.combo.addItems(self.Emails.emails)

        #self.combo.activated[str].connect(self.onActivated)

        #layouts sendmail
        hbox22=QtGui.QHBoxLayout()
        hbox22.addWidget(self.lblSubject)
        hbox22.addWidget(self.leSubject)
        hbox22.addWidget(self.btnSubject)
        hbox22.setSpacing(5)
        hbox33=QtGui.QHBoxLayout()
        hbox33.addWidget(self.lblTo)
        hbox33.addWidget(self.leTo)
        hbox33.addWidget(self.combo)
        hbox33.setSpacing(5)
        hbox44=QtGui.QHBoxLayout()
        hbox44.addWidget(self.lblAttach)
        hbox44.addWidget(self.leAttach)
        hbox44.setSpacing(5)
        
        hbox44.addWidget(self.btnAttach)
        hbox55=QtGui.QHBoxLayout()
        self.labelbody.adjustSize()
        hbox55.addWidget(self.labelbody)
        
        hbox55.addWidget(self.btnfont)
        hbox55.addWidget(self.colbtn)
        hbox55.addWidget(self.addbodybtn)
        hbox55.setSpacing(5)
        
        
        
        hbox66=QtGui.QHBoxLayout()
        hbox66.addWidget(self.body)
        hbox77=QtGui.QHBoxLayout()
        hbox77.addWidget(self.status)
        
        hbox77.addWidget(self.SendButton)
        

        form=QtGui.QFormLayout()
        form.addItem(hbox22)
        form.addItem(hbox33)
        form.addItem(hbox44)
        form.addItem(hbox55)
        form.addItem(hbox66)
        form.addItem(hbox77)
        form.setSpacing(5)

        vbox11=QtGui.QVBoxLayout()
        vbox11.addItem(form)
        # create widgets
        #a = WIDGET(vbox00)
        #b = WIDGET(vbox)
        #c = WIDGET(vbox11)
        #d = QLabel('D', self)
        crawlerGroup=QtGui.QGroupBox('Scrape')
        senderGroup=QtGui.QGroupBox("specifications")
        emailGroup=QtGui.QGroupBox('Mail')

        crawlerGroup.setLayout(vbox00)
        senderGroup.setLayout(vbox)
        emailGroup.setLayout(vbox11)

        HBOX1=QtGui.QHBoxLayout()
        HBOX1.addWidget(crawlerGroup)
        #HBOX1.setSpacing(100)
        HBOX1.addWidget(senderGroup)

        HBOX2=QtGui.QHBoxLayout()
        HBOX2.addWidget(emailGroup)

        FinalVbox=QtGui.QVBoxLayout()
        FinalVbox.addLayout(HBOX1)
        FinalVbox.addLayout(HBOX2)
        self.setLayout(FinalVbox)





        #for lbl in (a,b,c,d):
            #lbl.setAlignment(Qt.AlignCenter)

        # create 2 horizontal splitters
        #h_splitter1 = QSplitter(Qt.Horizontal, self)
        #h_splitter1.addWidget(a)
        #h_splitter1.addWidget(b)

        #h_splitter2 = QSplitter(Qt.Horizontal, self)
        #.addWidget(c)
        #h_splitter2.addWidget(d)

        #.splitterMoved.connect(self.moveSplitter)
        #h_splitter2.splitterMoved.connect(self.moveSplitter)

        #self._spltA = h_splitter1
        #self._spltB = h_splitter2

        # create a vertical splitter
        #v_splitter = QSplitter(Qt.Vertical, self)
        #v_splitter.addWidget(h_splitter1)
        #v_splitter.addWidget(h_splitter2)

        #layout = QVBoxLayout()
        #layout.addWidget(v_splitter)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

        #Plastique,CDE,GTK+,Cleanlooks,Motif
        

    #def moveSplitter( self, index, pos ):
        #splt = self._spltA if self.sender() == self._spltB else self._spltB
        #splt.blockSignals(True)
    #crawler ---------------------------
    def button_click(self):
        self.teCrawl.setText('')
        self.Play('sounds/crawl.wav')
        
        url_str=str(self.leURL.text())
        
        
        
       
        
        #browser = webdriver.Firefox()
        #browser.get(url_str)
        #browser.find_element_by_name('email').send_keys('arian@hosseini.com')
        #time.sleep(1) 
        #browser.find_element_by_name('password').send_keys('123123')
        #time.sleep(1) 
        #browser.find_element_by_name('Login').click()
        #time.sleep(1) 
        if url_str=='http://localhost:8000/login':
            driver = webdriver.Chrome('C:/Users/soheil/Desktop/chromedriver.exe')
            driver.get(url_str)
            driver.find_element_by_name('email').send_keys('arian@hosseini.com')

            driver.find_element_by_name('password').send_keys('123123')

            #crawling 5 pages simultanously 
            driver.find_element_by_name('Login').click()
            driver.get('http://localhost:8000/vertex/arian_x/')
            content=driver.page_source
            driver.get('http://localhost:8000/vertex/bardia_heydarinejad/')
            content+=driver.page_source
            driver.get('http://localhost:8000/vertex/soheil_khodayari/')
            content+=driver.page_source
            driver.get('http://localhost:8000/vertex/meraj_noorodini/')
            content+=driver.page_source
            driver.get('http://localhost:8000/vertex/hossein_khalili/')
            content+=driver.page_source
            self.Emails.collectAllEmail(content)
            driver.close()
            print self.Emails.emails
        else:
            soup=BeautifulSoup(urlopen(url_str).read())  ##f=urlopen(url_str) solution2  maybe better
            f=open('webpage.htm','w+')
            f.write(soup.prettify()) 
            self.Emails.collectAllEmail(f.read())  
            print self.Emails.emails
        
        
        self.toolmenu = QtGui.QMenu(self)
        for i in range(len(self.Emails.emails)):
                self.combo.setObjectName(self.Emails.emails[i])
                action = self.toolmenu.addAction(self.Emails.emails[i])
                action.setObjectName(self.Emails.emails[i])
                action.setCheckable(True)

        self.combo.setMenu(self.toolmenu)
        self.combo.setPopupMode(QtGui.QToolButton.InstantPopup)
        for i in self.Emails.emails:
            #self.te.setText(str(self.te.text())+'\n'+ str(i))
            if not self.teCrawl.find(i):
                self.teCrawl.append('\n'+str(i))
        self.Play('sounds/crawl2.wav')
        self.Num.setText("Number of found mails : " +str(len(self.Emails.emails)))
    def OnClicked(self):
        self.Play('sounds/e.wav')
        url_str=self.leURL.text()
        self.leURL.setText(url_str)
    #---------------------------------
    def showDialog1(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter your Username:')

        if ok:
            self.le1.setText(str(text))
    def showDialog2(self):

        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter your Password:')

        if ok:
            self.le2.setText(str(text))
   
    def CreateSender(self):
         try:
            self.email=emailSender(str(self.le1.text()),str(self.le2.text()),str(self.le3.text()),int(str(self.le4.text())))

            if str(self.le1.text()) != '' and str(self.le2.text())  != '':
                self.FreeLable.setText('logged in successfully')
                self.Play('sounds/login1 .wav')
            else:
                self.FreeLable.setText('Failed, Requisites Must be Provided Properly')
                self.Play('sounds/login2.wav')
            #self.email.setUser(str(self.le1.text()))
            #self.email.setPwd(str(self.le2.text()))
            #self.email.setSmtp(str(self.le3.text()))
            #self.email.setPort(str(self.le4.text()))
          #if self.email do sth
         except:
             self.FreeLable.setText('Wrong Credentials, Try again') #does' nt work?? freelable needs self argument maybe
             self.Play('sounds/wrongcredint.wav')
             self.FreeLable.adjustSize()
    # ------------------------------------------------------sendmail funcs
    def openfile(self):
        if self.InsideSound:
            self.Play('sounds/w.wav')
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')
        self.leAttach.setText(str(fname))
        #f = open(fname, 'r')

        #with f:
            #data = f.read()
    def AddSubject(self):
         self.Play('sounds/2.wav')
         if str(self.leSubject.text()) != 'None':
            self.leSubject.setText(str(self.leSubject.text()))
    def Addbody(self):
        self.Play('sounds/e.wav')
        self.body.setText(str(self.body.toPlainText()))  # looks like toplain text will  work / selectAll doesnt
    #def onActivated(self,text):
         #self.leTo.setText(str(text))
    def onActivated(self,text):
         self.Play('sounds/2.wav')
         self.leTo.setText(str(text.objectName())+', '+str(self.leTo.text()))
    def onActivatedServer(self,text):   #self.combo3.currenttext() also catches its selection
        if text=='Live':
            self.le3.setText('smtp.live.com')
        elif text=='Yahoo':
            self.le3.setText('smtp.mail.yahoo.com')
        elif text=='Gmail':
            self.le3.setText('smtp.gmail.com')
    def onActivatedPort(self,text):
        if text=='Live Port':
            self.le4.setText('587')
        else: self.le4.setText('465')
        
        
    def showcolDialog(self):
        if self.InsideSound:
            self.Play('sounds/w.wav')
        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.body.setStyleSheet("color: %s"
                % col.name())
    def showfontDialog(self):
        if self.InsideSound:
            self.Play('sounds/w.wav')
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.body.setFont(font)      
            

    def Send(self): 
         self.status.setText('Pre-Requisites are not fully filled, Try again  ')
         
         
         mystr=str(self.leTo.text())
         mylist=mystr.split(',')
         mylist=mylist[:-1]
         TempList=[]
         ToList=[]
         for elm in mylist:
             k=elm.strip()
             TempList.append(k)
             
         for elm in TempList:
             temp=elm
             ToList.append(temp)
         # ToList available now ---list of selected emails
         self.__ok=False
         for element in ToList:
             
                #print element
            if str(self.leAttach.text()) != 'None' or '':
                self.email.send(str(element),str(self.leSubject.text()),str(self.body.toPlainText()),attach=str(self.leAttach.text()))
                print 'Sent email to {}'.format(element)
                self.status.setText('Sent Succesfully')
                self.__ok=True
                #create a label or qmessagebox to show it has been sent
            else:
                self.email.send(str(element),str(self.leSubject.text()),str(self.body.toPlainText()),attach=None)
                print 'Sent email to {}'.format(element)
                self.status.setText('Sent Succesfully')
                self.__ok=True
         if self.__ok: 
              self.Play('sounds/send1.wav')
         if not self.__ok:
              self.Play('sounds/send2.wav')
             
                
    def setPulse(self):
        self.__soundType=self.sounds["Pulse A"]
        self.soundChanged()
    def setCool(self):
        self.__soundType=self.sounds["Cool"]
        self.soundChanged()
    def setCloud(self):
        self.__soundType=self.sounds["CloudNine"]
        self.soundChanged()
    def setGreen(self):
        self.__soundType=self.sounds["GreenPlace"]
        self.soundChanged()
    def setDarkclouds(self):
        self.__soundType=self.sounds["darkclouds"]
        self.soundChanged()
    def toggleSound(self):
        if self.__pSound:
            self.__pSound = False
            #self.Stop("sounds/dramatic.wav")
            #self.Stop("sounds/fivestars.wav")
            #self.Stop("sounds/funny.wav")
            #self.Stop("sounds/enemylines.wav")
            #self.Stop("sounds/darkclouds.wav")
            
        else:
            self.__pSound = True
        self.soundChanged()
    def Play(self,address):

        QtGui.QSound(address).play()
    def Stop(self,address):
            QtGui.QSound(address).stop()
    def soundChanged(self):
        if self.__soundType == self.sounds["Pulse A"]:
            self.sound = self.Play("sounds/Pulse A.wav")
        elif self.__soundType == self.sounds["Cool"] :
            self.sound = self.Play("sounds/Cool.wav")
        elif self.__soundType == self.sounds["CloudNine"]:
            self.sound = self.Play("sounds/CloudNine.wav")
        elif self.__soundType == self.sounds["GreenPlace"]:
            self.sound=self.Play("sounds/GreenPlace.wav")
        else:
             self.sound = self.Play("sounds/darkclouds.wav")
             


class ServersDialog(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ServersDialog, self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.resize(200,120)
        self.setWindowTitle('SMTP HELP')
        self.setWindowIcon(QtGui.QIcon('icons/manual.png'))




        self.lbl1=QtGui.QLabel('<b>Prefered Servers</b>')

        self.lbl2=QtGui.QLabel('smtp.live.com')
        self.lbl4=QtGui.QLabel('smtp.mail.yahoo.com')
        self.lbl3=QtGui.QLabel('smtp.gmail.com')

        self.lbl5=QtGui.QLabel('<b>port</b>')
        self.lbl6=QtGui.QLabel('587')
        self.lbl7=QtGui.QLabel('465')
        self.lbl8=QtGui.QLabel('465')



        hbox1=QtGui.QHBoxLayout()
        hbox1.addWidget(self.lbl1)
        hbox2=QtGui.QHBoxLayout()
        hbox2.addWidget(self.lbl2)
        hbox3=QtGui.QHBoxLayout()
        hbox3.addWidget(self.lbl3)
        hbox4=QtGui.QHBoxLayout()
        hbox4.addWidget(self.lbl4)
        vbox=QtGui.QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        hbox5=QtGui.QHBoxLayout()
        hbox5.addWidget(self.lbl5)
        hbox6=QtGui.QHBoxLayout()
        hbox6.addWidget(self.lbl6)
        hbox7=QtGui.QHBoxLayout()
        hbox7.addWidget(self.lbl7)
        hbox8=QtGui.QHBoxLayout()
        hbox8.addWidget(self.lbl8)
        vbox2=QtGui.QVBoxLayout()
        vbox2.addLayout(hbox5)
        vbox2.addLayout(hbox6)
        vbox2.addLayout(hbox7)
        vbox2.addLayout(hbox8)

        Hbox=QtGui.QHBoxLayout()
        Hbox.addLayout(vbox)
        Hbox.addLayout(vbox2)
        group=QtGui.QGroupBox('SMTP')
        group.setLayout(Hbox)
        Hbox2=QtGui.QHBoxLayout()
        Hbox2.addWidget(group)
        self.setLayout(Hbox2)
        self.show()
class About(QtGui.QWidget):

    def __init__(self,parent):
        super(About,self).__init__()


        self.initUI()
    def initUI(self):
        self.setWindowTitle("FOLLOW US")
        self.ok=QtGui.QPushButton('OK')
        self.ok.setFixedSize(self.ok.sizeHint())
        self.ok.clicked.connect(self.close)
        self.lbl1=QtGui.QLabel('An ultimate Email app,written to ease  all complicated mail issues ')
        self.lbl2=QtGui.QLabel('Developed by Soheil Khodayari')
        self.lb3=QtGui.QLabel('Started at 2014')
        self.lb4=QtGui.QLabel('Iran University Of Science And Technology')
        self.setWindowIcon(QtGui.QIcon('icons/1.png'))


        group=QtGui.QGroupBox('About')

        hbox1=QtGui.QHBoxLayout()
        hbox1.addWidget(self.lbl1)
        hbox2=QtGui.QHBoxLayout()
        hbox2.addWidget(self.lbl2)
        hbox3=QtGui.QHBoxLayout()
        hbox3.addWidget(self.lb3)
        hbox4=QtGui.QHBoxLayout()
        hbox4.addWidget(self.lb4)
        vbox=QtGui.QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.lbl2)
        vbox.addWidget(self.lb3)
        vbox.addWidget(self.lb4)
        vbox.setSpacing(15)
        group.setLayout(vbox)
        vbox00=QtGui.QVBoxLayout()
        vbox00.addWidget(group)
        vbox00.addWidget(self.ok)





        self.setLayout(vbox00)
        self.show()
    #def buttonClicked(self):

        #webbrowser.open('http://iust.ac.ir')
    





