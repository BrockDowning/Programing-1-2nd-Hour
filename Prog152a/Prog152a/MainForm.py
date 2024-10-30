import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(13, 77)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(676, 355)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(241, 58)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(260, 13)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(241, 58)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(507, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(182, 58)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(701, 444)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog152a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        header = ""
        sum = 0
        for num in range(3, 9669+1, 3):
            sum += num
        Line = "3 + 6 + 9 +12 ... 9669 = " + str(sum)
        self._listBox1.Items.Add(Line)

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()