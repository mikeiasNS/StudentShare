package br.edu.fa7.e2.SS;

import java.util.List;

import javax.faces.bean.ManagedBean;

@ManagedBean
public class TestBean {
	
	private ProfileDAO DAO = new ProfileDAO();
	
	public List<String> getTopMatchs(String registry) {
		List<String> list = DAO.getTopMatchs("1321389");
		
		return list;
	}
	
}
