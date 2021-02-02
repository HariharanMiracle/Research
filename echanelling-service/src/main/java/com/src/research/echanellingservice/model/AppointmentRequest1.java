package com.src.research.echanellingservice.model;

public class AppointmentRequest1 {

	private String name;
	private String nic;
	private String email;
	private String contact;
	private int aSlotId;
	private String creditCardNumber;
	private String cvc;
	
	public AppointmentRequest1() {
		super();
		// TODO Auto-generated constructor stub
	}

	public AppointmentRequest1(String name, String nic, String email, String contact, int aSlotId,
			String creditCardNumber, String cvc) {
		super();
		this.name = name;
		this.nic = nic;
		this.email = email;
		this.contact = contact;
		this.aSlotId = aSlotId;
		this.creditCardNumber = creditCardNumber;
		this.cvc = cvc;
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

	public String getCreditCardNumber() {
		return creditCardNumber;
	}

	public void setCreditCardNumber(String creditCardNumber) {
		this.creditCardNumber = creditCardNumber;
	}

	public String getCvc() {
		return cvc;
	}

	public void setCvc(String cvc) {
		this.cvc = cvc;
	}

	@Override
	public String toString() {
		return "AppointmentRequest1 [name=" + name + ", nic=" + nic + ", email=" + email + ", contact=" + contact
				+ ", aSlotId=" + aSlotId + ", creditCardNumber=" + creditCardNumber + ", cvc=" + cvc + "]";
	}
	
}
