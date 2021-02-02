package com.src.research.echanellingservice.model;

import java.sql.Date;
import java.sql.Time;

public class Appointment_slot {
	private int id;
	private int doctorId;
	private int hospitalId;
	private Date date;
	private double charge;
	private int totalSeats;
	private int availableSeats;
	private Time startTime;
	
	public Appointment_slot() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Appointment_slot(int id, int doctorId, int hospitalId, Date date, double charge, int totalSeats,
			int availableSeats, Time startTime) {
		super();
		this.id = id;
		this.doctorId = doctorId;
		this.hospitalId = hospitalId;
		this.date = date;
		this.charge = charge;
		this.totalSeats = totalSeats;
		this.availableSeats = availableSeats;
		this.startTime = startTime;
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

	public Date getDate() {
		return date;
	}

	public void setDate(Date date) {
		this.date = date;
	}

	public double getCharge() {
		return charge;
	}

	public void setCharge(double charge) {
		this.charge = charge;
	}

	public int getTotalSeats() {
		return totalSeats;
	}

	public void setTotalSeats(int totalSeats) {
		this.totalSeats = totalSeats;
	}

	public int getAvailableSeats() {
		return availableSeats;
	}

	public void setAvailableSeats(int availableSeats) {
		this.availableSeats = availableSeats;
	}

	public Time getStartTime() {
		return startTime;
	}

	public void setStartTime(Time startTime) {
		this.startTime = startTime;
	}

	@Override
	public String toString() {
		return "Appointment_slot [id=" + id + ", doctorId=" + doctorId + ", hospitalId=" + hospitalId + ", date=" + date
				+ ", charge=" + charge + ", totalSeats=" + totalSeats + ", availableSeats=" + availableSeats
				+ ", startTime=" + startTime + "]";
	}
}
