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
        [sg.Button('Issue dates'), sg.Button('Current status')],
        [sg.Button('Number of owners'), sg.Button('Upload new data')],
        [sg.Button('Logout')]]
    return sg.Window('Data Source Page', layout, finalize=True, size=(500,150), element_justification='c' )

def DES1():
    layout = [
        [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
        [sg.Multiline(default_text='Data Information Summary:', size=(35, 5)), sg.Multiline(default_text='Chat System:',size=(35, 5))],
        [sg.Button('Next'), sg.Button('Previous')],
        [sg.Button('Back'), sg.Button('Logout')],
        ]
    return sg.Window('Property Issue Dates', layout, finalize=True, size=(800,450))

def event():
    window1 = None  #window1 = login_main()
    window2 = Data_source_page()
    window3 = DES1()
    while True:             # The Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit Application':
            window.close()  
            break

   

if __name__ == "__main__":
    # def function here
    #login_main()
    #Data_source_page()
    event()
    pass