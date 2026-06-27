/*
=========================================
Author: Marcellino Modesto
Date: 06/27/2026
Assignment: Hands-On 4.2 MongoDB Database Setup and Querying
Database: web335DB
Collection: users
=========================================
*/


// a. Display all users in the users collection
db.users.find();


// b. Display the user with the email address jbach@me.com
db.users.find({ email: "jbach@me.com" });


// c. Display the user with the last name Mozart
db.users.find({ lastName: "Mozart" });


// d. Display the user with the first name Richard
db.users.find({ firstName: "Richard" });


// e. Display the user with employeeId 1010
db.users.find({ employeeId: 1010 });