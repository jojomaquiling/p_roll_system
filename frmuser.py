import clr
import sys
import System.Windows.Forms as WinForms
import System.Drawing
from System.Drawing import Point
import System.Windows.Forms
import clr
clr.AddReference("ObjectListView")

from System.Data import DataTable, DataRow
import BrightIdeasSoftware
from System.Windows.Forms import MessageBox,DialogResult,MessageBoxButtons

from db import Database
from db import userinfo

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class frmUser(WinForms.Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self.current_user_id = None
		self._dataGrid1 = BrightIdeasSoftware.DataListView()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label5 = System.Windows.Forms.Label()
		self._cboUserLevel = System.Windows.Forms.ComboBox()
		self._txtLastname = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._txtFirstname = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._txtPassword = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._txtUsername = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._btnAddUpdate = System.Windows.Forms.Button()
		self._btnDelete = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# dataGrid1
		# 

		
		self._dataGrid1.DataMember = ""
		self._dataGrid1.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right |System.Windows.Forms.AnchorStyles.Bottom
		self._dataGrid1.HeaderForeColor = System.Drawing.SystemColors.ControlText
		self._dataGrid1.Location = System.Drawing.Point(12, 20)
		self._dataGrid1.Name = "dataGrid1"
		self._dataGrid1.Size = System.Drawing.Size(488, 155)
		self._dataGrid1.TabIndex = 16
		# 
		# groupBox1
		# 
		self._groupBox1.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._cboUserLevel)
		self._groupBox1.Controls.Add(self._txtLastname)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._txtFirstname)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._txtPassword)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._txtUsername)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(12, 173)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(488, 159)
		self._groupBox1.TabIndex = 20
		self._groupBox1.TabStop = False
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(12, 126)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(65, 20)
		self._label5.TabIndex = 39
		self._label5.Text = "User Level"
		# 
		# cboUserLevel
		# 
		self._cboUserLevel.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._cboUserLevel.FormattingEnabled = True
		self._cboUserLevel.Items.AddRange(System.Array[System.Object](
			["1 - SuperUser",
			"2 - Administrator",
			"3 - Encoder",
			"4 - Viewer"]))
		self._cboUserLevel.Location = System.Drawing.Point(83, 123)
		self._cboUserLevel.Name = "cboUserLevel"
		self._cboUserLevel.Size = System.Drawing.Size(226, 21)
		self._cboUserLevel.TabIndex = 38
		# 
		# txtLastname
		# 
		self._txtLastname.Location = System.Drawing.Point(83, 97)
		self._txtLastname.Name = "txtLastname"
		self._txtLastname.Size = System.Drawing.Size(226, 20)
		self._txtLastname.TabIndex = 37
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 100)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(65, 20)
		self._label4.TabIndex = 36
		self._label4.Text = "Lastname"
		# 
		# txtFirstname
		# 
		self._txtFirstname.Location = System.Drawing.Point(83, 71)
		self._txtFirstname.Name = "txtFirstname"
		self._txtFirstname.Size = System.Drawing.Size(226, 20)
		self._txtFirstname.TabIndex = 35
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 74)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(65, 20)
		self._label3.TabIndex = 34
		self._label3.Text = "Firstname"
		# 
		# txtPassword
		# 
		self._txtPassword.Location = System.Drawing.Point(83, 45)
		self._txtPassword.Name = "txtPassword"
		self._txtPassword.Size = System.Drawing.Size(134, 20)
		self._txtPassword.TabIndex = 33
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 48)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(65, 20)
		self._label2.TabIndex = 32
		self._label2.Text = "Password"
		# 
		# txtUsername
		# 
		self._txtUsername.Location = System.Drawing.Point(83, 19)
		self._txtUsername.Name = "txtUsername"
		self._txtUsername.Size = System.Drawing.Size(96, 20)
		self._txtUsername.TabIndex = 31
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(65, 20)
		self._label1.TabIndex = 30
		self._label1.Text = "Username"
		# 
		# btnAddUpdate
		# 
		self._btnAddUpdate.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left
		self._btnAddUpdate.Location = System.Drawing.Point(144, 338)
		self._btnAddUpdate.Name = "btnAddUpdate"
		self._btnAddUpdate.Size = System.Drawing.Size(75, 23)
		self._btnAddUpdate.TabIndex = 21
		self._btnAddUpdate.Text = "Add"
		self._btnAddUpdate.UseVisualStyleBackColor = True
		self._btnAddUpdate.Click += self.AddUpdate
		# 
		# btnClose
		# 
		self._btnClose.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left 
		self._btnClose.Location = System.Drawing.Point(305, 338)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(75, 23)
		self._btnClose.TabIndex = 22
		self._btnClose.Text = "Close"
		self._btnClose.UseVisualStyleBackColor = True


		self._btnDelete.Anchor = System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left 
		self._btnDelete.Location = System.Drawing.Point(224, 338)
		self._btnDelete.Name = "btnClose"
		self._btnDelete.Size = System.Drawing.Size(75, 23)
		self._btnDelete.TabIndex = 22
		self._btnDelete.Text = "Delete"
		self._btnDelete.UseVisualStyleBackColor = True
		self._btnDelete.Click += self.DeleteUser
		self._btnDelete.Enabled = False

		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(512, 374)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnAddUpdate)
		self.Controls.Add(self._btnDelete)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._dataGrid1)
		self.Name = "Form1"
		self.Text = "User Management"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
                self.ResumeLayout(False)
        	self._btnClose.Click += self.btnCancel_Click
        	self._txtPassword.Enabled = False
        	self.Load += self.LoadData
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen

	def create_interval_record_table(self):
		_table = DataTable()
		_table.Clear()
		_table.Columns.Add("ID")
		_table.Columns.Add("Username")
		_table.Columns.Add("Lastname")
		_table.Columns.Add("Firstname")
		_table.Columns.Add("Userlevel")
		return _table
	

	def btnCancel_Click(self, sender, e):
		if self.Owner == None :
			self.Close()
		else:
			self.Owner.Close()
	
	def LoadData(self,sender,e):
		self.LoadUserData()
	
	def LoadUserData(self):
		datag = self.create_interval_record_table()
		for data in Database.user.all():
			datag.Rows.Add(data.user_id,data.username,data.lastname,data.firstname,data.userlevel)
		self._dataGrid1.DataSource = datag.DefaultView
		self._dataGrid1.Refresh()
		self._dataGrid1.UseCustomSelectionColors = True
		self._dataGrid1.AlternateRowBackColor = System.Drawing.Color.Green
		self._dataGrid1.HighlightBackgroundColor = System.Drawing.Color.Orange
		self._dataGrid1.FullRowSelect = True	
		self._dataGrid1.Columns[0].Width = 30
		self._dataGrid1.Columns[1].Width = 100
		self._dataGrid1.Columns[2].Width = 100
		self._dataGrid1.Columns[3].Width = 100
		self._dataGrid1.Columns[4].Width = 70
		self._dataGrid1.SelectionChanged += self.SelectionChanged
	
	def ResetEntry(self):
			self._txtUsername.Text = ""
			self._txtLastname.Text =  ""
			self._txtFirstname.Text = ""
			self._btnAddUpdate.Text = "Add"
			self._txtUsername.Enabled = True
			self._btnDelete.Enabled = False
                        self._cboUserLevel.SelectedIndex = self._cboUserLevel.FindString("4")		
			self._txtUsername.Focus()

	def SelectionChanged(self,sender,e):
		try:
			selected_row = sender.SelectedIndex
			user_id = sender.Items[selected_row].RowObject[0]
			userinfo = self.getUserInfo(user_id)
			if userinfo != None:
				self.current_user_id = userinfo.user_id
				self._txtUsername.Text = userinfo.username
				self._txtLastname.Text =  userinfo.lastname
				self._txtFirstname.Text =  userinfo.firstname
				self._txtPassword.Text = userinfo.password
				self._txtUsername.Enabled = False
				self._cboUserLevel.SelectedIndex = self._cboUserLevel.FindString(str(userinfo.userlevel))
				self._txtPassword.Enabled = False
				self._btnDelete.Enabled = True 
				self._btnAddUpdate.Text = "Update"
		except :
			self.ResetEntry()
	
	def DeleteUser(self,sender,e):
		#db.loans.delete(db.loans.book_id==2)
		#loan = db.loans.filter_by(book_id=2, user_name='Bhargan Basepair').one()
                #dialogResult = MessageBox.Show("Sure", "Some Title", MessageBoxButtons.YesNo);
                #if(dialogResult == DialogResult.Yes)
                #{
                #    //do something
                #}
                dlgResult = MessageBox.Show("Are you sure you want to delete this user?","Delete User",MessageBoxButtons.YesNo)
                if (dlgResult == DialogResult.Yes):
                        user = self.getUserInfo(self.current_user_id)
		#user = Database.user.filter(Database.user.user_id==3).one()
                        Database.delete(user)
                        Database.commit()
                        self.LoadUserData()
                        System.Windows.Forms.MessageBox.Show("Finished deleting..")
		

	def UpdateUser(self,user_id):
		#db.loans.filter_by(db.loans.book_id==2).update({'book_id':1})
		userlevel = str(self._cboUserLevel.Text).split(" ")[0]
		Database.user.filter(Database.user.user_id==user_id).update({'firstname':self._txtFirstname.Text,'lastname':self._txtLastname.Text,'userlevel':userlevel})
		Database.commit()
		#Database.user.filter_by(Database.user.user_id==user_id).update({'lastname':self._txtLastname,'firstname':self._txtFirstname,'userlevel': userlevel})
		self.LoadUserData()


	def SaveUser(self):
		#db.loans.insert(book_id=book_id, user_name=user.name)
		userlevel_ = str(self._cboUserLevel.Text).split(" ")[0]
		Database.user.insert(username=self._txtUsername.Text,firstname=self._txtFirstname.Text,lastname=self._txtLastname.Text,userlevel=userlevel_)
		Database.commit()
		self.LoadUserData()

	def AddUpdate(self,sender,e):
		if str(self._txtUsername.Text).strip() != "":
			if sender.Text == "Add":
				self.SaveUser()
				System.Windows.Forms.MessageBox.Show("Finished Adding")
			else:
				self.UpdateUser(self.current_user_id)
				System.Windows.Forms.MessageBox.Show("Finished updating...")
		else:
			System.Windows.Forms.MessageBox.Show("Please enter the username")

	
	
	def getUserInfo(self,user_id):
		try:
			user = Database.user.filter(Database.user.user_id==user_id).one()
		except:
			user = None
		return user
		


   	def agoy(self):
		WinForms.Application.Run(self)
    
        
    
    
    


def main():
    frmUser().agoy()


if __name__ == '__main__':
    main()
