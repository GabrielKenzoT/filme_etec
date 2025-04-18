from flask import render_template, request

filmelist = [
    {'titulo': 'Lego Batman','ano': 2018,'genero': 'Animação','descricao':'O filme "LEGO Batman: O Filme" é uma comédia animada cheia de ação, que explora o mundo do super-herói solitário enquanto ele aprende o valor da amizade e da colaboração para salvar Gotham City. Com humor cativante e cenas incríveis, é diversão garantida para fãs de todas as idades!'},
    {'titulo': 'Uma aventura no Tempo','ano': 2020,'genero': 'Infantil', 'descricao': '"Uma Aventura no Tempo" narra a emocionante jornada de jovens exploradores que, ao ativarem um misterioso artefato, são transportados para diferentes períodos históricos. Enfrentando desafios e aprendendo lições valiosas, eles descobrem que o verdadeiro poder do tempo está nas conexões humanas e nas escolhas que moldam o futuro. Uma história envolvente cheia de descobertas e emoção!'}
    ]
feedbacklist = [
    {'nome': 'Ramon Trigon','email': 'ramontrigon@hotmail', 'opcoes': 'Outros', 'descricao': 'Cara eu nunca vi um site tão bom como esse, acho que deveria merecer um MB'}
]

def init_app(app):
    
    @app.route('/')
    
    def home():
        return render_template('home.html')
    
    
    @app.route('/lista', methods=['GET', 'POST'])

    def lista():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('genero') and request.form.get('descricao'):
                filmelist.append({'titulo': request.form.get('titulo'), 
                                'ano': request.form.get('ano'),
                                'genero': request.form.get('genero'),
                                'descricao': request.form.get('descricao')})
                
        return render_template('lista.html', 
                               filmelist = filmelist)
   
    
    @app.route('/feedback', methods=['GET', 'POST'])
    
    def feedback():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('email') and request.form.get('opcoes') and request.form.get('descricao'):
                feedbacklist.append({'nome': request.form.get('nome'),
                                'email': request.form.get('email'), 
                                'opcoes': request.form.get('opcoes'),
                                'descricao': request.form.get('descricao')})
                

        return render_template('feedback.html', 
                               feedbacklist = feedbacklist)
    
    @app.route('/cadastro', methods=['GET', 'POST'])

    def cadastro():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('genero') and request.form.get('descricao'):
                filmelist.append({'titulo': request.form.get('titulo'), 
                                'ano': request.form.get('ano'),
                                'genero': request.form.get('genero'),
                                'descricao': request.form.get('descricao')})
                
        
        return render_template('cadastro.html',
                               filmelist = filmelist)