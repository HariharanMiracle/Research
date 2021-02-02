package com.src.research.echanellingservice.model;

public class AppointmentResponse1 {
	
	private String message;
	private int status;

	public AppointmentResponse1() {
		super();
		// TODO Auto-generated constructor stub
	}

	public AppointmentResponse1(String message, int status) {
		super();
		this.message = message;
		this.status = status;
	}
	
	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
	
	public int getStatus() {
		return status;
	}

	public void setStatus(int status) {
		this.status = status;
	}

	@Override
	public String toString() {
		return "AppointmentResponse1 [message=" + message + "]";
	}
	
}
