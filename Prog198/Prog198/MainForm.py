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
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._button1.Location = System.Drawing.Point(38, 368)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(477, 59)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate Average"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._button2.Location = System.Drawing.Point(556, 358)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(162, 40)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._button3.Location = System.Drawing.Point(556, 404)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(162, 40)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Aquamarine
        self._label1.Location = System.Drawing.Point(23, 21)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(383, 39)
        self._label1.TabIndex = 3
        self._label1.Text = "Enter three test scores:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Aquamarine
        self._label2.Location = System.Drawing.Point(87, 87)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(153, 38)
        self._label2.TabIndex = 4
        self._label2.Text = "Score 1: "
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Aquamarine
        self._label3.Location = System.Drawing.Point(87, 170)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(153, 38)
        self._label3.TabIndex = 5
        self._label3.Text = "Score 2: "
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Aquamarine
        self._label4.Location = System.Drawing.Point(87, 250)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(153, 38)
        self._label4.TabIndex = 6
        self._label4.Text = "Score 3: "
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Aquamarine
        self._label5.Location = System.Drawing.Point(513, 22)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(153, 38)
        self._label5.TabIndex = 7
        self._label5.Text = "Average:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.MintCream
        self._label6.Location = System.Drawing.Point(513, 75)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(153, 50)
        self._label6.TabIndex = 8
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(247, 87)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(233, 45)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(246, 163)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(233, 45)
        self._textBox2.TabIndex = 10
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(246, 250)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(233, 45)
        self._textBox3.TabIndex = 11
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightSeaGreen
        self.ClientSize = System.Drawing.Size(748, 453)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "Prog198"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Score1 = float(self._textBox1.Text)
        Score2 = float(self._textBox2.Text)
        Score3 = float(self._textBox3.Text)
        Sum = Score1 + Score2 + Score3
        Average = Sum / 3
        self._label6.Text = "" + str(round(Average, 2))

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()