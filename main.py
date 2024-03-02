import random

print("Final Fantasy VII")
print("'The world will be saved. But will you?' A strange and calm voice recites these words in Cloud's head, a first class soldier turned into a merc. 'What ya looking at merc?!' yelled Barret, as they boarded the train. Their mission, blow up a mako reactor belonging to shinra, a megacorp that uses mako, life´s and earth´s source of energy as fuel. Cloud simply shakes his head, ignoring Barret and the rest of the crew. They were five in total. They rode the train and arrive at the reactors station, only to be ambushed by shinra guards. What will your action be?'\n")

charhp_cloud = 100
charhp_barret = 120
shinra_guardhp = 35
scorpion_shinrahp = 200
tank_shinrahp = 110

while charhp_cloud > 0 and shinra_guardhp > 0:
  chardmg = random.randrange(1, 30)
  healing_materia = random.randrange(1, 9)
  
  command = input("Type one of the commands below:\nAttack\nDefend\nHeal\n")
  if command == "Attack":
    enemydmg = random.randrange(1, 30)
    shinra_guardhp -= enemydmg
    print(f"You have dealt {enemydmg} to the shinra guards. The shinra guards have {shinra_guardhp} hp left.\n")
  elif command == "Defend":
    enemydmg = random.randrange(1, 30)
    charhp_cloud -= enemydmg
    print(f"You took {enemydmg} damage. You still have {charhp_cloud} left.\n")
  elif command == "Heal":
    charhp_cloud += healing_materia
    print(f"You have healed {healing_materia} hp. You now have {charhp_cloud} hp.\n")
  if shinra_guardhp == 0:
    print("Shinra guards have been defeated.\n")
    break
  else:
    print("Enter a valid command.")
# The loop will end when either the character or the shinra guard is defeated.

print("After your battle against the shinra guard, Cloud approaches the leader of the so called Avalanche, Barret. Hes is a big man, using a machine gun instead of his right arm. Right next to him, you see a cheerfull man named Biggs, a naive looking Wedge and a extroverted Jessie. Barret is still a little unsure about cloud, but joins him when they have to separate from the others. As they approach the reactor's core, they decide to plant the bomb. Barret leaves the time decision to Cloud. He can choose between setting up to 20 minutes or 10 minutes. Choose one of the options: \n")

if command == "10 minutes":
  print("Cloud is confident enough that they can make it in 10 minutes. 'A little cocky, don´t ya think?' Says Barret. As they prepare to leave the reactor, a strange noise is heard. They look arround and see a scorpion, a very dangerous mettalic creature. Battle is iminent, so they get ready to strike. Choose one of the options: \n")

while charhp_cloud > 0 and scorpion_shinrahp > 0:
  chardmg = random.randrange(1, 30)
  healing_materia = random.randrange(1, 9)
  command = input("Type one of the commands below:\nAttack\nDefend\nHeal\n")
  if command == "Attack":
      enemydmg = random.randrange(1, 30)
      scorpion_shinrahp -= enemydmg
      print(f"You have dealt {enemydmg} to the scorpion. The scorpion has {scorpion_shinrahp} hp left.\n")
  elif command == "Defend":
      enemydmg = random.randrange(1, 30)
      charhp_cloud -= enemydmg
      print(f"You took {enemydmg} damage. You still have {charhp_cloud} left.\n")
  elif command == "Heal":
      charhp_cloud += healing_materia
      print(f"You have healed {healing_materia} hp. You now have {charhp_cloud} hp.\n")
  if scorpion_shinrahp == 0:
      print("Scorpion has been defeated.\n")
      break
  elif command == "20 minutes":
    print("Cloud feels very cautious about it, so he sets it to 20 minutes. 'Scared are ya?' says Barret. 'No. I´m just not stupid enough to blow this whole thing wihout thinking about it.' Cloud says to Barret. As they prepare to leave the reactor, a strange noise is heard. They look arround, and see a giant tank, controlled remotely by someone at shinra. They prepare for battle. Choose one of the options: \n")

  while charhp_cloud > 0 and tank_shinrahp > 0:
    chardmg = random.randrange(1, 30)
    healing_materia = random.randrange(1, 9)
    command = input("Type one of the commands below:\nAttack\nDefend\nHeal\n")
    if command == "Attack":
        enemydmg = random.randrange(1, 30)
        tank_shinrahp -= enemydmg
        print(f"You have dealt {enemydmg} to the tank. The tank has {tank_shinrahp} hp left.\n")
    elif command == "Defend":
        enemydmg = random.randrange(1, 30)
        charhp_cloud -= enemydmg
        print(f"You took {enemydmg} damage. You still have {charhp_cloud} left.\n")
    elif command == "Heal":
        charhp_cloud += healing_materia
        print(f"You have healed {healing_materia} hp. You now have {charhp_cloud} hp.\n")
    if scorpion_shinrahp == 0:
        print("Shinra tank has been defeated.\n")