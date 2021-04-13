import csv
from django.core.management.base import BaseCommand, CommandError
from adopt.models import sightings
from django.db import models

class Command(BaseCommand):
  help = 'A valid path to export data'
  
  def add_arguments(self,parser):
    parser.add_argument('path',type=str,nargs='*')

  def handle(self,*args,**kwargs):
    path = kwargs['path']
    
    new_f = open(path, 'a', newline = '')
    obj = sightings.objects.all()
    lst = obj.values_list()
    fields = sightings.getattrlist()
    csv_write = csv.writer(out, dialect='excel')
    csv_write.writerow(fields)
    for i in lst:
        csv_write.writerow(i)
    
