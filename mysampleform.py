import clr
clr.AddReference("BaseForm")
import BaseForm
import System.Windows.Forms as WinForms
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(BaseForm.frmMyBaseForm):
        def __init__(self):
                self.InitializeComponent()
        
        def InitializeComponent(self):
                self._menuStrip1 = System.Windows.Forms.MenuStrip()
                self._fileToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._menu1ToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._menu2ToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._menuStrip1.SuspendLayout()
                self.SuspendLayout()
                # 
                # menuStrip1
                # 
                self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
                        [self._fileToolStripMenuItem]))
                self._menuStrip1.Location = System.Drawing.Point(0, 0)
                self._menuStrip1.Name = "menuStrip1"
                self._menuStrip1.Size = System.Drawing.Size(338, 24)
                self._menuStrip1.TabIndex = 0
                self._menuStrip1.Text = "menuStrip1"
                # 
                # fileToolStripMenuItem
                # 
                self._fileToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
                        [self._menu1ToolStripMenuItem,
                        self._menu2ToolStripMenuItem]))
                self._fileToolStripMenuItem.Name = "fileToolStripMenuItem"
                self._fileToolStripMenuItem.Size = System.Drawing.Size(37, 20)
                self._fileToolStripMenuItem.Text = "File"
                # 
                # menu1ToolStripMenuItem
                # 
                self._menu1ToolStripMenuItem.Name = "menu1ToolStripMenuItem"
                self._menu1ToolStripMenuItem.Size = System.Drawing.Size(152, 22)
                self._menu1ToolStripMenuItem.Text = "Menu1"
                # 
                # menu2ToolStripMenuItem
                # 
                self._menu2ToolStripMenuItem.Name = "menu2ToolStripMenuItem"
                self._menu2ToolStripMenuItem.Size = System.Drawing.Size(152, 22)
                self._menu2ToolStripMenuItem.Text = "Menu2"
                # 
                # MainForm
                # 
                self.ClientSize = System.Drawing.Size(338, 341)
                self.Controls.Add(self._menuStrip1)
                self.MainMenuStrip = self._menuStrip1
                self.Name = "MainForm"
                self.Text = "Payroll System"
		self.AppTitle = "GemSoft Systems"
                self._menuStrip1.ResumeLayout(False)
                self._menuStrip1.PerformLayout()
                self.ResumeLayout(False)
                self.PerformLayout()
    
        def agoy(self):
                WinForms.Application.Run(self)
    
    
        
    
    
    
    


def main():
    MainForm().agoy()


if __name__ == '__main__':
    main()
