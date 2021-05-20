#!/usr/bin/env python

import csv

fields=[ 
    "Airline", "Airline_ID", "Source_airport", "Source_airport_ID",
    "Destination_airport", "Destination_airport_ID", "Codeshare", "Stops", "Equipment"
]

# create a set of airports to ensure we have these
airports = set()
with open("airports.csv") as ports:
    rows = csv.DictReader(ports)
    for row in rows:
        airports.add(row['Airport_ID'])

out_fields=["src", "dest", "airline", "stops:INT"]

with open('ROUTE.csv', 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=out_fields)
    writer.writeheader()
    with open('routes.dat', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            res = {fields[i]: row[i] for i in range(len(fields))}
            if res["Source_airport_ID"] != "\\N" and res["Destination_airport_ID"] != "\\N" and res["Airline_ID"] != "\\N":
                if res["Source_airport_ID"] in airports and res["Destination_airport_ID"] in airports:
                    writer.writerow({
                        "src": res["Source_airport_ID"],
                        "dest": res["Destination_airport_ID"],
                        "airline": res["Airline_ID"],
                        "stops:INT": int(res["Stops"]),
                    })
