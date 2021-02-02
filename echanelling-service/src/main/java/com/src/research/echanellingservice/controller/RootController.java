package com.src.research.echanellingservice.controller;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.src.research.echanellingservice.model.Appointment;
import com.src.research.echanellingservice.model.AppointmentRequest1;
import com.src.research.echanellingservice.model.AppointmentResponse1;
import com.src.research.echanellingservice.model.AppointmentSlotWithAllDetailsResponse1;
import com.src.research.echanellingservice.model.Doctor;
import com.src.research.echanellingservice.model.Request;
import com.src.research.echanellingservice.repository.AppointmentRepository;
import com.src.research.echanellingservice.repository.AppointmentSlotWithAllDetailsResponse1Repository;
import com.src.research.echanellingservice.repository.DoctorRespository;

@Controller
@RequestMapping(value="Echannel")
public class RootController {
	private Logger logger = LoggerFactory.getLogger(this.getClass());
	
	@Autowired
	AppointmentSlotWithAllDetailsResponse1Repository appointmentSlotWithAllDetailsResponse1Repository;
	
	@Autowired
	AppointmentRepository appointmentRepository;
	
	@GetMapping(value="/listAllDoctorsByDoctorName")
	@ResponseBody
	public List<AppointmentSlotWithAllDetailsResponse1> listAllDoctorsByDoctorName(@RequestParam("doctorName") String doctorName) {
		return appointmentSlotWithAllDetailsResponse1Repository.listAllDoctorsByDoctorName(doctorName);
	}
	
	@GetMapping(value="/listAllDoctorsByHospitalAndSpecializatiom")
	@ResponseBody
	public List<AppointmentSlotWithAllDetailsResponse1> listAllDoctorsByHospitalAndSpecializatiom(@RequestParam("specialization") String specialization, @RequestParam("hospital") String hospital) {
		return appointmentSlotWithAllDetailsResponse1Repository.listAllDoctorsByHospitalAndSpecializatiom(hospital, specialization);
	}
	
	@GetMapping(value="/listAllDoctorsByLocationAndSpecialization")
	@ResponseBody
	public List<AppointmentSlotWithAllDetailsResponse1> listAllDoctorsByLocationAndSpecialization(@RequestParam("specialization") String specialization, @RequestParam("location") String location) {
		return appointmentSlotWithAllDetailsResponse1Repository.listAllDoctorsByLocationAndSpecialization(specialization, location);
	}
	
	@GetMapping(value="/listAllDoctorsByZipcodeAndSpecialization")
	@ResponseBody
	public List<AppointmentSlotWithAllDetailsResponse1> listAllDoctorsByZipcodeAndSpecialization(@RequestParam("specialization") String specialization, @RequestParam("zipcode") String zipcode) {
		return appointmentSlotWithAllDetailsResponse1Repository.listAllDoctorsByZipcodeAndSpecialization(specialization, zipcode);
	}
	
	@PostMapping(path="/makeAppointment", consumes = "application/x-www-form-urlencoded", produces = "application/json")
	@ResponseBody
	public AppointmentResponse1 makeAppointment(AppointmentRequest1 appointmentRequest1) {
		System.out.println("AppointmentRequest1: " + appointmentRequest1.toString());
		AppointmentResponse1 appointmentResponse1 = new AppointmentResponse1();
		
		if(appointmentRequest1.getCreditCardNumber().length() == 16 && appointmentRequest1.getCvc().length() == 3) {
			// Credit card accepted
			Appointment appointment = new Appointment();
			appointment.setName(appointmentRequest1.getName());
			appointment.setaSlotId(appointmentRequest1.getaSlotId());
			appointment.setContact(appointmentRequest1.getContact());
			appointment.setEmail(appointmentRequest1.getEmail());
			appointment.setNic(appointmentRequest1.getNic());
			
			System.out.println("appointment.toString(): " + appointment.toString());
			
			int x = appointmentRepository.makeAppointment(appointment);
			
			if(x == 0) {
				appointmentResponse1.setStatus(0);
				appointmentResponse1.setMessage("Sorry something went wrong, Please try again later!!!");
			}
			else {
				appointmentResponse1.setStatus(1);
				appointmentResponse1.setMessage("Successfully made appointment, thankyou!!!");
			}
		}
		else {
			//wrong credit card
			appointmentResponse1.setStatus(0);
			appointmentResponse1.setMessage("Sorry your credit card number or cvc is incorrect, Please try again later!!!");
		}
		
		return appointmentResponse1;
	}
}
