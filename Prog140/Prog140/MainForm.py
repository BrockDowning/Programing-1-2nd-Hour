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
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 35, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(549, 52)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(58, 55)
        self._button1.TabIndex = 0
        self._button1.Text = "+"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 35, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(613, 52)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(58, 55)
        self._button2.TabIndex = 1
        self._button2.Text = "-"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 35, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(677, 52)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(58, 55)
        self._button3.TabIndex = 2
        self._button3.Text = "*"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 35, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(549, 125)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(58, 55)
        self._button4.TabIndex = 3
        self._button4.Text = "^"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 35, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(613, 125)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(58, 55)
        self._button5.TabIndex = 4
        self._button5.Text = "/"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(677, 125)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(58, 55)
        self._button6.TabIndex = 5
        self._button6.Text = "//"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.BackColor = System.Drawing.Color.FromArgb(0, 192, 192)
        self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(571, 186)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(147, 54)
        self._button7.TabIndex = 6
        self._button7.Text = "MOD"
        self._button7.UseVisualStyleBackColor = False
        self._button7.Click += self.Button7Click
        # 
        # button8
        # 
        self._button8.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(571, 259)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(147, 42)
        self._button8.TabIndex = 7
        self._button8.Text = "Clear"
        self._button8.UseVisualStyleBackColor = False
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.BackColor = System.Drawing.Color.Red
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(549, 307)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(186, 42)
        self._button9.TabIndex = 8
        self._button9.Text = "Exit"
        self._button9.UseVisualStyleBackColor = False
        self._button9.Click += self.Button9Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(194, 52)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(226, 45)
        self._textBox1.TabIndex = 9
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(194, 225)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(226, 45)
        self._textBox2.TabIndex = 10
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 52)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(175, 45)
        self._label1.TabIndex = 11
        self._label1.Text = "Number 1:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(13, 135)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(175, 45)
        self._label2.TabIndex = 12
        self._label2.Text = "Operation:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 225)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(175, 45)
        self._label3.TabIndex = 13
        self._label3.Text = "Number 2:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(194, 135)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(226, 45)
        self._label4.TabIndex = 14
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 332)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(175, 45)
        self._label5.TabIndex = 15
        self._label5.Text = "Result:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(194, 332)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(226, 45)
        self._label6.TabIndex = 16
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self.ClientSize = System.Drawing.Size(784, 443)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog140"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button8Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = ""
        self._label6.Text = ""

    def Button1Click(self, sender, e):
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        Answer = Num1 + Num2
        self._label4.Text = " +"
        self._label6.Text = "" + str(Answer)

    def Button2Click(self, sender, e):
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        Answer = Num1 - Num2
        self._label4.Text = " -"
        self._label6.Text = "" + str(Answer)

    def Button3Click(self, sender, e):
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        Answer = Num1 * Num2
        self._label4.Text = " *"
        self._label6.Text = "" + str(Answer)

    def Button4Click(self, sender, e):
        Num1 = float(self._textBox1.Text)
        Num2 = float(self._textBox2.Text)
        Answer = Num1**Num2
        self._label4.Text = " ^"
        self._label6.Text = "" + str(Answer)

    def Button5Click(self, sender, e):
        Num1 = float(self._textBox1.Text)
        Num2 = float(self._textBox2.Text)
        Answer = Num1 / Num2
        self._label4.Text = " /"
        self._label6.Text = "" + str(Answer)

    def Button6Click(self, sender, e):
        Num1 = float(self._textBox1.Text)
        Num2 = float(self._textBox2.Text)
        Answer = Num1 // Num2
        self._label4.Text = " //"
        self._label6.Text = "" + str(Answer)

    def Button7Click(self, sender, e):
        Num1 = float(self._textBox1.Text)
        Num2 = float(self._textBox2.Text)
        Answer = Num1%Num2
        self._label4.Text = " MOD"
        self._label6.Text = "" + str(Answer)

    def Button9Click(self, sender, e):
        Application.Exit()

    def MainFormLoad(self, sender, e):
        pass