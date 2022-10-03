# BasicC2Server
A basic C2 server used in some workshops
Pls don't use maliciously

In the workshops I deploy this onto a Rasperry Pi on the same LAN (for demo purposes). But it could just as easily be placed into a digital ocean droplets and used the same way (just remember to change the IP accordingly in the payloads)

## Setup
### Pre-Reqs
- Download python (I'm using 3.10.7)
```
>> py -m pip install flask
```

### Running the app
```
>> py app.py
 * Serving Flask app 'app'
 * Debug mode: on
 WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 ...
```
Now navigate to `http://YOUR_IP:5000/upload` to upload a file, or use within your own payloads
