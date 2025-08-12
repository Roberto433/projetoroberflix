from django.apps import AppConfig



class FilmeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "filme"

    def ready(self):
        from filme.models import Usuario
        import os

        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        Usuario.objects.filter(username='admin').exists()

        Usuario.objects.filter(username='admin').delete()

        if not Usuario.objects.filter(username="admin").exists():
            Usuario.objects.create_superuser(username="admin", email=email, password=senha)



