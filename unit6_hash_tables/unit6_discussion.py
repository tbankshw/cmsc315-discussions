def show_reservations(label, reservations):
    print(f"{label}: {reservations}")


def main():
    print("=== RESTAURANT RESERVATION HASH TABLE ===")

    reservations = {
        "R1001": "Jordan Lee - 2 guests",
        "R1002": "Avery Patel - 4 guests",
        "R1003": "Morgan Chen - 3 guests",
        "R1004": "Taylor Smith - 6 guests",
        "R1005": "Casey Brown - 2 guests",
    }

    print("\n=== INSERT OPERATIONS ===")
    show_reservations("Five reservations stored by confirmation number", reservations)
    reservations["R1006"] = "Riley Johnson - 5 guests"
    print("Added R1006 for Riley Johnson")
    show_reservations("After insertion", reservations)

    print("\n=== LOOKUP OPERATIONS ===")
    for confirmation in ("R1002", "R1005"):
        print(f"{confirmation}: {reservations[confirmation]}")

    print("\n=== UPDATE OPERATIONS ===")
    show_reservations("Before updating R1003", reservations)
    reservations["R1003"] = "Morgan Chen - 5 guests"
    print(f"Updated R1003: {reservations['R1003']}")
    show_reservations("After update", reservations)

    print("\n=== DELETE OPERATIONS ===")
    show_reservations("Before deleting R1004", reservations)
    removed = reservations.pop("R1004")
    print(f"Deleted R1004: {removed}")
    show_reservations("After deletion", reservations)

    print("\n=== EDGE CASES ===")
    missing_lookup = reservations.get("R9999", "Reservation not found")
    print(f"Missing lookup R9999: {missing_lookup}")
    missing_delete = reservations.pop("R9999", None)
    print(f"Safe deletion of R9999 changed the table: {missing_delete is not None}")
    empty_reservations = {}
    print(f"Empty reservation table contains entries: {bool(empty_reservations)}")
    reservations["R1007"] = "Duplicate Guest - 2 guests"
    reservations["R1007"] = "Duplicate Guest - 4 guests"
    print(f"Repeated key R1007 keeps one updated record: {reservations['R1007']}")

    print("\n=== FINAL RESERVATION TABLE ===")
    show_reservations("Current reservations", reservations)


if __name__ == "__main__":
    main()
