from flask import Flask
from routes.career import career_bp

app = Flask(__name__)
app.register_blueprint(career_bp, url_prefix='/api/career')

if __name__ == '__main__':
    app.run(debug=True)
