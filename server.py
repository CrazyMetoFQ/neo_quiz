import os
import sys

from flask import Flask


app = Flask(__name__)

# Initialize our ngrok settings into Flask
app.config.from_mapping(
BASE_URL="http://localhost:5000",
USE_NGROK=True
)

# pyngrok will only be installed, and should only ever be initialized, in a dev environment
from pyngrok import ngrok
# Get the dev server port (defaults to 5000 for Flask, can be overridden with --port
# when starting the server
port = 5000
# Open a ngrok tunnel to the dev server
ngrok.set_auth_token("24k83aoHO3om9fz4iWAhPgQBymf_6ri1xmk9vXw8cWp3kbVzh")
public_url = ngrok.connect(port, bind_tls=True) # .public_url
# print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url,port))
# # Update any base URLs or webhooks to use the public ngrok URL
# app.config["BASE_URL"] = public_url

# # init_webhooks(public_url)
# # # ... Initialize Blueprints and the rest of our app

@app.route("/")
def home():
	return  str(public_url) # f"<a href='{public_url}'>ng</a> "

@app.route("/user/<ty>")
def tri(ty):
	return f"hello {ty}"

app.run()