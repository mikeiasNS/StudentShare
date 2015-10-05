package br.edu.fa7.studentshare.models;

public class Student {
	private String code;
	private double match;
	private long matricula;

	public Student(String code, double match, long matricula) {
		super();
		this.code = code;
		this.match = match;
		this.matricula = matricula;
	}

	public String getCode() {
		return code;
	}

	public double getMatch() {
		return match;
	}

	public long getMatricula() {
		return matricula;
	}

	public void setCode(String code) {
		this.code = code;
	}

	public void setMatch(double match) {
		this.match = match;
	}

	public void setMatricula(long matricula) {
		this.matricula = matricula;
	}
}