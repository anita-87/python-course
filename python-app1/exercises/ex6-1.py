file = open('../files/members.txt', 'r')
members = file.readlines()
file.close()

member = input("Add a new member: ")
members.append(member+ "\n")
file = open('../files/members.txt', 'w')
file.writelines(members)
file.close()
