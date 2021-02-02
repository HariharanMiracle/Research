package com.src.research.echanellingservice.model;

public class Appointment {
	
	private int id;
	private String name;
	private String nic;
	private String email;
	private String contact;
	private int aSlotId;
	
	public Appointment() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Appointment(int id, String name, String nic, String email, String contact, double payment, int aSlotId) {
		super();
		this.id = id;
		this.name = name;
		this.nic = nic;
		this.email = email;
		this.contact = contact;
		this.aSlotId = aSlotId;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getNic() {
		return nic;
	}

	public void setNic(String nic) {
		this.nic = nic;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getContact() {
		return contact;
	}

	public void setContact(String contact) {
		this.contact = contact;
	}

	public int getaSlotId() {
		return aSlotId;
	}

	public void setaSlotId(int aSlotId) {
		this.aSlotId = aSlotId;
	}

	@Override
	public String toString() {
		return "Appointment [id=" + id + ", name=" + name + ", nic=" + nic + ", email=" + email + ", contact=" + contact
				+ ", aSlotId=" + aSlotId + "]";
	}
	
}
