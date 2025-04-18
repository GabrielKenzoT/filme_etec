from flask import render_template, request

filmelist = [
    {'titulo': 'Lego Batman','ano': 2018,'genero': 'Animação'},
    {'titulo': 'Uma aventura no Tempo','ano': 2020,'genero': 'Infantil'}
    ]

def init_app(app):
    
    @app.route('/')
    
    def home():
        return render_template('home.html')
    
    @app.route('/lista')
    def lista():
        return render_template('lista.html')
    
    @app.route('/lista', methods=['GET', 'POST'])
    def lista():
        # acessando o primeiro jogo da lista de jogos
        filmelist = filmelist[0]
   
    
    @app.route('/feedback')
    
    
    def feedback():
        return render_template('feedback.html')
    
    @app.route('/cadastro')


    def cadastro():
        return render_template('cadastro.html')