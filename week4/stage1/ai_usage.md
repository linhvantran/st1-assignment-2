# Stage 1 – SmartCare Prototype
# Human-written version + one controlled improvement

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# -----------------------------
# Task 1 – Basic Python version
# -----------------------------

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'

print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'

print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")


# ---------------------------------------------------
# Enhanced version – lists, dictionaries, functions
# ---------------------------------------------------

appointments = []

# Controlled improvement: prevent double-booking
def check_double_booking(practitioner_name, appointment_time):
    for a in appointments:
        if a["practitioner"] == practitioner_name and a["time"] == appointment_time:
            raise ValueError("Double booking detected")


def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

    # Improvement added here
    check_double_booking(practitioner_name, appointment_time)

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)


def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")


print("\nWelcome to SmartCare: The Clinical Appointment Booking System!")

# Book two appointments
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')

# Display all appointments
display_appointments()
