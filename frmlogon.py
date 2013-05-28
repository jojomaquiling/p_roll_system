import clr
import System.Windows.Forms as WinForms
import System.Drawing
import System.Windows.Forms

from System.Security.Cryptography import *
from System.Data.SqlClient import *

class frmLogon(WinForms.Form):
	def __init__(self):
		self.InitializeComponent()
 #Add any initialization after the InitializeComponent() call #Form overrides dispose to clean up the component list.
	def Dispose(self, disposing):
		if disposing:
			if not (self._components is None):
				self._components.Dispose()
		self.Dispose(disposing)
 #Required by the Windows Form Designer #NOTE: The following procedure is required by the Windows Form Designer #It can be modified using the Windows Form Designer.   #Do not modify it using the code editor.
	def InitializeComponent(self):
		self._btnLogon = System.Windows.Forms.Button()
		self._btnCancel = System.Windows.Forms.Button()
		self._gpbLogon = System.Windows.Forms.GroupBox()
		self._txtPassword = System.Windows.Forms.TextBox()
		self._Label2 = System.Windows.Forms.Label()
		self._txtUserName = System.Windows.Forms.TextBox()
		self._Label1 = System.Windows.Forms.Label()
		self._stbMessage = System.Windows.Forms.StatusBar()
		self._Panel1 = System.Windows.Forms.StatusBarPanel()
		self._Panel2 = System.Windows.Forms.StatusBarPanel()
		self._gpbLogon.SuspendLayout()
		self._Panel1.BeginInit()
		self._Panel2.BeginInit()
		self.SuspendLayout() # #btnLogon #
		self._btnLogon.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._btnLogon.Location = System.Drawing.Point(64, 128)
		self._btnLogon.Name = "btnLogon"
		self._btnLogon.Size = System.Drawing.Size(80, 24)
		self._btnLogon.TabIndex = 1
		self._btnLogon.Text = "Logon" # #btnCancel #
		self._btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel
		self._btnCancel.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._btnCancel.Location = System.Drawing.Point(160, 128)
		self._btnCancel.Name = "btnCancel"
		self._btnCancel.Size = System.Drawing.Size(80, 24)
		self._btnCancel.TabIndex = 2
		self._btnCancel.Text = "Cancel" # #gpbLogon #
		self._btnCancel.Click += self.btnCancel_Click
		self._gpbLogon.Controls.Add(self._txtPassword)
		self._gpbLogon.Controls.Add(self._Label2)
		self._gpbLogon.Controls.Add(self._txtUserName)
		self._gpbLogon.Controls.Add(self._Label1)
		self._gpbLogon.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._gpbLogon.Location = System.Drawing.Point(16, 8)
		self._gpbLogon.Name = "gpbLogon"
		self._gpbLogon.Size = System.Drawing.Size(264, 104)
		self._gpbLogon.TabIndex = 0
		self._gpbLogon.TabStop = False # #txtPassword #
		self._txtPassword.Location = System.Drawing.Point(72, 58)
		self._txtPassword.Name = "txtPassword"
		self._txtPassword.PasswordChar = '*'
		self._txtPassword.Size = System.Drawing.Size(176, 21)
		self._txtPassword.TabIndex = 2
		self._txtPassword.Text = "" # #Label2 #
		self._Label2.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._Label2.Location = System.Drawing.Point(8, 58)
		self._Label2.Name = "Label2"
		self._Label2.Size = System.Drawing.Size(56, 16)
		self._Label2.TabIndex = 6
		self._Label2.Text = "&Password" # #txtUserName #
		self._txtUserName.Location = System.Drawing.Point(72, 26)
		self._txtUserName.Name = "txtUserName"
		self._txtUserName.Size = System.Drawing.Size(176, 21)
		self._txtUserName.TabIndex = 0
		self._txtUserName.Text = "" # #Label1 #
		self._Label1.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._Label1.Location = System.Drawing.Point(8, 26)
		self._Label1.Name = "Label1"
		self._Label1.Size = System.Drawing.Size(56, 16)
		self._Label1.TabIndex = 3
		self._Label1.Text = "&Username" # #stbMessage #
		self._stbMessage.Location = System.Drawing.Point(0, 161)
		self._stbMessage.Name = "stbMessage"
		#self._stbMessage.Panels.AddRange([System.Windows.Forms.StatusBarPanel]((self._Panel1, self._Panel2)))
		self._stbMessage.ShowPanels = True
		self._stbMessage.Size = System.Drawing.Size(298, 22)
		self._stbMessage.TabIndex = 35 # #Panel1 #
		self._Panel1.Width = 200 # #Panel2 #
		self._Panel2.Width = 141 # #frmLogon #
		self.AcceptButton = self._btnLogon
		self.AutoScaleBaseSize = System.Drawing.Size(5, 14)
		self.CancelButton = self._btnCancel
		self.ClientSize = System.Drawing.Size(298, 183)
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.ControlBox = False
		self.Controls.Add(self._stbMessage)
		self.Controls.Add(self._gpbLogon)
		self.Controls.Add(self._btnCancel)
		self.Controls.Add(self._btnLogon)
		self.Font = System.Drawing.Font("Tahoma", 8, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None
		self._Name = "frmLogon"
		self.ShowInTaskbar = False
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Please Log on"
		self._gpbLogon.ResumeLayout(False)
		self._Panel1.EndInit()
		self._Panel2.EndInit()
		self.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide
		self.BackColor = System.Drawing.Color.SkyBlue
		self.Size =  System.Drawing.Size(304,211)
		self.ResumeLayout(False)

	def btnCancel_Click(self, sender, e):
		if self.Owner == None :
			self.Close()
		else:
			self.Owner.Close()

	def frmLogon_Load(self, sender, e):
		self._Owner.stbMessage.Panels(0).Text = "Please log on.."
		self._txtUserName.Focus()

	def isNoEmpty(self):
		misNoempty = True
		enumerator = self._gpbLogon.Controls.GetEnumerator()
		while enumerator.MoveNext():
			MyObject = enumerator.Current
			if not ((MyObject.GetType.ToString == "System.Windows.Forms.Label") | (MyObject.GetType.ToString == "System.Windows.Forms.ComboBox") | (MyObject.GetType.ToString == "System.Windows.Forms.LinkLabel") | (MyObject.GetType.ToString == "System.Windows.Forms.Button")):
				misNoempty = misNoempty & ((MyObject.Text.Trim) != "")
				if ((MyObject.Text.Trim) == ""):
					MyObject.Focus()
		return misNoempty

	def btnLogon_Click(self, sender, e):
		pass


	def txtUserName_GotFocus(self, sender, e):
		self._txtUserName.SelectAll()

	def txtPassword_GotFocus(self, sender, e):
		self._txtPassword.SelectAll()

   	def agoy(self):
		WinForms.Application.Run(self)
    
        
    
    
    
    


def main():
    frmLogon().agoy()


if __name__ == '__main__':
    main()
