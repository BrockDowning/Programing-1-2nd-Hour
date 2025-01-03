﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.R = System.Random()
        self.ballup = 0
        self.balld = 0
        self.flagleft = False
        self.flagright = False
    
    def InitializeComponent(self):
        self._components = System.ComponentModel.Container()
        self._lbltitle = System.Windows.Forms.Label()
        self._leftscore = System.Windows.Forms.Label()
        self._rightscore = System.Windows.Forms.Label()
        self._lblball = System.Windows.Forms.Label()
        self._lblleft = System.Windows.Forms.Label()
        self._lblright = System.Windows.Forms.Label()
        self._timerdummy = System.Windows.Forms.Timer(self._components)
        self._timerboolean = System.Windows.Forms.Timer(self._components)
        self._timerright = System.Windows.Forms.Timer(self._components)
        self._timerleft = System.Windows.Forms.Timer(self._components)
        self._timerball = System.Windows.Forms.Timer(self._components)
        self._timermulti = System.Windows.Forms.Timer(self._components)
        self.SuspendLayout()
        # 
        # lbltitle
        # 
        self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._lbltitle.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._lbltitle.Location = System.Drawing.Point(12, 25)
        self._lbltitle.Name = "lbltitle"
        self._lbltitle.Size = System.Drawing.Size(958, 52)
        self._lbltitle.TabIndex = 0
        self._lbltitle.Text = "Press Enter to Start or M to Start Multiplayer"
        self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # leftscore
        # 
        self._leftscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._leftscore.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._leftscore.Location = System.Drawing.Point(78, 96)
        self._leftscore.Name = "leftscore"
        self._leftscore.Size = System.Drawing.Size(166, 109)
        self._leftscore.TabIndex = 1
        self._leftscore.Text = "0"
        self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # rightscore
        # 
        self._rightscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._rightscore.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._rightscore.Location = System.Drawing.Point(734, 96)
        self._rightscore.Name = "rightscore"
        self._rightscore.Size = System.Drawing.Size(166, 109)
        self._rightscore.TabIndex = 2
        self._rightscore.Text = "0"
        self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._rightscore.DoubleClick += self.RightscoreDoubleClick
        # 
        # lblball
        # 
        self._lblball.BackColor = System.Drawing.Color.White
        self._lblball.Location = System.Drawing.Point(479, 304)
        self._lblball.Name = "lblball"
        self._lblball.Size = System.Drawing.Size(20, 20)
        self._lblball.TabIndex = 3
        self._lblball.Click += self.LblballClick
        # 
        # lblleft
        # 
        self._lblleft.BackColor = System.Drawing.Color.White
        self._lblleft.Location = System.Drawing.Point(12, 246)
        self._lblleft.Name = "lblleft"
        self._lblleft.Size = System.Drawing.Size(20, 100)
        self._lblleft.TabIndex = 4
        self._lblleft.DoubleClick += self.LblleftDoubleClick
        # 
        # lblright
        # 
        self._lblright.BackColor = System.Drawing.Color.White
        self._lblright.Location = System.Drawing.Point(950, 246)
        self._lblright.Name = "lblright"
        self._lblright.Size = System.Drawing.Size(20, 100)
        self._lblright.TabIndex = 5
        # 
        # timerdummy
        # 
        self._timerdummy.Interval = 1
        # 
        # timerboolean
        # 
        self._timerboolean.Enabled = True
        self._timerboolean.Interval = 95
        self._timerboolean.Tick += self.TimerbooleanTick
        # 
        # timerright
        # 
        self._timerright.Interval = 20
        self._timerright.Tick += self.TimerrightTick
        # 
        # timerleft
        # 
        self._timerleft.Interval = 20
        self._timerleft.Tick += self.TimerleftTick
        # 
        # timerball
        # 
        self._timerball.Interval = 10
        self._timerball.Tick += self.TimerballTick
        # 
        # timermulti
        # 
        self._timermulti.Interval = 20
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(988, 607)
        self.Controls.Add(self._lblright)
        self.Controls.Add(self._lblleft)
        self.Controls.Add(self._lblball)
        self.Controls.Add(self._rightscore)
        self.Controls.Add(self._leftscore)
        self.Controls.Add(self._lbltitle)
        self.Name = "MainForm"
        self.Text = "Pong"
        self.Load += self.MainFormLoad
        self.SizeChanged += self.MainFormSizeChanged
        self.KeyDown += self.MainFormKeyDown
        self.ResumeLayout(False)


    def TimerballTick(self, sender, e):
        ball = self._lblball
        lpdl = self._lblleft
        rpdl = self._lblright
        rscore = int(self._rightscore.Text)
        lscore = int(self._leftscore.Text)
        ball.Top += self.ballup
        ball.Left += 8 * self.balld
        
        if ball.Right >= rpdl.Right and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
            self.balld = -1
            self.ballup = self.R.Next(-4, 5)
        elif ball.Left <= lpdl.Left and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
            self.balld = 1
            self.ballup = self.R.Next(-4, 5)
        
        if ball.Top <= 0:
            self.balld = -1
            self.Top += 5 * self.balld
        elif ball.Bottom >= self.Height:
            self.balld = 1
            self.Top += 5 * self.balld
        
        if ball.Top <= self.Top + 10:
            self.ballup = 1
        elif ball.Top >= self.Height - 50:
            self.ballup = -1
        
        if ball.Location.X <= 0 or \
           (ball.Location.X < lpdl.Left - 20 and ball.Location.Y < lpdl.Top):
               rscore += 1
               self._rightscore.Text = str(rscore)
               ball.Left = self.Width // 2
               ball.Top = self.Height // 2
        
        if ball.Location.X >= self.Width or \
           (ball.Location.X > rpdl.Right + 20 and ball.Location.Y > rpdl.Top):
               lscore += 1
               self._leftscore.Text = str(lscore)
               ball.Left = self.Width // 2
               ball.Top = self.Height // 2
               
        if rscore == 10:  # Right win condition
            self._timerball.Enabled = False
            ball.Left = self.Width // 2
            ball.Top = self.Height // 2
            self.ballup = 0
            self._lbltitle.Text = "Right Player Wins! Press R to restart"
            self._lbltitle.Visible = True
        
        if lscore == 10:  # Left win condition
            self._timerball.Enabled = False
            ball.Left = self.Width // 2
            ball.Top = self.Height // 2
            self.ballup = 0
            self._lbltitle.Text = "Left Player Wins! Press R to restart"
            self._lbltitle.Visible = True
        
        """ TODO: ? """
        if self._timerboolean.Enabled:
            lpdl.Top = ball.Top - 20
            if lscore > rscore:
                lpdl.Location.X = - 75
        pass

    def MainFormKeyDown(self, sender, e):
        tball  = self._timerball
        tdum   = self._timerdummy
        tbool  = self._timerboolean
        tmult  = self._timermulti
        tleft  = self._timerleft
        tright = self._timerright
        bl     = self._lblball
        lpdl   = self._lblleft
        rpdl   = self._lblright
        title  = self._lbltitle
        
        def reset():
            title.Visible = True
            title.Text = "Press Enter to Start or M to Start Multiplayer"
            self._leftscore.Text = "0"
            self._rightscore.Text = "0"
            tball.Enabled  = False
            tdum.Enabled   = False
            tbool.Enabled  = False
            tmult.Enabled  = False
            tleft.Enabled  = False
            tright.Enabled = False
            bl.Left = self.Width // 2
            bl.Top = self.Height // 2
            lpdl.Top = (self.Height // 2) - 50 + lpdl.Height
            rpdl.Top = (self.Height // 2) - 50 + rpdl.Height
            self.BackColor = Color.Black
            self._lblball.BackColor = Color.White
            self._lblleft.BackColor = Color.White
            self._lblright.BackColor = Color.White
            self._rightscore.BackColor = Color.Black
            self._leftscore.BackColor = Color.Black
            self._rightscore.ForeColor = Color.White
            self._leftscore.ForeColor = Color.White
            self._lbltitle.ForeColor  = Color.White
            bl.BackColor = Color.White
            
        if e.KeyCode == Keys.R:
            reset()
            
        """ TODO: SECRET CONTROL """
        
        if e.KeyCode == Keys.Enter:
            tball.Enabled = True
            tdum.Enabled  = True
            tbool.Enabled = not tmult.Enabled
            title.Visible = False
            
        if e.KeyCode == Keys.M:
            reset()
            title.Visible = True
            title.Text = "Use W and S to Move the Left Paddle; Hit Enter to Start"
            tmult.Enabled = True
            
        if tdum.Enabled:
            if e.KeyCode == Keys.Up:
                self.flagright = False
                tright.Enabled = True
            elif e.KeyCode == Keys.Down:
                self.flagright = True
                tright.Enabled = True
                
        if e.KeyCode == Keys.B:
            tbool.Enabled = False
                
        if tmult.Enabled and tball.Enabled:
            if e.KeyCode == Keys.W:
                self.flagleft = False
                tleft.Enabled = True
            elif e.KeyCode == Keys.S:
                self.flagleft = True
                tleft.Enabled = True
            
        pass

    def MainFormLoad(self, sender, e):
        self.balld = 1
        self.balldup = self.R.Next(-4, 5)
    
    def pdlTick(self, pdl, flagd, tmr):
        if flagd == True:
            pdl.Top += 5
        else:
            pdl.Top -= 5
        if pdl.Top <= 10 or pdl.Bottom >= self.Height - 50:
            tmr.Enabled = False

    def TimerleftTick(self, sender, e):
        self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

    def TimerrightTick(self, sender, e):
        self.pdlTick(self._lblright, self.flagright, self._timerright)

    def LblballClick(self, sender, e):
        self._lblball.BackColor = Color.Blue
        self.BackColor = Color.Red 

    def MainFormSizeChanged(self, sender, e):
        self._lblright.Left = self.Width - 25 - self._lblright.Width
        self._rightscore.Left = self.Width - 75 - self._rightscore.Width
        self._lbltitle.Width = self.Width - 25
        self._lblball.Left = self.Width // 2
        self._lblball.Top = self.Height // 2

    def RightscoreDoubleClick(self, sender, e):
        self._rightscore.BackColor = Color.Azure
        self._leftscore.BackColor  = Color.Bisque
        self._lblright.BackColor   = Color.DarkKhaki
        self._lblleft.BackColor    = Color.DarkKhaki
        self._rightscore.ForeColor = Color.Black
        self._leftscore.ForeColor  = Color.Black
        

    def LblleftDoubleClick(self, sender, e):
        self.BackColor         = Color.AntiqueWhite
        self._lblball.BackColor  = Color.Aqua
        self._lblright.BackColor = Color.CadetBlue
        self._lblleft.BackColor  = Color.CornflowerBlue
        self._rightscore.ForeColor = Color.Navy
        self._leftscore.ForeColor  = Color.Navy
        self._lbltitle.ForeColor      = Color.Navy

    def TimerbooleanTick(self, sender, e):
        pass