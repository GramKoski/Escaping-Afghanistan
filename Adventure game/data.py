from classes_v2 import *

# Characters:

Dadullah = Character('Dadullah the Taliban General', 'There is no god but god')
Ghulam = Character('Ghulam the Pashtun Villager', 'Salaam. You are welcome in my home.')
Taliban = Character('Taliban', 'Afghanistan Zindabad!')





# Things:
ak = Thing('AK-47', 'Automatic Assualt Rifle. Perfect for looting the Taliban headquarters')
helicopter = Thing('helicopter', 'Blackhawk Helicopter left over from the war. Luckily you learned how to fly one. It only has enough gas to get to Kabul.')
ticket = Thing('plane ticket', 'With this ticket you can board a flight to the USA.')



# Places:

Kunar = Place('Kunar Province','Kunar is a mountainous area of Afghanistan located east of Kabul. There are many people here that follow Pashtunwali (tribal law) and will give you asylum.', [Taliban], [], False)
Village = Place('village', 'Small Pashtun farming community located in the hills of Kunar province. They offer asylum according to tribal law but there are police around. You cannot stay for long.', [Ghulam, Taliban], [helicopter], False)
Kabul = Place('Kabul', 'Capital of Afghanistan. You must get in to the Kabul International Airport in order to escape to the USA', [], [], True)
bazaar = Place('Mandai Bazaar', 'Largest bazaar in Kabul. They have many cheap, unregistered russian and american guns that you can buy', [Taliban], [ak], False)
headquarters = Place('Taliban Military Headquarters', 'Inside is high-ranking Taliban general Dadullah. He has executed journalists and translators, and confiscated thier plane tickets. The tickets are sitting on his desk.', [Dadullah, Taliban], [ticket], False)
airport = Place('Kabul International Airport', 'Here you can board a flight to the USA.', [], [],  False)

 


# Exits:
Kunar.add_exits([Village])
Village.add_exits([Kabul])
Kabul.add_exits([bazaar, airport, headquarters])
bazaar.add_exits([Kabul])
headquarters.add_exits([Kabul])
airport.add_exits([Kabul])




# Player:
me = Player('Abdhul, Afghan-american translator', Kunar, [])


