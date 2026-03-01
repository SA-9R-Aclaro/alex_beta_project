from pyscript import document

teams = {
    "Train": {
        "team_name": "Yellow Tigers"
    },
    "Garrison": {
        "team_name": "Blue Bears"
    },
    "Scout": {
        "team_name": "Green Hornets"
    },
    "MP": {
        "team_name": "Red Bulldogs"
    }
}

def team_checker(event):
    team_select = document.querySelector("#Regiment").value
    leader_input = document.querySelector("#leader_input").value
    
    member1 = document.querySelector("#member1").value
    member2 = document.querySelector("#member2").value
    member3 = document.querySelector("#member3").value
    member4 = document.querySelector("#member4").value
    member5 = document.querySelector("#member5").value
    
    members = [m for m in [member1, member2, member3, member4, member5] if m.strip()]
    
    if team_select in teams:
        team_info = teams[team_select]
        
        if not leader_input.strip():
            document.querySelector("#leader").textContent = "Please enter a team leader name"
            return
        
        if not members:
            document.querySelector("#output").textContent = "Please enter at least one team member name"
            return
        
        leader_div = document.querySelector("#leader")
        leader_div.textContent = f"Leader: {leader_input} ({team_info['team_name']})"
        
        members_div = document.querySelector("#output")
        members_text = "Team Members: " + ", ".join(members)
        members_div.textContent = members_text
    else:
        document.querySelector("#output").textContent = "Please select a team"
