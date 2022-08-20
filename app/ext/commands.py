from app.core.create_superuser import CreateSuperuser


def init_app(app):
    @app.cli.command("app-install")
    def create_superuser(username, email, password):
        print("Create superuser command")
        try:
            CreateSuperuser(username=username, email=email, password=password)
        except Exception as error:
            print(error)
            
    app.cli.add_command(create_superuser)
    