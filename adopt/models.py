from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class sightings(models.Model):
    Latitude=models.FloatField(
            null=True,blank=True,
            help_text=_('Latitude'),
    )
    Longitude=models.FloatField(
            null=True,blank=True,
            help_text=_('Longitude'),
    )
    Unique_Squirrel_ID=models.CharField(
            max_length=20,
            help_text=_('Unique Squirrel ID'),
    )
    PM='PM'
    AM='AM'
    Shift_choices=(
            (PM,'PM'),
            (AM,'AM'),
    )
    Shift=models.CharField(
            max_length=20,
            blank=True,
            choices=Shift_choices,
    )
    Date=models.DateField(
            help_text=_('Date'),
            null=True,
            blank=True,
    )

    adult='adult'
    juvenile='juvenile'
    other='other'
    Age_Choices=(
            (adult,'adult'),
            (juvenile,'juvenile'),
            (other,'other'),
    )
    Age=models.CharField(
            max_length=10,
            choices=Age_Choices,
            blank=True,
    )
    gray='gray'
    cinnamon='cinnamon'
    black='black'
    other='other'
    Fur_color_choices=(
            (gray,'gray'),
            (cinnamon,'cinnamon'),
            (black,'black'),
            (other,'other'),
    )
    Primary_Fur_Color=models.CharField(
            max_length=20,
            choices=Fur_color_choices,
            blank=True,
            help_text=_('Primary Fur Color'),
    )
    ground_plane='ground plane'
    above_ground='above ground'
    Location_choices=(
            (ground_plane,'ground plane'),
            (above_ground,'above ground'),
            (other,'other'),
    )
    Location=models.CharField(
            max_length=20,
            choices=Location_choices,
            blank=True,
    )
    Specific_location=models.CharField(
            max_length=200,
            help_text=_('Specific location'),
            blank=True,
    )

    Running=models.BooleanField(help_text=_('Is the squirrel running?'), default=False)
    Chasing=models.BooleanField(help_text=_('Is the squirrel chasing?'), default=False)
    Climbing=models.BooleanField(help_text=_('Is the squirrel climbing?'), default=False)
    Eating=models.BooleanField(help_text=_('Is the squirrel eating?'), default=False)
    Foraging=models.BooleanField(help_text=_('Is the squirrel foraging?'), default=False)
    Other_Activities=models.CharField(
        max_length=200, help_text='What other activites is the squirrel doing?', blank=True)
    Kuks=models.BooleanField(help_text=_('Is the squirrel kuking?'), default=False)
    Quaas=models.BooleanField(help_text=_('Is the squirrel quaaing?'), default=False)
    Moans=models.BooleanField(help_text=_('Is the squirrel moaning?'), default=False)
    Tail_flags=models.BooleanField(help_text=_('Does the squirrel have a tail flag?'), default=False)
    Tail_twitches=models.BooleanField(help_text=_('Is the squirrel\'s tail twitching?'), default=False)
    Approaches=models.BooleanField(help_text=_('Did the squirrel approach you?'), default=False)
    Indifferent=models.BooleanField(help_text=_('Was the squirrel indifferent to you?'), default=False)
    Runs_from=models.BooleanField(help_text=_('Did the squirrel run from you?'), default=False)

    def __str__(self):
        return self.Unique_Squirrel_ID

    def getattrlist():
        return [i.name for i in sightings._meta.fields]

