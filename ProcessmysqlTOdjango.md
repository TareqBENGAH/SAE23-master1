SAE23-master1 
Tout d'abord il y'a deux branch la branch -master celle ou l'on va mettre tous codes fonctionnelles à 100% ainsi que la branch -master2test celle qui va nous permettre de tous nos codes de test
pour essayer de ne pas tous mélanger. 

Télécharger le logiciel mysqlserver : https://dev.mysql.com/downloads/mysql/
Puis lancer le serveur en root puis crée un mot de passe : ***root : djangoserver
Il faut également télécharger l'application Mysqlworkbench :*** https://www.mysql.com/fr/products/workbench/ ***


Maintenant faire la table dans MysqlWorkbench après avoir crée la table il faut se rendre sur django puis aller dans settings.py > databases :

***DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': '', mettre le nom de la table dans mysql (ne pas oublier d'avoir le serveur mysql actif)
        'USER': 'root',
        'HOST': 'localhost', #recopier comme cela
        'PORT': '3306',
        'PASSWORD': '', ##entrer le mot de passe enregistrer précedement 
    }
}
Puis se rendre dans le fichier _init_.py pour importer le mysqlclient (le serveur mysql) 
  Rajouter cette commande : 
        import pymysql
        pymysql.install_as_MySQLdb()
Ensuite lancer python manage.py makemigrations pour pouvoir réaliser les migrations puis appliquer python manage.py migrate 
Cela fait crée un fichier manage.py avec toutes les tables dedans donc faire cette commande :
python manage.py inspectdb > models.py  
puis après le déplacer dans votre application vous verrez cela fonctionne

