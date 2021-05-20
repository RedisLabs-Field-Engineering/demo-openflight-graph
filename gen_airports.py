#!/usr/bin/env python

import csv

fields=[ "Airport_ID", "Name", "City", "Country", "IATA", "ICAO", "Latitude", "Longitude", "Altitude"]


with open('airports.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=[ "Airport_ID", "Name", "City", "Country", "ICAO", "Latitude", "Longitude", "Altitude"])
    writer.writeheader()
    with open('airports.dat', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            res = {fields[i]: row[i] for i in range(len(fields))}
            del(res['IATA'])
            writer.writerow(res)
