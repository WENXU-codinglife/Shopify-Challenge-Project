"""
This is a file residing outside 'project' directory.
It is essetially not necessary when starting the app by 'flask run',
but used to ensure the app to run successfully on Heroku.
"""

from project import *

app = create_app()


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='localhost', port=port)
