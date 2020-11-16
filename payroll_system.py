import clr

clr.AddReference('System.Windows.Forms')
import System.Windows.Forms as WinForms

clr.AddReference("BaseForm")
import BaseForm

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

import frmuser
import frmdbsetup

from frmlogon import frmLogon



class MainForm(BaseForm.frmMyBaseForm):
        def __init__(self):
                self.InitializeComponent()
        
        def InitializeComponent(self):
                self._statusStrip1 = System.Windows.Forms.StatusStrip()
                self._label1 = System.Windows.Forms.Label()
                self._panel1 = System.Windows.Forms.Panel()
                self._menuStrip1 = System.Windows.Forms.MenuStrip()
                self._toolStripMenuItem1 = System.Windows.Forms.ToolStripMenuItem()
                self._tsDepartment = System.Windows.Forms.ToolStripMenuItem()
                self._companyToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._employeeMasterToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._toolStripSeparator1 = System.Windows.Forms.ToolStripSeparator()
                self._ratesToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._deductionCategoryToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._toolStripSeparator2 = System.Windows.Forms.ToolStripSeparator()
                self._ratesTableToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._deductionSetupToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._toolStripSeparator3 = System.Windows.Forms.ToolStripSeparator()
                self._dailyTimesheetEntryToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._toolStripSeparator4 = System.Windows.Forms.ToolStripSeparator()
                self._quitToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._reportToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._payrollListingToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._payrollSummaryToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._toolsToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._databaseSetupToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._userManagementToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._accessConfigToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._helpToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._aboutToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
                self._statusStrip1.SuspendLayout()
                self._panel1.SuspendLayout()
                self._menuStrip1.SuspendLayout()
                self.SuspendLayout()
                # 
                # statusStrip1
                # 
                # 
                # label1
                # 
                #self._label1.Dock = System.Windows.Forms.DockStyle.Top
                #self._label1.Font = System.Drawing.Font("Comic Sans MS", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
                #self._label1.Location = System.Drawing.Point(0, 0)
                #self._label1.Name = "label1"
                #self._label1.ForeColor = System.Drawing.Color.Firebrick
                #self._label1.Size = System.Drawing.Size(409, 52)
                #self._label1.TabIndex = 0
                #self._label1.Text = "gemsoft payroll system"
                #self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
                # 
                # panel1
                # 
               # self._panel1.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
               # self._panel1.Controls.Add(self._menuStrip1)
               # self._panel1.Location = System.Drawing.Point(0, 52)
	#	self._panel1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
               # self._panel1.Name = "panel1"
               # self._panel1.Size = System.Drawing.Size(73, 262)
               # self._panel1.TabIndex = 6
                # 
                # menuStrip1
                # 
                self._menuStrip1.Dock = System.Windows.Forms.DockStyle.Top
                self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
                        [self._toolStripMenuItem1,
                        self._reportToolStripMenuItem,
                        self._toolsToolStripMenuItem,
                        self._helpToolStripMenuItem]))
                self._menuStrip1.Location = System.Drawing.Point(0, 0)
                self._menuStrip1.Name = "menuStrip1"
                self._menuStrip1.Size = System.Drawing.Size(60, 262)
                self._menuStrip1.Stretch = False
                self._menuStrip1.TabIndex = 3
                self._menuStrip1.Text = "menuStrip1"
                # 
                # toolStripMenuItem1
                # 
                self._toolStripMenuItem1.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
                        [self._tsDepartment,
                        self._companyToolStripMenuItem,
                        self._employeeMasterToolStripMenuItem,
                        self._toolStripSeparator1,
                        self._ratesToolStripMenuItem,
                        self._deductionCategoryToolStripMenuItem,
                        self._toolStripSeparator2,
                        self._ratesTableToolStripMenuItem,
                        self._deductionSetupToolStripMenuItem,
                        self._toolStripSeparator3,
                        self._dailyTimesheetEntryToolStripMenuItem,
                        self._toolStripSeparator4,
                        self._quitToolStripMenuItem]))
                self._toolStripMenuItem1.Name = "toolStripMenuItem1"
                self._toolStripMenuItem1.Size = System.Drawing.Size(47, 19)
                self._toolStripMenuItem1.Text = "File"
                # 
                # tsDepartment
                # 
                self._tsDepartment.Name = "tsDepartment"
                self._tsDepartment.Size = System.Drawing.Size(188, 22)
                self._tsDepartment.Text = "Department"
                # 
                # companyToolStripMenuItem
                # 
                self._companyToolStripMenuItem.Name = "companyToolStripMenuItem"
                self._companyToolStripMenuItem.Size = System.Drawing.Size(188, 22)
                self._companyToolStripMenuItem.Text = "Company"
                # 
                # employeeMasterToolStripMenuItem
                # 
                self._employeeMasterToolStripMenuItem.Name = "employeeMasterToolStripMenuItem"
                self._employeeMasterToolStripMenuItem.Size = System.Drawing.Size(188, 22)
                self._employeeMasterToolStripMenuItem.Text = "Employee Master"
                # 
                # toolStripSeparator1
                # 
                # 
                # ratesToolStripMenuItem
                # 
                self._ratesToolStripMenuItem.Name = "ratesToolStripMenuItem"
                self._ratesToolStripMenuItem.Size = System.Drawing.Size(188, 22)
                self._ratesToolStripMenuItem.Text = "Rates"
                # 
                # deductionCategoryToolStripMenuItem
                # 
                self._deductionCategoryToolStripMenuItem.Name = "deductionCategoryToolStripMenuItem"
                self._deductionCategoryToolStripMenuItem.Size = System.Drawing.Size(188, 22)
                self._deductionCategoryToolStripMenuItem.Text = "Deduction Category"
                # 
                # toolStripSeparator2
                # 
                self._toolStripSeparator2.Size = System.Drawing.Size(185, 6)
                # 
                # ratesTableToolStripMenuItem
                # 
                self._ratesTableToolStripMenuItem.Name = "ratesTableToolStripMenuItem"
                self._ratesTableToolStripMenuItem.Size = System.Drawing.Size(188, 22)
                self._ratesTableToolStripMenuItem.Text = "Rates Table"
                # 
                # deductionSetupToolStripMenuItem
                # 
                self._deductionSetupToolStripMenuItem.Name = "deductionSetupToolStripMenuItem"
                self._deductionSetupToolStripMenuItem.Size = System.Drawing.Size(188, 22)
                self._deductionSetupToolStripMenuItem.Text = "Deduction Setup"
                # 
                # toolStripSeparator3
                # 
                self._toolStripSeparator3.Name = "toolStripSeparator3"
                self._toolStripSeparator3.Size = System.Drawing.Size(185, 6)
                # 
                # dailyTimesheetEntryToolStripMenuItem
                # 
                self._dailyTimesheetEntryToolStripMenuItem.Name = "dailyTimesheetEntryToolStripMenuItem"
                self._dailyTimesheetEntryToolStripMenuItem.Size = System.Drawing.Size(188, 22)
                self._dailyTimesheetEntryToolStripMenuItem.Text = "Daily Timesheet Entry"
                # 
                # toolStripSeparator4
                # 
                self._toolStripSeparator4.Name = "toolStripSeparator4"
                self._toolStripSeparator4.Size = System.Drawing.Size(185, 6)
                # 
                # quitToolStripMenuItem
                # 
                self._quitToolStripMenuItem.Name = "quitToolStripMenuItem"
                self._quitToolStripMenuItem.Size = System.Drawing.Size(188, 22)
                self._quitToolStripMenuItem.Text = "Quit"
                self._quitToolStripMenuItem.Click += self.QuitToolStripMenuItemClick
                # 
                # reportToolStripMenuItem
                # 
                self._reportToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
                        [self._payrollListingToolStripMenuItem,
                        self._payrollSummaryToolStripMenuItem]))
                self._reportToolStripMenuItem.Name = "reportToolStripMenuItem"
                self._reportToolStripMenuItem.Size = System.Drawing.Size(47, 19)
                self._reportToolStripMenuItem.Text = "Report"
                # 
                # payrollListingToolStripMenuItem
                # 
                self._payrollListingToolStripMenuItem.Name = "payrollListingToolStripMenuItem"
                self._payrollListingToolStripMenuItem.Size = System.Drawing.Size(164, 22)
                self._payrollListingToolStripMenuItem.Text = "Payroll Listing"
                # 
                # payrollSummaryToolStripMenuItem
                # 
                self._payrollSummaryToolStripMenuItem.Name = "payrollSummaryToolStripMenuItem"
                self._payrollSummaryToolStripMenuItem.Size = System.Drawing.Size(164, 22)
                self._payrollSummaryToolStripMenuItem.Text = "Payroll Summary"
                # 
                # toolsToolStripMenuItem
                # 
                self._toolsToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
                        [self._databaseSetupToolStripMenuItem,
                        self._userManagementToolStripMenuItem,
                        self._accessConfigToolStripMenuItem]))
                self._toolsToolStripMenuItem.Name = "toolsToolStripMenuItem"
                self._toolsToolStripMenuItem.Size = System.Drawing.Size(47, 19)
                self._toolsToolStripMenuItem.Text = "Tools"
                # 
                # databaseSetupToolStripMenuItem
                # 
                self._databaseSetupToolStripMenuItem.Name = "databaseSetupToolStripMenuItem"
                self._databaseSetupToolStripMenuItem.Size = System.Drawing.Size(171, 22)
                self._databaseSetupToolStripMenuItem.Text = "Database Setup"
                self._databaseSetupToolStripMenuItem.Click += self.LoadDBSetup
                # 
                # userManagementToolStripMenuItem
                # 
                self._userManagementToolStripMenuItem.Name = "userManagementToolStripMenuItem"
                self._userManagementToolStripMenuItem.Size = System.Drawing.Size(171, 22)
                self._userManagementToolStripMenuItem.Text = "User Management"
                self._userManagementToolStripMenuItem.Click += self._Load

                # 
                # accessConfigToolStripMenuItem
                # 
                self._accessConfigToolStripMenuItem.Name = "accessConfigToolStripMenuItem"
                self._accessConfigToolStripMenuItem.Size = System.Drawing.Size(171, 22)
                self._accessConfigToolStripMenuItem.Text = "Access Config"
                # 
                # helpToolStripMenuItem
                # 
                self._helpToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
                        [self._aboutToolStripMenuItem]))
                self._helpToolStripMenuItem.Name = "helpToolStripMenuItem"
                self._helpToolStripMenuItem.Size = System.Drawing.Size(47, 19)
                self._helpToolStripMenuItem.Text = "Help"
                # 
                # aboutToolStripMenuItem
                # 
                self._aboutToolStripMenuItem.Name = "aboutToolStripMenuItem"
                self._aboutToolStripMenuItem.Size = System.Drawing.Size(107, 22)
                self._aboutToolStripMenuItem.Text = "About"
                # 
                # MainForm
                # 
                self.ClientSize = System.Drawing.Size(409, 341)
                #self.Controls.Add(self._panel1)
                #self.Controls.Add(self._label1)
                self.Controls.Add(self._menuStrip1)
                self.Controls.Add(self._statusStrip1)
                self.IsMdiContainer = True
                self.Name = "MainForm"
                self.Text = "Payroll System"
                
                self._statusStrip1.ResumeLayout(False)
                self._statusStrip1.PerformLayout()
                self._panel1.ResumeLayout(False)
                self._panel1.PerformLayout()
                self._menuStrip1.ResumeLayout(False)
                self._menuStrip1.PerformLayout()
                self.ResumeLayout(False)
                self.PerformLayout()
                
                self.WindowState = WinForms.FormWindowState.Maximized #Windows is Maximized by default

                self.AppTitle = "GemSoft Systems" #Application title
                self.LowerColor = System.Drawing.Color.Green
                self.Load += self._Load

        def ToolStripMenuItem1Click(self, sender, e):
                pass

        def ToolStripMenuItem2Click(self, sender, e):
                pass

        def QuitToolStripMenuItemClick(self, sender, e):
                self.Close()
        
        def _Load(self,sender, e):
                #frmLogon_ = frmLogon()
                #frmLogon_.ShowDialog(self)
                frmuser_ = frmuser.frmUser()
                frmuser_.MdiParent = self
                frmuser_.Show()
        
        def LoadDBSetup(self,sender,e):
                frmdbsetup_ = frmdbsetup.frmDBSetup()
                frmdbsetup_.Owner = self
                #frmdbsetup_.MdiParent = self
                frmdbsetup_.ShowDialog()

                


        def run(self):
                WinForms.Application.Run(self)


def main():
    MainForm().run()


if __name__ == '__main__':
    main()


