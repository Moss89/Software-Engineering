# Defines Flask application instance

"""
This is just for running the app
"""

from app import app

# IDE sometimes says app stuff doesn't exist but works


if __name__ == "main":
    app.run(debug=True)