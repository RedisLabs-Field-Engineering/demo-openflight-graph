# Open Flight Graph

## Running with Docker

### Prerequisites 
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Running Dockerized Version

```
git clone https://github.com/RedisLabs-Field-Engineering/demo-openflight-graph
cd demo-openflight-graph
docker-compose up
```

### Navigate to RedisInsight
[Open This Link in Your Browser](http://localhost:8001)

[Example Queries Available](./InsightQueries.md)


## Running from Source

### Data Source

https://openflights.org/data.html

### Running Graph

RedisGraph can be run from docker

```
docker run --rm -p 6379:6379 redislabs/redisgraph:edge
```

### Loading Data

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
