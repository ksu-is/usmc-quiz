from flask import Flask, render_template, request

app = Flask(QUIZ)

@app.route('/')
def index():
    return render_template('index-quizgame.html')

@app.route('/py', methods=['GET', 'POST'])

def quiz():

    character_names = open('characters.txt','r')
    characters = character_names.readline()

    while characters:
        characters = character_names.readline()
    
    if request.method == "POST":

        input01 = request.form['input01'].capitalize()
        input02 = request.form['input02'].capitalize()
        input03 = request.form['input03'].capitalize()
        input04 = request.form['input04'].capitalize()
        input05 = request.form['input05'].capitalize()
        input06 = request.form['input06'].capitalize()
        input07 = request.form['input07'].capitalize()
        input08 = request.form['input08'].capitalize()
        input09 = request.form['input09'].capitalize()
        input10 = request.form['input10'].capitalize()
        input11 = request.form['input11'].capitalize()
        input12 = request.form['input12'].capitalize()
        input13 = request.form['input13'].capitalize()
        input14 = request.form['input14'].capitalize()
        input15 = request.form['input15'].capitalize()
        input16 = request.form['input16'].capitalize()
        input17 = request.form['input17'].capitalize()
        input18 = request.form['input18'].capitalize()
        input19 = request.form['input19'].capitalize()
        input20 = request.form['input20'].capitalize()
        input21 = request.form['input21'].capitalize()
        input22 = request.form['input22'].capitalize()
        input23 = request.form['input23'].capitalize()
        input24 = request.form['input24'].capitalize()
        input25 = request.form['input25'].capitalize()
        input26 = request.form['input26'].capitalize()
        input27 = request.form['input27'].capitalize()
        input28 = request.form['input28'].capitalize()
        input29 = request.form['input29'].capitalize()
        input30 = request.form['input30'].capitalize()

        correct = []
        incorrect = []
        input_names = []
    
        for name in characters:
            if input01 in characters:
                correct.append(name)
            else:
                incorrect.append(name)            

if QUIZ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
