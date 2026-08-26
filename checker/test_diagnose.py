from diagnose import diagnose


test_cases = [
    "PC0 cannot reach the default gateway",
    "PC0 cannot communicate with PC1",
    "PC0 has an incorrect default gateway",
    "PC1 cannot reach router",
    "VLAN 10 PC cannot communicate with VLAN 20 PC",
]


for symptom in test_cases:

    print("\n==============================")
    print("Input:", symptom)
    print("==============================")

    result = diagnose(symptom)

    print("Case ID:", result.get("case_id"))
    print("Fault:", result.get("expected_fault"))
    print("OSI Layer:", result.get("osi_layer"))
    print("Concept:", result.get("concept"))
    print("Severity:", result.get("severity"))