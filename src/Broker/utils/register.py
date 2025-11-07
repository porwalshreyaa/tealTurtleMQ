from .db_operations import add_client
def register_user(role:str, username:str, password:str):
    if (check_if_registered(role, username)):
        print("already there")
        return "connected"
    else:
        add_client(username, password, role)
        # register user based on role and generate id

def check_if_registered(role:str, username:str):
    # query data base
    query = False    # for now
    if query:
        return True
    else:
        return False