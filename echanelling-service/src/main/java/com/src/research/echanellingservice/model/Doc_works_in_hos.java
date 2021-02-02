package com.src.research.echanellingservice.model;

public class Doc_works_in_hos {

	private int id;
	private int doctorId;
	private int hospitalId;
	
	public Doc_works_in_hos() {
		super();
	}

	public Doc_works_in_hos(int id, int doctorId, int hospitalId) {
		super();
		this.id = id;
		this.doctorId = doctorId;
		this.hospitalId = hospitalId;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getDoctorId() {
		return doctorId;
	}

	public void setDoctorId(int doctorId) {
		this.doctorId = doctorId;
	}

	public int getHospitalId() {
		return hospitalId;
	}

	public void setHospitalId(int hospitalId) {
		this.hospitalId = hospitalId;
	}

	@Override
	public String toString() {
		return "DocWorkInHos [id=" + id + ", doctorId=" + doctorId + ", hospitalId=" + hospitalId + "]";
	}
	
}