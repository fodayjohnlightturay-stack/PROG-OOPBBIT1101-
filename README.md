# Patient Record System

PROG211 – Object-Oriented Programming 1, Individual Assignment 1.

## Problem
Many clinics keep patient records on paper, so files get lost and doctors cannot see a patient's past visits. This program stores each patient's visit history and lets doctors add new visits.

## How to Run
Requires Python 3.8+ (no extra libraries).
```
python patient_record_system.py
```
Choose **option 8** first to load sample data.

| Option | Action | Option | Action |
|---|---|---|---|
| 1 | Register a patient | 5 | Update a patient record |
| 2 | Record a visit | 6 | Delete a patient |
| 3 | View a patient record | 7 | View doctors |
| 4 | View all patients | 8 | Load sample data |
| | | 0 | Exit |

## OOP Requirements
| Requirement | Where in the code |
|---|---|
| Classes and objects | `Patient` and `Doctor`; created by constructor or `Patient.from_string()` |
| Object interaction | `doctor.treat(patient, diagnosis, treatment)` adds a visit to a patient |
| Data structure | Dictionary `patient_records` (patient ID → Patient object) |
| Tuples (bonus) | `AGE_GROUPS`, `BLOOD_GROUPS`, `DOCTORS`; each visit is a `(date, doctor, diagnosis, treatment)` tuple |
| Instance methods | `add_visit()`, `display_info()`, `display_record()`, `update_record()`, `treat()` |
| Class methods | `from_string()`, `get_total_patients()`, `patient_removed()`, `get_total_doctors()` |
| Static methods | `is_valid_id()`, `is_valid_text()` |

## DPG Alignment
- **Open source:** public repository under the [MIT License](LICENSE).
- **Inclusive and accessible:** simple text menu, works offline on any computer with Python, clear error messages.
- **Privacy-respecting:** patients are identified only by ID, age group, blood group and district. No names, contacts or dates of birth are stored, and nothing is saved to disk.
- **Modular and reusable:** classes, data storage and menu are separate sections.

## Sample Output
```
ID        Age Group       Blood  District            Visits
PAT-001   Child (0-12)    O+     Bo                  1
PAT-002   Adult (18-59)   A+     Kenema              1
PAT-003   Senior (60+)    B-     Western Area Urban  1
```
```
Patient ID  : PAT-004
Age group   : Adult (18-59)
Blood group : O+
District    : Port Loko
Visits      : 1
  2026-10-20 | DOC-01 | Pneumonia -> Antibiotics and rest
```

## GitHub
The lecturer has been added as a collaborator on this repository.

## Author
[Your Full Name] – Student ID: [Your Student ID], Limkokwing University of Creative Technology
