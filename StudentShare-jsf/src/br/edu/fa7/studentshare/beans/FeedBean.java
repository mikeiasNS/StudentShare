package br.edu.fa7.studentshare.beans;

import java.util.ArrayList;

import javax.faces.bean.ManagedBean;

import br.edu.fa7.studentshare.daos.StudentDAO;
import br.edu.fa7.studentshare.models.Student;

@ManagedBean
public class FeedBean {
	private ArrayList<Student> topfive = new ArrayList<Student>();
	private Student student = new Student("dhghja",4,154646L);

	public Student getStudent() {
		return student;
	}

	public void setStudent(Student student) {
		this.student = student;
	}

	public ArrayList<Student> getTopfive() {
		topfive = StudentDAO.getMatches(student);
		return topfive;
	}

	public void setTopfive(ArrayList<Student> topfive) {
		this.topfive = topfive;
	}
}
