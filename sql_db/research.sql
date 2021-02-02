/*
SQLyog Ultimate v12.4.3 (64 bit)
MySQL - 5.5.41 : Database - research
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`research` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `research`;

/*Table structure for table `appointment` */

DROP TABLE IF EXISTS `appointment`;

CREATE TABLE `appointment` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `nic` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `aSlotId` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `appointment` */

insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (1,'Hariharan','991133992V','hariharansliit@gmail.com','0776318136',1);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (2,'Hariharan','991133992V','hariharansliit@gmail.com','0776318136',2);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (3,'Sarah','972255698V','sarah97@gmail.com','0776325987',2);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (4,'Matthew','962290698V','chamikaravinda@gmail.com','0723464646',2);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (5,'Kalana','961136559V','kalana96@gmail.com','0778965326',3);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (6,'John','965561556V','john96@gmail.com','0779656895',1);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (7,'Harry','991122557V','harry99@gmail.com','0775698789',3);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (8,'Dhivya','996655889V','veni22@gmail.com','0769856985',2);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (9,'Yasikaran','996632552V','yasikaran@gmail.com','0779632546',1);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (10,'Vasudevan','622143143V','vasudevan59@gmail.com','0779784296',1);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (11,'Anbarasi','661133992V','anbarasi@gmail.com','0779784296',1);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (12,'Keerthana','991133992V','keerthna@gmail.com','069071957',4);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (13,'Ashim','991133991V','asdf@gmail.com','0765559699',3);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (14,'Hariharan','991133992V','hariharankim@gmail.com','0779784296',3);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (15,'Hariharan','868632941V','tharushana@gmail.com','0774596632',1);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (16,'Gajen','896699882V','gajenpurushoth@gmail.com','0777898922',5);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (17,'Hariharan','991133992V','hariharansliit@gmail.com','0776318136',1);
insert  into `appointment`(`id`,`name`,`nic`,`email`,`contact`,`aSlotId`) values (18,'Yashikaran','991133992V','yaka@gmail.com','0776318136',1);

/*Table structure for table `appointment_slot` */

DROP TABLE IF EXISTS `appointment_slot`;

CREATE TABLE `appointment_slot` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `doctorId` int(10) NOT NULL,
  `hospitalId` int(10) NOT NULL,
  `date` date NOT NULL,
  `charge` double NOT NULL,
  `totalSeats` int(10) NOT NULL,
  `availableSeats` int(10) NOT NULL,
  `startTime` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `appointment_slot` */

insert  into `appointment_slot`(`id`,`doctorId`,`hospitalId`,`date`,`charge`,`totalSeats`,`availableSeats`,`startTime`) values (1,4,1,'2020-11-28',800,40,27,'15:00:00');
insert  into `appointment_slot`(`id`,`doctorId`,`hospitalId`,`date`,`charge`,`totalSeats`,`availableSeats`,`startTime`) values (2,5,1,'2020-11-02',750,40,30,'15:00:00');
insert  into `appointment_slot`(`id`,`doctorId`,`hospitalId`,`date`,`charge`,`totalSeats`,`availableSeats`,`startTime`) values (3,6,2,'2020-11-02',800,40,28,'17:00:00');
insert  into `appointment_slot`(`id`,`doctorId`,`hospitalId`,`date`,`charge`,`totalSeats`,`availableSeats`,`startTime`) values (4,1,2,'2021-03-25',700,30,29,'17:00:00');
insert  into `appointment_slot`(`id`,`doctorId`,`hospitalId`,`date`,`charge`,`totalSeats`,`availableSeats`,`startTime`) values (5,2,2,'2021-03-25',700,30,29,'17:00:00');

/*Table structure for table `doc_works_in_hos` */

DROP TABLE IF EXISTS `doc_works_in_hos`;

CREATE TABLE `doc_works_in_hos` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `doctorId` int(10) NOT NULL,
  `hospitalId` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `doc_works_in_hos` */

insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (1,1,1);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (2,2,1);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (3,3,1);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (4,4,1);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (5,5,1);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (6,6,1);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (7,1,2);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (8,2,2);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (9,3,2);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (10,4,2);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (11,5,2);
insert  into `doc_works_in_hos`(`id`,`doctorId`,`hospitalId`) values (12,6,2);

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `regNo` varchar(50) NOT NULL COMMENT 'eg: med-000-000-001',
  `name` varchar(50) NOT NULL COMMENT 'eg: Dr. Kasun Perera',
  `specialization` varchar(50) NOT NULL COMMENT 'eg: Cardiologist',
  `contactNo` varchar(10) NOT NULL COMMENT 'eg: 077123456',
  PRIMARY KEY (`id`),
  UNIQUE KEY `regNo` (`regNo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`id`,`regNo`,`name`,`specialization`,`contactNo`) values (1,'med-000-000-001','Dr. Hanar Moses','Physician','0769071957');
insert  into `doctor`(`id`,`regNo`,`name`,`specialization`,`contactNo`) values (2,'med-000-000-002','Dr. Theeban Rajendra','Physician','0771264309');
insert  into `doctor`(`id`,`regNo`,`name`,`specialization`,`contactNo`) values (3,'med-000-000-003','Dr. Nimalee Weerasooriya','Cardiologist','0710122220');
insert  into `doctor`(`id`,`regNo`,`name`,`specialization`,`contactNo`) values (4,'med-000-000-004','Dr. Vino Manohar','Cardiologist','0766665295');
insert  into `doctor`(`id`,`regNo`,`name`,`specialization`,`contactNo`) values (5,'med-000-000-005','Dr. Dhivya Hariharan','Physician','0717494853');
insert  into `doctor`(`id`,`regNo`,`name`,`specialization`,`contactNo`) values (6,'med-000-000-006','Dr. Hirunika Perera','Cardiologist','0712330256');

/*Table structure for table `hospital` */

DROP TABLE IF EXISTS `hospital`;

CREATE TABLE `hospital` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `zipcode` varchar(5) NOT NULL,
  `location` varchar(50) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `hospital` */

insert  into `hospital`(`id`,`name`,`zipcode`,`location`,`contact`,`address`) values (1,'Nawaloka','00200','Colombo','0115577111','Deshamanya, 23 H K Dharmadasa Mawatha, 00200');
insert  into `hospital`(`id`,`name`,`zipcode`,`location`,`contact`,`address`) values (2,'Asiri','00500','Colombo','0114524400','21 Kirimandala Mawatha, Colombo 00500');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(1000) DEFAULT NULL,
  `nic` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `contact` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`password`,`nic`,`email`,`contact`) values (3,'Hariharan','2KnDwetZSiyfhtTxwUF24Q==','991133992V','hari@gmail.com','0776318136');
insert  into `user`(`id`,`username`,`password`,`nic`,`email`,`contact`) values (4,'DarkRaven','Y55z7iyb16LxaCkkLVXl+g==','991133992V','darkraven@gmail.com','0776318136');
insert  into `user`(`id`,`username`,`password`,`nic`,`email`,`contact`) values (5,'DarkRaven1','Y55z7iyb16LxaCkkLVXl+g==','991133992V','darkraven@gmail.com','0776318136');
insert  into `user`(`id`,`username`,`password`,`nic`,`email`,`contact`) values (6,'yaka','2KnDwetZSiyfhtTxwUF24Q==','991133992V','yaka@gmail.com','0776318136');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
