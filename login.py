import PySimpleGUI as sg
import datasourcenav

def login_main():
    layout = [
        [sg.Text('Username:')],
        [sg.InputText('')],
        [sg.Text('Password:')],
        [sg.InputText('')],
        [sg.Button('Login')],
        [sg.Button('Exit Application')]]
    window = sg.Window('Property Tiles Login Page', layout, finalize=True)
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Login':
        window.close()
        datasourcenav.Data_source_page()
    if event == 'Exit Application':
        window.close()
# ------------------------------- LOGIN MAIN PAGE END -------------------------------

# ------------------------------- LOGIN WELCOME PAGE START -------------------------------

def login_main_Welcome():
    layout = [
        [sg.Text('Welcome')],
        [sg.Text('Username')],
        [sg.Button('View Data')],
        [sg.Button('Logout')]]
    window = sg.Window('Property Tiles Login Page', layout,
                       finalize=True, size=(350, 150), element_justification='c')
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'View Data':
        window.close()
        datasourcenav.Data_source_page()
    if event == 'Exit Application':
        window.close()
# ------------------------------- LOGIN WELCOME PAGE END -------------------------------

# ------------------------------- LOGIN ERROR PAGE START -------------------------------

def login_main_Unsuccessful():
    layout = [
        [sg.Text('The entered password and or username is incorrect.\nPlease enter your correct username and password')],
        [sg.Button('Login')]]
    window = sg.Window('Property Tiles Login Page', layout,
                       finalize=True, size=(350, 150), element_justification='c')
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Login':
        window.close()
        login_main()
# ------------------------------- LOGIN ERROR PAGE END -------------------------------

if __name__ == "__main__":
    # def function here
    login_main()
    pass