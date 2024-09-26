import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Pink
        self._textBox1.Location = System.Drawing.Point(13, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(233, 53)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Pink
        self._textBox2.Location = System.Drawing.Point(13, 335)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(233, 53)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.Pink
        self._textBox3.Location = System.Drawing.Point(13, 227)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(233, 53)
        self._textBox3.TabIndex = 2
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.Pink
        self._textBox4.Location = System.Drawing.Point(13, 118)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(233, 53)
        self._textBox4.TabIndex = 3
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Ivory
        self._label1.Font = System.Drawing.Font("Tw Cen MT Condensed", 40, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(471, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(327, 83)
        self._label1.TabIndex = 4
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Lime
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(268, 227)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(204, 226)
        self._button1.TabIndex = 5
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Cyan
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(496, 227)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(159, 226)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Red
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(678, 227)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(159, 226)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Ivory
        self._label2.Font = System.Drawing.Font("Tw Cen MT Condensed", 40, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(471, 118)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(327, 83)
        self._label2.TabIndex = 8
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox5
        # 
        self._textBox5.BackColor = System.Drawing.Color.SteelBlue
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(304, 46)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(149, 35)
        self._textBox5.TabIndex = 9
        self._textBox5.Text = "Sum:"
        # 
        # textBox6
        # 
        self._textBox6.BackColor = System.Drawing.Color.SteelBlue
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(304, 141)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(149, 35)
        self._textBox6.TabIndex = 10
        self._textBox6.Text = "Average:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SteelBlue
        self.ClientSize = System.Drawing.Size(862, 465)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = int(self._textBox3.Text)
        num4 = int(self._textBox4.Text)
        sum  = num1 + num2 + num3 + num4
        Avg = sum // 4.0
        self._label1.Text = str(sum)
        self._label2.Text = str(Avg)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()