import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Lime
        self._button1.Font = System.Drawing.Font("Niagara Solid", 24.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(56, 357)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(201, 62)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Black
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(103, 37)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(253, 29)
        self._label1.TabIndex = 1
        self._label1.Text = "Sales for the Month:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Black
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Location = System.Drawing.Point(78, 83)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(278, 29)
        self._label2.TabIndex = 2
        self._label2.Text = "Advance pay Awarded:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Black
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Location = System.Drawing.Point(141, 135)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(215, 29)
        self._label3.TabIndex = 3
        self._label3.Text = "Commision Rate:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Black
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Location = System.Drawing.Point(200, 187)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(156, 29)
        self._label4.TabIndex = 4
        self._label4.Text = "Commision:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Black
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Location = System.Drawing.Point(244, 238)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(112, 29)
        self._label5.TabIndex = 5
        self._label5.Text = "Net Pay:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(363, 37)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(207, 32)
        self._textBox1.TabIndex = 6
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(363, 83)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(207, 32)
        self._textBox2.TabIndex = 7
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label6.Location = System.Drawing.Point(363, 135)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(207, 29)
        self._label6.TabIndex = 8
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label7.Location = System.Drawing.Point(362, 187)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(207, 29)
        self._label7.TabIndex = 9
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label8.Location = System.Drawing.Point(363, 238)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(207, 29)
        self._label8.TabIndex = 10
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Lime
        self._button2.Font = System.Drawing.Font("Niagara Solid", 24.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(299, 357)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(201, 62)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Lime
        self._button3.Font = System.Drawing.Font("Niagara Solid", 24.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(535, 357)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(201, 62)
        self._button3.TabIndex = 12
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(773, 431)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog240"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        SFM     = float(self._textBox1.Text)
        APA     = float(self._textBox2.Text)
        ComishR = 0
        if SFM <= 10000:
            ComishR = 0.05
        elif SFM > 10000 and SFM < 15000:
            ComishR = 0.10
        elif SFM >= 15000 and SFM < 18000:
            ComishR = 0.12
        elif SFM >= 18000 and SFM < 22000:
            ComishR = 0.14
        else:
            ComishR = 0.16
        Comish  = SFM * ComishR
        NetPay  = Comish - APA
        ComishR = str(ComishR)
        self._label6.Text = "% " + str(ComishR[2:])
        self._label7.Text = "$ " + str(Comish)
        self._label8.Text = "$ " + str(NetPay)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()