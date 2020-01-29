from flask import Flask, request, jsonify, send_from_directory, render_template 
import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Gegevens.html')

@app.route('/agenda/')
def about():
    return render_template('kapper.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)                                 
    
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/afspraak', methods=['POST'])
def afspraak_invoegen():
    data = request.json
    db.execute_sql("INSERT INTO afspraak(naam, email, tijdstip, behandeling) VALUES ('{}','{}','{}','{}')".format(data['naam'], data['email'], data['tijdstip'], data['behandeling']))
    return jsonify({'succes' : True}), 200, {'ContenType': 'application/json'}

@app.route('/afspraken', methods=['GET'])
def vraag_afspraken_op():
    dbafspraken = db.execute_sql('SELECT * FROM afspraak ORDER BY tijdstip')

    afspraken = []
    for afspraak in dbafspraken: 
        afspraken.append(
            {'naam': afspraak['naam'], 'email': afspraak['email'], 'behandeling': afspraak['behandeling'], 'tijdstip': afspraak['tijdstip'] }
        )
    return jsonify(afspraken), 200, {'ContentType': 'application/json'}

app.run()