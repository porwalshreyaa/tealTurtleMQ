from server import app
from flask import Flask, request, jsonify
from utils.register import register_user

# common connect route for producer/consumer client
@app.route("/connect", methods=["POST"])
def connect_user():
    try:
        data = request.get_json()
        username =str(data["username"])
        password =str(data["password"])
        role =str(data["role"])
        # generate unique id for each client, active_id = username + sessipn_date
        unique_id = register_user(role, username, password)  # add in register user to return some unique id, haven't added yet
        return {"result":"success", "data":{"username": username, "role": role, "active_id": unique_id}}
    except:
        return {"result": "error", "data": {"msg": "could not generate data"}}
# common disconnect route for producer/consumer client
@app.route("/disconnect", methods=["POST"])
def disconnect_user():
    try:
        data = request.get_json()
        username =str(data["username"])
        password =str(data["password"])
        role =str(data["role"])
        remove_user(role, username, password)
        return {"result": "success"}
    except:
        return {"result": "error"}
# producer specific
@app.route("/send", methods=["POST"])
def send_msg():
    data = request.get_json()
    if data:
        # after all data validation
        return {"result": "success"}
    return {"result":"error"}

# consumer specific
@app.route("/subscribe", methods=["POST"])
def declare():
    data = request.get_json()
    if data:
        # after all validation
        queue_name = data["queue_name"]
        # generate queue_url = queue_name + user role + active_id
        queue_url = ""
        # create queue
        return {"result": "success", "data": { "queue_url": queue_url}}
    return {"result": "error"}

@app.route("/pull/<queue_url>", methods=["GET","POST"])
def pull():
    data = request.get_json()
    # extract queue url, 
    # check if there is msg for user in the queue
    # if yes, then send to user
    return
@app.route("/ack", methods=["POST"])
def ack():
    data = request.get_json()
    return

@app.route("/nack", methods=["POST"])
def nack():
    data = request.get_json()
    return