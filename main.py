# This is a sample Python script.
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog


# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
#fDialog = QFileDialog(parent=window,directory=os.getcwd())
#fDialog.fileMode(QFileDialog.D)
folderpath = QFileDialog.getExistingDirectory(parent=window, caption='Select Data Folder',
                                              directory=os.getcwd()+"/data")

window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
