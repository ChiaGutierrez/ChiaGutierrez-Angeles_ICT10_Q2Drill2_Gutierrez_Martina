
from pyscript import document, when

# Predefined sets for each grade
grade7 = {
    "Chris P. Bacon",
    "Deedee Megan Dodo",
    "Angelina Huli",
    "christina Angel"
}

grade8 = {
    "Sum Ting Wong",
    "Rudy Pastine",
    "Joe Kerr"
}

grade9 = {
    "Luke Dunphy",
    "Alex Dunphy",
    "Hailey Dunphy"
}

grade10 = {
    "Ron Weasley",
    "Hermione Granger",
    "Harry Potter"
}

# Set for new members
new_members = set()

# Combine all grade sets
all_members = grade7 | grade8 | grade9 | grade10 | new_members


# Function to display all members
def update_results():
    all_members = grade7 | grade8 | grade9 | grade10 | new_members

    member_list = "<br>".join(sorted(all_members))

    document.getElementById("results").innerHTML = f"""
        All members:<br>
        {member_list}<br>
        Total members: {len(all_members)}
    """


# Function to add a new member
@when("click", "#add_member")
def add_member(event):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    new_member = first_name + " " + last_name

    new_members.add(new_member)

    update_results()

    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""


# Display initial members
update_results()
