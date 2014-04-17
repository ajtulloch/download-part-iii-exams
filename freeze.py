from flask_frozen import Freezer
from cam import cam

freezer = Freezer(cam)

if __name__ == '__main__':
    freezer.freeze()
