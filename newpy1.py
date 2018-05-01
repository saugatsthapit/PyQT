#! python2
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * # Import the PyQt5 module we'll need
import sys # We need sys so that we can pass argv to QApplication
import mysql.connector
from mysql.connector import errorcode
import untitled # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
__metaclass__ = type

import viewertools

#Database connection
try:
    connection = mysql.connector.connect(user='admin',
                                         password= 'admin',
                                         host='127.0.0.1',
                                         port='3306',
                                         database = 'multivender_test')
    cursor = connection.cursor()

      # QtSql.QSqlDatabase db = QSqlDatabase.addDatabase("QMYSQL");
      #   db.setHostName("127.0.0.1);
      #   db.setDatabaseName("multivender_test");
      #   db.setUserName("admin");
      #   db.setPassword("admin");
      #   bool ok = db.open();

    class ExampleApp(QDialog):

        def __init__(self):
            # super allows us to
            # access variables, methods etc in the design.py file
            super(ExampleApp, self).__init__()
            self.ui = untitled.Ui_Dialog()
            self.ui.setupUi(self) # This is defined in design.py file automatically
                                # It sets up layout and widgets that are defined
            self.setWindowState(Qt.WindowMaximized)
            self.ui.btn1.clicked.connect(self.insertList)
            self.ui.btn2.clicked.connect(self.loaddata)
            self.show()

        def insertList(self):
            # QtSql.QSqlQuery query;
            # query.execute('select * from volume_dicominfo');
            import pdb
            #pdb.set_trace()
            viewertools.show(r"D:\projects\share\data\CT\1.3.12.2.1107.5.1.4.12345.4.0.1740126031831309")
            sql = ('select * from volume_dicominfo');
            cursor.execute(sql)
            rows = cursor.fetchone()
            print(rows)


        def loaddata(self):
           query = ('select * from volume_dicominfo');
           result = cursor.execute(query)
           self.ui.TableWidget.setrowcount(0)

           for row_number, row_data in enumerate(result):
               self.TableWidget.InsertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.TableWidget.setitem(row_number, column_number, QtWidgets.QTableidgetItem(str(data)))

    def main():
        app = QApplication(sys.argv)  # A new instance of QApplication
        form = ExampleApp()                 # We set the form to be our ExampleApp (design)
        form.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        form.move(0,0)
        form.show()                         # Show the form
        sys.exit(app.exec_())                      # and execute the app


    if __name__ == '__main__':              # if we're running file directly and not importing it
        main()                              # run the main function

    # insertList(cursor)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Wrong Username/password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    else:
        print(err)
else:
    connection.close()