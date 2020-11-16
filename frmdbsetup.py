import clr
import System.Windows.Forms as WinForms
import System.Drawing
import System.Windows.Forms
import clr

from System.Data.SqlClient import *
from System.IO import *

class frmDBSetup(System.Windows.Forms.Form):
	def __init__(self):
		#self.New() #This call is required by the Windows Form Designer.
		self.InitializeComponent() #Add any initialization after the InitializeComponent() call
		#self._AppString = "SOFTWARE\\RD Corporation\\" + Application.CompanyName + "\\" + Application.ProductName + "\\Settings"
	#	Key = Microsoft.Win32.Registry.CurrentUser.OpenSubKey(self._AppString, True)
	#	if Key is None:
	#		Key = Microsoft.Win32.Registry.CurrentUser.CreateSubKey(self._AppString)
	#	else:
	#		self._txtDBName.Text = Purchasing.mdlStandardModule.GetDecryptedData(Key.GetValue("DBName"))
	#		strTemp = Purchasing.mdlStandardModule.GetDecryptedData(Key.GetValue("Server"))
			#self._stbMessage.Panels(0).Text = "System's Current Server : " + Microsoft.VisualBasic.IIf(strTemp == "", "None", strTemp)
 #Key.SetValue("Server", "(local)") #Key.SetValue("Connected", "0") #Key.SetValue("Author", "pepesmith") #Form overrides dispose to clean up the component list.
	def Dispose(self, disposing):
		if disposing:
			if not (self._components is None):
				self._components.Dispose()
		self.Dispose(disposing)
 #Required by the Windows Form Designer #NOTE: The following procedure is required by the Windows Form Designer #It can be modified using the Windows Form Designer.   #Do not modify it using the code editor.
	def InitializeComponent(self):
	#	resources = System.Resources.ResourceManager(clr.GetClrType(frmDBSetup))
		self._btnLogin = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._Label1 = System.Windows.Forms.Label()
		self._Label2 = System.Windows.Forms.Label()
		self._txtUsername = System.Windows.Forms.TextBox()
		self._txtPassword = System.Windows.Forms.TextBox()
		self._Label3 = System.Windows.Forms.Label()
		self._GroupBox1 = System.Windows.Forms.GroupBox()
		self._GroupBox2 = System.Windows.Forms.GroupBox()
		self._PictureBox1 = System.Windows.Forms.PictureBox()
		self._Label5 = System.Windows.Forms.Label()
		self._txtServer = System.Windows.Forms.TextBox()
		self._lblFormName = System.Windows.Forms.Label()
		self._rbSQL = System.Windows.Forms.RadioButton()
		self._rbTrusted = System.Windows.Forms.RadioButton()
		self._Label4 = System.Windows.Forms.Label()
		self._GroupBox3 = System.Windows.Forms.GroupBox()
		self._btnTest = System.Windows.Forms.Button()
		self._txtDBName = System.Windows.Forms.TextBox()
		self._Label6 = System.Windows.Forms.Label()
		self._stbMessage = System.Windows.Forms.StatusBar()
		self._Panel1 = System.Windows.Forms.StatusBarPanel()
		self._GroupBox3.SuspendLayout()
		self._Panel1.BeginInit()
		self.SuspendLayout() # #btnLogin #
		self._btnLogin.DialogResult = System.Windows.Forms.DialogResult.OK
		self._btnLogin.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnLogin.Location = System.Drawing.Point(64, 288)
		self._btnLogin.Name = "btnLogin"
		self._btnLogin.TabIndex = 5
		self._btnLogin.Text = "&Connect!" # #btnClose #
		self._btnClose.DialogResult = System.Windows.Forms.DialogResult.Cancel
		self._btnClose.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnClose.Location = System.Drawing.Point(152, 288)
		self._btnClose.Name = "btnClose"
		self._btnClose.TabIndex = 6
		self._btnClose.Text = "&Close" # #Label1 #
		self._Label1.BackColor = System.Drawing.Color.Transparent
		self._Label1.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Label1.Location = System.Drawing.Point(8, 86)
		self._Label1.Name = "Label1"
		self._Label1.TabIndex = 2
		self._Label1.Text = "Username:"
		self._Label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight # #Label2 #
		self._Label2.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Label2.Location = System.Drawing.Point(8, 109)
		self._Label2.Name = "Label2"
		self._Label2.TabIndex = 3
		self._Label2.Text = "Password:"
		self._Label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight # #txtUsername #
		self._txtUsername.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
		self._txtUsername.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._txtUsername.Location = System.Drawing.Point(112, 88)
		self._txtUsername.Name = "txtUsername"
		self._txtUsername.Size = System.Drawing.Size(152, 21)
		self._txtUsername.TabIndex = 0
		self._txtUsername.Text = ""
		self._txtUsername.TextAlign = System.Windows.Forms.HorizontalAlignment.Center # #txtPassword #
		self._txtPassword.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._txtPassword.Location = System.Drawing.Point(112, 112)
		self._txtPassword.Name = "txtPassword"
		self._txtPassword.PasswordChar = "*"
		self._txtPassword.Size = System.Drawing.Size(152, 21)
		self._txtPassword.TabIndex = 1
		self._txtPassword.Text = ""
		self._txtPassword.TextAlign = System.Windows.Forms.HorizontalAlignment.Center # #Label3 #
		self._Label3.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Label3.Location = System.Drawing.Point(8, 72)
		self._Label3.Name = "Label3"
		self._Label3.Size = System.Drawing.Size(100, 16)
		self._Label3.TabIndex = 6
		self._Label3.Text = "User Information" # #GroupBox1 #
		self._GroupBox1.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._GroupBox1.Location = System.Drawing.Point(96, 72)
		self._GroupBox1.Name = "GroupBox1"
		self._GroupBox1.Size = System.Drawing.Size(192, 8)
		self._GroupBox1.TabIndex = 7
		self._GroupBox1.TabStop = False # #GroupBox2 #
		self._GroupBox2.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._GroupBox2.Location = System.Drawing.Point(0, 272)
		self._GroupBox2.Name = "GroupBox2"
		self._GroupBox2.Size = System.Drawing.Size(288, 8)
		self._GroupBox2.TabIndex = 9
		self._GroupBox2.TabStop = False # #PictureBox1 #
		#self._PictureBox1.Image = resources.GetObject("PictureBox1.Image")
		self._PictureBox1.Location = System.Drawing.Point(216, 16)
		self._PictureBox1.Name = "PictureBox1"
		self._PictureBox1.Size = System.Drawing.Size(48, 48)
		self._PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PictureBox1.TabIndex = 13
		self._PictureBox1.TabStop = False # #Label5 #
		self._Label5.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Label5.Location = System.Drawing.Point(8, 168)
		self._Label5.Name = "Label5"
		self._Label5.TabIndex = 14
		self._Label5.Text = "Server:"
		self._Label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight # #txtServer #
		self._txtServer.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
		self._txtServer.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._txtServer.Location = System.Drawing.Point(112, 168)
		self._txtServer.Name = "txtServer"
		self._txtServer.Size = System.Drawing.Size(152, 21)
		self._txtServer.TabIndex = 3
		self._txtServer.Text = "PEPESMITH"
		self._txtServer.TextAlign = System.Windows.Forms.HorizontalAlignment.Center # #lblFormName #
		self._lblFormName.Font = System.Drawing.Font("Tahoma", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblFormName.Location = System.Drawing.Point(8, 28)
		self._lblFormName.Name = "lblFormName"
		self._lblFormName.Size = System.Drawing.Size(208, 16)
		self._lblFormName.TabIndex = 17
		self._lblFormName.Text = "Database Connection Setup"
		self._lblFormName.TextAlign = System.Drawing.ContentAlignment.TopCenter # #rbSQL #
		self._rbSQL.Location = System.Drawing.Point(16, 16)
		self._rbSQL.Name = "rbSQL"
		self._rbSQL.TabIndex = 0
		self._rbSQL.Text = "SQL Server" # #rbTrusted #
		self._rbTrusted.Location = System.Drawing.Point(16, 40)
		self._rbTrusted.Name = "rbTrusted"
		self._rbTrusted.Size = System.Drawing.Size(128, 24)
		self._rbTrusted.TabIndex = 1
		self._rbTrusted.Text = "Trusted Connection" # #Label4 #
		self._Label4.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Label4.Location = System.Drawing.Point(8, 192)
		self._Label4.Name = "Label4"
		self._Label4.TabIndex = 20
		self._Label4.Text = "Login Type:"
		self._Label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight # #GroupBox3 #
		self._GroupBox3.Controls.Add(self._rbSQL)
		self._GroupBox3.Controls.Add(self._rbTrusted)
		self._GroupBox3.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._GroupBox3.Location = System.Drawing.Point(112, 192)
		self._GroupBox3.Name = "GroupBox3"
		self._GroupBox3.Size = System.Drawing.Size(152, 72)
		self._GroupBox3.TabIndex = 21
		self._GroupBox3.TabStop = False # #btnTest #
		self._btnTest.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnTest.Location = System.Drawing.Point(16, 240)
		self._btnTest.Name = "btnTest"
		self._btnTest.TabIndex = 4
		self._btnTest.Text = "&Test" # #txtDBName #
		self._txtDBName.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._txtDBName.Location = System.Drawing.Point(112, 136)
		self._txtDBName.Name = "txtDBName"
		self._txtDBName.Size = System.Drawing.Size(152, 21)
		self._txtDBName.TabIndex = 2
		self._txtDBName.Text = ""
		self._txtDBName.TextAlign = System.Windows.Forms.HorizontalAlignment.Center # #Label6 #
		self._Label6.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Label6.Location = System.Drawing.Point(8, 133)
		self._Label6.Name = "Label6"
		self._Label6.Size = System.Drawing.Size(96, 23)
		self._Label6.TabIndex = 23
		self._Label6.Text = "Database"
		self._Label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight # #stbMessage #
		self._stbMessage.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._stbMessage.Location = System.Drawing.Point(0, 324)
		self._stbMessage.Name = "stbMessage"
		#self._stbMessage.Panels.AddRange(Array[System.Windows.Forms.StatusBarPanel]((self._Panel1)))
		self._stbMessage.ShowPanels = True
		self._stbMessage.Size = System.Drawing.Size(290, 22)
		self._stbMessage.TabIndex = 44 # #Panel1 #
		self._Panel1.AutoSize = System.Windows.Forms.StatusBarPanelAutoSize.Spring
		self._Panel1.Width = 274 # #frmDBSetup #
		self.AutoScaleBaseSize = System.Drawing.Size(5, 13)
		self.ClientSize = System.Drawing.Size(290, 346)
		self.ControlBox = False
		self.Controls.Add(self._stbMessage)
		self.Controls.Add(self._txtDBName)
		self.Controls.Add(self._txtServer)
		self.Controls.Add(self._txtPassword)
		self.Controls.Add(self._txtUsername)
		self.Controls.Add(self._Label6)
		self.Controls.Add(self._btnTest)
		self.Controls.Add(self._GroupBox3)
		self.Controls.Add(self._Label4)
		self.Controls.Add(self._lblFormName)
		self.Controls.Add(self._Label5)
		self.Controls.Add(self._PictureBox1)
		self.Controls.Add(self._GroupBox2)
		self.Controls.Add(self._GroupBox1)
		self.Controls.Add(self._Label3)
		self.Controls.Add(self._Label2)
		self.Controls.Add(self._Label1)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnLogin)
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.Name = "frmDBSetup"
		self.ShowInTaskbar = False
		self.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self._GroupBox3.ResumeLayout(False)
		self._Panel1.EndInit()
		self.ResumeLayout(False)
		self._btnClose.Click += self.btnClose_Click

	def frmLogon_Load(self, sender, e):
		self.ClearForm()
		self._txtUsername.Focus()

	def ClearForm(self):
		self._txtUsername.Enabled = False
		self._txtPassword.Enabled = False
		self._txtServer.Text = "pepesmith"
		self._rbTrusted.Select()

	def get_Username(self):
		return self._mUserName

	def set_Username(self, value):
		self._mUserName = Value

	Username = property(fget=get_Username, fset=set_Username)

	def get_Password(self):
		return self._mPassword

	def set_Password(self, value):
		self._mPassword = Value

	Password = property(fget=get_Password, fset=set_Password)

	def get_Server(self):
		return self._mServer

	def set_Server(self, value):
		self._mServer = Value

	Server = property(fget=get_Server, fset=set_Server)

	def get_LoginType(self):
		return self._mLoginType

	def set_LoginType(self, value):
		self._mLoginType = Value

	LoginType = property(fget=get_LoginType, fset=set_LoginType)

	def btnTest_Click(self, sender, e):
		if self.TestConnection() == True:
			System.Windows.Forms.MessageBox.Show("Connection Succeded", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information)
		else:
			System.Windows.Forms.MessageBox.Show("Connection Failed", "Failure", MessageBoxButtons.OK, MessageBoxIcon.Information)

	def TestConnection(self):
		connection = None
		try:
			connection = SqlConnection(GetConnectionString)
			connection.Open()
			return True
		except Exception as ex:
			return False
		finally:
			connection.Close()

	def GetConnectionString(self):
		self.Server = self._txtServer.Text
		self.Username = self._txtUsername.Text
		self.Password = self._txtPassword.Text
		sDBName = self._txtDBName.Text

		

		if self._rbSQL.Checked:
			if self._txtServer.Text.Trim.Length == 0 | self._txtUsername.Text.Trim.Length == 0 | self._txtPassword.Text.Trim.Length == 0 | self._txtDBName.Text.Trim.Length == 0:
				sConnString = ""
			else: #Fail it when either Server,Username,Password or Database is blank
				sConnString = "Data Source=" + self.Server + ";Initial Catalog=" + sDBName + ";user id=" + self.Username + ";password=" + self.Password
		else:
			if self._txtDBName.Text.Trim.Length == 0:
				sConnString = ""
			else: #Fail it when Database is blank
				sConnString = "Data Source=" + self.Server + ";Initial Catalog=" + sDBName + ";Integrated Security=SSPI"
		return sConnString

	def btnLogin_Click(self, sender, e):
		if self.TestConnection() == True: #SaveToText()
			self.WriteToRegistry()
		else:
			System.Windows.Forms.MessageBox.Show("Connection Failed.", "Failure", MessageBoxButtons.OK, MessageBoxIcon.Information)
			self._DialogResult = System.Windows.Forms.DialogResult.Retry

	def SaveToText(self): # Create an instance of StreamWriter to write text to a file at the roaming applications folder
		AppPath = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + "\\" + Application.CompanyName
		try:
			if not Directory.Exists(AppPath):
				Directory.CreateDirectory(AppPath)
			sw = StreamWriter(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + "\\" + Application.CompanyName + "\\DBConStr.ini")
			sw.WriteLine(GetConnectionString)
			sw.Close()
		except Exception as ex:
			self.MsgBox(ex.Message)
		finally:
			pass
	def btnClose_Click(self, sender, e):
		self.Close()

	def rbSQL_CheckedChanged(self, sender, e):
		if self._rbSQL.Checked:
			self._txtUsername.Enabled = True
			self._txtPassword.Enabled = True
			self._txtUsername.Focus()

	def rbTrusted_CheckedChanged(self, sender, e):
		if self._rbTrusted.Checked:
			self.ClearForm()

	def WriteToRegistry(self):
		Key = Microsoft.Win32.Registry.CurrentUser.CreateSubKey(self._AppString)
		Key.SetValue("Name", Purchasing.mdlStandardModule.GetEncryptedData(self._txtUsername.Text))
		Key.SetValue("Pass", Purchasing.mdlStandardModule.GetEncryptedData(self._txtPassword.Text))
		Key.SetValue("DBName", Purchasing.mdlStandardModule.GetEncryptedData(self._txtDBName.Text))
		Key.SetValue("Server", Purchasing.mdlStandardModule.GetEncryptedData(self._txtServer.Text))
		Key.SetValue("Version", "1.0")
		if self._rbSQL.Checked:
			Key.SetValue("Trusted", False)
		else:
			Key.SetValue("Trusted", True)

	def txtUsername_KeyDown(self, sender, e):
		if e.KeyCode == Keys.Enter:
			SendKeys.Send("{TAB}")

	def txtPassword_KeyDown(self, sender, e):
		if e.KeyCode == Keys.Enter:
			SendKeys.Send("{TAB}")

	def txtDBName_KeyDown(self, sender, e):
		if e.KeyCode == Keys.Enter:
			SendKeys.Send("{TAB}")

	def txtServer_KeyDown(self, sender, e):
		if e.KeyCode == Keys.Enter:
			SendKeys.Send("{TAB}")

	def agoy(self):
		WinForms.Application.Run(self)
    
        
    
    
    
    


def main():
    frmDBSetup().agoy()


if __name__ == '__main__':
    main()
