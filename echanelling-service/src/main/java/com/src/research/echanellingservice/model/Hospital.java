package com.src.research.echanellingservice.model;

public class Hospital {

	private int id;
	private String name;
	private String zipcode;
	private String location;
	private String contact;
	private String address;
	
	public Hospital() {
		super();
	}

	public Hospital(int id, String name, String zipcode, String location, String contact, String address) {
		super();
		this.id = id;
		this.name = name;
		this.zipcode = zipcode;
		this.location = location;
		this.contact = contact;
		this.address = address;
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

	public String getZipcode() {
		return zipcode;
	}

	public void setZipcode(String zipcode) {
		this.zipcode = zipcode;
	}

	public String getLocation() {
		return location;
	}

	public void setLocation(String location) {
		this.location = location;
	}

	public String getContact() {
		return contact;
	}

	public void setContactNo(String contact) {
		this.contact = contact;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public void setContact(String contact) {
		this.contact = contact;
	}

	@Override
	public String toString() {
		return "Hospital [id=" + id + ", name=" + name + ", zipcode=" + zipcode + ", location=" + location
				+ ", contact=" + contact + ", address=" + address + "]";
	}
	
}
