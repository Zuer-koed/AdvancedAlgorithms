class Person:
    def __init__(self, name, gender, biography, privacy="public"):
        """
        Initialize a Person object for social media profile.

        Args:
            name (str): The person's name
            gender (str): The person's gender
            biography (str): Short bio/description
            privacy (str): "public" or "private"
        """
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy

    def display_profile(self):
        """
        Display the person's profile based on privacy settings.
        For private profiles, only show name.
        """
        print(f"\n=== {self.name}'s Profile ===")
        print(f"Name: {self.name}")

        if self.privacy.lower() == "public":
            print(f"Gender: {self.gender}")
            print(f"Biography: {self.biography}")
            print("Privacy: Public Profile")
        else:
            print("This is a private profile. Other details are hidden.")
        print("====")

    def get_name(self):
        """Get the person's name."""
        return self.name

    def get_privacy(self):
        """Get the privacy setting."""
        return self.privacy

    def __str__(self):
        """String representation of the person."""
        return self.name