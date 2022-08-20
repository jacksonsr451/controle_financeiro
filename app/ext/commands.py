from app.core.create_superuser import CreateSuperuser


def init_app(app):
    @app.cli.command("create-superuser")
    def create_superuser():
        print("Create superuser command:")
        username = input("Username: ")
        email = input("E-Mail: ")
        password = input("Password: ")
        try:
            CreateSuperuser(username=username, email=email, password=password)
        except Exception as error:
            print(error)
            
    app.cli.add_command(create_superuser)
    