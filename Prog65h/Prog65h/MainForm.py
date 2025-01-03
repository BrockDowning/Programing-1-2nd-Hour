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
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(377, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(186, 67)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(377, 142)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(186, 67)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(377, 280)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(186, 67)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(13, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(194, 38)
        self._textBox1.TabIndex = 3
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(214, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(157, 38)
        self._label1.TabIndex = 4
        self._label1.Text = "<-Pounds"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(214, 115)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(157, 38)
        self._label2.TabIndex = 5
        self._label2.Text = "<-Shilings"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(214, 210)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(157, 38)
        self._label3.TabIndex = 6
        self._label3.Text = "<-Pences"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(14, 115)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(194, 38)
        self._textBox2.TabIndex = 8
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(14, 210)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(194, 38)
        self._textBox3.TabIndex = 9
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(213, 319)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(157, 38)
        self._label6.TabIndex = 11
        self._label6.Text = "<-NewAmount"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._label7.Location = System.Drawing.Point(12, 319)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(195, 38)
        self._label7.TabIndex = 12
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Fuchsia
        self.ClientSize = System.Drawing.Size(596, 422)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog65h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Pound   = float(self._textBox1.Text)
        UndividedShiling = float(self._textBox2.Text)
        Shiling = UndividedShiling * 0.05
        UndividedPence  = float(self._textBox3.Text)
        Pence = float(UndividedPence / 240)
        Total = float(round(Pound + Shiling + Pence,2))
        self._label7.Text = "" + str(Total)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label7.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()