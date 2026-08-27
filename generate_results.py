import csv
import os

from checker.diagnose import diagnose


CASES_FILE = os.path.join("cases", "cases.csv")
RESULTS_DIR = "results"
RESULTS_FILE = os.path.join(RESULTS_DIR, "results.csv")


def generate_results():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    results = []

    with open(CASES_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for case in reader:
            case_id = case["case_id"]
            symptom = case["symptom"]
            expected_fault = case["expected_fault"]

            result = diagnose(symptom)

            ai_root_cause = result.get("expected_fault", "")
            match = ai_root_cause == expected_fault

            results.append({
                "case_id": case_id,
                "symptom": symptom,
                "expected_fault": expected_fault,
                "ai_root_cause": ai_root_cause,
                "osi_layer": result.get("osi_layer", ""),
                "concept": result.get("concept", ""),
                "severity": result.get("severity", ""),
                "recommendation": result.get("recommendation", ""),
                "match": match,
                "diagnosis_source": "rule_based"
            })

    fieldnames = [
        "case_id",
        "symptom",
        "expected_fault",
        "ai_root_cause",
        "osi_layer",
        "concept",
        "severity",
        "recommendation",
        "match",
        "diagnosis_source"
    ]

    with open(RESULTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("====================================")
    print("NetSage AI - Results Generator")
    print("====================================")
    print(f"Processed cases : {len(results)}")
    print(f"Results file    : {RESULTS_FILE}")
    print("====================================")


if __name__ == "__main__":
    generate_results()