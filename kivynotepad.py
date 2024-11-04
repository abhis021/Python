#code by abhis021@github
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

class NotepadApp(App):
    def build(self):
        self.title = "Kivy Notepad"
        layout = BoxLayout(orientation='vertical')

        # Create a TextInput for the notepad area
        self.text_input = TextInput(hint_text='Type your text here...', multiline=True)
        layout.add_widget(self.text_input)

        # Create buttons for saving and opening files
        button_layout = BoxLayout(size_hint_y=None, height=50)

        save_button = Button(text='Save')
        save_button.bind(on_press=self.save_file)
        button_layout.add_widget(save_button)

        open_button = Button(text='Open')
        open_button.bind(on_press=self.open_file)
        button_layout.add_widget(open_button)

        layout.add_widget(button_layout)
        return layout

    def save_file(self, instance):
        filechooser = FileChooserIconView()
        popup = Popup(title='Save File', content=filechooser, size_hint=(0.9, 0.9))
        filechooser.bind(on_submit=self._save_file)
        popup.open()

    def _save_file(self, filechooser, selection, touch):
        if selection:
            with open(selection[0], 'w') as f:
                f.write(self.text_input.text)
        filechooser.parent_window.dismiss()

    def open_file(self, instance):
        filechooser = FileChooserIconView()
        popup = Popup(title='Open File', content=filechooser, size_hint=(0.9, 0.9))
        filechooser.bind(on_submit=self._load_file)
        popup.open()

    def _load_file(self, filechooser, selection, touch):
        if selection:
            with open(selection[0], 'r') as f:
                self.text_input.text = f.read()
        filechooser.parent_window.dismiss()

if __name__ == '__main__':
    NotepadApp().run()
