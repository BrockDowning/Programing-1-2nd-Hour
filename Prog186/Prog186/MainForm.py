import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 64, 0)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 35.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(382, 54)
        self._label1.TabIndex = 0
        self._label1.Text = "Stadium Seating"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 64, 0)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(13, 99)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(197, 28)
        self._label2.TabIndex = 1
        self._label2.Text = "Tickets Sold"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(192, 64, 0)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(484, 99)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(197, 28)
        self._label3.TabIndex = 2
        self._label3.Text = "Revenue Generated"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(192, 64, 0)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(13, 140)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(382, 181)
        self._label4.TabIndex = 3
        self._label4.Text = "Enter the number of tickets sold for each class of seats"
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.Black
        self._label5.Location = System.Drawing.Point(40, 190)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(88, 28)
        self._label5.TabIndex = 4
        self._label5.Text = "Class A: "
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.Black
        self._label6.Location = System.Drawing.Point(40, 235)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(88, 28)
        self._label6.TabIndex = 5
        self._label6.Text = "Class B: "
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.Black
        self._label7.Location = System.Drawing.Point(40, 279)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(88, 28)
        self._label7.TabIndex = 6
        self._label7.Text = "Class C: "
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(135, 190)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(230, 27)
        self._textBox1.TabIndex = 7
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(135, 236)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(230, 27)
        self._textBox2.TabIndex = 8
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(134, 280)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(230, 27)
        self._textBox3.TabIndex = 9
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(192, 64, 0)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(401, 140)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(366, 181)
        self._label8.TabIndex = 10
        self._label8.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.Color.Black
        self._label9.Location = System.Drawing.Point(432, 158)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(88, 28)
        self._label9.TabIndex = 11
        self._label9.Text = "Class A: "
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.Black
        self._label10.Location = System.Drawing.Point(432, 193)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(88, 28)
        self._label10.TabIndex = 12
        self._label10.Text = "Class B: "
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.Color.Black
        self._label11.Location = System.Drawing.Point(432, 235)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(88, 28)
        self._label11.TabIndex = 13
        self._label11.Text = "Class C: "
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.ForeColor = System.Drawing.Color.Black
        self._label12.Location = System.Drawing.Point(432, 279)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(150, 28)
        self._label12.TabIndex = 14
        self._label12.Text = "Total Revenue: "
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("NSimSun", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(40, 349)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(226, 88)
        self._button1.TabIndex = 19
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("NSimSun", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(281, 349)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(226, 88)
        self._button2.TabIndex = 20
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("NSimSun", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(530, 349)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(226, 88)
        self._button3.TabIndex = 21
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.White
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.ForeColor = System.Drawing.Color.Black
        self._label13.Location = System.Drawing.Point(526, 158)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(230, 28)
        self._label13.TabIndex = 22
        self._label13.Text = "$ "
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.White
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.ForeColor = System.Drawing.Color.Black
        self._label14.Location = System.Drawing.Point(526, 193)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(230, 28)
        self._label14.TabIndex = 23
        self._label14.Text = "$ "
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.White
        self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.ForeColor = System.Drawing.Color.Black
        self._label15.Location = System.Drawing.Point(526, 235)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(230, 28)
        self._label15.TabIndex = 24
        self._label15.Text = "$ "
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.White
        self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.ForeColor = System.Drawing.Color.Black
        self._label16.Location = System.Drawing.Point(581, 279)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(175, 28)
        self._label16.TabIndex = 25
        self._label16.Text = "$ "
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self.ClientSize = System.Drawing.Size(779, 458)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog186"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        ClassA  = float(self._textBox1.Text)
        ClassB  = float(self._textBox2.Text)
        ClassC  = float(self._textBox3.Text)
        ClassAR = ClassA * 15
        ClassBR = ClassB * 12
        ClassCR = ClassC * 9
        TotRev  = ClassAR + ClassBR + ClassCR
        self._label13.Text = "$ " + str(ClassAR)
        self._label14.Text = "$ " + str(ClassBR)
        self._label15.Text = "$ " + str(ClassCR)
        self._label16.Text = "$ " + str(TotRev)
        

    def Button2Click(self, sender, e):
        self._label13.Text = "$ "
        self._label14.Text = "$ "
        self._label15.Text = "$ "
        self._label16.Text = "$ "
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()