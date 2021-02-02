package com.src.research.echanellingservice.repository;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import com.src.research.echanellingservice.model.Doctor;

@Repository
public class DoctorRespository {

//	@Autowired
//	JdbcTemplate jdbcTemplate;
//	
//	class DoctorRowMapper implements RowMapper<Doctor> {
//		@Override
//		public Doctor mapRow(ResultSet rs, int rowNum) throws SQLException {
//			Doctor doctor = new Doctor();
//			doctor.setId(rs.getInt("id"));
//			doctor.setName(rs.getString("name"));
//			doctor.setDoctor_type(rs.getString("doctor_type"));
//			return doctor;
//		}
//	}
//	
//	public List<Doctor> findAll() {
//		return jdbcTemplate.query("select * from doctor", new DoctorRowMapper());
//	}
//	
//	public List<Doctor> findAllByDoctor_Type(String doctor_type) {
//		return jdbcTemplate.query("SELECT * FROM `doctor` WHERE `doctor_type` = '"+ doctor_type +"'", new DoctorRowMapper());
//	}
//	
//	public List<Doctor> findAllByNameLike(String name) {
//		return jdbcTemplate.query("SELECT * FROM `doctor` WHERE `name` like '%"+ name +"%'", new DoctorRowMapper());
//	}
	
}
