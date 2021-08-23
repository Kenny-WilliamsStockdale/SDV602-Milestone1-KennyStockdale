import PySimpleGUI as sg
"""
Making test scripts for Data Explorer screens and various connecting interfaces 
 
"""
def login_main():
    layout = [
        [sg.Text('Username:')],
        [sg.InputText('')],
        [sg.Text('Password:')],
        [sg.InputText('')],
        [sg.Button('Login')],
        [sg.Button('Exit Application')]]
    return sg.Window('Property Tiles Login Page', layout, finalize=True)

def Data_source_page():
    layout = [
        [sg.Button('Login')],
        [sg.Button('Exit Application')]]
    return sg.Window('Data Source Page', layout, finalize=True, size=(500,150))

def event():
    window1 = None  #window1 = login_main()
    window2 = Data_source_page()
    while True:             # The Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit Application':
            window.close()   # if closing win 1, exit program
            break

   

if __name__ == "__main__":
    # def function here
    #login_main()
    #Data_source_page()
    event()
    pass