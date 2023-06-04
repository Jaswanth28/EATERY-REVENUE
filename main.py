from PyQt5 import uic,QtWidgets,QtGui
import pandas as pd
from PyQt5.QtWidgets import * 
import sys
import csv

def v(x1,x2,x3):

    if x3 == "In line":
        x3 = "IL"
    elif x3 == "Food Court":
        x3 = "FC"
    elif x3 == "Mobile":
        x3 = "MB"
    else:
        x3 = "DT"

    id = ""
    if x1 and x3 and x2:
        with open('csv/test.csv', 'r') as f:
            reader = csv.reader(f)
            for data in reader:
                if data[2] == x1 and data[4] == x3 and data[3] == x2:
                    id = data[0]
                    break
        if id:
            with open('csv/revenue.csv', 'r') as f:
                reader = csv.reader(f)
                for data in reader:
                    if data[0] == id:
                        value = data[1]
                        o=(f'Approximate Annual Revenue is :{value}')
                        m.res.setText(o)
                        break
        else:
            m.res.setText("No results found")

def ll():
    m.res.clear()
    x1=m.loc.currentText()
    x2=m.ct.currentText()
    x3=m.rt.currentText()
    if(m.loc.currentIndex()==0 & m.ct.currentIndex()==0 & m.rt.currentIndex()==0):
        m.res.setText("enter valid inputs")
    else:
        v(x1,x2,x3)

j=QtWidgets.QApplication([])
r=0
m=uic.loadUi('ut1.ui')
m.show()
m.setStyleSheet("#centralwidget{background-image:url(bg1.jpg);}")
m.setWindowTitle('Home')
m.pred.clicked.connect(ll)
sys.exit(j.exec_())