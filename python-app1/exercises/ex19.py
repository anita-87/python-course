import PySimpleGUI as Sg

Sg.theme("black")

label1 = Sg.Text("Enter feet:")
input1 = Sg.Input(key="feet")

label2 = Sg.Text("Enter inches:")
input2 = Sg.Input(key="inches")

convert_button = Sg.Button("Convert")
exit_button = Sg.Button("Exit")
conversion_label = Sg.Text(key="conversion")

window = Sg.Window("Convertor",
                   layout=[
                       [label1, input1],
                       [label2, input2],
                       [convert_button, exit_button, conversion_label]
                   ])

while True:
    event, values = window.read()
    print(values)

    match event:
        case "Convert":
            try:
                feet = int(values["feet"])
                inches = int(values["inches"])
                meters = feet * 0.3048 + inches * 0.0254
                window["conversion"].update(value=f"{meters} m")
            except ValueError:
                Sg.popup("Please provide two numbers", font=("Helvetica", 20))
        case "Exit":
            window.close()
        case Sg.WINDOW_CLOSED:
            break

window.close()
