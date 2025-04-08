from flask import render_template, request

def init_app(app):
    
    @app.route('/')
    
    def home():
        return render_template('home.html')
    
    @app.route('/lista')
    
    def lista():
        return render_template('lista.html')
    
    @app.route('/feedback')
    
    
    def feedback():
        return render_template('feedback.html')
    
    @app.route('/Login')
    
    def Login():
        return render_template('login.html')