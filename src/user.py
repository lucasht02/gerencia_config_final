class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, candidate_password):
        return candidate_password == self.password

    def update_profile(self, new_username=None, new_password=None):
        if new_username:
            self.username = new_username
        if new_password:
            self.password = new_password
