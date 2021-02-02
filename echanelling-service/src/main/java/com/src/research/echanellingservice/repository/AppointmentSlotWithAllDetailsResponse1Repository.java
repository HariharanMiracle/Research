package com.src.research.echanellingservice.repository;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import com.src.research.echanellingservice.model.AppointmentSlotWithAllDetailsResponse1;

@Repository
public class AppointmentSlotWithAllDetailsResponse1Repository {

	@Autowired
	JdbcTemplate jdbcTemplate;
	
	class AppointmentSlotWithAllDetailsResponse1RowMapper implements RowMapper<AppointmentSlotWithAllDetailsResponse1> {
		@Override
		public AppointmentSlotWithAllDetailsResponse1 mapRow(ResultSet rs, int rowNum) throws SQLException {
			AppointmentSlotWithAllDetailsResponse1 object = new AppointmentSlotWithAllDetailsResponse1();
			object.setAppointmentSlotId(rs.getInt(1));
			object.setDoctorName(rs.getString(2));
			object.setHospitalName(rs.getString(3));
			object.setDate(rs.getDate(4));
			object.setTime(rs.getTime(5));
			object.setCharge(rs.getDouble(6));
			object.setAddress(rs.getString(7));
			
			return object;
		}
	}
	
	public List<AppointmentSlotWithAllDetailsResponse1> listAllDoctorsByLocationAndSpecialization(String specialization, String location) {
		return jdbcTemplate.query("SELECT dh.id, d.name, h.name, dh.date, dh.startTime, dh.charge, h.address from doctor d, hospital h, appointment_slot dh where d.id = dh.doctorId and h.id = dh.hospitalId and d.specialization = '"+specialization+"' and h.location = '"+location+"' and dh.availableSeats > 0 and DATEDIFF(dh.date, CURDATE()) > 0", new AppointmentSlotWithAllDetailsResponse1RowMapper());
	}
	
	
	public List<AppointmentSlotWithAllDetailsResponse1> listAllDoctorsByZipcodeAndSpecialization(String specialization, String zipcode) {
		return jdbcTemplate.query("SELECT dh.id, d.name, h.name, dh.date, dh.startTime, dh.charge, h.address from doctor d, hospital h, appointment_slot dh where d.id = dh.doctorId and h.id = dh.hospitalId and d.specialization = '"+specialization+"' and h.zipcode = '"+zipcode+"' and dh.availableSeats > 0 and DATEDIFF(dh.date, CURDATE()) > 0", new AppointmentSlotWithAllDetailsResponse1RowMapper());
	}
	
	public List<AppointmentSlotWithAllDetailsResponse1> listAllDoctorsByDoctorName(String doctorName){
		return jdbcTemplate.query("SELECT dh.id, d.name, h.name, dh.date, dh.startTime, dh.charge, h.address" + 
				"from doctor d, hospital h, appointment_slot dh " + 
				"where d.id = dh.doctorId " + 
				"and h.id = dh.hospitalId " + 
				"and d.name LIKE '%"+doctorName+"%' " +
				"and dh.availableSeats > 0" + 
				"and DATEDIFF(dh.date, CURDATE()) > 0", new AppointmentSlotWithAllDetailsResponse1RowMapper());
	}
	
	public List<AppointmentSlotWithAllDetailsResponse1> listAllDoctorsByHospitalAndSpecializatiom(String hospital, String specialization){
		return jdbcTemplate.query("SELECT dh.id, d.name, h.name, dh.date, dh.startTime, dh.charge, h.address" + 
				"from doctor d, hospital h, appointment_slot dh" + 
				"where d.id = dh.doctorId" + 
				"and h.id = dh.hospitalId" + 
				"and h.name LIKE '%"+hospital+"%'" + 
				"and d.specialization = '"+specialization+"'" + 
				"and dh.availableSeats > 0" + 
				"and DATEDIFF(dh.date, CURDATE()) > 0", new AppointmentSlotWithAllDetailsResponse1RowMapper());
	}
	
}


//SELECT dh.id, d.name, h.name, dh.date, dh.startTime, dh.charge, h.address
//from doctor d, hospital h, appointment_slot dh
//where d.id = dh.doctorId
//and h.id = dh.hospitalId
//and h.name LIKE '%nawaloka%'
//and d.specialization = 'Cardiologist'
//and dh.availableSeats > 0
//and DATEDIFF(dh.date, CURDATE()) > 0