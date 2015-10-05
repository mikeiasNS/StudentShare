package br.edu.fa7.studentshare.daos;

import java.util.ArrayList;

import br.edu.fa7.studentshare.models.Student;

public class StudentDAO {
	
	private static ArrayList<Student> students = new ArrayList<Student>();
	
	static {
		students.add(new Student("xjhlsh", 10, 1310432L));
		students.add(new Student("gfdugfd", 5.5, 132456L));
		students.add(new Student("xjhldff", 3.2, 1450432L));
		}
	
	public static ArrayList<Student> getMatches(Student student){
		
		//pesquisa no banco
		
		return students;
	}
}
