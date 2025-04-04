from flask import render_template, request

def init_app(app):
    
    @app.route('/')
    
    def home():
        return render_template('index.html')
    
    @app.route('/lista')
    
    def lista():
        return render_template('lista.html')
    
    @app.route('/cadfilmes')
    
    
    def cadfilmes():
        return render_template('cadfilmes.html')
    
    @app.route('/cadseries')
    
    def cadseries():
        return render_template('cadseries.html')