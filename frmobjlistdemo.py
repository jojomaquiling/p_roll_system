import clr
import System.Windows.Forms as WinForms
import System.Drawing
import System.Windows.Forms
import clr
clr.AddReference("ObjectListView")

from System.Data import DataTable, DataRow
import BrightIdeasSoftware
from BrightIdeasSoftware import RowBorderDecoration,HotItemStyle

from db import Database
import System.Drawing
import System.Windows.Forms

from System.Drawing import Pen,Color,Size
from System.Windows.Forms import *
from  System.Collections.Generic import List

class person(System.Object):
	def __init__(self,_firstname,_lastname):
		self.firstname = _firstname
		self.lastname = _lastname
	
	def Firstname(self):
		return self.firstname



class Form1(WinForms.Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._objectListView1 = BrightIdeasSoftware.DataListView()
		self.SuspendLayout()
		# 
		# objectListView1
		# 
		self._objectListView1.Location = System.Drawing.Point(12, 23)
		self._objectListView1.Name = "objectListView1"
		self._columnHeader1 = BrightIdeasSoftware.OLVColumn()
		self._columnHeader1.Text = "Item"
		self._columnHeader1.AspectName = "toString"
		self._objectListView1.Columns.AddRange(System.Array[ BrightIdeasSoftware.OLVColumn](
			[self._columnHeader1]))		
		self._objectListView1.Size = System.Drawing.Size(385, 143)
		self._objectListView1.TabIndex = 0
		self._objectListView1.UseCompatibleStateImageBehavior = False
		self._objectListView1.View = System.Windows.Forms.View.Details
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(409, 265)
		self.Controls.Add(self._objectListView1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.ResumeLayout(False)
		self.Load += self.LoadRecord

	

	def btnCancel_Click(self, sender, e):
		if self.Owner == None :
			self.Close()
		else:
			self.Owner.Close()

#
#
#RowBorderDecoration rbd = new RowBorderDecoration(); rbd.BorderPen = new Pen(Color.FromArgb(128, Color.LightSeaGreen), 2); rbd.BoundsPadding = new Size(1, 1); rbd.CornerRounding = 4.0f; // Put the decoration onto the hot item this.olv1.HotItemStyle = new HotItemStyle(); this.olv1.HotItemStyle.Decoration = rbd;

#Read more: http://objectlistview.sourceforge.net/cs/recipes.html#how-can-i-emphasise-the-row-under-the-mouse#ixzz2UEUx2QGv

#
#


	def LoadRecord(self,sender,e):


		rbd = RowBorderDecoration()
		rbd.BorderPen = Pen(Color.FromArgb(128, Color.LightSeaGreen), 2)
		rbd.BoundsPadding = Size(1, 1)
		rbd.CornerRounding = 4.0

		self._objectListView1.FullRowSelect = True
		self._objectListView1.minimumWidth    = 100 
		datag = self.create_interval_record_table()
		for data in Database.user.all():
			datag.Rows.Add(data.user_id,data.username,data.firstname,data.lastname)
		#self._dataGrid1.DataSource = datag.DefaultView		
		self._objectListView1.DataSource = datag.DefaultView
		self._objectListView1.UseCustomSelectionColors = True
		self._objectListView1.AlternateRowBackColor = System.Drawing.Color.Green
		self._objectListView1.HighlightBackgroundColor = System.Drawing.Color.Orange
		
		#for col in self._objectListView1.Columns:
		#	col.Width = 100
		self._objectListView1.Columns[0].Width = 70
		self._objectListView1.Columns[1].Width = 100
		self._objectListView1.Columns[2].Width = 100
		self._objectListView1.Columns[3].Width = 100
		self._objectListView1.SelectionChanged += self.MouseUp
		#self._objectListView1.HotItemStyle =  HotItemStyle()
		#self._objectListView1.Decoration = rbd;
		self._objectListView1.Refresh()
		#listing = List[person]()
		#listing.Add(person('jojo','maquiling'))
		#listing.Add(person('gary','granada'))
		#self._objectListView1.SetObjects(listing)
	
	def MouseUp(self,sender,event):
		try :
			#Items[0].RowObject[0]
			selected_row = sender.SelectedIndex
			System.Windows.Forms.MessageBox.Show(str(sender.Items[selected_row].RowObject[0]))
		except:
			pass

	
	def create_interval_record_table(self):
		_table = DataTable()
		_table.Clear()
		_table.Columns.Add("id")
		_table.Columns.Add("username")
		_table.Columns.Add("firstname")
		_table.Columns.Add("lastname")
		return _table

   	def agoy(self):
		WinForms.Application.Run(self)
    
        
    
    
    
    


def main():
    Form1().agoy()


if __name__ == '__main__':
    main()
