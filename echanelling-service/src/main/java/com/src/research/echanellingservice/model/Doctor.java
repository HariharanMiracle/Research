package com.src.research.echanellingservice.model;

public class Doctor {
	
	private int id;
	private String regNo;
	private String name;
	private String specialization;
	private String contactNo;
	
	public Doctor() {
		super();
	}
	
	public Doctor(int id, String regNo, String name, String specialization, String contactNo) {
		super();
		this.id = id;
		this.regNo = regNo;
		this.name = name;
		this.specialization = specialization;
		this.contactNo = contactNo;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getRegNo() {
		return regNo;
	}

	public void setRegNo(String regNo) {
		this.regNo = regNo;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSpecialization() {
		return specialization;
	}

	public void setSpecialization(String specialization) {
		this.specialization = specialization;
	}

	public String getContactNo() {
		return contactNo;
	}

	public void setContactNo(String contactNo) {
		this.contactNo = contactNo;
	}

	@Override
	public String toString() {
		return "Doctor [id=" + id + ", regNo=" + regNo + ", name=" + name + ", specialization=" + specialization
				+ ", contactNo=" + contactNo + "]";
	}
	
}
