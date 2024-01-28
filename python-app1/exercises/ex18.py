import PySimpleGUI as Sg

label1 = Sg.Text("Enter feet:")
input1 = Sg.Input(key="feet")

label2 = Sg.Text("Enter inches:")
input2 = Sg.Input(key="inches")

convert_button = Sg.Button("Convert")
conversion_label = Sg.Text(key="conversion")

window = Sg.Window("Convertor",
                   layout=[[label1, input1], [label2, input2], [convert_button, conversion_label]])

while True:
    event, values = window.read()
    print(values)

    match event:
        case "Convert":
            feet = int(values["feet"])
            inches = int(values["inches"])
            meters = feet * 0.3048 + inches * 0.0254
            window["conversion"].update(value=f"{meters} m")
        case Sg.WINDOW_CLOSED:
            break

window.close()
