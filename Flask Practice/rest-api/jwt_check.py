from user import User
users = [
    User(1, 'Exia', 'abc123'),
    User(2, 'Legna', 'def456'),
    User(3, 'Zero', 'ghi789'),   
]

# Dictionary Comprehensions to create lookup tables for users by username and by id
username_tbl = { u.username: u for u in users }
userid_tbl = { u.id: u for u in users }

def authenticate(username, password): # Might need to rename to authenticate to work with flask-jwt-extended
    user = username_tbl.get(username, None) # Use get instead of a call to avoid KeyError if username not found
    if user and user.password == password:
        return user
    else:
        return None

# Flask extended doesnt need this
# def identify(payload):# Might need to rename to identity to work with flask-jwt
#     u_id = payload['identity'] # This is how flask-jwt-extended passes the identity of the user in the payload of the JWT
#     return userid_tbl.get(u_id, None)