import obd
import guizero
import random

connection = obd.OBD("192.168.0.10",35000)

refresh = 1000 #in MS

def update_temp():
	try:
		get_coolant = connection.query(obd.commands.COOLANT_TEMP) #Celsius
		new_temp = round(float(get_coolant.value.magnitude) * 1.8 + 32,2)
	except:
		new_temp = float(temp.value)
	print(new_temp)
	if new_temp >= 220:
		temp.bg ='red'
		temp.text_color = 'white'
	else:
		temp.bg ='black'
		temp.text_color = 'red'
	temp.value = str("{:.2f}".format(new_temp))	

def update_boost():
	try:
		get_boost = connection.query(obd.commands.INTAKE_PRESSURE) #kPa
		new_boost = round(float(get_boost.value.magnitude) / 6.895 - 14.696,2)
	except:
		new_boost = float(boost.value)
	print(new_boost)
	if new_boost >= 17:
		boost.bg ='red'
		boost.text_color = 'white'
	else:
		boost.bg ='black'
		boost.text_color = 'red'
	boost.value = str("{:.2f}".format(new_boost))

def update_voltage():
	try:
		get_voltage = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE) #volts
		new_voltage = round(float(get_voltage.value.magnitude),2)
	except:
		new_voltage = float(voltage.value)
	print(new_voltage)
	if new_voltage <= 11:
		voltage.bg ='red'
		voltage.text_color = 'white'
	else:
		voltage.bg ='black'
		voltage.text_color = 'red'
	voltage.value = str("{:.2f}".format(new_voltage))

text_size=100
font_choice="Courier"
app = guizero.App(width="750",height="320",bg="black")

title_box = guizero.Box(app,height="fill",align="left",layout="grid")

title_temp = guizero.Text(title_box, grid=[0,0], align="left", text="T: ",font=font_choice,size=text_size,color="white")
title_boost = guizero.Text(title_box, grid=[0,1],align="left", text="B: ",font=font_choice,size=text_size,color="white")
title_voltage = guizero.Text(title_box, grid=[0,2],align="left", text="V: ",font=font_choice,size=text_size,color="white")

value_box = guizero.Box(app,align="left",height="fill",layout="grid")

temp = guizero.Text(value_box, grid=[0,0],align="right",width="6",text="-00.00",font=font_choice,size=text_size,color="red")
temp.repeat(refresh,update_temp)

boost = guizero.Text(value_box, grid=[0,1],align="right",width="6",text="-00.00",font=font_choice,size=text_size,color="red")
boost.repeat(refresh,update_boost)

voltage = guizero.Text(value_box, grid=[0,2],align="right",width="6",text="-00.00",font=font_choice,size=text_size,color="red")
voltage.repeat(refresh,update_voltage)

unit_box =  guizero.Box(app,height="fill",align="right",layout="grid")

unit_temp = guizero.Text(unit_box, grid=[0,0], text=u"\N{DEGREE SIGN} F",font=font_choice,size=text_size,color="white")
unit_boost = guizero.Text(unit_box, grid=[0,1], text="PSI",font=font_choice,size=text_size,color="white")
unit_voltage = guizero.Text(unit_box, grid=[0,2], text="VDC",font=font_choice,size=text_size,color="white")



app.display()
