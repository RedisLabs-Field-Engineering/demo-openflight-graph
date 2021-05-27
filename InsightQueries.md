
# Example Queries

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

Find me the most connected airports using Page Rank

```
CALL algo.pageRank('Airport', 'ROUTE') YIELD node, score RETURN node.Name, node.Country, score LIMIT 10
```

Find me all connections 3 deep for ATL using Breadth-first search

```
MATCH (zeronode:Airport{IATA: 'ATL'})  CALL algo.BFS(zeronode, 3, 'ROUTE') YIELD nodes  UNWIND nodes as n WITH collect(n.IATA) as signs RETURN signs

```


