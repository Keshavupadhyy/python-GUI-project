import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock

class ClockApp(App):
    def build(self):
        layout = GridLayout(cols=2, padding=10, spacing=10)

        self.time_label = Label(text='00:00:00', font_size=50)
        layout.add_widget(self.time_label)

        self.update_time()

        reset_button = Button(text='Reset', font_size=20)
        reset_button.bind(on_press=self.reset_time)
        layout.add_widget(reset_button)

        return layout

    def update_time(self, *args):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.text = current_time

    def reset_time(self, instance):
        self.time_label.text = '00:00:00'

if __name__ == '__main__':
    ClockApp().run()