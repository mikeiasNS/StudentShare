package br.edu.fa7.e2.SS;

import java.util.ArrayList;
import java.util.List;

import com.mongodb.MongoClient;
import com.mongodb.client.MongoDatabase;

public class ProfileDAO {
	
	private MongoClient mongoClient = new MongoClient();
	private MongoDatabase mongoDB = mongoClient.getDatabase("studentShareTest");

	public List<String> TestList() {
		
		List<String> hum = new ArrayList<String>();
		
		return null;
	}
}