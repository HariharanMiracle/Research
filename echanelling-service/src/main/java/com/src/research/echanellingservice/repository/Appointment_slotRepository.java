package com.src.research.echanellingservice.repository;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import com.src.research.echanellingservice.model.Appointment_slot;

@Repository
public class Appointment_slotRepository {

	@Autowired
	JdbcTemplate jdbcTemplate;
	
	class Appointment_slotRowMapper implements RowMapper<Appointment_slot> {
		@Override
		public Appointment_slot mapRow(ResultSet rs, int rowNum) throws SQLException {
			Appointment_slot appointment_slot = new Appointment_slot();
			
			appointment_slot.setId(rs.getInt("id"));
			appointment_slot.setDoctorId(rs.getInt("doctorId"));
			appointment_slot.setHospitalId(rs.getInt("hospitalId"));
			appointment_slot.setDate(rs.getDate("date"));
			appointment_slot.setCharge(rs.getDouble("charge"));
			appointment_slot.setTotalSeats(rs.getInt("totalSeats"));
			appointment_slot.setAvailableSeats(rs.getInt("availableSeats"));
			appointment_slot.setStartTime(rs.getTime("startTime"));
			
			return appointment_slot;
			
		}
	}
	
	public Appointment_slot findAppointment_slotById(String id) {
		Appointment_slot appointment_Slot = jdbcTemplate.queryForObject("SELECT * FROM `appointment_slot` WHERE `id` = '"+id+"'", new Appointment_slotRowMapper());
		
		System.out.println("appointment slot from find appointment slot by id: " + appointment_Slot.toString());
		
		return appointment_Slot;
	}
}
