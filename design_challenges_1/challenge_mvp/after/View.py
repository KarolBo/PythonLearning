import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb

from Presenter import PresenterAbs, response


class GuiView:
    def __init__(self, presenter: PresenterAbs):
        self._presenter = presenter

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Data Processing GUI")

        # Create the widgets for the GUI
        load_button = tk.Button(self.root, text="Load CSV", command=self._load_data)
        show_input_data_button = tk.Button(
            self.root, text="Show input data", command=self._show_input_data
        )
        analyze_button = tk.Button(self.root, text="Analyze Data", command=self._analyze_data)
        # Create a variable to store the selected option
        self.selected_option = tk.StringVar(self.root)
        # Create a list of options
        options = ["All", "Temperature", "Humidity", "CO2"]
        # Set the default selected option
        self.selected_option.set(options[0])
        # Create an OptionMenu widget
        option_menu = tk.OptionMenu(self.root, self.selected_option, *options)

        export_button = tk.Button(self.root, text="Export Data", command=self._export_data)
        # Create a Text widget to display the data
        self.text_widget = tk.Text(self.root)

        # Arrange the widgets in the main window
        self.text_widget .pack(side=tk.BOTTOM)
        load_button.pack(side=tk.LEFT)
        show_input_data_button.pack(side=tk.LEFT)
        analyze_button.pack(side=tk.LEFT)
        option_menu.pack(side=tk.LEFT)
        export_button.pack(side=tk.LEFT)


    def run(self):
        # Start the main loop
        self.root.mainloop()


    def _load_data(self) -> None:
        file_path = fd.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        resp: response = self._presenter.load_data(file_path)
        if resp['header'] == 'Error':
            mb.showinfo("Error", resp['payload'])
            return
        mb.showinfo(resp['header'], resp['payload'])


    def _show_input_data(self) -> None:
        self.text_widget .delete("1.0", tk.END)
        resp: response = self._presenter.get_input_data()
        if resp['header'] == 'Error':
            mb.showinfo("Error", resp['payload'])
            return
        self.text_widget.insert(tk.END, resp['payload'])
    

    def _analyze_data(self) -> None:
        self.text_widget.delete("1.0", tk.END)
        option: str = self.selected_option.get()
        resp: response = self._presenter.get_analyzed_data(option)
        if resp['header'] == 'Error':
            mb.showinfo("Error", resp['payload'])
            return
        self.text_widget.insert(tk.END, resp['payload'])


    def _export_data(self) -> None: 
        file_path = fd.asksaveasfile(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )
        if file_path is None:
            return
        option: str = self.selected_option.get()
        resp: response = self._presenter.export_data(option, file_path)
        if resp['header'] == 'Error':
            mb.showinfo("Error", resp['payload'])
            return
        mb.showinfo("Export", resp['payload'])