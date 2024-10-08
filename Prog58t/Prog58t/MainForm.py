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
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(110, 148)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 0
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(243, 40)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 1
        self._label1.Text = "label1"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(95, 302)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "label2"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(423, 302)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 3
        self._label3.Text = "label3"
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(345, 173)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 23)
        self._button2.TabIndex = 4
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(567, 191)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 23)
        self._button3.TabIndex = 5
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(36, 103)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(394, 117)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 7
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(697, 445)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Total = float(self._textBox1.Text)
        Paid  = float(self._textBox2.Text)
        Change = float(Paid - Total)
        QuarterChange = float(Change / 25)
        PaidInQuarters = int