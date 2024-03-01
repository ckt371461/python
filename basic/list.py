christopher = {}
christopher['First'] = 'Chirstopher'
christopher['Last'] = 'Harrison'

susan = {}
susan['First'] = 'Susan'
susan['Last'] = 'Ibach'

people = []
people.append(christopher)
people.append(susan)
people.append({
    'First' : 'Bill', 'last' : 'Gates'
})
presenters  = people[0:2]
print(people)
print()
print(presenters)