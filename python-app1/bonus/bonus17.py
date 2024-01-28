import PySimpleGUI as Sg
from zip_creator import make_archive

label1 = Sg.Text("Select files to compress: ")
input1 = Sg.Input()
choose_button1 = Sg.FilesBrowse("Choose", key="files")

label2 = Sg.Text("Select destination folder: ")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

compress_button = Sg.Button("Compress")
output_label = Sg.Text(key="output", text_color="white")

window = Sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]

    match event:
        case "Compress":
            make_archive(filepaths, folder)
            window["output"].update(value="Compression completed")
        case Sg.WINDOW_CLOSED:
            break

window.close()
