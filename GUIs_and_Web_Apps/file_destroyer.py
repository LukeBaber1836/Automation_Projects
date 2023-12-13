from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select Files')
    message.setText('\n' .join(filenames))

def delete_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')  # overwite file with blank info
        path.unlink()
        message.setText('Destruction Seccessful!')

app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')
layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. <font color="red"> WARNING these files will be permanently deleted!</font>')
description.setFixedWidth(250)
description.setFixedHeight(50)
description.setWordWrap(True)
layout.addWidget(description, alignment=Qt.AlignmentFlag.AlignCenter)

open_btn = QPushButton('Select Files')
open_btn.setToolTip('Select the files that will be deleted')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

delete_btn = QPushButton('Delete Files')
delete_btn.setToolTip('Destroys selected files')
delete_btn.setFixedWidth(100)
layout.addWidget(delete_btn, alignment=Qt.AlignmentFlag.AlignCenter)
delete_btn.clicked.connect(delete_files)

message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()
