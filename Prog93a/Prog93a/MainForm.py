import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(142, 25)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(153, 35)
        self._textBox1.TabIndex = 0
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(26, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(110, 56)
        self._label1.TabIndex = 1
        self._label1.Text = "Kilowatts Used:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 85)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(643, 47)
        self._label2.TabIndex = 2
        self._label2.Text = "_____________________________________________"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(26, 156)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(125, 39)
        self._label3.TabIndex = 3
        self._label3.Text = "Base Rate:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(26, 229)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(125, 39)
        self._label4.TabIndex = 4
        self._label4.Text = "Surcharge:"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(26, 322)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(125, 39)
        self._label5.TabIndex = 5
        self._label5.Text = "CityTax:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(142, 156)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(177, 39)
        self._label6.TabIndex = 6
        self._label6.Text = "$ "
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(142, 229)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(177, 39)
        self._label7.TabIndex = 7
        self._label7.Text = "$ "
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(142, 322)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(177, 39)
        self._label8.TabIndex = 8
        self._label8.Text = "$ "
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(428, 195)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(177, 39)
        self._label9.TabIndex = 9
        self._label9.Text = "$ "
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(455, 156)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(125, 39)
        self._label10.TabIndex = 10
        self._label10.Text = "TOTAL"
        self._label10.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label11
        # 
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(405, 257)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(225, 39)
        self._label11.TabIndex = 11
        self._label11.Text = "After May 20th Pay"
        self._label11.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(428, 305)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(177, 39)
        self._label12.TabIndex = 12
        self._label12.Text = "$ "
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(314, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(155, 56)
        self._button1.TabIndex = 13
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(475, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(155, 56)
        self._button2.TabIndex = 14
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(405, 74)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(136, 35)
        self._button3.TabIndex = 15
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(642, 443)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def TextBox1TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        KiloUsed = int(self._textBox1.Text)
        BaseR    = float(KiloUsed * 0.0475)
        BaseR    = self._label6.Text = "$ " + str(BaseR)
        SurCharge = float(round(BaseR * 0.10,2))
        SurCharge = self._label7.Text = "$ " + str(SurCharge)
        CityTax  = float(round(BaseR * 0.03,2))
        CityTax  = self._label8.Text = "$ " + str(CityTax)
        Total    = BaseR + SurCharge + CityTax
        Total    = self._label9.Text = "$ " + str(Total)
        TotMay   = Total * 1.04
        TotMay   = self._label12.Text = "$ " + str(TotMay)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""
        self._label9.Text = ""
        self._label12.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()