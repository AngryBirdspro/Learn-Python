camp_list = ['tent', 'sleeping bag','water','rasberry pi','coffee','knife','ethernet cable','flash drive','beard oil','marshmellows']
camp_site = ["twin towers",404,89.3,True]
print(type(camp_site))
camp_list.insert(0, 'paper')
camp_list.insert(-1, 'nothing')
camp_list.pop(0)
camp_list.pop(0)
me = camp_list[4]
print(me)
you = camp_list[-1]
print(you)
camp_list.insert(0, 'glock')
print(camp_list)
print(camp_list[-1])