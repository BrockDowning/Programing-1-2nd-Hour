﻿import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Black
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.White
        self._textBox1.Location = System.Drawing.Point(526, 52)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(244, 53)
        self._textBox1.TabIndex = 0
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Black
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.White
        self._textBox2.Location = System.Drawing.Point(526, 148)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(244, 53)
        self._textBox2.TabIndex = 1
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Black
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(526, 243)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(244, 54)
        self._label1.TabIndex = 2
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Black
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(526, 338)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(244, 54)
        self._label2.TabIndex = 3
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(-2, 243)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(313, 21)
        self._label3.TabIndex = 4
        self._label3.Text = "_______________________________________________________________"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(285, 264)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(26, 212)
        self._label4.TabIndex = 5
        self._label4.Text = "IIIIII"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 33, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 264)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(267, 169)
        self._label5.TabIndex = 6
        self._label5.Text = "PROG162h"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Black
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._button1.Location = System.Drawing.Point(13, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(266, 92)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Black
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._button2.Location = System.Drawing.Point(13, 131)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(266, 92)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Black
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._button3.Location = System.Drawing.Point(285, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(235, 211)
        self._button3.TabIndex = 9
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Lime
        self.ClientSize = System.Drawing.Size(806, 442)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog162h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        n = int(self._textBox1.Text)
        r = int(self._textBox2.Text)
        permutations = math.factorial (n) / math.factorial(n - r)
        GS = n - r
        self._label1.Text = "" + str(permutations)
        self._label2.Text = "" + str(GS)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()