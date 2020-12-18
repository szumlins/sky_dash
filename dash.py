import obd
import time
import os
connection = obd.OBD("192.168.0.10",35000)

while True:
	coolant = connection.query(obd.commands.COOLANT_TEMP) #Celsius
	boost = connection.query(obd.commands.INTAKE_PRESSURE) #kPa
	voltage = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE) #volts

	
	coolant_display = str(round(float(coolant.value.magnitude) * 1.8 + 32,2))
	boost_display = str(round(float(boost.value.magnitude) / 6.895 - 14.696,2))
	voltage_display = str(round(float(voltage.value.magnitude),2))
	os.system('clear')	
	print("Coolant Temp: " + coolant_display + " F")
	print("Boost: " + boost_display + " psi")
	print("Voltage: " + voltage_display + "v")

	time.sleep(.2)	
