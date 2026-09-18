"""
SmartCare v0.3 — Domain model skeletons (Stage 3, Part G)

Required by the lab (Part G): Patient, Practitioner, Appointment.
AppointmentBook is the optional class justified by FR-05 in the
design rationale.
"""


class Patient:
    """A person receiving care. FR-07, FR-03, FR-10, FR-13."""

    def __init__(self, patient_id, name, contact_detail):
        if not name:
            raise ValueError("Patient name cannot be empty")
        self.patient_id = patient_id
        self.name = name
        self.contact_detail = contact_detail

    def __repr__(self):
        return f"Patient({self.patient_id}, {self.name!r})"


class Practitioner:
    """A clinician who sees patients. FR-08, FR-04."""

    def __init__(self, practitioner_id, name, specialty):
        if not name:
            raise ValueError("Practitioner name cannot be empty")
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def __repr__(self):
        return f"Practitioner({self.practitioner_id}, {self.name!r})"


class Appointment:
    """A booking linking one Patient and one Practitioner at a time.
    FR-01, FR-02, FR-06, FR-09, FR-11, FR-12."""

    def __init__(self, appointment_id, patient, practitioner, date_time):
        if not patient or not practitioner or not date_time:
            raise ValueError("Appointment requires a patient, practitioner, and date/time")
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = "booked"

    def cancel(self):
        #set self.status = "cancelled"
        pass

    def update_time(self, new_time):
        #update self.date_time; re-check conflicts via AppointmentBook
        pass

    def mark_completed(self):
        # set self.status = "completed" — provisional, see Assumptions
        pass

    def __repr__(self):
        return f"Appointment({self.appointment_id}, {self.patient.name} with {self.practitioner.name} @ {self.date_time}, {self.status})"


class AppointmentBook:
    def __init__(self):
        self.appointments = []

    def book(self, patient, practitioner, date_time):
        #check has_conflict() first, then create and store an Appointment
        pass

    def has_conflict(self, practitioner, date_time):
        #True if practitioner already has an appointment at date_time
        pass

    def find_by_patient(self, patient):
        #return all appointments for this patient
        pass

    def find_by_practitioner(self, practitioner):
        #return all appointments for this practitioner
        pass

    def find_by_day(self, date):
        # return all appointments on this date
        pass


if __name__ == "__main__":
    alice = Patient(1, "Alice Smith", "0400 000 000")
    dr_doe = Practitioner(1, "Dr. John Doe", "General Practice")
    appt = Appointment(1, alice, dr_doe, "2024-07-20 10:00 AM")
    print(alice)
    print(dr_doe)
    print(appt)

    try:
        Patient(2, "", "x")
    except ValueError as e:
        print("Validation works as designed:", e)

    book = AppointmentBook()
    print("AppointmentBook created, ready for future logic:", book.appointments)