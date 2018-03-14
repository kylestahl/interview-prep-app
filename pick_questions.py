import wx


class AppFrame(wx.Frame):
    # Constructor
    def __init__(self, parent, id, title):
        # Call Frame Constrcutor
        wx.Frame.__init__(self, parent, id, title, 
                          wx.DefaultPosition, wx.Size(500, 500))
        
        # Create Panels for a new button and some text
        panel = wx.Panel(self,-1)
        
        
        # Add a button into the panel
        wx.Button(panel, -1, "New Question", (250,250))
        wx.StaticText(panel, -1, "Tell me about yourself.", 
                      (250, 100), style=wx.ALIGN_CENTRE)

class InterviewApp(wx.App):
    def OnInit(self):
        frame = AppFrame(None, -1, 'Interview Prep App')
        frame.Show(True)
        frame.Centre()
        return True

if __name__ == "__main__":
    app = InterviewApp()
    app.MainLoop()

# Randomized Question Picker
with open('questions.txt') as f:
   questions = f.readlines()
from random import randint
print(questions[randint(0,177)].strip())