payroll = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}


payroll['emp3']['salary'] = 8500


del payroll['emp3']
payroll['emp4'] = {'name': 'Humberto', 'salary': 7000}


for key in payroll.items():
    print("Nombre ", key[0], " salario ", key[1])
