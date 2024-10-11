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
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Green
        self._button1.Location = System.Drawing.Point(15, 362)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(180, 71)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._label1.Location = System.Drawing.Point(466, 142)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(149, 23)
        self._label1.TabIndex = 1
        self._label1.Text = "Total Due:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._label2.Location = System.Drawing.Point(466, 60)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(149, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "Total Paid:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Green
        self._button2.Location = System.Drawing.Point(258, 362)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(180, 71)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear Data"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Green
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(482, 362)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(180, 71)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(399, 96)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(275, 32)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(399, 14)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(275, 32)
        self._textBox2.TabIndex = 7
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Lime
        self._label3.Location = System.Drawing.Point(15, 9)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(180, 37)
        self._label3.TabIndex = 8
        self._label3.Text = "Change: $"
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Lime
        self._label4.Location = System.Drawing.Point(15, 60)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(156, 37)
        self._label4.TabIndex = 9
        self._label4.Text = "Dollars:$"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Lime
        self._label5.Location = System.Drawing.Point(15, 113)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(156, 37)
        self._label5.TabIndex = 10
        self._label5.Text = "Quarters: "
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Lime
        self._label6.Location = System.Drawing.Point(15, 167)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(156, 37)
        self._label6.TabIndex = 11
        self._label6.Text = "Dimes:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Lime
        self._label7.Location = System.Drawing.Point(15, 217)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(156, 37)
        self._label7.TabIndex = 12
        self._label7.Text = "Nickels:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Lime
        self._label8.Location = System.Drawing.Point(15, 271)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(156, 29)
        self._label8.TabIndex = 13
        self._label8.Text = "Pennies:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(0, 64, 0)
        self.ClientSize = System.Drawing.Size(697, 445)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Clear Data"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Total  = float(self._textBox1.Text)
        Paid   = float(self._textBox2.Text)
        Change = float(Paid - Total)
        ChangeAmount = Change
        self._label3.Text = "Change :$ " + str(Change)
        DollarsDue = int(Change / 1)
        Change = Change - DollarsDue
        QuartersDue = int(Change / 0.25)
        self._label5.Text = "Quarters Due: " + str(QuartersDue)
        Change = Change - (QuartersDue * 0.25)
        DimesDue = int(Change / 0.10)
        self._label6.Text = "Dimes Due: " + str(DimesDue)
        Change = Change - (DimesDue * 0.10)
        NickelsDue = int(Change / 0.05)
        self._label7.Text = "Nickels Due: " + str(NickelsDue)
        Change = Change - (NickelsDue * 0.05)
        PenniesDue = Change / 0.01
        self._label8.Text = "Pennies Due: " + str(round(PenniesDue,0))   

        
        self._label3.Text = "Change:$ " + str(ChangeAmount)
        self._label4.Text = "Dollars:$ " + str(DollarsDue)
        self._label5.Text = "Quarters: " + str(QuartersDue)
        self._label6.Text = "Dimes: " + str(DimesDue)
        self._label7.Text = "Nickels: " + str(NickelsDue)
        self._label8.Text = "Pennies: " + str(PenniesDue)
        
        
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text = "Total Due: "
        self._label3.Text = "Total Due:$ "
        self._label4.Text = "Total Due:$ "
        self._label5.Text = "Total Due: "
        self._label6.Text = "Total Due: "
        self._label7.Text = "Total Due: "
        self._label8.Text = "Total Due: "

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label3Click(self, sender, e):
        pass