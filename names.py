def convert_to_lua(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        f_out.write('Citizen.CreateThread(function()\n')
        for line in f_in:
            stripped_line = line.strip()
            if stripped_line:
                hash_code, value = stripped_line.split(' = ')
                f_out.write(f'    AddTextEntry("{
                            hash_code}", "{value}")\n')
        f_out.write('end)\n')


convert_to_lua('global.txt', 'vehicle_names.lua')
