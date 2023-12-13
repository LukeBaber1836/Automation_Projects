import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
import requests

def show_currency():
    # Inputs
    in_curr = in_combo.currentText()
    out_curr = target_combo.currentText()
    input_text = float(text.text())

    # Convert
    rate = get_currency_rate(in_curr, out_curr)
    output = round(input_text * rate, 2)

    # Output message
    message = f'{input_text} {in_curr} is {output} {out_curr}'
    output_label.setText(str(message))

# Returns float of currency rate based off of the input_curr
def get_currency_rate(input_curr, output_curr):
    exchange_rate_url = f"https://openexchangerates.org/api/latest.json?app_id={os.getenv('currency_converter_key')}&base={input_curr}"
    content = requests.get(exchange_rate_url).json()
    rate = float(content['rates'][output_curr])
    return rate
    
app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

# Main box
layout = QVBoxLayout()

# Inputs, selections horizontal box
layout_1 = QHBoxLayout()
layout.addLayout(layout_1)

# Currency Selections
layout_2 = QVBoxLayout()
layout_1.addLayout(layout_2)

in_combo = QComboBox()
currencies = ['USD', 'EUR', 'MXN', 'GBP']
in_combo.addItems(currencies)
layout_2.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout_2.addWidget(target_combo)


# Input, button
layout_3 = QVBoxLayout()
layout_1.addLayout(layout_3)

text = QLineEdit()
layout_3.addWidget(text)

btn = QPushButton('Convert')
layout_3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(show_currency)

# Output
output_label = QLabel('')
layout.addWidget(output_label)

# Deploy
window.setLayout(layout)
window.show()
app.exec()