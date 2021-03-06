package br.edu.fa7.estagio2.beans;

import java.util.List;

import javax.faces.bean.ManagedBean;

import br.edu.fa7.estagio2.dao.MongoDAO;
import br.edu.fa7.estagio2.models.Client;

@ManagedBean
public class ClientBean {
	private MongoDAO DAO = MongoDAO.singletonDAO();
	private Client client = new Client();
	
	public String insert(){
		DAO.insert(client);
		return "clients";
	}
	
	public List<Client> list(){
		return DAO.list();
	}
	
	public void edit(Client client) {
		DAO.edit(client);
	}
	
	public void delete(Client client){
		DAO.delete(client);
	}
	
	public Client getClient() {
		return client;
	}
	
	public void setClient(Client client) {
		this.client = client;
	}
}
