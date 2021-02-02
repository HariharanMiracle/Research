package com.src.research.echanellingservice.controller;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.src.research.echanellingservice.model.Doctor;
import com.src.research.echanellingservice.model.Request;
import com.src.research.echanellingservice.repository.DoctorRespository;

@Controller
@RequestMapping(value="Doctor")
public class DoctorController {

	private Logger logger = LoggerFactory.getLogger(this.getClass());

	@Autowired
	DoctorRespository doctorRespository;
	
//	@GetMapping(value="/listAllDoctorsByName/{name}")
//	@ResponseBody
//	public List<Doctor> listAllDoctorsByName(@PathVariable String name) {
//	    return doctorRespository.findAllByNameLike(name);
//	}
//	
//	@GetMapping(value="/listAllDoctors")
//	@ResponseBody
//	public List<Doctor> listAllDoctors() {
//	    return doctorRespository.findAll();
//	}
//	
//	@GetMapping(value="/listAllDoctorsByDoctor_Type")
//	@ResponseBody
//	public List<Doctor> listAllDoctorsByDoctor_Type(@RequestParam("facility_type") String facility_type, @RequestParam("doctor_type") String doctor_type) {
//	    if(facility_type.equals("aaaa-a11a")) {
//	    	return doctorRespository.findAllByDoctor_Type(doctor_type);
//	    }
//	    return null;
//	}
	
	@PostMapping(path="/add", consumes = "application/x-www-form-urlencoded", produces = "application/json")
	@ResponseBody
	public Doctor addFunction(Request request) {
		System.out.println("Request: " + request.toString());
		Doctor doc1 = new Doctor(6, "med-128-028-222", "Dr.Dharshana", "Cardiologist", "+94 077-2233662");
		return doc1;
	}

	@GetMapping(value="/listAllDoctorsByLocationAndSpecialization")
	@ResponseBody
	public List<Doctor> listAllDoctorsByLocationAndSpecialization(@RequestParam("specialization") String specialization, @RequestParam("location") String location) {
	    
		System.out.println("########### listAllDoctorsByLocationAndSpecialization  ###########");
		
		List<Doctor> doctorList = new ArrayList<>();
		
		Doctor doc1 = new Doctor(1, "med-128-028-066", "Dr.Hanarshanya", "Cardiologist", "+94 077-9784296");
		Doctor doc2 = new Doctor(2, "med-128-126-630", "Dr.Ronaldo", "Cardiologist", "+94 077-6318136");
		Doctor doc3 = new Doctor(3, "med-128-236-546", "Dr.Williams", "Cardiologist", "+94 076-1845526");
		Doctor doc4 = new Doctor(4, "med-128-451-012", "Dr.Pathmanathan", "Cardiologist", "+94 071-7871848");
		Doctor doc5 = new Doctor(5, "med-128-895-122", "Dr.Prakash", "Cardiologist", "+94 077-7373414");
		
		doctorList.add(doc1);
		doctorList.add(doc2);
		doctorList.add(doc3);
		doctorList.add(doc4);
		doctorList.add(doc5);
		
		return doctorList;
		
	}
	
	@GetMapping(value="/getDoctorById")
	@ResponseBody
	public Doctor getDoctorById(@RequestParam("doctor_id") String doctor_id) {
		
		System.out.println("########### getDoctorById  ###########");
		
		Doctor doc1 = new Doctor(1, "med-128-028-066", "Dr.Hanarshanya", "Cardiologist", "+94 077-9784296");
		return doc1;
		
	}
	
	@GetMapping(value="/listAllDoctorsByLocation_ZipCodeAndSpecialization")
	@ResponseBody
	public List<Doctor> listAllDoctorsByLocation_ZipCodeAndSpecialization(@RequestParam("specialization") String specialization, @RequestParam("zipcode") String zipcode) {
	    
		System.out.println("########### listAllDoctorsByLocation_ZipCodeAndSpecialization  ###########");
		
		List<Doctor> doctorList = new ArrayList<>();
		
		Doctor doc1 = new Doctor(6, "med-128-028-222", "Dr.Dharshana", "Cardiologist", "+94 077-2233662");
		Doctor doc2 = new Doctor(7, "med-128-126-333", "Dr.Ferme", "Cardiologist", "+94 077-3612163");
		Doctor doc3 = new Doctor(8, "med-128-236-444", "Dr.James", "Cardiologist", "+94 076-8725034");
		Doctor doc4 = new Doctor(9, "med-128-451-555", "Dr.Harry", "Cardiologist", "+94 071-6069878");
		Doctor doc5 = new Doctor(10, "med-128-895-666", "Dr.Luna", "Cardiologist", "+94 077-9765486");
		
		doctorList.add(doc1);
		doctorList.add(doc2);
		doctorList.add(doc3);
		doctorList.add(doc4);
		doctorList.add(doc5);
		
		return doctorList;
		
	}
	
}



// sql 1
//SELECT dh.id, d.regNo, d.name, d.specialization, d.contact, h.name, h.location, h.zipcode, d.id, h.id, dh.charge, dh.totalSeats, dh.availableSeats, dh.date
//from doctor d, hospital h, appointment_slot dh
//where d.id = dh.doctorId
//and h.id = dh.hospitalId
//and d.specialization = 'Cardiologist'
//and h.location = 'Colombo'
//and dh.availableSeats > 0
//and DATEDIFF(dh.date, CURDATE()) > 0

//sql 2
