from sys import exit

number_of_code_lines = raw_input('Hany sor kodot irtal az evben? ')

if not number_of_code_lines.isdigit():
    print('Egesz szam megadasa kotelezo')
    exit(1)

number_of_code_lines = int(number_of_code_lines)

if number_of_code_lines < 1000:
    print('kodolj tovabb')
    exit(0)

is_member = raw_input('Tag vagy (y/n)? ').strip().lower() == 'y'

if not is_member:
    print('Mar csak tagga kell valnod')
    exit(0)

paid = raw_input('Fizettel a honapban tagdijat (y/n)? ').lower() == 'y'

if paid:
    print('Wohoo')
    exit(0)

print('meeh')
