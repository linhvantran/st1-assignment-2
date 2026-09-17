# AI Usage Documentation — Stage 1

## Part C — AI as Tutor

**Prompt used:**
> Act as a Python tutor. I am learning introductory software technology. Here is a small appointment-booking function. 1. Explain what the code does. 2. Identify three limitations. 3. Suggest improvements. 4. Do not rewrite the whole application. 5. Ask me two questions to test my understanding.

*(I pasted my `book_appointment` and `display_appointments` functions after this.)*

**What the AI said:**

1. What the code does: `book_appointment` creates a dictionary with patient, practitioner, and time, checks that the patient name isn't empty, and appends the appointment to the `appointments` list. `display_appointments` prints every stored appointment, or a message if the list is empty.

2. Three limitations it identified:
   - No validation for practitioner or appointment time — empty or invalid values could be added without warning.
   - No double-booking protection — the same practitioner could be booked at the same time multiple times.
   - The function assumes `appointments` already exists as a list; if it isn't defined before the function is called, the program crashes.

3. Suggested improvements: add checks for empty practitioner/time fields, add a double-booking check before appending, and add error handling or default initialization in case `appointments` is missing.

4. Questions it asked back:
   - What would happen if you called `book_appointment()` before defining the `appointments` list?
   - Why might a clinic need a double-booking check for practitioners?

**My answers to those questions:**
- If `book_appointment()` is called before `appointments = []` exists, Python raises a `NameError` because the function references a name that hasn't been defined yet — the function doesn't create the list itself, it only appends to one that's assumed to already exist.
- A clinic needs a double-booking check because a practitioner can only physically see one patient at a time. Without that check, the system would let two patients believe they both have the same appointment slot, and one of them would show up to find the practitioner already occupied.

## Part D — Generate an Alternative

**Prompt used:**
> Create a simple, beginner-friendly Python function that stores a patient name, a practitioner name, and an appointment time. Do not use a database. Do not use a GUI.

**AI-generated response:**
```python
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    return appointment
```
AI's summary of what it gave me: a small, self-contained function with basic validation on all three fields, using only an in-memory list — no database, no GUI, matching the prompt's restrictions. It offered to add double-booking checks, nicer printing, or time formatting as optional next steps, but didn't add them unprompted.

## Decisions

- **Accepted:** the dictionary structure — matches my own version, confirming I'd structured the data sensibly.
- **Noted, didn't adopt:** the AI version validates all three fields (patient, practitioner, time), while my human version only validates patient name. This is actually more thorough than mine — I'm keeping my version as the "official" prototype since it's the one I wrote and can fully explain line by line, but the gap is worth acknowledging rather than hiding.
- **Confirmed independently:** both versions share the same double-booking gap — the AI wasn't asked to fix it, and it didn't invent a fix I hadn't requested, which matches the "do not rewrite/extend beyond what's asked" instruction in Part D.