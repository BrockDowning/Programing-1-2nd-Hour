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
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightCoral
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(39, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(147, 103)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightCoral
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(296, 331)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(147, 103)
        self._button2.TabIndex = 1
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightCoral
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(552, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(147, 103)
        self._button3.TabIndex = 2
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MistyRose
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 40, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 156)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(218, 135)
        self._label1.TabIndex = 3
        self._label1.Text = "A = "
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MistyRose
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 40, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(261, 156)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(218, 135)
        self._label2.TabIndex = 4
        self._label2.Text = "C = "
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MistyRose
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 40, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(515, 156)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(218, 135)
        self._label3.TabIndex = 5
        self._label3.Text = "R = "
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(245, 40)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(253, 45)
        self._textBox1.TabIndex = 6
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(745, 446)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 50, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        radius = float(self._textBox1.Text)
        P = 3.14159
        area = round(P * radius**2,3)
        circum = 2 * radius * P
        self._label1.Text = str(area)
        self._label2.Text = str(circum)
        self._label3.Text = str(radius)


    def Button3Click(self, sender, e):
        self._textBox1.Text = ""
        self._label1.Text = "A= "
        self._label2.Text = "C= "
        self._label3.Text = "R= "

    def Button2Click(self, sender, e):
        Application.Exit()