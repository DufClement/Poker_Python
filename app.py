from flask import Flask, render_template, request
from videoPoker.Poker import Poker

app = Flask(__name__)

poker = Poker()

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html', banque=poker.get_banque(), resultat=poker.get_resultat())

@app.route('/commencer', methods=['POST','GET'])
def commencer():
    poker.init_deck()

    rejouer = False

    if request.method == 'POST':
        rejouer = True
    else:
        poker.set_banque(0)

    return render_template('commencer.html', decks=poker.decks(), rejouer=rejouer, banque=poker.get_banque())

@app.route('/miser', methods=['POST','GET'])
def miser():
    if request.method == 'POST':

        if len(request.form) == 2:
            banque = int(request.form['banque'])
            poker.set_banque((banque))

        mise = int(request.form['mise'])

        poker.set_mise(mise)

        main, decks = poker.premier_tirage()


        return render_template('miser.html', main=main, decks=decks, banque=poker.get_banque())


@app.route('/jeu', methods=['POST','GET'])
def jeu():
    if request.method == 'POST':

        tirage = list(request.form)

        dernier_tirage = poker.deuxieme_tirage(tirage)

        resultat, banque, msg = poker.video_poker(dernier_tirage)

        return render_template('jeu.html', dernier_tirage=dernier_tirage, decks=poker.decks(), resultat=poker.get_resultat(), banque=poker.get_banque(), msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
