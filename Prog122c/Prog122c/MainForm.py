import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(128, 64, 64)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 17)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(157, 75)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(23, 355)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(157, 75)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(511, 355)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(157, 75)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(177, 13)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(491, 329)
        self._listBox1.TabIndex = 3
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self.ClientSize = System.Drawing.Size(680, 442)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog122c"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        Output = 

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()