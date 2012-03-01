from SS import SafeSide2
import sys
try:  
    import pygtk  
    pygtk.require("2.0")  
except:
    print 'error'
    pass  
try:  
    import gtk  
    import gtk.glade  
except:  
    print("GTK Not Availible")
    sys.exit(1)
class SSgui:
    wTree = None
    def __init__( self ):
        self.wTree = gtk.glade.XML("SSGui.Glade")
        dic = { 
        "on_Encrypt_button_press_event" : self.encrypt,
        "on_Decrypt_button_press_event" : self.decrypt,
        "on_windowMain_destroy" : self.quit,
        }
        self.wTree.signal_autoconnect( dic )
        gtk.main()
    def encrypt(self, widget,wtf):
        try:
            GUI_string= self.wTree.get_widget("entry2").get_text()
            self.wTree.get_widget("output").set_text(SafeSide2().encryptstr(self.wTree.get_widget("keybox").get_text(),GUI_string))
        except ValueError:
            self.wTree.get_widget("hboxWarning").show()
        return 0
    def decrypt(self, widget,wtf):
        try:
            GUI_string= self.wTree.get_widget("entry1").get_text()
            self.wTree.get_widget("output").set_text(SafeSide2().decryptstr(self.wTree.get_widget("keybox").get_text(),GUI_string))
        except ValueError:
            self.wTree.get_widget("hboxWarning").show()
        return 0
    
    def quit(self, widget):
        sys.exit(0)
SSgui()
