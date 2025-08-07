from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import sql_communicatie
import move as move_script

app = Flask(__name__, template_folder='website', static_folder='website')

@app.route('/')
def index():
    return render_template('index.html', images = sql_communicatie.lijst_img())

@app.route('/besturing')
def besturing():
    return render_template('html/besturing.html')

@app.route('/insert')
def insert():
    return render_template('html/insert.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    command = data.get("move")
    move_script.Besturing(command)
    return "Als deze string er niet staat flipt hij"

@app.route('/actie', methods=['POST'])
def actie():
    data = request.get_json()
    actie = data.get('actie')
    coordinaat = sql_communicatie.find_coordinate(int(actie[3:]))
    move_script.Cordinate(coordinaat)
    return "Als deze string er niet staat flipt hij"




@app.route('/zoek_suggesties')
def zoek_suggesties():
    alle_data = sql_communicatie.lijst_items()
    zoekterm = request.args.get('q', '').lower()
    if len(zoekterm) != 0:
        suggesties = [item for item in alle_data if zoekterm in item.lower()]
        return jsonify({'suggesties': suggesties[:10]})
    return jsonify({"suggesties":[]})

@app.route('/verwerk_zoekopdracht', methods=['POST'])
def verwerk_zoekopdracht():
    data = request.get_json()
    gekozen_item = data.get('item')
    print(f"Gebruiker selecteerde: {gekozen_item}")
    # Voer hier je Python-methode uit, bijvoorbeeld:
    # start_script(gekozen_item)
    return f"Opdracht ontvangen voor '{gekozen_item}'"



UPLOAD_FOLDER = 'website/img/items'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/insert', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Afbeelding ophalen
        if 'image' not in request.files:
            return "Geen afbeelding gevonden", 400
        image = request.files['image']
        if image.filename == '':
            return "Geen bestandsnaam", 400

        # Tekstinvoer ophalen
        x = request.form.get('x', '')
        y = request.form.get('y','')
        naam = request.form.get('naam','')

        # Bestand veilig opslaan
        filename = secure_filename(image.filename)
        path_img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(path_img)
        image.save(path_img)

        # Hier kun je description gebruiken zoals je wil
        print(f"naam: {naam}, x: {x}, y: {y}")
        sql_communicatie.new_item(naam,x,y,path_img)
        

    return render_template('index.html', images = sql_communicatie.lijst_img())



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

