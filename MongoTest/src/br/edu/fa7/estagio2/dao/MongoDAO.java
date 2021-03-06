package br.edu.fa7.estagio2.dao;

import java.util.ArrayList;
import java.util.List;

import org.bson.Document;

import br.edu.fa7.estagio2.models.Client;

import com.mongodb.Block;
import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoDatabase;

public class MongoDAO {
	private MongoClient mongoClient;
	private MongoDatabase dataBase;

	public MongoDAO(String DB) {
		mongoClient = new MongoClient();
		dataBase = mongoClient.getDatabase(DB);
	}

	public void insert(Client client) {
		Document document = new Document("name", client.getName()).append(
				"phone", client.getPhone()).append("age", client.getAge());

		dataBase.getCollection("client").insertOne(document);
	}

	public List<Client> list() {
		final List<Client> clients = new ArrayList();
		FindIterable<Document> it = dataBase.getCollection("client").find();

		it.forEach(new Block<Document>() {
			@Override
			public void apply(Document doc) {
				Client c = new Client(doc.getString("name"), doc
						.getString("phone"), doc.getInteger("age"));
				clients.add(c);
			}
		});

		return clients;
	}

	public static MongoDAO singletonDAO() {
		return new MongoDAO("aff");
	}

	public void edit(Client client) {
		//dataBase.getCollection("client").updateOne(new Document("name", client.getName()), );
	}

	public void delete(Client client) {
		dataBase.getCollection("client").deleteOne(new Document("name", client.getName()));
	}
}
