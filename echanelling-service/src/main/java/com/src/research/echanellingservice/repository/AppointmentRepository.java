package com.src.research.echanellingservice.repository;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Properties;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import com.src.research.echanellingservice.model.Appointment;
import com.src.research.echanellingservice.model.AppointmentSlotWithAllDetailsResponse1;
import com.src.research.echanellingservice.model.Appointment_slot;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

@Repository
public class AppointmentRepository {

	@Autowired
	JdbcTemplate jdbcTemplate;
	
	@Autowired
	Appointment_slotRepository appointment_slotRepository;
	
	class AppointmentRowMapper implements RowMapper<Appointment> {
		@Override
		public Appointment mapRow(ResultSet rs, int rowNum) throws SQLException {
			Appointment object = new Appointment();
			object.setId(rs.getInt("id"));
			object.setaSlotId(rs.getInt("aSlotId"));
			object.setContact(rs.getString("contact"));
			object.setEmail(rs.getString("email"));
			object.setName(rs.getString("name"));
			object.setNic(rs.getString("nic"));
			
			return object;
		}
	}
	
	public int makeAppointment(Appointment appointment) {
		try {
			System.out.println("make appointment");
			int x = jdbcTemplate.update("INSERT INTO `appointment`(`name`, `nic`, `email`, `contact`, `aSlotId`) VALUES ('"+appointment.getName()+"', '"+appointment.getNic()+"', '"+appointment.getEmail()+"', '"+appointment.getContact()+"', '"+appointment.getaSlotId()+"')");

			Appointment_slot appointment_slot = (Appointment_slot) appointment_slotRepository.findAppointment_slotById(appointment.getaSlotId() + "");		
			
			System.out.println("appointment_slot => " + appointment_slot.toString());
			
			int seats = appointment_slot.getAvailableSeats() - 1;
			int y = jdbcTemplate.update("update `appointment_slot` set availableSeats = '"+seats+"' where id = '"+appointment.getaSlotId()+"'");
			
			
			
//			// Recipient's email ID needs to be mentioned.
//	        String to = "hariharankim@gmail.com";
//			
//	        // Sender's email ID needs to be mentioned
//	        String from = "hariharansliit@gmail.com";
//			
//	        // Assuming you are sending email from through gmails smtp
//	        String host = "smtp.gmail.com";
//	        
//	        // Get system properties
//	        Properties properties = System.getProperties();
//	        
//	        // Setup mail server
//	        properties.put("mail.smtp.host", host);
//	        properties.put("mail.smtp.port", "465");
//	        properties.put("mail.smtp.ssl.enable", "true");
//	        properties.put("mail.smtp.auth", "true");
//	        
//	        // Get the Session object.// and pass username and password
//	        Session session = Session.getInstance(properties, new javax.mail.Authenticator() {
//
//	            protected PasswordAuthentication getPasswordAuthentication() {
//
//	                return new PasswordAuthentication("hariharansliit@gmail.com", "e2fk123nf#");
//
//	            }
//
//	        });
	        
	     // Used to debug SMTP issues
//	        session.setDebug(true);

//	        try {
//	            // Create a default MimeMessage object.
//	            MimeMessage message = new MimeMessage(session);
//
//	            // Set From: header field of the header.
//	            message.setFrom(new InternetAddress(from));
//
//	            // Set To: header field of the header.
//	            message.addRecipient(Message.RecipientType.TO, new InternetAddress(to));
//
//	            // Set Subject: header field
//	            message.setSubject("This is the Subject Line!");
//
//	            // Now set the actual message
//	            message.setText("This is actual message");
//
//	            System.out.println("sending...");
//	            // Send message
//	            Transport.send(message);
//	            System.out.println("Sent message successfully....");
//	        } catch (MessagingException mex) {
//	            mex.printStackTrace();
//	        }
			
			return 1;
		}
		catch(Exception e) {
			System.out.println(e);
			System.out.println("###############################################");
			e.printStackTrace();
			return 0;
		}
	}
	
}
