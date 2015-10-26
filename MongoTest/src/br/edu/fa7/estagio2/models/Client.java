package br.edu.fa7.estagio2.models;

public class Client {
	private String name;
	private String phone;
	private int age;
	
	public Client(String name, String phone, int age){
		this.age = age;
		this.phone = phone;
		this.name = name;
	}
	
	public Client(){
		
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
}
