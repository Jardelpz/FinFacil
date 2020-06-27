from app import app
from app import db
from model.user import User
from model.divida import Divida
from routes import user, divida

if __name__ == '__main__':
    app.run(debug=True, port=5000)
