from pyscript import document

def checkmem(e):
    document.getElementById("output1").innerHTML = "" # clears previous result

    club_members = ["Johanna Ramos", "Julienne Miranda", "Kailey Gayas", "Hope Benitez", "Aaliyah Pangilinan"]

    first_name = document.getElementById("firstname").value
    last_name = document.getElementById("lastname").value

    new_first_name = first_name.title()
    new_last_name = last_name.title()

    full_name = new_first_name + " " + new_last_name

    confirm_mem = full_name in club_members

    message = (f'Sorry {new_first_name} {new_last_name}, your name is not on the list. Try again next year!' , f'Congrats! {new_first_name} {new_last_name}, you passed! You are now part of the Volleyball Varsity of OBMC.')

    document.getElementById("output1").innerHTML = message[confirm_mem]
