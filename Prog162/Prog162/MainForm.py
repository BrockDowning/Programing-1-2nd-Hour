import time
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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._textBox7 = System.Windows.Forms.TextBox()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self._label18 = System.Windows.Forms.Label()
        self._label19 = System.Windows.Forms.Label()
        self._label20 = System.Windows.Forms.Label()
        self._label21 = System.Windows.Forms.Label()
        self._label23 = System.Windows.Forms.Label()
        self._dateTimePicker1 = System.Windows.Forms.DateTimePicker()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(28, 387)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(166, 58)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(226, 387)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(166, 58)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(420, 387)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(166, 58)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._label1.Font = System.Drawing.Font("MV Boli", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(249, 37)
        self._label1.TabIndex = 4
        self._label1.Text = "Highlander Hotel"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("MV Boli", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(239, 63)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(150, 29)
        self._label2.TabIndex = 5
        self._label2.Text = "Today's Date: "
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label4.Font = System.Drawing.Font("MV Boli", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(28, 100)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(226, 29)
        self._label4.TabIndex = 8
        self._label4.Text = "Room Information"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label5.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(28, 175)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(136, 23)
        self._label5.TabIndex = 9
        self._label5.Text = "Nightly Charge:"
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(157, 132)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(148, 30)
        self._textBox3.TabIndex = 10
        self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(157, 168)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(148, 30)
        self._textBox4.TabIndex = 11
        self._textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label6.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(28, 139)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(123, 23)
        self._label6.TabIndex = 12
        self._label6.Text = "Nights:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._label7.Font = System.Drawing.Font("MV Boli", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(344, 139)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(226, 29)
        self._label7.TabIndex = 13
        self._label7.Text = "Additional Charges"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._label8.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(331, 175)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(123, 23)
        self._label8.TabIndex = 14
        self._label8.Text = "Room Service:"
        # 
        # textBox5
        # 
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(448, 171)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(148, 30)
        self._textBox5.TabIndex = 15
        self._textBox5.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._label9.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(331, 204)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(123, 23)
        self._label9.TabIndex = 16
        self._label9.Text = "Telephone: "
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._label10.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(331, 236)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(123, 23)
        self._label10.TabIndex = 17
        self._label10.Text = "Misc:"
        # 
        # textBox6
        # 
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(448, 203)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(148, 30)
        self._textBox6.TabIndex = 18
        self._textBox6.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox7
        # 
        self._textBox7.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox7.Location = System.Drawing.Point(448, 236)
        self._textBox7.Name = "textBox7"
        self._textBox7.Size = System.Drawing.Size(148, 30)
        self._textBox7.TabIndex = 19
        self._textBox7.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label11.Font = System.Drawing.Font("MV Boli", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(28, 217)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(226, 29)
        self._label11.TabIndex = 20
        self._label11.Text = "Total Charges"
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label12.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(28, 260)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(123, 23)
        self._label12.TabIndex = 21
        self._label12.Text = "Room Charges:"
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label13.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(-2, 297)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(166, 23)
        self._label13.TabIndex = 22
        self._label13.Text = "Additional Charges:"
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label14.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(28, 333)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(89, 23)
        self._label14.TabIndex = 23
        self._label14.Text = "Subtotal: "
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label15.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(239, 334)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(89, 23)
        self._label15.TabIndex = 24
        self._label15.Text = "Tax:"
        self._label15.Click += self.Label15Click
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label16.Font = System.Drawing.Font("MV Boli", 10, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.Location = System.Drawing.Point(448, 284)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(122, 23)
        self._label16.TabIndex = 25
        self._label16.Text = "Total Charges: "
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.White
        self._label17.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label17.Location = System.Drawing.Point(145, 260)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(126, 23)
        self._label17.TabIndex = 26
        self._label17.Text = "$"
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.Color.White
        self._label18.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label18.Location = System.Drawing.Point(157, 297)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(126, 23)
        self._label18.TabIndex = 27
        self._label18.Text = "$"
        # 
        # label19
        # 
        self._label19.BackColor = System.Drawing.Color.White
        self._label19.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label19.Location = System.Drawing.Point(107, 334)
        self._label19.Name = "label19"
        self._label19.Size = System.Drawing.Size(126, 23)
        self._label19.TabIndex = 28
        self._label19.Text = "$"
        # 
        # label20
        # 
        self._label20.BackColor = System.Drawing.Color.White
        self._label20.Font = System.Drawing.Font("Microsoft Sans Serif", 10, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label20.Location = System.Drawing.Point(282, 334)
        self._label20.Name = "label20"
        self._label20.Size = System.Drawing.Size(126, 23)
        self._label20.TabIndex = 29
        self._label20.Text = "$"
        # 
        # label21
        # 
        self._label21.BackColor = System.Drawing.Color.White
        self._label21.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label21.Location = System.Drawing.Point(420, 317)
        self._label21.Name = "label21"
        self._label21.Size = System.Drawing.Size(176, 49)
        self._label21.TabIndex = 30
        self._label21.Text = "$"
        # 
        # label23
        # 
        self._label23.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label23.Font = System.Drawing.Font("MV Boli", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label23.Location = System.Drawing.Point(362, 95)
        self._label23.Name = "label23"
        self._label23.Size = System.Drawing.Size(224, 29)
        self._label23.TabIndex = 32
        # 
        # dateTimePicker1
        # 
        self._dateTimePicker1.Location = System.Drawing.Point(386, 63)
        self._dateTimePicker1.Name = "dateTimePicker1"
        self._dateTimePicker1.Size = System.Drawing.Size(210, 20)
        self._dateTimePicker1.TabIndex = 33
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 64, 64)
        self.ClientSize = System.Drawing.Size(622, 457)
        self.Controls.Add(self._dateTimePicker1)
        self.Controls.Add(self._label23)
        self.Controls.Add(self._label21)
        self.Controls.Add(self._label20)
        self.Controls.Add(self._label19)
        self.Controls.Add(self._label18)
        self.Controls.Add(self._label17)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._textBox7)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog162"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label15Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        Nights = float(self._textBox3.Text)
        NightC = float(self._textBox4.Text)
        RoomS  = float(self._textBox5.Text)
        Tele   = float(self._textBox6.Text)
        Misc   = float(self._textBox7.Text)
        RoomC  = Nights * NightC
        AddiC  = RoomS + Tele + Misc
        SubTot = RoomC + AddiC
        Tax    = SubTot * 0.08
        TotC   = SubTot + Tax
        self._label17.Text = "$ " + str(round(RoomC, 3))
        self._label18.Text = "$ " + str(round(AddiC, 3))
        self._label19.Text = "$ " + str(round(SubTot, 3))
        self._label20.Text = "$ " + str(round(Tax, 3))
        self._label21.Text = "$ " + str(round(TotC, 3))

    def Button2Click(self, sender, e):
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._textBox6.Text = ""
        self._textBox7.Text = ""
        self._label17.Text = "$ "
        self._label18.Text = "$ "
        self._label19.Text = "$ "
        self._label20.Text = "$ "
        self._label21.Text = "$ "
        self._label23.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def MainFormLoad(self, sender, e):
        self._label23.Text = time.strftime("Time : %I: %M: %S: %p")