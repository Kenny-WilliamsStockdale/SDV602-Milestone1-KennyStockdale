import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
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
        
def login_main_Welcome():
    layout = [
        [sg.Text('Welcome')],
        [sg.Text('Username')],
        [sg.Button('View Data')],
        [sg.Button('Logout')]]
    window = sg.Window('Property Tiles Login Page', layout, finalize=True, size=(350, 150), element_justification='c')
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'View Data':
        window.close()
        Data_source_page()
    if event == 'Exit Application':
        window.close()
        
def login_main_Unsuccessful():
    layout = [
        [sg.Text('The entered password and or username is incorrect.\nPlease enter your correct username and password')],
        [sg.Button('Login')]]
    window = sg.Window('Property Tiles Login Page', layout, finalize=True, size=(350, 150), element_justification='c')
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Login':
        window.close()
        login_main()

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
    if event == 'Logout':
        window.close()
        login_main()
        
def Upload_new_data_page():
    layout = [
        [sg.Text('Title_No', size=(5,1)), sg.InputText('', size=(15,1))], 
        [sg.Text('Status'), sg.InputText('', size=(15,1))], 
        [sg.Text('Type'), sg.InputText('', size=(15,1))],
        [sg.Text('Land_district'), sg.InputText('', size=(15,1))], 
        [sg.Text('Issue_date'), sg.InputText('', size=(15,1))],
        [sg.Text('Guarantee_Status'), sg.InputText('', size=(15,1))],
        [sg.Text('Number_Owners'), sg.InputText('', size=(15,1))]
        ]
    window = sg.Window('Data Source Page', layout, finalize=True)

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Back':
        window.close()
        Data_source_page()


def DataExplorerScreen1():
    # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------
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

    # ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

    # ------------------------------- Beginning of Matplotlib helper code -----------------------

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ------------------------------- Beginning of GUI CODE -------------------------------

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


def DataExplorerScreen2():
    # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------
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

    # ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

    # ------------------------------- Beginning of Matplotlib helper code -----------------------

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ------------------------------- Beginning of GUI CODE -------------------------------

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


def DataExplorerScreen3():
    # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------
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

    # ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

    # ------------------------------- Beginning of Matplotlib helper code -----------------------

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ------------------------------- Beginning of GUI CODE -------------------------------

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

# def event():
#     window = DataExplorerScreen1()  #window1 = login_main()
#     while True:             # The Event Loop
#         event, values = window.read()
#         if event == None or event == 'Exit Application':
#             window.close()
#             break


if __name__ == "__main__":
    # def function here
    login_main()
    # Data_source_page()
    # event()
    # DataExplorerScreen1()
    # login_main_Welcome()
    # login_main_Unsuccessful()
    Upload_new_data_page()
    pass
