from archives.models import Data
from datetime import datetime
import csv

def run():
    fhand = open('public/upload/sample.csv')
    reader = csv.reader(fhand)
    next(reader)

    for row in reader:
        if len(row) == 0:
            continue
        
        data, created = Data.objects.get_or_create(
            boro = row[0],
            objectid = int(row[1]),
            the_geom = row[2],
            type = row[3],
            provider = row[4],
            name = row[5],
            location = row[6],
            lat = float(row[7]),  
            lon = float(row[8]), 
            x = float(row[9]), 
            y = float(row[10]), 
            location_t = row[11],
            remarks = row[12],
            city = row[13],
            ssid = row[14],
            sourceid = row[15],
            activated = datetime.strptime(' '.join(row[16].split(' ')[:2]), '%m/%d/%Y %H:%M:%S'),    
            borocode = int(row[17]),   
            boroname = row[18],
        )