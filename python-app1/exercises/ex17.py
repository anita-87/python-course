import PySimpleGUI as Sg

label1 = Sg.Text("Enter feet:")
input1 = Sg.Input()

label2 = Sg.Text("Enter inches:")
input2 = Sg.Input()

convert_button = Sg.Button("Convert")

window = Sg.Window("Convertor",
                   layout=[[label1, input1], [label2, input2], [convert_button]])

window.read()
window.close()
