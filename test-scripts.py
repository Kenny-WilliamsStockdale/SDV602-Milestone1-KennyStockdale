import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')

# ------------------------------- LOGIN PAGE MAIN START -------------------------------
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
        Data_source_page()
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
        Data_source_page()
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

# ------------------------------- DATA SOURCE PAGE START-------------------------------

def Data_source_page():
    layout = [
        [sg.Button('Property issue dates'),
         sg.Button('Current property status')],
        [sg.Button('Number of property owners'), sg.Button('Upload new data')],
        [sg.Button('Logout')]]
    window = sg.Window('Data Source Page', layout, finalize=True,
                       size=(500, 150), element_justification='c')

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Property issue dates':
        window.close()
        DataExplorerScreen1()
    if event == 'Current property status':
        window.close()
        DataExplorerScreen2()
    if event == 'Number of property owners':
        window.close()
        DataExplorerScreen3()
    if event == 'Upload new data':
        window.close()
        Upload_new_data_page()
    if event == 'Logout':
        window.close()
        login_main()
# ------------------------------- DATA SOURCE PAGE END -------------------------------

# ------------------------------- UPLOAD PAGE START -------------------------------

def Upload_new_data_page():
    layout = [
            [sg.Frame(layout=[
                [sg.Text('Title_No:', size=(14, 1)), sg.InputText(
                    '', size=(15, 1))],
                [sg.Text('Status:', size=(14, 1)), sg.InputText(
                    '', size=(15, 1))],
                [sg.Text('Type:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))],
                [sg.Text('Land_district:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))],
                [sg.Text('Issue_date:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))],
                [sg.Text('Guarantee_Status:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))],
                [sg.Text('Number_Owners:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))]
            ], title=""), sg.Frame(layout=[

                [sg.Text('Estate_description')],
                [sg.Multiline('', size=(35, 5))]], title="")],
            [sg.Button('Back'), sg.Button('Upload new data')]
            
        ]
            
    
    window = sg.Window('Upload new data page', layout,
                       finalize=True, size=(500, 250))

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Back':
        window.close()
        Data_source_page()
    if event == 'Upload new data':
        window.close()
        Upload_new_data_successful()
# ------------------------------- UPLOAD PAGE END -------------------------------

# ------------------------------- UPLOAD CONFIRMATION PAGE START -------------------------------

def Upload_new_data_successful():
    layout = [
        [sg.Text('Success! New data has been added.')],
        [sg.Button('Ok')]]
    window = sg.Window('New data confirmation', layout,
                       finalize=True, size=(350, 80), element_justification='c')
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Ok':
        window.close()
        Upload_new_data_page()
# ------------------------------- UPLOAD CONFIRMATION PAGE END -------------------------------

# ------------------------------- DATA EXPLORER SCREEN ONE START -------------------------------

def DataExplorerScreen1():
    # ---- MATPLOTLIB CODE HERE -----
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(len(labels))
    fig, ax = plt.subplots()
    width = 0.35
    rects1 = ax.bar(t - width/2, men_means, width, label='Men')
    rects2 = ax.bar(t + width/2, women_means, width, label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(t)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    # ---- END OF MATPLOTLIB CODE ----

    # ---- Beginning of Matplotlib helper code ----

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ---- Beginning of GUI CODE ----

    # define the window layout
    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
              [sg.Multiline(default_text='Data Information Summary:', size=(
                  35, 5)), sg.Multiline(default_text='Chat System:', size=(35, 5))],
              [sg.Button('Previous'), sg.Button('Next')],
              [sg.Button('Back'), sg.Button('Logout')]]

    # create the form and show it without the plot
    window = sg.Window('Property issue dates', layout, finalize=True,
                       element_justification='center', size=(800, 700))

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Previous':
        window.close()
        DataExplorerScreen3()
    if event == 'Next':
        window.close()
        DataExplorerScreen2()
    if event == 'Back':
        window.close()
        Data_source_page()
    if event == 'Logout':
        window.close()
        login_main()
# ------------------------------- DATA EXPLORER SCREEN ONE END -------------------------------

# ------------------------------- DATA EXPLORER SCREEN TWO START -------------------------------

def DataExplorerScreen2():
    # ---- MATPLOTLIB CODE HERE -----
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(len(labels))
    fig, ax = plt.subplots()
    width = 0.35
    rects1 = ax.bar(t - width/2, men_means, width, label='Men')
    rects2 = ax.bar(t + width/2, women_means, width, label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(t)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    # ---- END OF MATPLOTLIB CODE ----

    # ---- Beginning of Matplotlib helper code ----

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ---- Beginning of GUI CODE ----

    # define the window layout
    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
              [sg.Multiline(default_text='Data Information Summary:', size=(
                  35, 5)), sg.Multiline(default_text='Chat System:', size=(35, 5))],
              [sg.Button('Previous'), sg.Button('Next')],
              [sg.Button('Back'), sg.Button('Logout')]]

    # create the form and show it without the plot
    window = sg.Window('Current property status', layout, finalize=True,
                       element_justification='center', size=(800, 700))

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Previous':
        window.close()
        DataExplorerScreen1()
    if event == 'Next':
        window.close()
        DataExplorerScreen3()
    if event == 'Back':
        window.close()
        Data_source_page()
    if event == 'Logout':
        window.close()
        login_main()
# ------------------------------- DATA EXPLORER SCREEN TWO END -------------------------------

# ------------------------------- DATA EXPLORER SCREEN THREE START -------------------------------

def DataExplorerScreen3():
    # ---- MATPLOTLIB CODE HERE -----
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(len(labels))
    fig, ax = plt.subplots()
    width = 0.35
    rects1 = ax.bar(t - width/2, men_means, width, label='Men')
    rects2 = ax.bar(t + width/2, women_means, width, label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(t)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    # ---- END OF MATPLOTLIB CODE ----

    # ---- Beginning of Matplotlib helper code ----

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ---- Beginning of GUI CODE ----

    # define the window layout
    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
              [sg.Multiline(default_text='Data Information Summary:', size=(
                  35, 5)), sg.Multiline(default_text='Chat System:', size=(35, 5))],
              [sg.Button('Previous'), sg.Button('Next')],
              [sg.Button('Back'), sg.Button('Logout')]]

    # create the form and show it without the plot
    window = sg.Window('Number of property owners', layout,
                       finalize=True, element_justification='center', size=(800, 700))

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Previous':
        window.close()
        DataExplorerScreen2()
    if event == 'Next':
        window.close()
        DataExplorerScreen1()
    if event == 'Back':
        window.close()
        Data_source_page()
    if event == 'Logout':
        window.close()
        login_main()
# ------------------------------- DATA EXPLORER SCREEN THREE END -------------------------------

if __name__ == "__main__":
    # def function here
    login_main()
    pass
