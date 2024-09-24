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
        self._label1 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._button10 = System.Windows.Forms.Button()
        self._button11 = System.Windows.Forms.Button()
        self._button12 = System.Windows.Forms.Button()
        self._button13 = System.Windows.Forms.Button()
        self._button14 = System.Windows.Forms.Button()
        self._button15 = System.Windows.Forms.Button()
        self._button16 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button17 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Cyan
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(73, 38)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Cyan
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(667, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(73, 38)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Teal
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(92, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(569, 38)
        self._label1.TabIndex = 2
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Cyan
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(667, 56)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(73, 38)
        self._button3.TabIndex = 3
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.Cyan
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(667, 100)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(73, 38)
        self._button4.TabIndex = 4
        self._button4.Text = "Clear"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.Cyan
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(667, 232)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(73, 38)
        self._button5.TabIndex = 5
        self._button5.Text = "Clear"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.Color.Cyan
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(667, 144)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(73, 38)
        self._button6.TabIndex = 6
        self._button6.Text = "Clear"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.BackColor = System.Drawing.Color.Cyan
        self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(667, 188)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(73, 38)
        self._button7.TabIndex = 7
        self._button7.Text = "Clear"
        self._button7.UseVisualStyleBackColor = False
        self._button7.Click += self.Button7Click
        # 
        # button8
        # 
        self._button8.BackColor = System.Drawing.Color.Cyan
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(667, 276)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(73, 38)
        self._button8.TabIndex = 8
        self._button8.Text = "Clear"
        self._button8.UseVisualStyleBackColor = False
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.BackColor = System.Drawing.Color.Cyan
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(667, 320)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(73, 38)
        self._button9.TabIndex = 9
        self._button9.Text = "Clear"
        self._button9.UseVisualStyleBackColor = False
        self._button9.Click += self.Button9Click
        # 
        # button10
        # 
        self._button10.BackColor = System.Drawing.Color.Cyan
        self._button10.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button10.Location = System.Drawing.Point(12, 277)
        self._button10.Name = "button10"
        self._button10.Size = System.Drawing.Size(73, 38)
        self._button10.TabIndex = 10
        self._button10.Text = "Show"
        self._button10.UseVisualStyleBackColor = False
        self._button10.Click += self.Button10Click
        # 
        # button11
        # 
        self._button11.BackColor = System.Drawing.Color.Cyan
        self._button11.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button11.Location = System.Drawing.Point(13, 233)
        self._button11.Name = "button11"
        self._button11.Size = System.Drawing.Size(73, 38)
        self._button11.TabIndex = 11
        self._button11.Text = "Show"
        self._button11.UseVisualStyleBackColor = False
        self._button11.Click += self.Button11Click
        # 
        # button12
        # 
        self._button12.BackColor = System.Drawing.Color.Cyan
        self._button12.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button12.Location = System.Drawing.Point(13, 189)
        self._button12.Name = "button12"
        self._button12.Size = System.Drawing.Size(73, 38)
        self._button12.TabIndex = 12
        self._button12.Text = "Show"
        self._button12.UseVisualStyleBackColor = False
        self._button12.Click += self.Button12Click
        # 
        # button13
        # 
        self._button13.BackColor = System.Drawing.Color.Cyan
        self._button13.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button13.Location = System.Drawing.Point(13, 145)
        self._button13.Name = "button13"
        self._button13.Size = System.Drawing.Size(73, 38)
        self._button13.TabIndex = 13
        self._button13.Text = "Show"
        self._button13.UseVisualStyleBackColor = False
        self._button13.Click += self.Button13Click
        # 
        # button14
        # 
        self._button14.BackColor = System.Drawing.Color.Cyan
        self._button14.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button14.Location = System.Drawing.Point(13, 101)
        self._button14.Name = "button14"
        self._button14.Size = System.Drawing.Size(73, 38)
        self._button14.TabIndex = 14
        self._button14.Text = "Show"
        self._button14.UseVisualStyleBackColor = False
        self._button14.Click += self.Button14Click
        # 
        # button15
        # 
        self._button15.BackColor = System.Drawing.Color.Cyan
        self._button15.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button15.Location = System.Drawing.Point(13, 57)
        self._button15.Name = "button15"
        self._button15.Size = System.Drawing.Size(73, 38)
        self._button15.TabIndex = 15
        self._button15.Text = "Show"
        self._button15.UseVisualStyleBackColor = False
        self._button15.Click += self.Button15Click
        # 
        # button16
        # 
        self._button16.BackColor = System.Drawing.Color.Cyan
        self._button16.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button16.Location = System.Drawing.Point(13, 321)
        self._button16.Name = "button16"
        self._button16.Size = System.Drawing.Size(73, 38)
        self._button16.TabIndex = 16
        self._button16.Text = "Show"
        self._button16.UseVisualStyleBackColor = False
        self._button16.Click += self.Button16Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Teal
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(92, 100)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(569, 38)
        self._label2.TabIndex = 17
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Teal
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(92, 188)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(569, 38)
        self._label3.TabIndex = 18
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Teal
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(92, 145)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(569, 38)
        self._label4.TabIndex = 19
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Teal
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(92, 57)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(569, 38)
        self._label5.TabIndex = 20
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Teal
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(92, 232)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(569, 38)
        self._label6.TabIndex = 21
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Teal
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(92, 277)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(569, 38)
        self._label7.TabIndex = 22
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Teal
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(92, 320)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(569, 38)
        self._label8.TabIndex = 23
        # 
        # button17
        # 
        self._button17.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button17.Location = System.Drawing.Point(12, 366)
        self._button17.Name = "button17"
        self._button17.Size = System.Drawing.Size(728, 61)
        self._button17.TabIndex = 24
        self._button17.Text = "EXIT"
        self._button17.UseVisualStyleBackColor = True
        self._button17.Click += self.Button17Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(0, 64, 64)
        self.ClientSize = System.Drawing.Size(752, 439)
        self.Controls.Add(self._button17)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button16)
        self.Controls.Add(self._button15)
        self.Controls.Add(self._button14)
        self.Controls.Add(self._button13)
        self.Controls.Add(self._button12)
        self.Controls.Add(self._button11)
        self.Controls.Add(self._button10)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "My Schedule"
        self.ResumeLayout(False)


    def Button11Click(self, sender, e):
        self._label6.Text = "Spanish III Class"

    def Button1Click(self, sender, e):
        self._label1.Text = "Pre-Cadet Class"

    def Button15Click(self, sender, e):
        self._label5.Text = "Computer Programming Class"

    def Button14Click(self, sender, e):
        self._label2.Text = "Chemistry Honors Class"

    def Button13Click(self, sender, e):
        self._label4.Text = "Geometry Honors Class"

    def Button12Click(self, sender, e):
        self._label3.Text = "United States History Class"

    def Button10Click(self, sender, e):
        self._label7.Text = "English 10 Class"

    def Button16Click(self, sender, e):
        self._label8.Text = "Construction and Engineering Class"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        self._label5.Text = ""

    def Button4Click(self, sender, e):
        self._label2.Text = ""

    def Button6Click(self, sender, e):
        self._label4.Text = ""

    def Button7Click(self, sender, e):
        self._label3.Text = ""

    def Button5Click(self, sender, e):
        self._label6.Text = ""

    def Button8Click(self, sender, e):
        self._label7.Text = ""

    def Button9Click(self, sender, e):
        self._label8.Text = ""

    def Button17Click(self, sender, e):
        Application.Exit()