import wx


class HelloFrame(wx.Frame):
    def __init__(self, title):
        super().__init__(None, title=title, size=(400, 300))
        self.name = '<unknown>'

        vertical_box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vertical_box_sizer)

        panel = wx.Panel(self)

        vertical_box_sizer.Add(panel,
                               wx.ID_ANY,
                               wx.EXPAND | wx.ALL,
                               20)

        grid = wx.GridSizer(4, 1, 5, 5)

        self.text = wx.TextCtrl(panel, size=(400, -1))

        enter_button = wx.Button(panel, label='Enter')
        enter_button.Bind(wx.EVT_BUTTON, self.set_name)

        self.label = wx.StaticText(panel,
                                   label='Welcome',
                                   style=wx.ALIGN_LEFT)

        message_button = wx.Button(panel, label='Show Message')
        message_button.Bind(wx.EVT_BUTTON, self.show_message)

        grid.AddMany([self.text,
                      enter_button,
                      self.label,
                      message_button])

        panel.SetSizer(grid)

        self.Centre()

    def show_message(self, event):
        """ Event Handler to display the Message Dialog
        using the current value of the name attribute. """
        dialog = wx.MessageDialog(None,
                                  message='Welcome To CRMA ' + self.name,
                                  caption='Hello',
                                  style=wx.OK)
        dialog.ShowModal()

    def set_name(self, event):
        """ Event Handler for the Enter button.
            Retrieves the text entered into the input field
            and sets the self.name attribute. This is then
            used to set the text label """
        self.name = self.text.GetLineText(0)
        self.label.SetLabelText('Welcome ' + self.name)


class MainApp(wx.App):

    def OnInit(self):
        """ Initialise the GUI display"""
        frame = HelloFrame(title='Enter&Exit Register')
        frame.Show()
        return True

    def OnExit(self):
        """ Executes when the GUI application shuts down"""
        print('Goodbye')
        return True


app = MainApp()
app.MainLoop()
