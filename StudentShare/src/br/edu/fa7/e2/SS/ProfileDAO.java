package br.edu.fa7.e2.SS;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

import org.apache.commons.lang.StringEscapeUtils;
import org.bson.Document;

import com.mongodb.Block;
import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoDatabase;

public class ProfileDAO {
	
	private MongoClient mongoClient = new MongoClient();
	private MongoDatabase mongoDB = mongoClient.getDatabase("studentShareTest");
	
	public Student getStudent(String registry){
		final Student student = new Student();
		
		FindIterable<Document> workDataIt = mongoDB.getCollection("workData").find(new Document("registry", registry));
		FindIterable<Document> studentIt = mongoDB.getCollection("students").find(new Document("registry", registry));
		
		student.setRegistry(registry);
		
		workDataIt.forEach(new Block<Document>(){

			@Override
			public void apply(Document doc) {
				student.setName( doc.getString("name") );
				
				ArrayList<String> recommendedSubjects = (ArrayList<String>)doc.get("recommendedSubjects");
				ArrayList<String> warningSubjects = (ArrayList<String>)doc.get("warningSubjects");
				ArrayList<String> topMatchs = (ArrayList<String>)doc.get("topMatchs");
				HashMap<String, Double> profile = new HashMap<String, Double>();
				Document docProfile = (Document) doc.get("profile");
				Set<String> profileKeys = docProfile.keySet();
				Iterator<String> profileIt = profileKeys.iterator();
				
				student.setRecommendedSubjects(recommendedSubjects);
				student.setWarningSubjects(warningSubjects);
				student.setTopMatchs(topMatchs);

				while(profileIt.hasNext()){
					String currentProfile = profileIt.next();
					profile.put(currentProfile, docProfile.getDouble(currentProfile));
				}
				
				student.setProfile(profile);				
			}
			
		});
		studentIt.forEach(new Block<Document>() {

			@Override
			public void apply(Document doc) {
				Document docGrades = (Document) doc.get("grades");
				HashMap<String, Double> grades = new HashMap<String, Double>();
				Set<String> subjects = docGrades.keySet();
				
				Iterator<String> subjIt = subjects.iterator();
				
				while(subjIt.hasNext()){
					String currentSubject = subjIt.next();
					Double currentGrade = Double.parseDouble(docGrades.getString(currentSubject).replace(",", "."));
					grades.put(currentSubject, currentGrade);
				}
				
				student.setGrades(grades);
			}
		});
		
		return student;
	}
	
	public boolean login(String registry){
		final List<Boolean> success = new ArrayList<Boolean>(); 
		FindIterable<Document> it = mongoDB.getCollection("students").find(new Document("registry", registry));
		
		it.forEach(new Block<Document>() {

			@Override
			public void apply(Document doc) {
				success.add(true);
				return;
			}
			
		});
		
		success.add(false);
		
		return success.get(0);
	}

	public HashMap<String, Double> getGrades(String registry) {
		final HashMap<String, Double> grades = new HashMap<String, Double>();
		FindIterable<Document> it = mongoDB.getCollection("students").find(new Document("registry", registry));
		
		it.forEach(new Block<Document>() {

			@Override
			public void apply(Document doc) {
				Document d = (Document) doc.get("grades");
				Set<String> subjects = d.keySet();
				
				Iterator<String> subjIt = subjects.iterator();
				
				while(subjIt.hasNext()){
					String currentSubject = subjIt.next();
					grades.put(currentSubject, Double.parseDouble(d.getString(currentSubject).replace(",", ".")));
				}
			}
			
		});
		
		return grades;
	}
}
