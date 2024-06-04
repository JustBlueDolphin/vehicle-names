open iv 
find americandlc.rpf 
export the golbal.gxt2 to txt
rename it to `input`
copy output to your selected car 
rename it to `vehicle_names`

add to the fxmanifest this:
`client_script 'vehicle_names.lua'`