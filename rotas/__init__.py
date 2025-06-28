def register_blueprints(app):
    from .jogador import jogador_bp
    from .jogada import jogada_bp
    from .rodada import rodada_bp

    app.register_blueprint(jogador_bp)
    app.register_blueprint(jogada_bp)
    app.register_blueprint(rodada_bp)
