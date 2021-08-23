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
    
    
window = login_main()
while True:             # The Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit Application':
            break
window.close()

   

if __name__ == "__main__":
    # def function here
    login_main()
    pass