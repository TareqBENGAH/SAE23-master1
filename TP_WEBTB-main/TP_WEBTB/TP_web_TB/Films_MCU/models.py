from django.db import models
import django.utils.timezone
# Create your models here.
class Superhero(models.Model):
    nom = models.CharField(max_length=100,blank=False)
    date = models.DateField(blank=False, default=django.utils.timezone.now())
    createur = models.CharField(max_length=100,blank=False)
    acteurs = models.TextField(blank=False)
    super_pouvoir = models.TextField(blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return f"{self.nom}"

    def dico(self):
        return{"nom": self.nom, "date": self.date , "createur" : self.createur , "acteurs" : self.acteurs, "super_pouvoir" : self.super_pouvoir, "description" : self.description}


class Acteurs(models.Model):
    nom = models.CharField(db_column='Nom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    age = models.DateTimeField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    photos = models.TextField(db_column='Photos', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.nom}"

    def dico(self):
        return{"nom": self.nom, "prénom": self.prénom, "age": self.age, "photos": self.photos}


    class Meta:
        managed = False
        db_table = 'Acteurs'


class Catgoriesfilms(models.Model):
    nom = models.CharField(max_length=45, blank=True, null=True)
    descriptif = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f"{self.nom}"

    def dico(self):
        return{"nom": self.nom, "descriptif": self.descriptif}

    class Meta:
        managed = False
        db_table = 'CatégoriesFilms'


class Commentairesfilms(models.Model):
    film = models.CharField(max_length=45, blank=True, null=True)
    personnes = models.CharField(db_column='Personnes', max_length=45, blank=True, null=True)  # Field name made lowercase.
    note = models.IntegerField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(db_column='Commentaire', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.film}"

    def dico(self):
        return{"film": self.film, "personnes": self.personnes, "note": self.note, "commentaire": self.commentaire, "date": self.date}

    class Meta:
        managed = False
        db_table = 'Commentairesfilms'


class Films(models.Model):
    film = models.CharField(db_column='Film', max_length=45, blank=True, null=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    année_sortie = models.DateTimeField(db_column='année sortie', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    affiche = models.CharField(max_length=45, blank=True, null=True)
    réalisateur = models.CharField(max_length=45, blank=True, null=True)
    catégorie = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f"{self.film}"
    def dico(self):
        return{"film": self.film, "titre": self.titre, "année_sortie": self.année_sortie, "affiche": self.affiche, "réalisateur": self.réalisateur, "catégorie": self.catégorie}

    class Meta:
        managed = False
        db_table = 'Films'


class FilmsMcuFilms(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_film = models.CharField(max_length=100)
    producteur = models.CharField(max_length=100)
    date = models.DateField()
    resume = models.TextField()
    superhero = models.ForeignKey('FilmsMcuSuperhero', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.nom_film}"
    def dico(self):
        return{"nom_film": self.nom_film, "producteur": self.producteur, "date": self.date, "resume": self.resume, "superhero": self.superhero}

    class Meta:
        managed = False
        db_table = 'Films_MCU_films'


class FilmsMcuSuperhero(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    date = models.DateField()
    createur = models.CharField(max_length=100)
    acteurs = models.TextField()
    super_pouvoir = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.nom}"
    def dico(self):
        return{"nom": self.nom, "date": self.date, "créateur": self.créateur, "acteurs": self.acteurs, "super_pouvoir": self.super_pouvoir, "description": self.description}

    class Meta:
        managed = False
        db_table = 'Films_MCU_superhero'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
