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

        input01 = request.form['input01']
        input02 = request.form['input02']
        input03 = request.form['input03']
        input04 = request.form['input04']
        input05 = request.form['input05']
        input06 = request.form['input06']
        input07 = request.form['input07']
        input08 = request.form['input08']
        input09 = request.form['input09']
        input10 = request.form['input10']
        input11 = request.form['input11']
        input12 = request.form['input12']
        input13 = request.form['input13']
        input14 = request.form['input14']
        input15 = request.form['input15']
        input16 = request.form['input16']
        input17 = request.form['input17']
        input18 = request.form['input18']
        input19 = request.form['input19']
        input20 = request.form['input20']
        input21 = request.form['input21']
        input22 = request.form['input22']
        input23 = request.form['input23']
        input24 = request.form['input24']
        input25 = request.form['input25']
        input26 = request.form['input26']
        input27 = request.form['input27']
        input28 = request.form['input28']
        input29 = request.form['input29']
        input30 = request.form['input30']

        correct = []
        incorrect = []
        input_names = []
    
        for name in characters:

            if input01.capitalize() in characters:
                correct.append
            

if QUIZ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
