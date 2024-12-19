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
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSkyBlue
        self._button1.Font = System.Drawing.Font("Segoe Script", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(53, 351)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(172, 90)
        self._button1.TabIndex = 0
        self._button1.Text = "Ok"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSkyBlue
        self._button2.Font = System.Drawing.Font("Segoe Script", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(557, 351)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(172, 90)
        self._button2.TabIndex = 1
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.DodgerBlue
        self._radioButton1.Font = System.Drawing.Font("Poor Richard", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(53, 52)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(207, 47)
        self._radioButton1.TabIndex = 2
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Choice 1"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.DodgerBlue
        self._radioButton2.Font = System.Drawing.Font("Poor Richard", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(53, 105)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(207, 47)
        self._radioButton2.TabIndex = 3
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Choice 2"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.DodgerBlue
        self._radioButton3.Font = System.Drawing.Font("Poor Richard", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(53, 158)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(207, 47)
        self._radioButton3.TabIndex = 4
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Choice 3"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.DodgerBlue
        self._checkBox1.Font = System.Drawing.Font("Sylfaen", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(453, 52)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(216, 47)
        self._checkBox1.TabIndex = 5
        self._checkBox1.Text = "Choice 4"
        self._checkBox1.UseVisualStyleBackColor = False
        self._checkBox1.CheckedChanged += self.CheckBox1CheckedChanged
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.DodgerBlue
        self._checkBox2.Font = System.Drawing.Font("Sylfaen", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(453, 106)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(216, 47)
        self._checkBox2.TabIndex = 6
        self._checkBox2.Text = "Choice 5"
        self._checkBox2.UseVisualStyleBackColor = False
        # 
        # checkBox3
        # 
        self._checkBox3.BackColor = System.Drawing.Color.DodgerBlue
        self._checkBox3.Font = System.Drawing.Font("Sylfaen", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(453, 158)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(216, 47)
        self._checkBox3.TabIndex = 7
        self._checkBox3.Text = "Choice 6"
        self._checkBox3.UseVisualStyleBackColor = False
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Navy
        self._label1.Font = System.Drawing.Font("Rockwell", 35.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(12, 3)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(324, 46)
        self._label1.TabIndex = 8
        self._label1.Text = "Radio Buttons"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Navy
        self._label2.Font = System.Drawing.Font("Rockwell", 35.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(426, 3)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(324, 46)
        self._label2.TabIndex = 9
        self._label2.Text = "Check Boxes"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightBlue
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(53, 208)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(676, 140)
        self._label3.TabIndex = 10
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Teal
        self.ClientSize = System.Drawing.Size(762, 453)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog247"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        one = ""
        two = ""
        three = ""
        four = ""
        five = ""
        six = ""
        if radioButton1Checked:
            one = "Choice 1"
        if radioButton2Checked:
            two = "Choice 2"
        if radioButton3Checked:
            three =  "Choice 3"
        if checkBox1Checked:
            four =  "Choice 4"
        if checkBox2Checked:
            five =  "Choice 5"
        if checkBox3Checked:
            six =  "Choice 6"
        self._label3.Text = "You selected" + one + " and " + two + " and " + three + " and " + four + " and " + five + " and " + six
        

    def Button2Click(self, sender, e):
        Application.Exit()

    def RadioButton1CheckedChanged(self, sender, e):
        pass

    def CheckBox1CheckedChanged(self, sender, e):
        pass