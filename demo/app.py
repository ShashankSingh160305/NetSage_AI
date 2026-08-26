import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)

from checker.diagnose import diagnose


print("=" * 50)
print("              NetSage AI")
print("        Network Fault Diagnosis")
print("=" * 50)

print("\nDescribe your network problem.")
print("Example: PC0 cannot reach the default gateway")

symptom = input("\nEnter problem: ")

result = diagnose(symptom)

print("\n" + "=" * 50)
print("                 DIAGNOSIS")
print("=" * 50)

if result["status"] == "No matching case found":

    print("\nNo matching network case was found.")
    print("Try describing the problem differently.")

else:

    print(f"\nCase ID       : {result['case_id']}")
    print(f"Symptom       : {result['symptom']}")
    print(f"Fault         : {result['expected_fault']}")
    print(f"OSI Layer     : {result['osi_layer']}")
    print(f"Concept       : {result['concept']}")
    print(f"Severity      : {result['severity']}")
    print(f"Recommendation: {result['recommendation']}")

print("\n" + "=" * 50)