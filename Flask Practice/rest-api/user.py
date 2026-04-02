# Simple example
class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password # TODO: Come back and add hashing to this

    def __repr__(self):
        return f'User(id={self.id}, username={self.username})'