from fakepinterest import database, app
#Página para criar o banco
with app.app_context():
    database.create_all()
