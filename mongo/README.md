
1.1 - Adicione outro Peixe e um Hamster com nome Frodo
> db.pets.insert({name:"Frodo", species: "Hamster"})
WriteResult({ "nInserted" : 1 })
> db.pets.insert({name:"Frodo", species: "Peixe"})
WriteResult({ "nInserted" : 1 })

1.2 - Faça uma contagem dos pets na coleção
>db.getCollection("pets").find({}).count()
8

1.3 - Retorne apenas um elemento o método prático possível
>db.getCollection("pets").findOne()
{
	"_id" : ObjectId("5e89e10fb16111f7184bd0a6"),
	"name" : "Mike",
	"species" : "Hamster"
}


1.4 - Identifique o ID para o Gato Kilha.
> db.getCollection("pets").find({"name": "Kilha"},{"_id":1})
{ "_id" : ObjectId("5e89e10fb16111f7184bd0a8") }


1.5 - Faça uma busca pelo ID e traga o Hamster Mike
> db.getCollection("pets").find({"_id": ObjectId("5e89e10fb16111f7184bd0a6")})
{ "_id" : ObjectId("5e89e10fb16111f7184bd0a6"), "name" : "Mike", "species" : "Hamster" }

1.6 - Use o find para trazer todos os Hamsters
> db.getCollection("pets").find({"species": "Hamster"})
{ "_id" : ObjectId("5e89e10fb16111f7184bd0a6"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5e89e832b16111f7184bd0ac"), "name" : "Frodo", "species" : "Hamster" }


1.7 - Use o find para listar todos os pets com nome Mike
> db.getCollection("pets").find({"name": "Mike"})
{ "_id" : ObjectId("5e89e10fb16111f7184bd0a6"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5e89e10fb16111f7184bd0a9"), "name" : "Mike", "species" : "Cachorro" }


1.8 - Liste apenas o documento que é um Cachorro chamado Mike
> db.getCollection("pets").findOne({"$and" : [{"name": "Mike"},{"species": "Cachorro"}]})
{
	"_id" : ObjectId("5e89e10fb16111f7184bd0a9"),
	"name" : "Mike",
	"species" : "Cachorro"
}


2.1 - Liste/Conte todas as pessoas que tem exatamente 99 anos.
> db.getCollection("italians").find({"age":99})
> db.getCollection("italians").find({"age":99}).count()
0

2.2 - Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos)
> db.getCollection("italians").find({"age":{"$gte" : 65}}).count()
1891


2.3 - Identifique todos os jovens (pessoas entre 12 a 18 anos).
>db.getCollection("italians").find({"age":{"$gte" : 12,"$lte" : 18 }}).count()
859
> db.getCollection("italians").find({"age":{"$gte" : 12,"$lte" : 18 }},{"firstname":1,"surname":1,"age":1,"_id":0}).limit(5)
{ "firstname" : "Gianluca", "surname" : "Leone", "age" : 14 }
{ "firstname" : "Michele", "surname" : "Silvestri", "age" : 18 }
{ "firstname" : "Monica", "surname" : "Pellegrino", "age" : 13 }
{ "firstname" : "Lucia", "surname" : "Marini", "age" : 13 }
{ "firstname" : "Simona", "surname" : "Fiore", "age" : 14 }
...

2.4 - Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois
>db.getCollection("italians").find({"cat" : {"$exists" : true}}).count()
6039
>db.getCollection("italians").find({"dog" : {"$exists" : true}}).count()
3854
>db.getCollection("italians").find({"$and" : [{"dog" : null},{"cat" : null}]}).count()
2399

2.5 - Liste/Conte todas as pessoas acima de 60 anos que tenham gato
> db.getCollection("italians").find({"$and" : [{"age":{"$gte" : 60}},{"cat" : {"$exists" : true}}]}).count()
1506
> db.getCollection("italians").find({"$and" : [{"age":{"$gte" : 60}},{"cat" : {"$exists" : true}}]},{"firstname":1,"surname":1,"age":1,"cat":1,"_id":0}).limit(5)
{ "firstname" : "Lorenzo", "surname" : "Ferrara", "age" : 79, "cat" : { "name" : "Marco", "age" : 9 } }
{ "firstname" : "Raffaele", "surname" : "Benedetti", "age" : 74, "cat" : { "name" : "Enrico", "age" : 3 } }
{ "firstname" : "Manuela", "surname" : "Bianco", "age" : 76, "cat" : { "name" : "Anna", "age" : 8 } }
{ "firstname" : "Matteo", "surname" : "De Angelis", "age" : 72, "cat" : { "name" : "Federica", "age" : 7 } }
{ "firstname" : "Maria", "surname" : "Santoro", "age" : 60, "cat" : { "name" : "Monica", "age" : 16 } }

2.6 - Liste/Conte todos os jovens com cachorro
> db.getCollection("italians").find({"$and" : [{"age":{"$gte" :12, "$lte" : 18}},{"dog" : {"$exists" : true}}]}).count()
322
> db.getCollection("italians").find({"$and" : [{"age":{"$gte" :12, "$lte" : 18}},{"dog" : {"$exists" : true}}]},{"firstname":1,"surname":1,"age":1,"dog":1,"_id":0}).limit(5)
{ "firstname" : "Michele", "surname" : "Silvestri", "age" : 18, "dog" : { "name" : "Pasquale", "age" : 6 } }
{ "firstname" : "Monica", "surname" : "Pellegrino", "age" : 13, "dog" : { "name" : "Teresa", "age" : 16 } }
{ "firstname" : "Lucia", "surname" : "Marini", "age" : 13, "dog" : { "name" : "Alex", "age" : 6 } }
{ "firstname" : "Simona", "surname" : "Fiore", "age" : 14, "dog" : { "name" : "Alessandra", "age" : 3 } }
{ "firstname" : "Claudio", "surname" : "Giordano", "age" : 15, "dog" : { "name" : "Carlo", "age" : 9 } }
...

2.7 - Utilizando o $where, liste todas as pessoas que tem gato e cachorro
???

2.8 - Liste todas as pessoas mais novas que seus respectivos gatos.
> db.italians.find( { $and: [ { cat: {$exists: true }}, { $where: "this.age < this.cat.age"}]}).count()
641
> db.getCollection("italians").find({ $and: [ { cat: {$exists: true }}, { $where: "this.age < this.cat.age"}]},{"firstname":1,"surname":1,"age":1,"cat":1,"_id":0}).limit(5)
{ "firstname" : "Alessio", "surname" : "Valentini", "age" : 9, "cat" : { "name" : "Lorenzo", "age" : 13 } }
{ "firstname" : "Eleonora", "surname" : "Caputo", "age" : 1, "cat" : { "name" : "Manuela", "age" : 10 } }
{ "firstname" : "Michele", "surname" : "Pellegrini", "age" : 5, "cat" : { "name" : "Veronica", "age" : 10 } }
{ "firstname" : "Luigi", "surname" : "Battaglia", "age" : 12, "cat" : { "name" : "Eleonora", "age" : 14 } }
{ "firstname" : "Patrizia", "surname" : "Russo", "age" : 2, "cat" : { "name" : "Sara", "age" : 10 } }
...


2.9 - Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro)
> db.italians.find( { "$or" : [{$and: [ { cat: {$exists: true }}, { $where: "this.firstname == this.cat.name"}]}, {$and: [ { dog: {$exists: true }}, { $where: "this.firstname == this.dog.name"}]}]}).count()
89
> db.getCollection("italians").find({ "$or" : [{$and: [ { cat: {$exists: true }}, { $where: "this.firstname == this.cat.name"}]}, {$and: [ { dog: {$exists: true }}, { $where: "this.firstname == this.dog.name"}]}]},{"firstname":1,"surname":1,"age":1,"cat":1,"dog":1,"_id":0}).limit(5)
{ "firstname" : "Fabrizio", "surname" : "D’Amico", "age" : 30, "cat" : { "name" : "Antonella", "age" : 6 }, "dog" : { "name" : "Fabrizio", "age" : 10 } }
{ "firstname" : "Giacomo", "surname" : "Greco", "age" : 39, "cat" : { "name" : "Giacomo", "age" : 5 }, "dog" : { "name" : "Teresa", "age" : 0 } }
{ "firstname" : "Claudia", "surname" : "Gentile", "age" : 68, "dog" : { "name" : "Claudia", "age" : 17 } }
{ "firstname" : "Ilaria", "surname" : "Caputo", "age" : 71, "cat" : { "name" : "Ilaria", "age" : 3 } }
{ "firstname" : "Serena", "surname" : "Rizzi", "age" : 49, "cat" : { "name" : "Serena", "age" : 14 }, "dog" : { "name" : "Roberto", "age" : 5 } }
...


2.10 - Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo
> db.getCollection("italians").find({"bloodType": /-/i}).count()
4985
> db.getCollection("italians").find({"bloodType": /-/i},{"firstname":1,"surname":1,"age":1,"bloodType":1,"_id":0}).limit(5)
{ "firstname" : "Alex", "surname" : "Gentile", "age" : 47, "bloodType" : "O-" }
{ "firstname" : "Angelo", "surname" : "Gallo", "age" : 24, "bloodType" : "B-" }
{ "firstname" : "Raffaele", "surname" : "Benedetti", "age" : 74, "bloodType" : "O-" }
{ "firstname" : "Rita", "surname" : "Montanari", "age" : 27, "bloodType" : "O-" }
{ "firstname" : "Daniela", "surname" : "Marino", "age" : 47, "bloodType" : "O-" }
...

2.11 - Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId)
db.getCollection("italians").find({ "$or" : [{ cat: {$exists: true }}, { dog: {$exists: true }}]},{"cat.name":1,"cat.age":1,"dog.name":1,"dog.age":1,"_id":0})
{ "cat" : { "name" : "Valentina", "age" : 4 } }
{ "cat" : { "name" : "Marco", "age" : 9 } }
{ "cat" : { "name" : "Rosa", "age" : 13 } }
{ "cat" : { "name" : "Claudio", "age" : 0 } }
{ "cat" : { "name" : "Enrico", "age" : 3 } }
{ "cat" : { "name" : "Mirko", "age" : 5 } }
{ "cat" : { "name" : "Giorgia", "age" : 6 }, "dog" : { "name" : "Gabiele", "age" : 9 } }
{ "cat" : { "name" : "Alex", "age" : 6 } }
{ "cat" : { "name" : "Antonio", "age" : 12 }, "dog" : { "name" : "Pasquale", "age" : 6 } }
{ "cat" : { "name" : "Domenico", "age" : 7 }, "dog" : { "name" : "Teresa", "age" : 16 } }
{ "cat" : { "name" : "Anna", "age" : 8 } }
{ "cat" : { "name" : "Andrea", "age" : 1 } }
{ "cat" : { "name" : "Federica", "age" : 7 }, "dog" : { "name" : "Alessio", "age" : 0 } }
{ "dog" : { "name" : "Davide", "age" : 4 } }
{ "cat" : { "name" : "Raffaele", "age" : 2 }, "dog" : { "name" : "Gabiele", "age" : 8 } }
{ "cat" : { "name" : "Rita", "age" : 2 } }
{ "cat" : { "name" : "Alessandro", "age" : 14 }, "dog" : { "name" : "Elisabetta", "age" : 6 } }
{ "cat" : { "name" : "Sabrina", "age" : 12 } }
{ "cat" : { "name" : "Monica", "age" : 16 } }
{ "cat" : { "name" : "Gianni", "age" : 17 } }
...


2.12 - Quais são as 5 pessoas mais velhas com sobrenome Rossi?
> db.getCollection("italians").find({ "surname": "Rossi" },{"firstname":1,"surname":1,"age":1}).sort({"age" :-1}).limit(5)
{ "_id" : ObjectId("5e88ccaa383ca8677b1f321f"), "firstname" : "Domenico", "surname" : "Rossi", "age" : 79 }
{ "_id" : ObjectId("5e88ccac383ca8677b1f3beb"), "firstname" : "Teresa", "surname" : "Rossi", "age" : 77 }
{ "_id" : ObjectId("5e88ccaa383ca8677b1f328a"), "firstname" : "Monica", "surname" : "Rossi", "age" : 76 }
{ "_id" : ObjectId("5e88ccac383ca8677b1f3da1"), "firstname" : "Claudia", "surname" : "Rossi", "age" : 76 }
{ "_id" : ObjectId("5e88ccaa383ca8677b1f3180"), "firstname" : "Ilaria", "surname" : "Rossi", "age" : 75 }


2.13 - Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano
> pessoa = { 
...     "firstname" : "Charles", 
...     "surname" : "Bambineti", 
...     "username" : "user999", 
...     "age" : 43.0, 
...     "email" : "charles@furb.br", 
...     "bloodType" : "B+", 
...     "id_num" : "946860259015", 
...     "registerDate" : ISODate("2020-03-19T10:49:02.553+0000"), 
...     "ticketNumber" : 9999.0, 
...     "jobs" : [
...         "Gestão de TI"
...     ], 
...     "favFruits" : [
...         "Banana"
...     ], 
...     "movies" : [
...         {
...             "title" : "À Espera de um Milagre (1999)", 
...             "rating" : 0.2
...         }, 
...         {
...             "title" : "Clube da Luta (1999)", 
...             "rating" : 1.06
...         }
...     ], 
...     "Lion" : {
...         "name" : "Alex", 
...         "age" : 4.0
...     }
... }
{
	"firstname" : "Charles",
	"surname" : "Bambineti",
	"username" : "user999",
	"age" : 43,
	"email" : "charles@furb.br",
	"bloodType" : "B+",
	"id_num" : "946860259015",
	"registerDate" : ISODate("2020-03-19T10:49:02.553Z"),
	"ticketNumber" : 9999,
	"jobs" : [
		"Gestão de TI"
	],
	"favFruits" : [
		"Banana"
	],
	"movies" : [
		{
			"title" : "À Espera de um Milagre (1999)",
			"rating" : 0.2
		},
		{
			"title" : "Clube da Luta (1999)",
			"rating" : 1.06
		}
	],
	"Lion" : {
		"name" : "Alex",
		"age" : 4
	}
}
> 
> db.italians.insert(pessoa)
WriteResult({ "nInserted" : 1 })
 

2.14 - Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.
> db.getCollection("italians").remove({"_id": ObjectId("5e93ae7334123205d832ae78")})
WriteResult({ "nRemoved" : 1 })


2.15 - Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1.
> db.italians.update({}, {"$inc": {"age": 1, "cat.age":1, "dog.age":1 } }, {multi: true});
WriteResult({ "nMatched" : 10000, "nUpserted" : 0, "nModified" : 10000 })


2.16 - O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos
>db.italians.remove({"$and" : [{"age":{"$gte" : 66}},{"cat" : {"$exists" : true}}]}, {multi: true}) 
WriteResult({ "nRemoved" : 2025 })

2.17 - Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.
>  db.italians.aggregate([
...      {'$match':{mother:{$exists:1}}},
...      {'$match':{ $or: [{cat:{$exists:1}}, {dog:{$exists:1}}]}}, 
...      {'$project':{
...          "firstname":1,
...          "mother":1,
...          "cat":1,
...          "dog":1,      
...          "isEqual":{"$cmp":["$firstname","$mother.firstname"]}
...      }},
...      {'$match':{"isEqual":0}}
...  ])
{ "_id" : ObjectId("5e88cca7383ca8677b1f23d8"), "firstname" : "Domenico", "mother" : { "firstname" : "Domenico", "surname" : "D’Angelo", "age" : 76 }, "dog" : { "name" : "Rita", "age" : 7 }, "cat" : { "age" : 2 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e88cca7383ca8677b1f2701"), "firstname" : "Patrizia", "mother" : { "firstname" : "Patrizia", "surname" : "Fontana", "age" : 45 }, "cat" : { "name" : "Michele", "age" : 13 }, "dog" : { "age" : 5 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e88ccaa383ca8677b1f31a6"), "firstname" : "Elisabetta", "mother" : { "firstname" : "Elisabetta", "surname" : "Vitali", "age" : 49 }, "cat" : { "name" : "Sabrina", "age" : 4 }, "dog" : { "age" : 5 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e88ccaa383ca8677b1f3496"), "firstname" : "Daniela", "mother" : { "firstname" : "Daniela", "surname" : "Martini", "age" : 30 }, "cat" : { "name" : "Chiara", "age" : 4 }, "dog" : { "name" : "Silvia", "age" : 10 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e88ccab383ca8677b1f3639"), "firstname" : "Ilaria", "mother" : { "firstname" : "Ilaria", "surname" : "De Angelis", "age" : 39 }, "dog" : { "name" : "Sergio", "age" : 20 }, "cat" : { "age" : 2 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e88ccac383ca8677b1f3c29"), "firstname" : "Rosa", "mother" : { "firstname" : "Rosa", "surname" : "Guerra", "age" : 66 }, "dog" : { "age" : 5 }, "cat" : { "age" : 2 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e88ccac383ca8677b1f3e81"), "firstname" : "Riccardo", "mother" : { "firstname" : "Riccardo", "surname" : "De Luca", "age" : 57 }, "cat" : { "name" : "Elena", "age" : 8 }, "dog" : { "name" : "Daniele", "age" : 14 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e88ccad383ca8677b1f3f36"), "firstname" : "Luca", "mother" : { "firstname" : "Luca", "surname" : "Romano", "age" : 71 }, "cat" : { "name" : "Emanuela", "age" : 9 }, "dog" : { "age" : 5 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e88ccae383ca8677b1f465b"), "firstname" : "Silvia", "mother" : { "firstname" : "Silvia", "surname" : "Piras", "age" : 42 }, "cat" : { "name" : "Enzo ", "age" : 9 }, "dog" : { "name" : "Giovanni", "age" : 22 }, "isEqual" : 0 }


2.18 -  Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome
> db.getCollection("italians").aggregate([  { $group : { _id : "$firstname" } } ])
{ "_id" : "Vincenzo" }
{ "_id" : "Silvia" }
{ "_id" : "Rosa" }
{ "_id" : "Giovanni" }
{ "_id" : "Lucia" }
{ "_id" : "Cristina" }
{ "_id" : "Alessandro" }
{ "_id" : "Lorenzo" }
{ "_id" : "Tiziana" }
{ "_id" : "Patrizia" }
{ "_id" : "Claudio" }
{ "_id" : "Sonia" }
{ "_id" : "Alberto" }
{ "_id" : "Laura" }
{ "_id" : "Simona" }
{ "_id" : "Sara" }
{ "_id" : "Gianni" }
{ "_id" : "Pasquale" }
{ "_id" : "Antonio" }
{ "_id" : "Andrea" }


2.19 - Agora faça a mesma lista do item acima, considerando nome completo.
> db.getCollection("italians").aggregate([  { $group : { _id : { firstname:"$firstname", surname:"$surname"} }} ])
{ "_id" : { "firstname" : "Sabrina", "surname" : "Barone" } }
{ "_id" : { "firstname" : "Sabrina", "surname" : "Guerra" } }
{ "_id" : { "firstname" : "Alessio", "surname" : "Martinelli" } }
{ "_id" : { "firstname" : "Domenico", "surname" : "Pellegrino" } }
{ "_id" : { "firstname" : "Laura", "surname" : "Giuliani" } }
{ "_id" : { "firstname" : "Stefano", "surname" : "Villa" } }
{ "_id" : { "firstname" : "Massimo", "surname" : "Ferraro" } }
{ "_id" : { "firstname" : "Elisabetta", "surname" : "Villa" } }
{ "_id" : { "firstname" : "Claudia", "surname" : "Mariani" } }
{ "_id" : { "firstname" : "Vincenzo", "surname" : "Costa" } }
{ "_id" : { "firstname" : "Sabrina", "surname" : "Martini" } }
{ "_id" : { "firstname" : "Elisa", "surname" : "Ferraro" } }
{ "_id" : { "firstname" : "Cristian", "surname" : "Lombardo" } }
{ "_id" : { "firstname" : "Giovanni", "surname" : "De Luca" } }
{ "_id" : { "firstname" : "Tiziana", "surname" : "Neri" } }
{ "_id" : { "firstname" : "Alessio", "surname" : "Messina" } }
{ "_id" : { "firstname" : "Roberto", "surname" : "Sartori" } }
{ "_id" : { "firstname" : "Cristina", "surname" : "Rinaldi" } }
{ "_id" : { "firstname" : "Cristina", "surname" : "Santoro" } }
{ "_id" : { "firstname" : "Simone", "surname" : "Martino" } }


2.20 - Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.
>  db.italians.aggregate([
...      {'$match':{"age":{"$gte" : 20,"$lte" : 60 }}},
...      {'$match':{favFruits : {$all : ["Maçã", "Banana"]}}},
...      {'$match':{ $or: [{cat:{$exists:1}}, {dog:{$exists:1}}]}}, 
...      {'$project':{
...          "firstname":1,
...          "favFruits":1,
...          "age":1,
...          "cat":1,
...          "dog":1,      
...          
...      }}
...  ])
{ "_id" : ObjectId("5e88cca6383ca8677b1f222a"), "firstname" : "Daniela", "age" : 49, "favFruits" : [ "Kiwi", "Banana", "Maçã" ], "cat" : { "name" : "Giorgia", "age" : 8 }, "dog" : { "name" : "Gabiele", "age" : 14 } }
{ "_id" : ObjectId("5e88cca6383ca8677b1f223d"), "firstname" : "Fabrizio", "age" : 38, "favFruits" : [ "Melancia", "Banana", "Maçã" ], "dog" : { "age" : 5 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca6383ca8677b1f2303"), "firstname" : "Roberta", "age" : 48, "favFruits" : [ "Banana", "Maçã" ], "dog" : { "age" : 5 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca6383ca8677b1f2316"), "firstname" : "Nicola", "age" : 24, "favFruits" : [ "Kiwi", "Banana", "Maçã" ], "cat" : { "name" : "Simona", "age" : 15 }, "dog" : { "age" : 5 } }
{ "_id" : ObjectId("5e88cca6383ca8677b1f2344"), "firstname" : "Cinzia", "age" : 34, "favFruits" : [ "Mamão", "Banana", "Maçã" ], "cat" : { "name" : "Mauro", "age" : 6 }, "dog" : { "age" : 5 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f236e"), "firstname" : "Giuseppe", "age" : 57, "favFruits" : [ "Uva", "Maçã", "Banana" ], "dog" : { "age" : 5 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f23a8"), "firstname" : "Michela", "age" : 46, "favFruits" : [ "Uva", "Banana", "Maçã" ], "cat" : { "name" : "Raffaele", "age" : 10 }, "dog" : { "age" : 5 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f23b5"), "firstname" : "Maurizio", "age" : 48, "favFruits" : [ "Banana", "Maçã" ], "dog" : { "name" : "Simone", "age" : 13 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f243d"), "firstname" : "Giuseppe", "age" : 28, "favFruits" : [ "Maçã", "Banana" ], "dog" : { "age" : 5 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f249a"), "firstname" : "Enzo ", "age" : 26, "favFruits" : [ "Banana", "Maçã" ], "dog" : { "name" : "Elisabetta", "age" : 5 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f24e1"), "firstname" : "Tiziana", "age" : 41, "favFruits" : [ "Banana", "Maçã" ], "dog" : { "name" : "Lucia", "age" : 21 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f2509"), "firstname" : "Michela", "age" : 28, "favFruits" : [ "Maçã", "Banana" ], "cat" : { "name" : "Filipo", "age" : 15 }, "dog" : { "age" : 5 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f250e"), "firstname" : "Eleonora", "age" : 60, "favFruits" : [ "Laranja", "Maçã", "Banana" ], "cat" : { "name" : "Raffaele", "age" : 5 }, "dog" : { "age" : 5 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f252c"), "firstname" : "Angelo", "age" : 24, "favFruits" : [ "Maçã", "Mamão", "Banana" ], "cat" : { "name" : "Elisa", "age" : 17 }, "dog" : { "name" : "Enrico", "age" : 22 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f254a"), "firstname" : "Alberto", "age" : 40, "favFruits" : [ "Maçã", "Banana", "Goiaba" ], "dog" : { "age" : 5 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f25ab"), "firstname" : "Antonio", "age" : 59, "favFruits" : [ "Banana", "Maçã", "Mamão" ], "cat" : { "name" : "Salvatore", "age" : 8 }, "dog" : { "age" : 5 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f25ac"), "firstname" : "Andrea", "age" : 49, "favFruits" : [ "Banana", "Maçã", "Tangerina" ], "dog" : { "name" : "Cristian", "age" : 8 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f25cf"), "firstname" : "Luigi", "age" : 39, "favFruits" : [ "Banana", "Maçã", "Melancia" ], "cat" : { "name" : "Federica", "age" : 8 }, "dog" : { "name" : "Rita", "age" : 13 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f2689"), "firstname" : "Simone", "age" : 28, "favFruits" : [ "Banana", "Maçã" ], "dog" : { "age" : 5 }, "cat" : { "age" : 2 } }
{ "_id" : ObjectId("5e88cca7383ca8677b1f26cf"), "firstname" : "Alessandra", "age" : 51, "favFruits" : [ "Banana", "Maçã", "Mamão" ], "cat" : { "name" : "Sergio", "age" : 2 }, "dog" : { "age" : 5 } }


3.1  Liste as ações com profit acima de 0.5 (limite a 10 o resultado)
> db.getCollection("stocks").find({"Profit Margin":{"$gte" : 0.5}},{"Ticker":1,"Company":1,"Profit Margin":1}).limit(10)
{ "_id" : ObjectId("52853800bb1177ca391c180f"), "Ticker" : "AB", "Profit Margin" : 0.896, "Company" : "AllianceBernstein Holding L.P." }
{ "_id" : ObjectId("52853801bb1177ca391c1895"), "Ticker" : "AGNC", "Profit Margin" : 0.972, "Company" : "American Capital Agency Corp." }
{ "_id" : ObjectId("52853801bb1177ca391c1950"), "Ticker" : "ARCC", "Profit Margin" : 0.654, "Company" : "Ares Capital Corporation" }
{ "_id" : ObjectId("52853801bb1177ca391c195a"), "Ticker" : "ARI", "Profit Margin" : 0.576, "Company" : "Apollo Commercial Real Estate Finance, Inc." }
{ "_id" : ObjectId("52853801bb1177ca391c1968"), "Ticker" : "ARR", "Profit Margin" : 0.848, "Company" : "ARMOUR Residential REIT, Inc." }
{ "_id" : ObjectId("52853801bb1177ca391c1998"), "Ticker" : "ATHL", "Profit Margin" : 0.732, "Company" : "Athlon Energy Inc." }
{ "_id" : ObjectId("52853801bb1177ca391c19f6"), "Ticker" : "AYR", "Profit Margin" : 0.548, "Company" : "Aircastle LTD" }
{ "_id" : ObjectId("52853801bb1177ca391c1a97"), "Ticker" : "BK", "Profit Margin" : 0.63, "Company" : "The Bank of New York Mellon Corporation" }
{ "_id" : ObjectId("52853801bb1177ca391c1abd"), "Ticker" : "BLX", "Profit Margin" : 0.588, "Company" : "Banco Latinoamericano de Comercio Exterior, S.A" }
{ "_id" : ObjectId("52853801bb1177ca391c1af0"), "Ticker" : "BPO", "Profit Margin" : 0.503, "Company" : "Brookfield Properties Corporation" 

3.2 Liste as ações com perdas (limite a 10 novamente)
> db.getCollection("stocks").find({"Profit Margin":{"$lte" : 0}},{"Ticker":1,"Company":1,"Profit Margin":1}).limit(10)
{ "_id" : ObjectId("52853800bb1177ca391c1806"), "Ticker" : "AAOI", "Profit Margin" : -0.023, "Company" : "Applied Optoelectronics, Inc." }
{ "_id" : ObjectId("52853800bb1177ca391c180c"), "Ticker" : "AAV", "Profit Margin" : -0.232, "Company" : "Advantage Oil & Gas Ltd." }
{ "_id" : ObjectId("52853800bb1177ca391c1815"), "Ticker" : "ABCD", "Profit Margin" : -0.645, "Company" : "Cambium Learning Group, Inc." }
{ "_id" : ObjectId("52853800bb1177ca391c1817"), "Ticker" : "ABFS", "Profit Margin" : -0.005, "Company" : "Arkansas Best Corporation" }
{ "_id" : ObjectId("52853800bb1177ca391c181b"), "Ticker" : "ABMC", "Profit Margin" : -0.0966, "Company" : "American Bio Medica Corp." }
{ "_id" : ObjectId("52853800bb1177ca391c1821"), "Ticker" : "ABX", "Profit Margin" : -0.769, "Company" : "Barrick Gold Corporation" }
{ "_id" : ObjectId("52853800bb1177ca391c182b"), "Ticker" : "ACFC", "Profit Margin" : -0.18, "Company" : "Atlantic Coast Financial Corporation" }
{ "_id" : ObjectId("52853800bb1177ca391c182f"), "Ticker" : "ACH", "Profit Margin" : -0.051, "Company" : "Aluminum Corporation Of China Limited" }
{ "_id" : ObjectId("52853800bb1177ca391c1832"), "Ticker" : "ACI", "Profit Margin" : -0.173, "Company" : "Arch Coal Inc." }
{ "_id" : ObjectId("52853800bb1177ca391c1835"), "Ticker" : "ACLS", "Profit Margin" : -0.179, "Company" : "Axcelis Technologies Inc." }


3.3 - Liste as 10 ações mais rentáveis 
> db.getCollection("stocks").find({},{"Ticker":1,"Company":1,"Profit Margin":1}).sort({"Profit Margin":-1}).limit(10)
{ "_id" : ObjectId("52853801bb1177ca391c1af3"), "Ticker" : "BPT", "Profit Margin" : 0.994, "Company" : "BP Prudhoe Bay Royalty Trust" }
{ "_id" : ObjectId("52853802bb1177ca391c1b69"), "Ticker" : "CACB", "Profit Margin" : 0.994, "Company" : "Cascade Bancorp" }
{ "_id" : ObjectId("5285380bbb1177ca391c2c3c"), "Ticker" : "ROYT", "Profit Margin" : 0.99, "Company" : "Pacific Coast Oil Trust" }
{ "_id" : ObjectId("52853808bb1177ca391c281b"), "Ticker" : "NDRO", "Profit Margin" : 0.986, "Company" : "Enduro Royalty Trust" }
{ "_id" : ObjectId("5285380fbb1177ca391c318e"), "Ticker" : "WHZ", "Profit Margin" : 0.982, "Company" : "Whiting USA Trust II" }
{ "_id" : ObjectId("52853808bb1177ca391c27bd"), "Ticker" : "MVO", "Profit Margin" : 0.976, "Company" : "MV Oil Trust" }
{ "_id" : ObjectId("52853801bb1177ca391c1895"), "Ticker" : "AGNC", "Profit Margin" : 0.972, "Company" : "American Capital Agency Corp." }
{ "_id" : ObjectId("5285380ebb1177ca391c3101"), "Ticker" : "VOC", "Profit Margin" : 0.971, "Company" : "VOC Energy Trust" }
{ "_id" : ObjectId("52853807bb1177ca391c279a"), "Ticker" : "MTR", "Profit Margin" : 0.97, "Company" : "Mesa Royalty Trust" }
{ "_id" : ObjectId("52853809bb1177ca391c2946"), "Ticker" : "OLP", "Profit Margin" : 0.97, "Company" : "One Liberty Properties Inc." }


3.4 - Qual foi o setor mais rentável?
> db.getCollection("stocks").aggregate([{$group: {_id : "$Industry", AVGProfit: {$avg: "$Profit Margin"}}},{$sort:{"AVGProfit":-1}},{$limit: 1}])
{ "_id" : "Diversified Investments", "AVGProfit" : 0.48268 }


3.5 - Ordene as ações pelo profit e usando um cursor, liste as ações.
> var cursor = db.getCollection("stocks").find({},{"Ticker":1,"Company":1,"Profit Margin":1}).sort({"Profit Margin":-1}).limit(5)
> 
> cursor.forEach(printjson);
{
	"_id" : ObjectId("52853801bb1177ca391c1af3"),
	"Ticker" : "BPT",
	"Profit Margin" : 0.994,
	"Company" : "BP Prudhoe Bay Royalty Trust"
}
{
	"_id" : ObjectId("52853802bb1177ca391c1b69"),
	"Ticker" : "CACB",
	"Profit Margin" : 0.994,
	"Company" : "Cascade Bancorp"
}
{
	"_id" : ObjectId("5285380bbb1177ca391c2c3c"),
	"Ticker" : "ROYT",
	"Profit Margin" : 0.99,
	"Company" : "Pacific Coast Oil Trust"
}
{
	"_id" : ObjectId("52853808bb1177ca391c281b"),
	"Ticker" : "NDRO",
	"Profit Margin" : 0.986,
	"Company" : "Enduro Royalty Trust"
}
{
	"_id" : ObjectId("5285380fbb1177ca391c318e"),
	"Ticker" : "WHZ",
	"Profit Margin" : 0.982,
	"Company" : "Whiting USA Trust II"
}


3.6 - Renomeie o campo “Profit Margin” para apenas “profit”.
>db.stocks.update({}, {$rename:{"Profit Margin":"profit"}}, false, true);
WriteResult({ "nMatched" : 6756, "nUpserted" : 0, "nModified" : 4302 })

3.7 - Agora liste apenas a empresa e seu respectivo resultado
> db.getCollection("stocks").find({},{"_id":0,"Company":1,"profit":1}).sort({"profit":-1}).limit(5)
{ "Company" : "BP Prudhoe Bay Royalty Trust", "profit" : 0.994 }
{ "Company" : "Cascade Bancorp", "profit" : 0.994 }
{ "Company" : "Pacific Coast Oil Trust", "profit" : 0.99 }
{ "Company" : "Enduro Royalty Trust", "profit" : 0.986 }
{ "Company" : "Whiting USA Trust II", "profit" : 0.982 }

3.8 - Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?
??

3.9 - Liste as ações agrupadas por setor.








