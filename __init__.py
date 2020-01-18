import wx

class ModPicker(wx.App):  # intro screen
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, id, title)

class Menu(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(101, '&Open', 'Open a new document')
        file.Append(102, '&Save', 'Save the document')
        file.AppendSeparator()
        quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')
        quit.SetBitmap(wx.Image('stock_exit-16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        countries = wx.Menu()  # for loop to collect countries in folder; >105


        menubar.Append(file, '&File')
        menubar.Append(countries, '&Countries')

        self.setMenuBar()
        self.CreateStatusBar()

class Editor(wx.app):
    def OnInit(self):
        frame = Menu(None, -1, "")
        frame.show(True)
        return True

app = Editor()
app.MainLoop()