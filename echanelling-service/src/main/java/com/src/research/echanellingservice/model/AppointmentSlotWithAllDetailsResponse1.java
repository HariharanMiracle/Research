package com.src.research.echanellingservice.model;

import java.sql.Date;
import java.sql.Time;

public class AppointmentSlotWithAllDetailsResponse1 {

	private int appointmentSlotId;
	private String doctorName;
	private String hospitalName;
	private Date date;
	private Time time;
	private double charge;
	private String address;
	
	public AppointmentSlotWithAllDetailsResponse1() {
		super();
		// TODO Auto-generated constructor stub
	}

	public AppointmentSlotWithAllDetailsResponse1(int appointmentSlotId, String doctorName, String hospitalName,
			Date date, Time time, double charge) {
		super();
		this.appointmentSlotId = appointmentSlotId;
		this.doctorName = doctorName;
		this.hospitalName = hospitalName;
		this.date = date;
		this.time = time;
		this.charge = charge;
	}

	public int getAppointmentSlotId() {
		return appointmentSlotId;
	}

	public void setAppointmentSlotId(int appointmentSlotId) {
		this.appointmentSlotId = appointmentSlotId;
	}

	public String getDoctorName() {
		return doctorName;
	}

	public void setDoctorName(String doctorName) {
		this.doctorName = doctorName;
	}

	public String getHospitalName() {
		return hospitalName;
	}

	public void setHospitalName(String hospitalName) {
		this.hospitalName = hospitalName;
	}

	public Date getDate() {
		return date;
	}

	public void setDate(Date date) {
		this.date = date;
	}

	public Time getTime() {
		return time;
	}

	public void setTime(Time time) {
		this.time = time;
	}

	public double getCharge() {
		return charge;
	}

	public void setCharge(double charge) {
		this.charge = charge;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	@Override
	public String toString() {
		return "AppointmentSlotWithAllDetailsResponse1 [appointmentSlotId=" + appointmentSlotId + ", doctorName="
				+ doctorName + ", hospitalName=" + hospitalName + ", date=" + date + ", time=" + time + ", charge="
				+ charge + ", address=" + address + "]";
	}
	
}
