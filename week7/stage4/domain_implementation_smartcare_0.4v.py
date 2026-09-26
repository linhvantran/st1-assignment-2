"""
SmartCare v0.4 — Domain layer implementation (Stage 4)

Patient and Practitioner (Parts B & C): manual implementation, AI OFF.
Appointment (Part D): AI ON — Copilot’s actual output is provided
as a full transcript in
ai_engineering_log.md — its attributes, method names,
and enum values are Copilot’s; the encapsulation (private fields +
read-only properties, InvalidStatusTransition exception) was added
in Part G after Part E’s manual testing revealed the original
@dataclass version allowed any code to completely bypass
cancel()/mark_completed() by assigning attributes directly.

AppointmentBook is omitted by design — Stage 4 only requires
Patient, Practitioner, and Appointment (see UML-to-Code Trace).
"""

from enum import Enum


class Patient:
    """FR-07, FR-03, FR-10, FR-13. AI OFF — implemented by hand (Part B)."""

    def __init__(self, patient_id: int, name: str, contact_detail: str):
        if not name:
            raise ValueError("Patient name cannot be empty")
        self._patient_id = patient_id
        self._name = name
        self._contact_detail = contact_detail

    @property
    def patient_id(self) -> int:
        return self._patient_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def contact_detail(self) -> str:
        return self._contact_detail

    def __repr__(self) -> str:
        return f"Patient({self._patient_id}, {self._name!r})"


class Practitioner:
    """FR-08, FR-04. AI OFF — implemented by hand (Part C)."""

    def __init__(self, practitioner_id: int, name: str, specialty: str):
        if not name:
            raise ValueError("Practitioner name cannot be empty")
        self._practitioner_id = practitioner_id
        self._name = name
        self._specialty = specialty

    @property
    def practitioner_id(self) -> int:
        return self._practitioner_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def specialty(self) -> str:
        return self._specialty

    def __repr__(self) -> str:
        return f"Practitioner({self._practitioner_id}, {self._name!r})"


class InvalidStatusTransition(Exception):
    """Raised specifically for illegal status transitions, held away
from ValueError, to allow callers to differentiate between 'bad input' and the
'illegal business-rule transition' (Part E finding: Copilot's actual output used
ValueError for both, conflating two different failure types)."""
    pass


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    COMPLETED = "completed"  # provisional — see Assumptions in v0.2


class Appointment:
    """FR-01, FR-02, FR-06, FR-09, FR-11, FR-12.

    Part D was created using @dataclass and public fields (see
ai_engineering_log.md for the real transcript). Let anyone bypass cancel()/mark_completed()
by direct assignment of attributes (appt.status = ... skipped any business
rules without error). Part G refactors to private attributes + read-only
properties, same encapsulation pattern used for Patient and Practitioner
above — everything else (attribute names, method names, enum values, docstring
reasoning) is same as Copilot produced it because only encapsulation was
broken.
    """

    def __init__(self, appointment_id: str, patient: Patient,
                 practitioner: Practitioner, date_time: str):
        if patient is None:
            raise ValueError("Appointment requires a patient.")
        if practitioner is None:
            raise ValueError("Appointment requires a practitioner.")
        if not date_time:
            raise ValueError("Appointment requires a date/time.")
        self._appointment_id = appointment_id
        self._patient = patient
        self._practitioner = practitioner
        self._date_time = date_time
        self._status = AppointmentStatus.SCHEDULED

    @property
    def appointment_id(self) -> str:
        return self._appointment_id

    @property
    def patient(self) -> Patient:
        return self._patient

    @property
    def practitioner(self) -> Practitioner:
        return self._practitioner

    @property
    def date_time(self) -> str:
        return self._date_time

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        """Business rules: a cancelled or completed appointment cannot be
        cancelled again; cancelled appointments remain as objects (no
        deletion) so they still appear in history."""
        if self._status == AppointmentStatus.CANCELLED:
            raise InvalidStatusTransition("Appointment is already cancelled.")
        if self._status == AppointmentStatus.COMPLETED:
            raise InvalidStatusTransition("Completed appointments cannot be cancelled.")
        self._status = AppointmentStatus.CANCELLED

    def update_time(self, new_time: str) -> None:
        """Business rule: only a SCHEDULED appointment can be rescheduled."""
        if self._status != AppointmentStatus.SCHEDULED:
            raise InvalidStatusTransition("Only scheduled appointments can have their time updated.")
        if not new_time:
            raise ValueError("New time must not be empty.")
        self._date_time = new_time

    def mark_completed(self) -> None:
        """Business rules: cancelled appointments cannot be completed;
        an already-completed appointment cannot be completed again."""
        if self._status == AppointmentStatus.CANCELLED:
            raise InvalidStatusTransition("Cancelled appointments cannot be completed.")
        if self._status == AppointmentStatus.COMPLETED:
            raise InvalidStatusTransition("Appointment is already completed.")
        self._status = AppointmentStatus.COMPLETED

    def __repr__(self) -> str:
        return (f"Appointment({self._appointment_id}, "
                f"{self._patient.name} with {self._practitioner.name} "
                f"@ {self._date_time}, {self._status.value})")


if __name__ == "__main__":
    # Part F — Manual Behaviour Checks
    print("--- Valid objects ---")
    alice = Patient(1, "Alice Smith", "0400 000 000")
    dr_doe = Practitioner(1, "Dr. John Doe", "General Practice")
    appt = Appointment(1, alice, dr_doe, "2024-07-20 10:00 AM")
    print(alice)
    print(dr_doe)
    print(appt)

    print()
    print("--- Invalid input ---")
    try:
        Patient(2, "", "x")
    except ValueError as e:
        print("Raised as expected:", e)

    print()
    print("--- Cancel a scheduled appointment ---")
    appt.cancel()
    print(appt)

    print()
    print("--- Illegal repeated transition (cancel a cancelled appointment) ---")
    try:
        appt.cancel()
    except InvalidStatusTransition as e:
        print("Raised as expected:", e)

    print()
    print("--- Illegal transition (reschedule a cancelled appointment) ---")
    try:
        appt.update_time("2024-07-21 09:00 AM")
    except InvalidStatusTransition as e:
        print("Raised as expected:", e)

    print()
    print("--- Confirming the Part D bypass no longer works (Part G fix) ---")
    try:
        appt.status = AppointmentStatus.SCHEDULED
    except AttributeError as e:
        print("Correctly blocked — status has no public setter:", e)