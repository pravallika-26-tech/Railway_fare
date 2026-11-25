#Railway_fare
Python Activity-Based Learning
Student Details
- Name: SEELAM PRAVALLIKA NARASA
- Roll Number: N26V01A0330
- Branch: CSE
- Section: 4
Case Study 6: Railway Fare and Reservation Calculator
1. Problem Statement
Develop a Python program to calculate railway fares for multiple passengers. The program uses distance-based fare slabs, different travel classes, age-based concessions, reservation fees, and a cancellation penalty. It displays the fare details, cancellation details, refund amount, and final summary for all passengers.
2. Objectives
- Accept details for multiple passengers.
- Calculate fares using distance slabs.
- Calculate fares according to the selected travel class.
- Apply concessions based on passenger age.
- Add a reservation fee to each ticket.
- Calculate cancellation penalties and refund amounts.
- Display an individual receipt and a final summary.
3. Assumptions and Fare Policy
The question does not provide exact fare rates, class multipliers, concession percentages, reservation fees, or cancellation penalties. Therefore, the following sample policy is assumed for this academic program. These values can be changed if the instructor provides a different policy.

Distance slabs (base fare):
Distance	Rate
First 100 km	Rs. 1.50 per km
Next 400 km (101–500 km)	Rs. 1.20 per km
Above 500 km	Rs. 0.90 per km


The fare is calculated progressively. For example, for a 600 km journey, the first 100 km use the first rate, the next 400 km use the second rate, and the remaining 100 km use the third rate.

Travel class multipliers:
Travel class	Multiplier
Sleeper	1
3AC	2
2AC	3
1AC	4


Age-based concessions:
Passenger category	Age condition	Concession
Child	12 years or below	50%
Adult	13 to 59 years	0%
Senior Citizen	60 years or above	30%


Other rules:
1. A reservation fee of Rs. 40 is added to every ticket after concession.
2. The concession is applied to the class fare, not to the reservation fee.
3. If a ticket is cancelled, the cancellation penalty is 20% of the discounted fare.
4. The reservation fee is non-refundable.
5. Refund = Discounted fare − Cancellation penalty.
6. Cancellation charges = Cancellation penalty + Non-refundable reservation fee.
7. A passenger who does not cancel has a confirmed ticket.
8. Age and journey distance must be greater than zero.
9. If an invalid travel-class option is entered, the program selects Sleeper class.
4. Algorithm
1. Start.
2. Read the number of passengers.
3. Check whether the number of passengers is greater than zero.
4. Repeat the following steps for each passenger:
   - Read passenger name, age, and journey distance.
   - Validate age and distance.
   - Display travel classes and read the class choice.
   - Select the class multiplier.
   - Calculate the base fare using the distance slabs.
   - Calculate the class fare using the class multiplier.
   - Identify the passenger category using age.
   - Calculate the concession amount.
   - Calculate the discounted fare.
   - Add the reservation fee to get the ticket amount.
   - Ask whether the passenger wants to cancel.
   - If cancelled, calculate the cancellation penalty and refund.
   - Otherwise, mark the ticket as confirmed and add its amount to the total.
   - Display the passenger receipt.
5. Display the final summary for all processed passengers.
6. Stop.
5. Pseudocode
START
    INPUT number_of_passengers

    IF number_of_passengers <= 0 THEN
        DISPLAY "Invalid number of passengers"
    ELSE
        SET total_ticket_amount = 0
        SET total_cancellation_charges = 0
        SET total_refund = 0

        FOR each passenger
            INPUT name, age, distance

            IF age <= 0 OR distance <= 0 THEN
                DISPLAY "Invalid age or distance"
            ELSE
                INPUT travel_class

                IF distance <= 100 THEN
                    distance_fare = distance * 1.50
                ELSE IF distance <= 500 THEN
                    distance_fare = 150 + (distance - 100) * 1.20
                ELSE
                    distance_fare = 150 + 480
                                   + (distance - 500) * 0.90
                END IF

                SELECT class multiplier
                class_fare = distance_fare * multiplier

                IF age <= 12 THEN
                    concession_rate = 50
                ELSE IF age >= 60 THEN
                    concession_rate = 30
                ELSE
                    concession_rate = 0
                END IF

                concession = class_fare * concession_rate / 100
                discounted_fare = class_fare - concession
                ticket_amount = discounted_fare + 40

                INPUT cancellation choice

                IF ticket is cancelled THEN
                    penalty = discounted_fare * 20 / 100
                    refund = discounted_fare - penalty
                    cancellation_charges = penalty + 40
                    ADD cancellation_charges to total
                    ADD refund to total
                ELSE
                    ADD ticket_amount to total_ticket_amount
                END IF

                DISPLAY passenger receipt
            END IF
        END FOR

        DISPLAY final summary
    END IF
