from app import app
from app.controllers import users
from app.controllers import svcs

if __name__=="__main__":
    app.run(debug=True)