 1.1: Retrieve all nodes from the database.
 match (n) return n
 
 1.2: Examine the data model for the graph.
 call db.schema.visualization()
 
 1.3: Retrieve all Person nodes.
 MATCH (n:Person) RETURN n 
 
 1.4: Retrieve all Movie nodes.
 MATCH (n:Movie) RETURN n
 
 2.1: Retrieve all movies that were released in a specific year.
 MATCH (n:Movie  {released: 2003}) RETURN n
 
 2.2: View the retrieved results as a table.
 ok
 
 2.3: Query the database for all property keys.
 call db.propertyKeys()
 
 2.4: Retrieve all Movies released in a specific year, returning their titles.
 MATCH (n:Movie {released: 2003}) RETURN n.title
 
 2.5: Display title, released, and tagline values for every Movie node in the graph.
 MATCH (n:Movie) RETURN n.title, n.released, n.tagline
 
 2.6: Display more user-friendly headers in the table
 MATCH (n:Movie) RETURN n.title as `Título`, n.released as `Lançado`, n.tagline as `Descrição`
 
 3.1: Display the schema of the database.
 call db.schema.visualization()
 
 3.2: Retrieve all people who wrote the movie Speed Racer.
 MATCH (people:Person)-[relatedTo]-(:Movie {title: "Speed Racer"}) RETURN people.name

 3.3: Retrieve all movies that are connected to the person, Tom Hanks.
 MATCH (m:Movie)<--(:Person {name: 'Tom Hanks'}) RETURN m.title

 3.4: Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier.
 Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier.

 3.5: Retrieve information about the roles that Tom Hanks acted in
 MATCH (m:Movie)-[rel:ACTED_IN]-(:Person {name: 'Tom Hanks'}) RETURN m.title, rel.roles

 4.1: Retrieve all movies that Tom Cruise acted in.
 MATCH(p:Person)-[:ACTED_IN]->(m:Movie) WHERE p.name='Tom Cruise' RETURN m.title as Movie

 4.2: Retrieve all people that were born in the 70’s.
 MATCH (p:Person) WHERE p.born >= 1970 AND p.born < 1980 RETURN p.name as Nome, p.born as Nascimento
 
 4.3: Retrieve the actors who acted in the movie The Matrix who were born after 1960.
 MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE p.born > 1960 AND m.title = 'The Matrix' 
 RETURN p.name as Nome, p.born as `Nascimento`

 4.4:  Retrieve  all  movies  by  testing  thenode  label  and  a property.
 MATCH (m) WHERE m:Movie AND m.released = 2000 RETURN m.title

 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes.
 MATCH (a)-[rel]->(m) WHERE a:Person AND type(rel) = 'WROTE' AND m:Movie
 RETURN a.name as Nome, m.title as Filme
  
 4.6:  Retrieve  all  people  in  the  graph  that  do  not  have  a property.
 MATCH (a:Person) WHERE NOT exists (a.born) RETURN a.name as Nome

 4.7:  Retrieve  all  people  related  to  movies  where  the relationship has a property.
 MATCH (a:Person)-[rel]->(m:Movie) WHERE exists(rel.rating)
 RETURN a.name as Name, m.title as Filme, rel.rating as Avaliação

 4.8: Retrieve all actors whose name begins with James.
 MATCH (p:Person)-[:ACTED_IN]->(:Movie) WHERE p.name STARTS WITH 'James'
 RETURN p.name as Nome

 4.9: Retrieve all all REVIEW relationships from the graph with filtered results.
 MATCH (:Person)-[r:REVIEWED]->(m:Movie) WHERE toLower(r.summary) CONTAINS 'fun'
 RETURN  m.title as Filme, r.summary as Sumário, r.rating as Pontuação

 