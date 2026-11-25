        if age <= 0 or distance <= 0:
            print("Invalid age or distance. This passenger's calculation is skipped.")
        else:
            print("\\nTravel classes:")
            print("1. Sleeper")
            print("2. 3AC")
            print("3. 2AC")
            print("4. 1AC")
            class_choice = int(input("Select travel class (1-4): "))

            if class_choice == 1:
                travel_class = "Sleeper"
                class_multiplier = 1
            elif class_choice == 2:
                travel_class = "3AC"
                class_multiplier = 2
            elif class_choice == 3:
                travel_class = "2AC"
                class_multiplier = 3
            elif class_choice == 4:
                travel_class = "1AC"
                class_multiplier = 4
            else:
                travel_class = "Sleeper"
                class_multiplier = 1
                print("Invalid class choice. Sleeper class will be selected.")

            # Calculate base fare using distance slabs:
            # First 100 km: Rs. 1.50 per km
            # Next 400 km: Rs. 1.20 per km
            # Above 500 km: Rs. 0.90 per km
            if distance <= 100:
                distance_fare = distance * 1.50
            elif distance <= 500:
                distance_fare = (100 * 1.50) + ((distance - 100) * 1.20)
            else:
                distance_fare = (100 * 1.50) + (400 * 1.20) + ((distance - 500) * 0.90)

            class_fare = distance_fare * class_multiplier

            # Age-based concession on class fare
            if age <= 12:
                concession_rate = 50
                passenger_category = "Child"
            elif age >= 60:
                concession_rate = 30
                passenger_category = "Senior Citizen"
            else:
                concession_rate = 0
                passenger_category = "Adult"

            concession_amount = class_fare * concession_rate / 100
            discounted_fare = class_fare - concession_amount

            # Reservation fee is added after concession
            ticket_amount = discounted_fare + RESERVATION_FEE

            print("\\nCancellation option:")
            print("Y - Cancel this reservation")
            print("N - Keep this reservation")
            cancel_choice = input("Do you want to cancel? (Y/N): ")

            if cancel_choice == "Y" or cancel_choice == "y":
                # Cancellation penalty applies to discounted fare.
                # Reservation fee is non-refundable.
                cancellation_penalty = discounted_fare * CANCELLATION_RATE / 100
                refund_amount = discounted_fare - cancellation_penalty
                cancellation_charges = cancellation_penalty + RESERVATION_FEE
                total_cancellation_charges = total_cancellation_charges + cancellation_charges
                total_refund = total_refund + refund_amount
                status = "Cancelled"
                amount_to_pay = 0
            else:
                cancellation_penalty = 0
                refund_amount = 0
                cancellation_charges = 0
                status = "Confirmed"
                amount_to_pay = ticket_amount
                total_ticket_amount = total_ticket_amount + ticket_amount

            receipt = (
                "\\nPassenger: " + passenger_name
                + "\\nAge: " + str(age)
                + "\\nCategory: " + passenger_category
                + "\\nDistance: " + str(distance) + " km"
                + "\\nTravel Class: " + travel_class
                + "\\nDistance Fare: Rs. " + str(round(distance_fare, 2))
                + "\\nClass Fare: Rs. " + str(round(class_fare, 2))
                + "\\nConcession: " + str(concession_rate) + "%"
                + "\\nConcession Amount: Rs. " + str(round(concession_amount, 2))
                + "\\nReservation Fee: Rs. " + str(RESERVATION_FEE)
                + "\\nTicket Amount: Rs. " + str(round(ticket_amount, 2))
                + "\\nCancellation Penalty: Rs. " + str(round(cancellation_penalty, 2))
                + "\\nRefund Amount: Rs. " + str(round(refund_amount, 2))
                + "\\nStatus: " + status
                + "\\nAmount Payable: Rs. " + str(round(amount_to_pay, 2))
            )
            passenger_receipts.append(receipt)
            print(receipt)

    print("\\n==============================================")
    print("                 FINAL SUMMARY")
    print("==============================================")

    for receipt in passenger_receipts:
        print(receipt)
        print("----------------------------------------------")

    print("Total amount for confirmed tickets: Rs.", round(total_ticket_amount, 2))
    print("Total cancellation charges: Rs.", round(total_cancellation_charges, 2))
    print("Total refund for cancelled tickets: Rs.", round(total_refund, 2))
    print("==============================================")
    print("Thank you for using the Railway Calculator!")
