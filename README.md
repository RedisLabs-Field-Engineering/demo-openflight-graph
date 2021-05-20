
## Data Source

https://openflights.org/data.html

## Loading Data

```
# Create a python virtual environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Load the data
redisgraph-bulk-loader FLIGHTS -n Airport.csv  -r ROUTE.csv

# Create the index
redis-cli
127.0.0.1:6379> GRAPH.QUERY FLIGHTS "CALL db.idx.fulltext.createNodeIndex('Airport', 'Name')"

```


## Queries

Display all of the Labels

```
CALL db.labels()
```

Display all of the relationships

```
CALL db.relationshipTypes
```

Show me an example airport

```
MATCH (a:Airport{Country: "Japan", City: "Tokyo"}) RETURN a
```

Search Airports:

```
CALL db.idx.fulltext.queryNodes('Airport', 'Wayne') YIELD node RETURN node.IATA, node.City, node.Country, node.Name
```


Get from San Francisco to Oita Japan:

```
MATCH path=(s:Airport{IATA:'SFO'})-[:ROUTE*..2]->(d:Airport{IATA: 'OIT'}) RETURN DISTINCT(path)
```

Find me the unique routes from San Francisco to Jackson WY that don't go through Salt Lake City

```
MATCH route=(src:Airport{IATA:'SFO'})-[:ROUTE*..2]->(dest:Airport{IATA: 'JAC'}) WITH route, dest AS DEST, src AS SRC, nodes(route) as legs  UNWIND legs as leg WITH route, SRC, DEST, collect((leg.IATA='SLC')) as icn, collect(leg.IATA) as hops WHERE NOT true IN icn RETURN DISTINCT(hops)
```
