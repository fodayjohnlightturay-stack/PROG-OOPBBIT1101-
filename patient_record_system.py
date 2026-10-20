"""
patient_record_system.py
=================================================================
PATIENT RECORD SYSTEM
PROG211 - Object-Oriented Programming 1, Individual Assignment 1

Problem: many clinics keep patient records on paper, so files get
lost and doctors cannot see a patient's past visits.
Solution: a simple program that stores each patient's visit history
and lets doctors add new visits.

Privacy (DPG): patients are identified only by ID, age group, blood
group and district. No names, phone numbers, addresses or dates of
birth are stored, and nothing is saved to disk.

Sections:  1 - Classes   2 - Data storage   3 - Menu
Run with:  python patient_record_system.py
=================================================================
"""

from datetime import date


# #################################################################
# SECTION 1 - CLASSES
# #################################################################

# =================================================================
# UML Diagram for Patient Class
# +-----------------------------------------------------+
# |                      Patient                        |
# +-----------------------------------------------------+
# | + system_name: str              (class attribute)   |
# | + AGE_GROUPS: tuple             (class attribute)   |
# | + BLOOD_GROUPS: tuple           (class attribute)   |
# | + total_patients: int           (class attribute)   |
# | - patient_id, age_group, blood_group, district: str |
# | - visits: tuple of (date, doctor, diagnosis, treat) |
# +-----------------------------------------------------+
# | + add_visit(doctor, diagnosis, treatment): None     |
# | + display_info(): None                              |
# | + display_record(): None                            |
# | + update_record(blood_group, district): None        |
# | + from_string(text): Patient      (classmethod)     |
# | + get_total_patients(): int       (classmethod)     |
# | + patient_removed(): None         (classmethod)     |
# | + is_valid_id(patient_id): bool   (staticmethod)    |
# +-----------------------------------------------------+
# =================================================================

class Patient:
    # Class attributes (shared by all patients)
    system_name = "PATIENT RECORD SYSTEM"
    AGE_GROUPS = ("Child (0-12)", "Teen (13-17)", "Adult (18-59)", "Senior (60+)")
    BLOOD_GROUPS = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
    total_patients = 0

    # Constructor
    def __init__(self, patient_id, age_group, blood_group, district):
        Patient.total_patients += 1
        self.patient_id = patient_id      # e.g. "PAT-001"
        self.age_group = age_group        # Age group instead of date of birth
        self.blood_group = blood_group    # e.g. "O+"
        self.district = district          # e.g. "Bo"
        self.visits = ()                  # Tuple of visit records

    # Instance method: add one visit as a tuple
    def add_visit(self, doctor, diagnosis, treatment):
        visit = (date.today(), doctor.doctor_id, diagnosis, treatment)
        self.visits = self.visits + (visit,)

    # Instance method: show the patient's basic details
    def display_info(self):
        print(f"\nPatient ID  : {self.patient_id}")
        print(f"Age group   : {self.age_group}")
        print(f"Blood group : {self.blood_group}")
        print(f"District    : {self.district}")
        print(f"Visits      : {len(self.visits)}")

    # Instance method: show the details plus the full visit history
    def display_record(self):
        self.display_info()
        for visit_date, doctor_id, diagnosis, treatment in self.visits:   # Tuple unpacking
            print(f"  {visit_date} | {doctor_id} | {diagnosis} -> {treatment}")

    # Instance method: update the patient's record (None = keep the old value)
    def update_record(self, blood_group=None, district=None):
        if blood_group is not None:
            self.blood_group = blood_group
        if district is not None:
            self.district = district
        print(f"Record for {self.patient_id} updated: {self.blood_group}, {self.district}.")

    # Class method: create a Patient from text, e.g. "PAT-002, Adult (18-59), A+, Kenema"
    @classmethod
    def from_string(cls, text):
        patient_id, age_group, blood_group, district = [x.strip() for x in text.split(",")]
        return cls(patient_id, age_group, blood_group, district)

    # Class method: total number of patients
    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    # Class method: lower the count when a patient is deleted
    @classmethod
    def patient_removed(cls):
        cls.total_patients -= 1

    # Static method: check the ID format, e.g. "PAT-001"
    @staticmethod
    def is_valid_id(patient_id):
        return patient_id.startswith("PAT-") and patient_id[4:].isdigit()


# =================================================================
# UML Diagram for Doctor Class
# +-----------------------------------------------------+
# |                       Doctor                        |
# +-----------------------------------------------------+
# | + total_doctors: int            (class attribute)   |
# | - doctor_id, department: str                        |
# | - patients_seen: int                                |
# +-----------------------------------------------------+
# | + treat(patient, diagnosis, treatment): None        |
# | + display_info(): None                              |
# | + get_total_doctors(): int        (classmethod)     |
# | + is_valid_text(text): bool       (staticmethod)    |
# +-----------------------------------------------------+
# =================================================================

class Doctor:
    total_doctors = 0

    def __init__(self, doctor_id, department):
        Doctor.total_doctors += 1
        self.doctor_id = doctor_id      # e.g. "DOC-01"
        self.department = department    # e.g. "General Medicine"
        self.patients_seen = 0

    # Instance method: OBJECT INTERACTION - a Doctor updates a Patient's record
    def treat(self, patient, diagnosis, treatment):
        patient.add_visit(self, diagnosis, treatment)
        self.patients_seen += 1
        print(f"{self.doctor_id} recorded a visit for {patient.patient_id}.")

    def display_info(self):
        print(f"{self.doctor_id:<8}{self.department:<20}Patients seen: {self.patients_seen}")

    @classmethod
    def get_total_doctors(cls):
        return cls.total_doctors

    # Static method: check text is not empty
    @staticmethod
    def is_valid_text(text):
        return text.strip() != ""


