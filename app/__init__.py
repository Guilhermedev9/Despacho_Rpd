from flask import Flask  # type: ignore

def create_app():
    app = Flask(__name__)
    # Configurações adicionais podem ser adicionadas aqui
    
    # Importar as rotas
    from .views import main
    app.register_blueprint(main)

    return app
