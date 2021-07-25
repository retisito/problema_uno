from archives.models import File, Data
import csv

def run():
    files = File.objects.all().filter(status = 'en proceso')[:5]
    rows = [
        [
            'BORO', 'OBJECTID', 'the_geom' , 'TYPE', 'PROVIDER', 'NAME', 'LOCATION', 'LAT', 'LON', 'X', 
            'Y', 'LOCATION_T', 'REMARKS', 'CITY', 'SSID', 'SOURCEID', 'ACTIVATED', 'BOROCODE', 'BORONAME'
        ]
    ]
    
    for file in files:
        for data in file.data_set.all():
            rows.append([
                data.boro, data.objectid, data.the_geom, data.type, data.provider, data.name, data.location, 
                data.lat, data.lon, data.x, data.y, data.location_t, data.remarks, data.city, data.ssid, 
                data.sourceid, data.activated, data.borocode, data.boroname
            ])

        with open(f'public/processed/{str(file.id)}_{file.name}', 'w', newline='') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerows(rows)
        
        file.status = 'procesado'  
        file.save()
        