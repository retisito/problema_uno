from archives.models import File, Data
from datetime import datetime
import csv, logging

def run():
    print("data_load")
    logger = logging.getLogger(__name__)
    files = File.objects.all().filter(status = 'sin procesar')[:50]

    for file in files:
        # Trata de abrir el file si existe y si el formato es correcto
        try:
            fhand = open(f'public/upload/{str(file.id)}_{file.name}')    
            reader = csv.reader(fhand)
            next(reader)
        except Exception as e:
            file.status = e.__class__.__name__
            file.save()
            continue

        for row in reader:
            if len(row) == 0: continue    
                
            # Se crea una entrada en Data si la data es correcta,
            # Si ya la entada existe, solo la retorna.    
            try:
                data, _ = Data.objects.get_or_create(
                    boro = row[0], objectid = int(row[1]), the_geom = row[2],
                    type = row[3], provider = row[4], name = row[5], location = row[6], 
                    lat = float(row[7]), lon = float(row[8]), x = float(row[9]), y = float(row[10]), 
                    location_t = row[11],remarks = row[12], city = row[13], ssid = row[14], sourceid = row[15],
                    activated = datetime.strptime(' '.join(row[16].split(' ')[:2]), '%m/%d/%Y %H:%M:%S'),    
                    borocode = int(row[17]), boroname = row[18],
                )
                
                # Se asocia la data al file correspondiente
                data.files.add(file)
            except Exception as e:
                logger.error(f'error :{e.__class__.__name__} on:')
                logger.error(row)
                logger.error('\n')
                continue

        file.status = 'en proceso'  
        file.save()      