STOP
6. Flowchart
              +-------------+
              |    START    |
              +-------------+
                     |
                     v
       +---------------------------+
       | Input number of passengers|
       +---------------------------+
                     |
                     v
       +---------------------------+
       | Is passenger count > 0 ?  |
       +---------------------------+
             | Yes          | No
             v              v
 +--------------------+  +------------------+
 | Read passenger     |  | Display invalid  |
 | name, age, distance|  | passenger count  |
 +--------------------+  +------------------+
             |
             v
 +---------------------------+
 | Validate age and distance |
 +---------------------------+
             |
             v
 +---------------------------+
 | Select travel class       |
 +---------------------------+
             |
             v
 +---------------------------+
 | Calculate distance fare   |
 | using distance slabs      |
 +---------------------------+
             |
             v
 +---------------------------+
 | Calculate class fare      |
 +---------------------------+
             |
             v
 +---------------------------+
 | Apply age-based concession|
 +---------------------------+
             |
             v
 +---------------------------+
 | Add reservation fee       |
 +---------------------------+
             |
             v
 +---------------------------+
 | Is ticket cancelled?      |
 +---------------------------+
       | Yes          | No
       v              v
+----------------+  +------------------+
| Calculate      |  | Mark as confirmed|
| penalty/refund |  | Add ticket amount|
+----------------+  +------------------+
       |              |
       +-------+------+
               |
               v
 +---------------------------+
 | Display passenger receipt |
 +---------------------------+
               |
               v
 +---------------------------+
 | More passengers remaining?|
 +---------------------------+
       | Yes          | No
       |              v
       |    +----------------------+
       |    | Display final summary|
       |    +----------------------+
       |              |
       +--------------+
                      v
                +-----------+
                |    STOP   |
                +-----------+
7. Python Concepts Used
Python concept	Application
Variables	Store passenger and fare details
Data types	String, integer, and float
Input/output	input() and print()
Arithmetic operators	+, -, *, /
Relational operators	<, >, <=, ==
Logical operators	and, or
Conditional statements	if, elif, else
Loops	for loop to process multiple passengers
Lists	Store passenger receipt details
Type conversion	int() and float()
Built-in function	range() and round()


8. Test Cases
Test	Passenger details	Expected result
1	Adult, 30 years, 100 km, Sleeper, not cancelled	Distance fare Rs. 150; ticket amount Rs. 190
2	Adult, 30 years, 300 km, Sleeper, not cancelled	Distance fare Rs. 390; ticket amount Rs. 430
3	Adult, 30 years, 600 km, Sleeper, not cancelled	Distance fare Rs. 720; ticket amount Rs. 760
4	Child, 10 years, 100 km, Sleeper, not cancelled	50% concession; ticket amount Rs. 115
5	Senior Citizen, 65 years, 100 km, Sleeper, not cancelled	30% concession; ticket amount Rs. 145
6	Adult, 30 years, 100 km, Sleeper, cancelled	Penalty Rs. 30; refund Rs. 120; reservation fee Rs. 40 is not refunded
7	Age 0 or distance 0	Invalid age or distance; calculation skipped


9. Sample Output
The following is an example for one adult passenger travelling 100 km in Sleeper class without cancellation.
==============================================
     RAILWAY FARE AND RESERVATION CALCULATOR
==============================================
Enter number of passengers: 1

----------------------------------------------
Passenger 1
----------------------------------------------
Enter passenger name: Ravi
Enter passenger age: 30
Enter journey distance in km: 100

Travel classes:
1. Sleeper
2. 3AC
3. 2AC
4. 1AC
Select travel class (1-4): 1

Cancellation option:
Y - Cancel this reservation
N - Keep this reservation
Do you want to cancel? (Y/N): N

Passenger: Ravi
Age: 30
Category: Adult
Distance: 100.0 km
Travel Class: Sleeper
Distance Fare: Rs. 150.0
Class Fare: Rs. 150.0
Concession: 0%
Concession Amount: Rs. 0.0
Reservation Fee: Rs. 40
Ticket Amount: Rs. 190.0
Cancellation Penalty: Rs. 0
Refund Amount: Rs. 0
Status: Confirmed
Amount Payable: Rs. 190.0

==============================================
                 FINAL SUMMARY
==============================================
Total amount for confirmed tickets: Rs. 190.0
Total cancellation charges: Rs. 0.0
Total refund for cancelled tickets: Rs. 0.0
==============================================
Thank you for using the Railway Calculator!
10. Conclusion
The Railway Fare and Reservation Calculator calculates fares for multiple passengers using distance slabs and travel-class multipliers. It applies age-based concessions, adds reservation fees, and calculates cancellation penalties and refunds. This program demonstrates the practical use of basic Python concepts such as variables, operators, conditional statements, loops, and lists.
11. How to Run
1. Install Python 3 on your computer.
2. Open the project folder in VS Code or another Python editor.
3. Open railway_fare_calculator.py.
4. Run the program.
5. Enter the number of passengers and their details.
6. Select the travel class and cancellation option.
7. Check the individual receipts and final summary.
Submission reminder: Add your actual execution screenshots to the repository. If your instructor provides different fare slabs, concessions, reservation fees, or cancellation rules, update the assumptions and program to match them.





















































































# Railway_fare
