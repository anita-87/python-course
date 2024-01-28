import PySimpleGUI as Sg
from zip_extractor import  extract_archive

Sg.theme("Black")

label1 = Sg.Text("Select archive:")
input1 = Sg.Input()
choose_button1 = Sg.FileBrowse("Choose", key="archive")

label2 = Sg.Text("Select dest dir:")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

extract_button = Sg.Button("Extract")
output_label = Sg.Text(key="output", text_color="green")

window = Sg.Window("Archive Extractor",
                   [[label1, input1, choose_button1],
                    [label2, input2, choose_button2],
                    [extract_button, output_label]])

while True:
    event, values = window.read()
    archive_path = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archive_path, dest_dir)
    window["output"].update(value="Extraction Completed!")


window.close()
