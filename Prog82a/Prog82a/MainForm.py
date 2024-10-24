﻿import System.Drawing
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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Yellow
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(47, 355)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(167, 79)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Yellow
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(266, 355)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(167, 79)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Yellow
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(486, 355)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(167, 79)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(47, 98)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(287, 38)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(366, 98)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(287, 38)
        self._textBox2.TabIndex = 4
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Yellow
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(88, 41)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(201, 43)
        self._label1.TabIndex = 5
        self._label1.Text = "Speed Limit"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Yellow
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(406, 41)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(201, 43)
        self._label2.TabIndex = 6
        self._label2.Text = "Speed"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Yellow
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(121, 171)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(462, 87)
        self._label3.TabIndex = 7
        self._label3.Text = "Fine = "
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._label3.Click += self.Label3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(701, 446)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog82a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        SpeedLimit = int(self._textBox1.Text)
        SpeedofCar = int(self._textBox2.Text)
        MphOver = SpeedofCar - SpeedLimit
        if MphOver < 0:
            Fine = 0
        Fine = 20.00 + (MphOver * 5.00)
        self._label3.Text = "Fine =$ " + str(Fine)
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label3.Text = "Fine =$ "

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label3Click(self, sender, e):
        pass