from database import create_database_and_tables, add_box, get_all_boxes, get_box, get_container, add_box_to_container,seed_data, get_all_containers, get_all_freight
from tabulate import tabulate

def retrieve_numeric_input(called):
    input_ok = False
    n = None

    while not input_ok:
        n = input(f"\nEnter {called} ")

        try:
            n = float(n)
            input_ok = True

        except ValueError:
            print("Please provide a numeric input")

    return n


def add_box_menu():
    box_name = input("\nEnter a name for the box: ")
    box_height = retrieve_numeric_input(called="The box's height in meters: ")
    box_width = retrieve_numeric_input(called="The box's width in meters: ")
    box_length = retrieve_numeric_input(called="The box's length in meters: ")

    add_box(connection, (box_name, box_height,box_width, box_length))

def display_box_types():
    boxes = get_all_boxes(connection)

    print("\n" + tabulate(boxes,
        headers=["box_id", "box_name", "height", "width", "length"],
        tablefmt="psql" + "\n"
                            ))

def load_box_menu():
    n = input("Enter the name of the box: ")

    box = get_box(connection, by_name=n)

    if not box:
        print("A box by that name could not be found.")
    else:
        box_dims = box.height * box.width * box.length
        container_id = input("Enter the id of the container to load the box to: ")

        container = get_container(connection, by_id=container_id)

        if container is None:
            add_box_to_container(connection, box.id, container_id)

        elif container.occupied_volume + box_dims <= 30:
            add_box_to_container(connection, box.id, container_id)

        else:
            print(f"Container {container_id} does not have enough space.")

def display_containers():
    containers = get_all_containers(connection)
    print("\n" + tabulate(containers, headers =["container_id", "occupied_volume"], tablefmt=  "fancy_grid") + "\n")

def display_summary():
    freight = get_all_freight(connection)
    containers = get_all_containers(connection) or ()

    nr_containers = len(containers)

    if not nr_containers:
        print("\nThere is no contracted freight.\n")
        return

    contracted_volume = sum([c.occupied_volume for c in containers])
    revenue = round(contracted_volume * 40,2)
    cost = nr_containers * config.get('COST_PER_CONTAINER')

    print(f"\nContracted {len(freight)} box(es) in {len(containers)} containers(s).")
    print(f"The total contracted volume is {contracted_volume} m3.")
    print(f"Estimated cost of carrying this freight is: ${cost}.")
    print(f"Estimated P/L: ${round(revenue - cost,2)}\n")

def main_menu():
    print("\nWelcome to Freight Manager")

    print("""
            1. Add a box type
            2. Show box types
            3. Load box to container
            4. Show container
            5. Summary Report
            x. Close
            """)

    n = 0

    while n != "x":
        n = input("\nYour Choice: ").lower()

        match n:
            case "1":
                add_box_menu()

            case "2":
                display_box_types()

            case "3":
                load_box_menu()

            case "4":
                display_containers()

            case "5":
                print("Choice 5 Selected")

            case "x":
                print("Goodbye!")

            case _:
                print("Invalid input")

if __name__ == "__main__":
    connection = create_database_and_tables(filename="freight_prod.db")
    seed_data(connection)
    config = get_config(connection)
    main_menu()
    connection.close()


