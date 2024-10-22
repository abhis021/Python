from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import os
from datetime import datetime

class NoteTakerApp(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Default save location
        self.save_location = MDApp.get_running_app().user_data_dir
        self.selected_location = ""

        # Text field for notes
        self.note_input = MDTextField(
            hint_text="Write your note here...",
            multiline=True,
            mode="rectangle",
            size_hint_y=None,
            height="200dp"
        )
        self.add_widget(self.note_input)

        # Button to choose save location
        self.choose_location_button = MDRaisedButton(
            text="Choose Save Location",
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            width=300
        )
        self.choose_location_button.bind(on_press=self.show_file_manager)
        self.add_widget(self.choose_location_button)

        # Buttons for saving and viewing notes
        self.save_button = MDRaisedButton(
            text="Save Note",
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            width=300
        )
        self.save_button.bind(on_press=self.save_note)
        self.add_widget(self.save_button)

        self.view_button = MDRaisedButton(
            text="View Saved Notes",
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            width=300
        )
        self.view_button.bind(on_press=self.view_notes)
        self.add_widget(self.view_button)

        # Label to show messages
        self.message_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Secondary"
        )
        self.add_widget(self.message_label)

        # File manager for choosing directories
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.set_save_location
        )

    def save_note(self, instance):
        note_text = self.note_input.text
        if note_text.strip() == "":
            self.message_label.text = "Note is empty, please write something."
            return

        try:
            # Save to selected location
            save_path = self.selected_location if self.selected_location else self.save_location
            file_name = f"note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            with open(os.path.join(save_path, file_name), 'w') as file:
                file.write(note_text)

            self.message_label.text = f"Note saved as {file_name}."
            self.note_input.text = ""
        except Exception as e:
            self.message_label.text = f"Error: {str(e)}"

    def view_notes(self, instance):
        save_path = self.selected_location if self.selected_location else self.save_location
        if not os.path.exists(save_path):
            self.message_label.text = "No notes found."
            return

        files = [f for f in os.listdir(save_path) if f.endswith(".txt")]
        if not files:
            self.message_label.text = "No notes found."
            return

        # Dialog to list saved notes
        notes_list = MDList()
        for file in files:
            item = OneLineListItem(text=file, on_release=self.open_note)
            notes_list.add_widget(item)

        scroll_view = ScrollView()
        scroll_view.add_widget(notes_list)

        self.dialog = MDDialog(
            title="Saved Notes",
            type="custom",
            content_cls=scroll_view,
            size_hint=(0.8, 0.8),
        )
        self.dialog.open()

    def open_note(self, instance):
        save_path = self.selected_location if self.selected_location else self.save_location
        file_name = instance.text
        file_path = os.path.join(save_path, file_name)

        try:
            with open(file_path, 'r') as file:
                note_content = file.read()

            # Show the content of the note in a popup
            note_popup = Popup(
                title=f"Note: {file_name}",
                content=TextInput(text=note_content, readonly=True, multiline=True),
                size_hint=(0.8, 0.8)
            )
            note_popup.open()
        except Exception as e:
            self.message_label.text = f"Error opening note: {str(e)}"

    def show_file_manager(self, instance):
        self.file_manager.show('/')  # Root directory

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def set_save_location(self, path):
        self.selected_location = path
        self.message_label.text = f"Save location set to: {path}"
        self.exit_file_manager()

class NoteTakerAppMD(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        Window.size = (400, 600)
        return NoteTakerApp()

if __name__ == '__main__':
    NoteTakerAppMD().run()
