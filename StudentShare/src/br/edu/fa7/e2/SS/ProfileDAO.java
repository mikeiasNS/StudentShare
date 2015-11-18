package br.edu.fa7.e2.SS;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

import org.bson.Document;

import com.mongodb.Block;
import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoDatabase;

public class ProfileDAO {
	
	private MongoClient mongoClient = new MongoClient();
	private MongoDatabase mongoDB = mongoClient.getDatabase("studentShareTest");

	public List<String> TestList() {
		
		final List<String> hum = new ArrayList<String>();
		FindIterable<Document> it = mongoDB.getCollection("workData").find(new Document("name", "Mikeias"));
		
		it.forEach(new Block<Document>() {

			@Override
			public void apply(Document doc) {
				ArrayList<String> d = (ArrayList<String>) doc.get("warningSubjects");
				
				for (int i = 0; i < d.size(); i++) {
					hum.add(d.get(i));
				}
			}
			
		});
		
		return hum;
	}
}
