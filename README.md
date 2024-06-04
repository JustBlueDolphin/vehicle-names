# vehicle-names
global.txt to vehicle_names.lua


- Open your selected cars dlc.rpf in OpenIV
- Find americandlc.RPF
    - `dlc.rpf\x64\data\lang` 
- Export the global.gxt2 to txt
- It should be named global global.txt
- Run the tool
- Copy output to your selected car
- Rename it to `vehicle_names`

Add to the fxmanifest of your car of choice:
>>>>>>> main
`client_script 'vehicle_names.lua'`
