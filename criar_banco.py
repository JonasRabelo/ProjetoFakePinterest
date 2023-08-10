from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

# pip install flask-login
# pip install flask-bcrypt
# Página para criar o banco
with app.app_context():
    database.create_all()
