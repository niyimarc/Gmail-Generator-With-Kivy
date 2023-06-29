from kivymd.app import MDApp
from kivy.lang import Builder
from kv_helpers import screen_helper
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard

Window.size = (500,700)
class DreyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        screen = Builder.load_string(screen_helper)

        return screen

    def get_android_screen_size(self):
        from jnius import autoclass
        # Get the current activity and display metrics
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        metrics = autoclass('android.util.DisplayMetrics')()

        # Get the default display
        display = activity.getWindowManager().getDefaultDisplay()
        display.getMetrics(metrics)

        # Return the screen width and height
        return (metrics.widthPixels, metrics.heightPixels)

    def getEmail(self, event):
        self.email = self.root.ids.email_input.text  # Access MDTextField using ids
        self.generate_email_addresses(self.email)

    def generate_email_addresses(self, email):
        """
        Generates a list of unique email addresses by inserting dots (.) between characters of the email address.

        Args:
        email (str): The email address to generate unique addresses from

        Returns:
        A list of unique email addresses
        """
        # Split the email address into username and domain parts
        email_parts = email.split('@')
        username = email_parts[0]
        domain = email_parts[1]

        # Initialize an empty set to hold unique email addresses
        unique_addresses = set()

        # Generate all possible combinations of dots in the username
        for i in range(2 ** (len(username) - 1)):
            # Convert the current number to binary, padded with leading zeros
            binary = format(i, f'0{len(username) - 1}b')

            # Start with the first character of the username
            new_username = username[0]

            # Insert dots where there are 1's in the binary representation
            for j, bit in enumerate(binary):
                if bit == '1':
                    # Make sure there's no more than one dot in a row
                    if new_username[-1] != '.':
                        new_username += '.'
                new_username += username[j + 1]

            # Add the new email address to the set of unique addresses
            unique_addresses.add(f'{new_username}@{domain}')


        # Save the generated email addresses to a file
        with open('email_addresses.txt', 'w') as f:
            for address in unique_addresses:
                f.write(address + '\n')

        # Read the contents of the file and update the MDLabel widget
        with open('email_addresses.txt', 'r') as f:
            text = f.read()
            self.root.ids.output.text = text

        results = self.root.ids.results
        results.pos_hint = {'center_x': 0.5, 'center_y': 0.4}

        return unique_addresses

    def copy_text(self):
        output_text = self.root.ids.output.text
        Clipboard.copy(output_text)

if __name__ == "__main__":
    DreyApp().run()
