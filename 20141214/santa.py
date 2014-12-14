def quiz():

    ret = {'number_of_code_lines': 'unknown',
           'member': 'unknown',
           'paid_member': 'unknown'}

    number_of_code_lines = raw_input('Hany sor kodot irtal az evben? ')
    if not number_of_code_lines.isdigit():
        print('Egesz szam megadasa kotelezo')
        return ret

    ret['number_of_code_lines'] = int(number_of_code_lines)

    if ret['number_of_code_lines'] < 1000:
        print('kodolj tovabb')
        return ret

    ret['member'] = raw_input('Tag vagy (y/n)? ').strip().lower() == 'y'

    if not ret['member']:
        print('Mar csak tagga kell valnod')
        ret['paid_member'] = False
        return ret

    ret['paid_member'] = raw_input('Fizettel a honapban tagdijat (y/n)?').lower() == 'y'

    if ret['paid_member']:
        print('Wohoo')
    else:
        print('meeh')

    return ret
