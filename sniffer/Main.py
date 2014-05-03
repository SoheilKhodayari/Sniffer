import sys
from PyQt4 import QtGui
from Widget import *
import webbrowser
class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.initUI()


    def initUI(self):
        self.grabber=MyWidget()
        self.setCentralWidget(self.grabber)
        self.center()
        self.setWindowTitle('SNIFFER')
        self.makeMenu()
        #self.resize(500,500)
        self.show()



    def closeEvent(self, event):
        self.play('sounds/exit.wav')

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def makeMenu(self):
        iconExit = QtGui.QIcon('icons/exit.png')
        exitAction = QtGui.QAction(iconExit, '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        iconAttach=QtGui.QIcon('icons/attach.png')
        attachAction=QtGui.QAction(iconAttach,'&Attachment',self)
        attachAction.setShortcut('Ctrl+A')
        attachAction.setStatusTip('Attach Files To Your Emails')
        attachAction.triggered.connect(self.Attach)

        iconFont=QtGui.QIcon('icons/font.png')
        fontAction=QtGui.QAction(iconFont,'&Font Options',self)
        fontAction.setShortcut('Ctrl+F')
        fontAction.setStatusTip('Set Appropriate Fonts And Sizes')
        fontAction.triggered.connect(self.Font)

        iconColor=QtGui.QIcon('icons/color.png')
        colorAction=QtGui.QAction(iconColor,'&Writing Hue',self)
        colorAction.setShortcut('Ctrl+C')
        colorAction.setStatusTip('Set Desired Hues Of Email Body ')
        colorAction.triggered.connect(self.Color)

        IconTxToBdy=QtGui.QIcon('icons/text.png')
        bodyAction=QtGui.QAction(IconTxToBdy,'&Text To Body',self)
        bodyAction.setShortcut('Ctrl+T')
        bodyAction.setStatusTip('Copy A Message From A Text File To Mail Body')
        bodyAction.triggered.connect(self.TextToBody)
        
        smtpIcon=QtGui.QIcon('icons/smtp.png')
        smtpAction=QtGui.QAction(smtpIcon,'&SMTP Servers Help',self)
        smtpAction.setShortcut('Ctrl+S')
        smtpAction.triggered.connect(self.SmtpHelp)
        
        AboutIcon=QtGui.QIcon('icons/about.png')
        aboutAction=QtGui.QAction(AboutIcon,'&About',self)
        aboutAction.setShortcut('Ctrl+O')
        aboutAction.triggered.connect(self.About)
        
        ForkIcon=QtGui.QIcon('icons/Fork.png')
        forkAction=QtGui.QAction(ForkIcon,'&Fork on Git',self)
        forkAction.setShortcut('Ctrl+F')
        forkAction.triggered.connect(self.Fork)
        
        IconHelp=QtGui.QIcon('icons/help.png')
        helpAction=QtGui.QAction(IconHelp,'&Help',self)
        helpAction.setShortcut('Ctrl+H')
        helpAction.triggered.connect(self.HelpFile)

        
        # to be added Help Option, Sound option , and More Option --thats it
        
        


        menubar = QtGui.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        #menubar.setFixedHeight(22)
        menufile = menubar.addMenu('File')
        menuSmtp=menubar.addMenu('SMTP')
        menuAbout=menubar.addMenu('About')
        
        menufile.addAction(attachAction)
        menufile.addSeparator()
        menufile.addAction(fontAction)
        menufile.addAction(colorAction)
        menufile.addAction(bodyAction)

        menufile.addAction(exitAction)
        
        menuSmtp.addAction(smtpAction)
        menuAbout.addAction(aboutAction)
        menuAbout.addSeparator()
        menuAbout.addAction(forkAction)
        
        helpmenu=menubar.addMenu('Help')
        helpmenu.addAction(helpAction)
        
        iconsound=QtGui.QIcon('icons/Play.png')
        soundAction=QtGui.QAction(iconsound,'&Play ',self)
        soundAction.setShortcut('Ctrl+Y')
        soundAction.setStatusTip('Sound <b>Activation</b>')
        soundAction.setCheckable(True)
        soundAction.triggered.connect(self.toggleSound)

        Stopicon=QtGui.QIcon('icons/stop.png')
        StopAction=QtGui.QAction(Stopicon,'&Stop ',self)
        StopAction.setShortcut('Ctrl+I')
        StopAction.setStatusTip('Sound <b>Interuption</b>')
        StopAction.setCheckable(True)
        StopAction.triggered.connect(self.Stop)
        
        SoundP=QtGui.QActionGroup(self)
        StopAction.setChecked(True)
        SoundP.addAction(soundAction)
        SoundP.addAction(StopAction)
        
        

        icond=QtGui.QIcon('icons/sound1.png')
        pulseAction=QtGui.QAction(icond,'&Pulse A',self)
        pulseAction.setCheckable(True)
        pulseAction.triggered.connect(self.setPulse)

        cloudAction=QtGui.QAction(icond,'&Cloud Nine',self)
        cloudAction.setCheckable(True)
        cloudAction.triggered.connect(self.setCloud)

        coolAction=QtGui.QAction(icond,'&Cool',self)
        coolAction.setCheckable(True)
        coolAction.triggered.connect(self.setCool)

        greenAction=QtGui.QAction(icond,'&Green Place',self)
        greenAction.setCheckable(True)
        greenAction.triggered.connect(self.setGreen)

        DarkcloudsSAction=QtGui.QAction(icond,'&Dark Cloud',self)
        DarkcloudsSAction.setCheckable(True)
        DarkcloudsSAction.triggered.connect(self.setDarkclouds)

        SoundM=QtGui.QActionGroup(self)
        DarkcloudsSAction.setChecked(True)
        SoundM.addAction(pulseAction)
        SoundM.addAction(cloudAction)
        SoundM.addAction(coolAction)
        SoundM.addAction(greenAction)
        SoundM.addAction(DarkcloudsSAction)
        
        soundmenu=menubar.addMenu('Sounds')
        soundmenu.addAction(soundAction)
        soundmenu.addAction(StopAction)
        soundmenu.addSeparator()
        
        soundmenu.addAction(pulseAction)
        soundmenu.addAction(cloudAction)
        soundmenu.addAction(coolAction)
        soundmenu.addAction(greenAction)
        soundmenu.addAction(DarkcloudsSAction)


    def Attach(self):
        
        self.play('sounds/attchmentfile.wav')
        self.grabber.InsideSound=False
        self.grabber.openfile()
        self.grabber.InsideSound=True
    def Font(self):
        self.play('sounds/font.wav')
        self.grabber.InsideSound=False
        self.grabber.showfontDialog()
        self.grabber.InsideSound=True
    def Color(self):
        
        self.grabber.InsideSound=False
        self.play('sounds/colorofpen.wav')
        self.grabber.showcolDialog()
        self.grabber.InsideSound=True
        
    def TextToBody(self):
        self.Play('sounds/TextToBody.wav')
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')
        if fname:

            f = open(fname, 'r')

            with f:
                data = f.read()
                self.grabber.body.setText(str(data))
    def SmtpHelp(self):
        self.play('sounds/smtp.wav')
    
        self.dialog = ServersDialog()
        self.dialog.show()
    def About(self,app):
        self.play('sounds/about.wav')
        self.wg= About(app)
        self.wg.show()
    def Fork(self):
        webbrowser.open('http://github.com')
    def HelpFile(self):
        os.system('start documentation/Help.pdf')
    def Play(self,address):

        #QtGui.QSound(address).play()
        self.grabber.Play(address)
    def toggleSound(self):
        self.grabber.toggleSound()
    def setPulse(self):
        self.grabber.setPulse()
    def setCloud(self):
        self.grabber.setCloud()
    def setGreen(self):
        self.grabber.setGreen()
    def setDarkclouds(self):
        self.grabber.setDarkclouds()
    def setCool(self):
        self.grabber.setCool()
    def Stop(self):
        self.grabber.Stop("sounds/Pulse A.wav")
        self.grabber.Stop("sounds/Cool.wav")
        self.grabber.Stop("sounds/CloudNine.wav")
        self.grabber.Stop("sounds/GreenPlace.wav")
        self.grabber.Stop("sounds/darkclouds.wav")
    def play(self,address):

        QtGui.QSound(address).play()
    
        

def main():

    app = QtGui.QApplication(sys.argv)
    import ctypes
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QtGui.QIcon('icons/cr2.png'))
    ex = Main()
    ex.play('sounds/StartApp2.wav')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

