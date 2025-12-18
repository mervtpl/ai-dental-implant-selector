def generate_txt_report(
    patient_info,
    special_conditions,
    selected_parameters,
    ai_result
):
    report = f"""
AI Dental Implant Recommendation Report
=======================================

PATIENT INFORMATION
-------------------
Age: {patient_info['age']}
Bone Type: {patient_info['bone_type']}
Jaw Region: {patient_info['jaw_region']}
Bone Density: {patient_info['bone_density']}
Smoking Status: {patient_info['smoking']}
Allergy Risk: {patient_info['allergy']}
Aesthetic Priority: {patient_info['aesthetic']}
Budget Level: {patient_info['budget']}

SPECIAL CLINICAL CONDITIONS
---------------------------
Diabetes: {special_conditions['diabetes']}
Bruxism: {special_conditions['bruxism']}

SELECTED LITERATURE PARAMETERS
------------------------------
"""

    for p in selected_parameters:
        report += f"- {p}\n"

    report += f"""

AI-BASED RECOMMENDATION
----------------------
{ai_result}

DISCLAIMER
----------
This output is generated using an AI-assisted,
literature-based decision support system.
It does not replace clinical judgment.
"""

    return report
