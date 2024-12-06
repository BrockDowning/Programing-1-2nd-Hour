import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(59, 57)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(176, 39)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Choice 1"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(59, 102)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(176, 39)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Choice 2"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(59, 147)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(176, 39)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Choice 3"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(346, 58)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(183, 39)
        self._checkBox1.TabIndex = 3
        self._checkBox1.Text = "Choice 4"
        self._checkBox1.UseVisualStyleBackColor = False
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(346, 103)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(183, 39)
        self._checkBox2.TabIndex = 4
        self._checkBox2.Text = "Choice 5"
        self._checkBox2.UseVisualStyleBackColor = False
        # 
        # checkBox3
        # 
        self._checkBox3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(346, 147)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(183, 39)
        self._checkBox3.TabIndex = 5
        self._checkBox3.Text = "Choice 6"
        self._checkBox3.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._button1.Font = System.Drawing.Font("Tempus Sans ITC", 45, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(31, 345)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(228, 94)
        self._button1.TabIndex = 6
        self._button1.Text = "Ok"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._button2.Font = System.Drawing.Font("Tempus Sans ITC", 45, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(321, 345)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(228, 94)
        self._button2.TabIndex = 7
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label1.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(49, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(200, 45)
        self._label1.TabIndex = 8
        self._label1.Text = "Radio Buttons"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
        self._label2.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(329, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(200, 45)
        self._label2.TabIndex = 9
        self._label2.Text = "Check Boxes"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Teal
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(59, 240)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(470, 56)
        self._label3.TabIndex = 10
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SteelBlue
        self.ClientSize = System.Drawing.Size(668, 451)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Name = "MainForm"
        self.Text = "Prog247"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        First = 0
        Second = 0  
        if checkBox1._checked:
            

    def Button2Click(self, sender, e):
        Application.Exit()