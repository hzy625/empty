from django.core.management.base import BaseCommand
from adopt.models import sightings
from datetime import datetime, date
import csv


class Command(BaseCommand):
  
    help = 'Import data from the csv file'

    def add_arguments(self, parser):
       parser.add_argument('path', type=str, help='The file path')

    def handle(self, *args, **kwargs):
      path = kwargs['path']
      
      try:
        with open(path,encoding='utf-8') as fp:
          data = csv.DictReader(fp)
          for i in data:
            s=sightings(
              X = i['X'],
              Y=i['Y'],
              Unique_squirrel_id=i['Unique Squirrel ID'],
              Shift=i['Shift'],
              Date=datetime.date(int(i['Date'][-4:]),int(i['Date'][:2]),int(i['Date'][2:4])),
              Age=i['Age'],
              Primary_Fur_Color=i['Primary Fur Color'],
              Location = i['Location'],
              Specific_location = i['Specific Location'],
              Running=i['Running'].upper(),
              Chasing=i['Chasing'].upper(),
              Climbing=i['Climbing'].upper(),
              Eating=i['Eating'].upper(),
              Foraging=i['Foraging'].upper(),
              Other_activities=i['Other Activities'],
              Kuks=i['Kuks'].upper(),
              Quaas=i['Quaas'].upper(),
              Moans=i['Moans'].upper(),
              Tail_flags=i['Tail flags'].upper(),
              Tail_twitches=i['Tail twitches'].upper(),
              Approaches=i['Approaches'].upper(),
              Indifferent=i['Indifferent'].upper(),
              Runs_from=i['Runs from'].upper(),
              )
              s.save()
              
      except csv.Error as e:
        print(f'An error has occured with the file imported')
        
            
      
