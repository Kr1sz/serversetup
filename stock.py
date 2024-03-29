#!/usr/bin/env python

"""
[stock]
[ktr]
[description]
"""

import os
from flask import Flask, render_template, url_for

def static(filename):
    """Provides the 'static' function that also appends the file's timestamp to the URL, usable in a template."""
    timestamp = os.path.getmtime(os.path.join(app.static_folder, filename))
    return "%s/%s?%s" % (app.static_url_path, filename, timestamp)

# Flask application
app = Flask(__name__)

# Views
@app.route('/')
def index():
    return "A"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

# Run dev server
if __name__ == '__main__':
    app.run()