# Doctors are fixed for the clinic, so they are stored in a TUPLE
DOCTORS = (Doctor("DOC-01", "General Medicine"),
           Doctor("DOC-02", "Paediatrics"),
           Doctor("DOC-03", "Maternity"))


# #################################################################
# SECTION 2 - DATA STORAGE (Dictionary: patient ID -> Patient)
# #################################################################

patient_records = {}


def add_patient(patient):
    if patient.patient_id in patient_records:
        print("This patient ID already exists.")
        Patient.patient_removed()
        return
    patient_records[patient.patient_id] = patient
    print(f"Patient {patient.patient_id} registered.")


def find_patient(patient_id):
    return patient_records.get(patient_id)


def delete_patient(patient_id):
    if patient_records.pop(patient_id, None) is None:
        print("Patient not found.")
    else:
        Patient.patient_removed()
        print(f"Patient {patient_id} deleted.")


def display_all_patients():
    if not patient_records:
        print("No patients registered.")
        return
    print(f"\n{'ID':<10}{'Age Group':<16}{'Blood':<7}{'District':<20}Visits")
    for p in patient_records.values():
        print(f"{p.patient_id:<10}{p.age_group:<16}{p.blood_group:<7}{p.district:<20}{len(p.visits)}")


# #################################################################
# SECTION 3 - MENU
# #################################################################

def choose(options, label=str):
    for i, option in enumerate(options, 1):
        print(f"  {i}. {label(option)}")
    pick = input("Choose: ").strip()
    if pick.isdigit() and 1 <= int(pick) <= len(options):
        return options[int(pick) - 1]
    print("Invalid choice.")
    return None


def register_patient():
    patient_id = input("Patient ID (e.g. PAT-004): ").strip().upper()
    if not Patient.is_valid_id(patient_id):
        print("Invalid ID. Use the format PAT-001.")
        return
    print("Age group:")
    age_group = choose(Patient.AGE_GROUPS)
    print("Blood group:")
    blood_group = choose(Patient.BLOOD_GROUPS)
    district = input("District: ").strip().title()
    if age_group and blood_group and Doctor.is_valid_text(district):
        add_patient(Patient(patient_id, age_group, blood_group, district))


def record_visit():
    patient = find_patient(input("Patient ID: ").strip().upper())
    if patient is None:
        print("Patient not found.")
        return
    print("Doctor:")
    doctor = choose(DOCTORS, label=lambda d: f"{d.doctor_id} - {d.department}")
    if doctor is None:
        return
    diagnosis = input("Diagnosis: ").strip()
    treatment = input("Treatment: ").strip()
    if Doctor.is_valid_text(diagnosis) and Doctor.is_valid_text(treatment):
        doctor.treat(patient, diagnosis, treatment)
    else:
        print("Diagnosis and treatment cannot be empty.")


def load_sample_data():
    if patient_records:
        print("Sample data already loaded.")
        return
    add_patient(Patient.from_string("PAT-001, Child (0-12), O+, Bo"))
    add_patient(Patient.from_string("PAT-002, Adult (18-59), A+, Kenema"))
    add_patient(Patient("PAT-003", "Senior (60+)", "B-", "Western Area Urban"))
    DOCTORS[1].treat(patient_records["PAT-001"], "Malaria", "ACT tablets")
    DOCTORS[0].treat(patient_records["PAT-002"], "Typhoid", "Antibiotics")
    DOCTORS[0].treat(patient_records["PAT-003"], "Hypertension", "Blood pressure medication")


def main():
    while True:
        print(f"\n===== {Patient.system_name} =====")
        print("1. Register a patient\n2. Record a visit\n3. View a patient record")
        print("4. View all patients\n5. Update a patient record\n6. Delete a patient")
        print("7. View doctors\n8. Load sample data\n0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_patient()
        elif choice == "2":
            record_visit()
        elif choice == "3":
            patient = find_patient(input("Patient ID: ").strip().upper())
            if patient:
                patient.display_record()
            else:
                print("Patient not found.")
        elif choice == "4":
            display_all_patients()
        elif choice == "5":
            patient = find_patient(input("Patient ID: ").strip().upper())
            if patient:
                print("New blood group:")
                new_group = choose(Patient.BLOOD_GROUPS)
                new_district = input("New district (press Enter to keep): ").strip().title()
                patient.update_record(new_group, new_district or None)
            else:
                print("Patient not found.")
        elif choice == "6":
            delete_patient(input("Patient ID to delete: ").strip().upper())
        elif choice == "7":
            for doctor in DOCTORS:
                doctor.display_info()
            print(f"Total doctors: {Doctor.get_total_doctors()}")
        elif choice == "8":
            load_sample_data()
        elif choice == "0":
            print(f"Total patients: {Patient.get_total_patients()}. Goodbye!")
            break
        else:
            print("Invalid option. Please type a number from the menu.")


if __name__ == "__main__":
    main()
