from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class SuperheroForm(ModelForm):
    class Meta:
        model = models.Superhero
        fields = ('nom','date','createur','acteurs','super_pouvoir','description')
        labels = {
            'nom':_("Le nom de l'acteur"),
            'date':_("Date de naissance de l'acteur"),
            'createur':_('Le nom du createur du superHero'),
            'acteurs': _('Le nom des acteurs ayant incarné ce superHero:'),
            'super_pouvoir':_("Le(s) performance(s) de l'acteur"),
            'description':_('Description sur cette acteur:')
        }
class ActeursForm(ModelForm):
    class Meta:
        model = models.Acteurs
        fields = ('nom','prénom','age','photos')
        labels = {
            'nom':_("Le nom de l'acteur"),
            'prénom':_("Le prénom de l'acteur"),
            'age':_("L'age de l'acteur"),
        }
class CatgoriesfilmsForm(ModelForm):
    class Meta:
        model = models.Catgoriesfilms
        fields = ('nom','descriptif')
        labels = {
            'nom':_("Le nom de la catégorie"),
            'descriptif':_("Le descriptif de la catégorie"),
        }

class CommentairesfilmsForm(ModelForm):
    class Meta:
        model = models.Commentairesfilms
        fields = ('film','commentaire')
        labels = {
            'film':_("Le nom du film"),
            'commentaire':_("Le commentaire"),
        }

class FilmsForm(ModelForm):
    class Meta:
        model = models.Films
        fields = ('film','titre', 'année_sortie','affiche','réalisateur','catégorie')
        labels = {
            'film':_("Le nom du film"),
            'titre':_("Le titre du film"),
            'année_sortie':_("L'année de sortie du film"),
            'affiche':_("L'affiche du film"),
            'réalisateur':_("Le réalisateur du film"),
            'catégorie':_("La catégorie du film"),
        }