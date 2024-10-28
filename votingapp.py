import csv
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.clock import Clock
from kivy.core.window import Window
import matplotlib.pyplot as plt
from kivy.core.audio import SoundLoader


class VotingApp(BoxLayout):
    candidates = []
    candidate_photos = []
    vote_counts = []
    is_admin = BooleanProperty(False)
    voter_id = StringProperty('')
    background_color = StringProperty("#FFFFFF")  # Default white background

    def __init__(self, **kwargs):
        super(VotingApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.setup_ui()

    def setup_ui(self):
        # Purpose of Voting
        purpose_label = Label(text="Purpose of Voting: Choose your preferred candidate!", size_hint_y=None, height=50)
        self.add_widget(purpose_label)

        # Voter ID input
        self.voter_id_input = TextInput(hint_text='Enter Voter ID (Name)', multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.voter_id_input)

        # Voting buttons (dynamic)
        self.vote_button_layout = BoxLayout(size_hint_y=None, height=40)
        self.add_widget(self.vote_button_layout)

        # Admin login button
        self.admin_login_button = Button(text="Admin Login", on_press=self.open_admin_login, size_hint_y=None, height=40)
        self.add_widget(self.admin_login_button)

        # Results button
        self.add_widget(Button(text="Export Results to CSV", on_press=self.export_results, size_hint_y=None, height=40))

        # Graph button
        self.add_widget(Button(text="Show Voting Graph", on_press=self.show_voting_graph, size_hint_y=None, height=40))

        # Background color selection
        self.add_widget(Button(text="Change Background Color", on_press=self.change_background_color, size_hint_y=None, height=40))

        # Background image selection (if needed)
        self.add_widget(Button(text="Change Background Image", on_press=self.change_background_image, size_hint_y=None, height=40))

    def open_admin_login(self, instance):
        # Admin login popup
        self.login_popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.password_input = TextInput(hint_text='Enter Admin Password', password=True, multiline=False)
        self.login_button = Button(text='Login', size_hint_y=None, height=40)

        self.login_popup_content.add_widget(self.password_input)
        self.login_popup_content.add_widget(self.login_button)

        self.login_popup = Popup(title='Admin Login', content=self.login_popup_content, size_hint=(None, None), size=(400, 200))
        self.login_button.bind(on_press=lambda x: self.admin_login(self.password_input.text))
        self.login_popup.open()

    def admin_login(self, password):
        if password == "admin123":  # Admin password check
            self.is_admin = True
            self.login_popup.dismiss()
            self.show_popup("Admin mode enabled", duration=3)
            self.open_candidate_management()
            self.admin_login_button.disabled = True  # Disable the admin login button
        else:
            self.show_popup("Incorrect password!", duration=3)

    def open_candidate_management(self):
        # Popup for managing candidates
        self.candidate_popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.candidate_name_input = TextInput(hint_text='Candidate Name', multiline=False)
        self.candidate_photo_input = TextInput(hint_text='Photo Path', multiline=False)
        self.candidate_symbol_input = TextInput(hint_text='ASCII Symbol', multiline=False)
        self.add_candidate_button = Button(text='Add Candidate', size_hint_y=None, height=40)

        self.candidate_popup_content.add_widget(self.candidate_name_input)
        self.candidate_popup_content.add_widget(self.candidate_photo_input)
        self.candidate_popup_content.add_widget(self.candidate_symbol_input)
        self.candidate_popup_content.add_widget(self.add_candidate_button)

        # Add logout button for admin
        self.logout_button = Button(text='Logout', size_hint_y=None, height=40)
        self.logout_button.bind(on_press=self.admin_logout)
        self.candidate_popup_content.add_widget(self.logout_button)

        self.candidate_popup = Popup(title='Manage Candidates', content=self.candidate_popup_content, size_hint=(None, None), size=(400, 300))
        self.add_candidate_button.bind(on_press=self.add_candidate)
        self.candidate_popup.open()

    def add_candidate(self, instance):
        name = self.candidate_name_input.text
        photo = self.candidate_photo_input.text
        symbol = self.candidate_symbol_input.text

        if name and photo:
            self.candidates.append(name)
            self.candidate_photos.append(photo)
            self.vote_counts.append(0)
            self.setup_vote_buttons()  # Refresh voting buttons
            self.candidate_popup.dismiss()
            self.show_popup(f"Candidate {name} added!", duration=3)
        else:
            self.show_popup("Please provide both name and photo path!", duration=3)

    def setup_vote_buttons(self):
        self.vote_button_layout.clear_widgets()
        for i, candidate in enumerate(self.candidates):
            vote_button = Button(text=f"{self.candidate_photos[i]} {candidate}", on_press=lambda x, idx=i: self.vote_candidate(idx))
            self.vote_button_layout.add_widget(vote_button)

    def vote_candidate(self, candidate_index):
        voter_name = self.voter_id_input.text.strip()
        if voter_name and voter_name not in self.voter_id:
            self.vote_counts[candidate_index] += 1
            self.voter_id = voter_name
            self.play_alert_sound()
            self.show_popup(f"Vote cast for {self.candidates[candidate_index]}!", duration=3)
        else:
            self.show_popup("You have already voted or entered an invalid name!", duration=3)

    def play_alert_sound(self):
        sound = SoundLoader.load('beep.wav')  # Replace with your beep sound file
        if sound:
            sound.play()

    def show_popup(self, message, duration=3):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        ok_button = Button(text='OK', size_hint_y=None, height=40)
        content.add_widget(ok_button)

        popup = Popup(title='Alert', content=content, size_hint=(None, None), size=(400, 200))
        ok_button.bind(on_press=popup.dismiss)
        popup.open()

        # Automatically dismiss after specified duration
        Clock.schedule_once(lambda dt: popup.dismiss(), duration)

    def export_results(self, instance):
        # Export voting results to CSV
        with open('voting_results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Candidate', 'Votes'])
            for candidate, count in zip(self.candidates, self.vote_counts):
                writer.writerow([candidate, count])
        self.show_popup("Results exported to voting_results.csv!", duration=3)

    def show_voting_graph(self, instance):
        # Plotting the voting results
        plt.bar(self.candidates, self.vote_counts)
        plt.xlabel('Candidates')
        plt.ylabel('Votes')
        plt.title('Voting Results')
        plt.savefig('voting_graph.png')  # Save as PNG
        plt.show()
        self.show_popup("Graph generated as voting_graph.png!", duration=3)

    def change_background_color(self, instance):
        # Change background color (this is a simple example)
        self.background_color = "#FFCCCB"  # Change to your desired color
        self.canvas.before.clear()
        with self.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(1, 0.8, 0.8, 1)  # Light red color
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def change_background_image(self, instance):
        # Change background image (optional)
        pass  # Implement background image change logic here

    def admin_logout(self, instance):
        self.is_admin = False
        self.show_popup("Admin mode disabled", duration=3)
        self.admin_login_button.disabled = False  # Re-enable admin login button
        self.candidates.clear()
        self.vote_counts.clear()
        self.vote_button_layout.clear_widgets()  # Clear vote buttons
        self.voter_id_input.text = ""  # Clear voter ID input

class VotingAppApp(App):
    def build(self):
        return VotingApp()

if __name__ == "__main__":
    VotingAppApp().run()
