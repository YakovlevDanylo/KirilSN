from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QLineEdit, QTextEdit, QLabel, QHBoxLayout, \
    QVBoxLayout, QInputDialog

import json
notes = {
    "Ласкаво просимо!": {
        "Текст": "витаю вас у нашому додатку",
        "Теги":["Вітання","Привіт"]
    },
    "Домашка": {
        "текст": "Треба зробити Домашку до понедилка",
        "теги":["Химия", "Математика"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Rozymni Zamitki")
window.risize(900,600)

list_notes = QListWidget
list_notes_label = QLabel("spisok zametok")

button_note_create = QPushButton("Stvorite Zamitku")
button_note_del = QPushButton("Vidalite Zamitku")
button_note_save = QPushButton("Zberegre Zamitku")

field_tag = QLineEdit("")
field_tag.setPlaceholderText("Vidit teg...")
field_text = QTextEdit()
list_tags = QListWidget()
list_tags_label = QLabel("Spiski Tegov")
button_tag_add = QPushButton("Dodati do zamitkiv")
button_tag_del = QPushButton("Vidkripite Vid Zametke")
button_tag_search = QPushButton("Shukate Zamitkepo te")

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(field_text)

col2 = QHBoxLayout()
col2.addWidget(list_notes_label)
col2.addWidget(list_notes)
col2

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key][""] = field_text.toPlainText()
        with open("","") as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print("Zamitka dla zberezenya ne obrana")

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_tags.clear()
        list_notes.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("", "") as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print("Zamitka dla videlanya ne obrana")


def show_notes():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tegs"])

def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати замітку", "Назва Замітки")
    if ok and note_name != "":
        notes[note_name] = {"текст": "", "теги": []}
        list_notes.addItem(note_name)

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print("Zamitka dla dodavanya tega ne obrana!")

def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["tegs"].remove(tag)
        list_tags.clear()
        list_tags.selectedItems(notes[key]["tegs"])
        with open("teg dla videlenya ne obranii"):
            json.dump(notes, file, sort_keys=True)
    else:
        print("teg dla videlenya ne obranii")

def search_tag():
    tag = field_tag.text()
    if button_tag_search.text():
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["tegs"]:
                notes_filtered[note] = notes[note]
        button_tag_search.setText("Skinuti poshuk")
        field_tag.clear()
        list_notes.clear()
        list_notes.addItems(notes_filtered)
    elif button_tag_search.text() == "skunuti poshuk":
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("Shukati zamitku po tegu")


list_notes.itemClicked.connect(show_notes)




list_notes.itemClicked.connect(show_notes)
button_note_create.clicked.connect(show_notes())
button_note_create.clicked.connect(add_note())
button_note_create.clicked.connect(del_note())
button_note_create.clicked.connect(save_note())
button_note_create.clicked.connect(add_tag)
button_note_create.clicked.connect(del_tag)
button_note_create.clicked.connect(search_tag)



list_notes.addItems(notes)
window.show()
app.exec_()

window.setStyleSheet("""
QWidget {
    background-color: light-green;
    font-size: 17px;
}
""")
