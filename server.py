from back_end import app

# ! CONTROLLERS HERE
from back_end.controllers import users


if __name__ == '__main__':
    app.run(debug=True, port=5003)