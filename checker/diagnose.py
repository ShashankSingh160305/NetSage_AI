import csv
import os


CASES_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "cases",
    "cases.csv"
)


def load_cases():
    cases = []

    with open(CASES_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cases.append(row)

    return cases


def diagnose(symptom):
    cases = load_cases()

    symptom = symptom.lower()

    best_case = None
    best_score = 0

    for case in cases:
        case_symptom = case["symptom"].lower()

        words = symptom.split()
        score = sum(word in case_symptom for word in words)

        if score > best_score:
            best_score = score
            best_case = case

    if best_case is None:
        return {
            "status": "No matching case found"
        }

    recommendations = {
        "CASE001": "Check the router interface status and enable GigabitEthernet0/0 if it is administratively down.",
        "CASE002": "Check the switch ports connected to PC0 and PC1 and verify their configuration.",
        "CASE003": "Verify the PC default gateway and make sure it matches the router interface address.",
        "CASE004": "Check the IP address and subnet mask configured on PC1.",
        "CASE005": "Check connectivity between PC0, the switch and Router1.",
        "CASE006": "Check VLAN configuration and verify that inter-VLAN routing is configured.",
        "CASE007": "Verify VLAN membership and switch port configuration.",
        "CASE008": "Check whether the VLAN exists and whether the required ports belong to it.",
        "CASE009": "Check the trunk configuration and verify that the required VLANs are allowed.",
        "CASE010": "Verify router subinterfaces, VLAN IDs and trunk configuration.",
        "CASE011": "Check the DHCP configuration and verify that the client is connected correctly.",
        "CASE012": "Verify the DHCP pool and network configuration.",
        "CASE013": "Check the DHCP pool network and default gateway settings.",
        "CASE014": "Verify DHCP pool availability and configuration.",
        "CASE015": "Check DNS configuration and test connectivity to the DNS server.",
        "CASE016": "Verify the DNS server address and DNS service configuration.",
        "CASE017": "Check connectivity between the client and DNS server.",
        "CASE018": "Verify the DHCP-assigned IP configuration and gateway.",
        "CASE019": "Check the routing table and verify a route exists to the remote network.",
        "CASE020": "Verify the routing configuration and next-hop information.",
        "CASE021": "Check the connection and IP configuration between the routers.",
        "CASE022": "Verify routes after the topology change.",
        "CASE023": "Check ACL rules that may be blocking the traffic.",
        "CASE024": "Review the ACL and verify whether the required server traffic is permitted.",
        "CASE025": "Check the ACL for a subnet-wide deny rule.",
        "CASE026": "Verify ACL direction, interface and rule ordering.",
        "CASE027": "Check NAT configuration and translation rules.",
        "CASE028": "Verify NAT inside/outside interfaces and translation rules.",
        "CASE029": "Check NAT configuration and the internal/external network settings.",
        "CASE030": "Check the wireless configuration, SSID and client network settings."
    }

    return {
        "status": "Match found",
        "case_id": best_case["case_id"],
        "symptom": best_case["symptom"],
        "expected_fault": best_case["expected_fault"],
        "osi_layer": best_case["osi_layer"],
        "concept": best_case["concept_tag"],
        "severity": best_case["severity"],
        "recommendation": recommendations.get(
            best_case["case_id"],
            "Check the network configuration related to this issue."
        )
    }


if __name__ == "__main__":

    print("================================")
    print("       NetSage AI Checker")
    print("================================")

    user_input = input("\nEnter network problem: ")

    result = diagnose(user_input)

    print("\nDiagnosis")
    print("--------------------------------")

    for key, value in result.items():
        print(f"{key}: {value}")