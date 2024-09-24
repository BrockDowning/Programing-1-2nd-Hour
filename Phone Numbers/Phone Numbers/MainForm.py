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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._button10 = System.Windows.Forms.Button()
        self._button11 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(508, 73)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(13, 100)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(508, 73)
        self._label2.TabIndex = 1
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 185)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(508, 73)
        self._label3.TabIndex = 2
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 274)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(508, 73)
        self._label4.TabIndex = 3
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(114, 361)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(406, 73)
        self._label5.TabIndex = 4
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(528, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(98, 73)
        self._button1.TabIndex = 5
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(632, 14)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(95, 72)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(13, 362)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(95, 70)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button8
        # 
        self._button8.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(528, 362)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(98, 73)
        self._button8.TabIndex = 12
        self._button8.Text = "Show"
        self._button8.UseVisualStyleBackColor = False
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(528, 274)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(98, 73)
        self._button9.TabIndex = 13
        self._button9.Text = "Show"
        self._button9.UseVisualStyleBackColor = False
        self._button9.Click += self.Button9Click
        # 
        # button10
        # 
        self._button10.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button10.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button10.Location = System.Drawing.Point(528, 185)
        self._button10.Name = "button10"
        self._button10.Size = System.Drawing.Size(98, 73)
        self._button10.TabIndex = 14
        self._button10.Text = "Show"
        self._button10.UseVisualStyleBackColor = False
        self._button10.Click += self.Button10Click
        # 
        # button11
        # 
        self._button11.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button11.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button11.Location = System.Drawing.Point(527, 100)
        self._button11.Name = "button11"
        self._button11.Size = System.Drawing.Size(98, 73)
        self._button11.TabIndex = 15
        self._button11.Text = "Show"
        self._button11.UseVisualStyleBackColor = False
        self._button11.Click += self.Button11Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(632, 363)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(95, 72)
        self._button4.TabIndex = 16
        self._button4.Text = "Clear"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(632, 275)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(95, 72)
        self._button5.TabIndex = 17
        self._button5.Text = "Clear"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(632, 186)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(95, 72)
        self._button6.TabIndex = 18
        self._button6.Text = "Clear"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(632, 101)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(95, 72)
        self._button7.TabIndex = 19
        self._button7.Text = "Clear"
        self._button7.UseVisualStyleBackColor = False
        self._button7.Click += self.Button7Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(739, 443)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button11)
        self.Controls.Add(self._button10)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Phone Numbers"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label1.Text = "(608) 758-2848  -  Olive Garden"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button11Click(self, sender, e):
        self._label2.Text = "(608) 856-5867  -  Sky Zone"

    def Button10Click(self, sender, e):
        self._label3.Text = "(608) 757-9700  -  Texas Roadhouse"

    def Button9Click(self, sender, e):
        self._label4.Text = "(920) 699-4950  -  Nike Outlet"

    def Button8Click(self, sender, e):
         self._label5.Text = " (608) 758-9337  -  Game Stop"

    def Button7Click(self, sender, e):
        self._label2.Text = ""

    def Button6Click(self, sender, e):
        self._label3.Text = ""

    def Button5Click(self, sender, e):
        self._label4.Text = ""

    def Button4Click(self, sender, e):
        self._label5.Text = ""