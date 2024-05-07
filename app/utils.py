def map_dr_severity(severity_level):
    severity_map = {
        0: "No DR",
        1: "Mild",
        2: "Moderate",
        3: "Severe",
        4: "Proliferative DR"
    }
    return severity_map.get(severity_level, "Unknown")