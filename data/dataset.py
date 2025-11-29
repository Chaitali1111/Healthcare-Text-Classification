import csv
import random

# Categories
categories = [
    "Cardiology",
    "Neurology",
    "Endocrinology",
    "Orthopedics",
    "Gastroenterology",
    "General Medicine",
    "Pulmonology",
    "Dermatology"
]

# Some text templates per category
templates = {
    "Cardiology": [
        "Patient reports chest pain and shortness of breath.",
        "Complaints of palpitations and irregular heartbeat.",
        "Severe chest discomfort during walking or climbing stairs.",
        "History of hypertension with recent chest tightness.",
        "Pain radiating to left arm with sweating and nausea."
    ],
    "Neurology": [
        "Patient reports frequent headaches and dizziness.",
        "Complaints of sudden loss of balance and blurred vision.",
        "History of seizures and loss of consciousness.",
        "Numbness and tingling in arms and legs.",
        "MRI suggests possible lesion in frontal lobe."
    ],
    "Endocrinology": [
        "Blood sugar levels are consistently very high.",
        "Patient has increased thirst and frequent urination.",
        "Complaints of weight gain and fatigue, possible thyroid issue.",
        "Diabetic foot ulcer showing slow healing.",
        "Insulin dosage adjustment recommended after lab results."
    ],
    "Orthopedics": [
        "Severe knee pain after sports injury, swelling noticed.",
        "Complaints of lower back pain radiating to the leg.",
        "Shoulder stiffness and difficulty lifting the arm.",
        "Pain in hip joint while walking long distances.",
        "Post-fracture follow-up with mild residual pain."
    ],
    "Gastroenterology": [
        "Patient complains of abdominal pain after meals.",
        "Symptoms include nausea, vomiting, and stomach cramps.",
        "Burning sensation in chest and sour belching.",
        "History of acidity and irregular bowel movements.",
        "Loose stools and dehydration for the last two days."
    ],
    "General Medicine": [
        "High fever with sore throat and body ache.",
        "Complaints of fatigue and loss of appetite.",
        "Mild cough and cold for past three days.",
        "General weakness and disturbed sleep pattern.",
        "Headache, low-grade fever, and joint pain."
    ],
    "Pulmonology": [
        "Persistent dry cough and shortness of breath.",
        "Wheezing sounds during breathing, especially at night.",
        "Difficulty breathing on exertion, history of smoking.",
        "Chest congestion and thick sputum production.",
        "Shortness of breath worsening when lying down."
    ],
    "Dermatology": [
        "Itchy red rashes on both arms and legs.",
        "Dry, flaky skin with occasional burning sensation.",
        "Small fluid-filled blisters on palms and fingers.",
        "Dark patches on face with mild itching.",
        "Scalp itching with dandruff and hair fall."
    ]
}

def generate_rows(num_rows: int = 500):
    rows = []
    for _ in range(num_rows):
        category = random.choice(categories)
        text = random.choice(templates[category])
        rows.append({"text": text, "category": category})
    return rows

def main():
    rows = generate_rows(500)
    filename = "healthcare_text_dataset_500.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "category"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} rows to {filename}")

if __name__ == "__main__":
    main()
