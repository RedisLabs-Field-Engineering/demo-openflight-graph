#!/usr/bin/env python

import csv

fields=[ "Airport_ID", "Name", "City", "Country", "IATA", "ICAO", "Latitude", "Longitude", "Altitude"]


with open('Airport.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    with open('airports.dat', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            res = {fields[i]: row[i] for i in range(len(fields))}
            if res["IATA"] != "\\N":
                writer.writerow(res)
