from flask import render_template, send_file, request
import connexion
import config
from models import Character
import markdown


app = config.connex_app
app.add_api(config.basedir / "swagger.yml", options={
        'swagger_ui': False
    })

@app.route('/')
def index():
    return render_template('home.html', title='Home', content="""Hello""")
    
@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route("/documentation.yml")
def swagger():
    return render_template("documentation.yml")

@app.route('/logo.png')
def serve_image():
    filename = '/Users/benjaminnour/Documents/Python/Projects/archer_API_flask/logo.png'  # replace with the actual path to your image file
    return send_file(filename, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)