sensors = ['GET_CURRENT_DTC','MIDS_A','MONITOR_O2_B1S1','MONITOR_O2_B1S2','MONITOR_O2_B1S3','MONITOR_O2_B1S4','MONITOR_O2_B2S1','MONITOR_O2_B2S2','MONITOR_O2_B2S3','MONITOR_O2_B2S4','MONITOR_O2_B3S1','MONITOR_O2_B3S2','MONITOR_O2_B3S3','MONITOR_O2_B3S4','MONITOR_O2_B4S1','MONITOR_O2_B4S2','MONITOR_O2_B4S3','MONITOR_O2_B4S4','','MIDS_B','MONITOR_CATALYST_B1','MONITOR_CATALYST_B2','MONITOR_CATALYST_B3','MONITOR_CATALYST_B4','','MONITOR_EGR_B1','MONITOR_EGR_B2','MONITOR_EGR_B3','MONITOR_EGR_B4','MONITOR_VVT_B1','MONITOR_VVT_B2','MONITOR_VVT_B3','MONITOR_VVT_B4','MONITOR_EVAP_150','MONITOR_EVAP_090','MONITOR_EVAP_040','MONITOR_EVAP_020','MONITOR_PURGE_FLOW','','MIDS_C','MONITOR_O2_HEATER_B1S1','MONITOR_O2_HEATER_B1S2','MONITOR_O2_HEATER_B1S3','MONITOR_O2_HEATER_B1S4','MONITOR_O2_HEATER_B2S1','MONITOR_O2_HEATER_B2S2','MONITOR_O2_HEATER_B2S3','MONITOR_O2_HEATER_B2S4','MONITOR_O2_HEATER_B3S1','MONITOR_O2_HEATER_B3S2','MONITOR_O2_HEATER_B3S3','MONITOR_O2_HEATER_B3S4','MONITOR_O2_HEATER_B4S1','MONITOR_O2_HEATER_B4S2','MONITOR_O2_HEATER_B4S3','MONITOR_O2_HEATER_B4S4','','MIDS_D','MONITOR_HEATED_CATALYST_B1','MONITOR_HEATED_CATALYST_B2','MONITOR_HEATED_CATALYST_B3','MONITOR_HEATED_CATALYST_B4','','MONITOR_SECONDARY_AIR_1','MONITOR_SECONDARY_AIR_2','MONITOR_SECONDARY_AIR_3','MONITOR_SECONDARY_AIR_4','','MIDS_E','MONITOR_FUEL_SYSTEM_B1','MONITOR_FUEL_SYSTEM_B2','MONITOR_FUEL_SYSTEM_B3','MONITOR_FUEL_SYSTEM_B4','MONITOR_BOOST_PRESSURE_B1','MONITOR_BOOST_PRESSURE_B2','','MONITOR_NOX_ABSORBER_B1','MONITOR_NOX_ABSORBER_B2','','MONITOR_NOX_CATALYST_B1','MONITOR_NOX_CATALYST_B2','','MIDS_F','MONITOR_MISFIRE_GENERAL','MONITOR_MISFIRE_CYLINDER_1','MONITOR_MISFIRE_CYLINDER_2','MONITOR_MISFIRE_CYLINDER_3','MONITOR_MISFIRE_CYLINDER_4','MONITOR_MISFIRE_CYLINDER_5','MONITOR_MISFIRE_CYLINDER_6','MONITOR_MISFIRE_CYLINDER_7','MONITOR_MISFIRE_CYLINDER_8','MONITOR_MISFIRE_CYLINDER_9','MONITOR_MISFIRE_CYLINDER_10','MONITOR_MISFIRE_CYLINDER_11','MONITOR_MISFIRE_CYLINDER_12','','MONITOR_PM_FILTER_B1','CLEAR_DTC','GET_DTC','STATUS','FREEZE_DTC','FUEL_STATUS','ENGINE_LOAD','COOLANT_TEMP','SHORT_FUEL_TRIM_1','LONG_FUEL_TRIM_1','SHORT_FUEL_TRIM_2','LONG_FUEL_TRIM_2','FUEL_PRESSURE','INTAKE_PRESSURE','RPM','SPEED','TIMING_ADVANCE','INTAKE_TEMP','MAF','THROTTLE_POS','AIR_STATUS','O2_SENSORS','O2_B1S1','O2_B1S2','O2_B1S3','O2_B1S4','O2_B2S1','O2_B2S2','O2_B2S3','O2_B2S4','OBD_COMPLIANCE','O2_SENSORS_ALT','AUX_INPUT_STATUS','RUN_TIME','PIDS_B','DISTANCE_W_MIL','FUEL_RAIL_PRESSURE_VAC','FUEL_RAIL_PRESSURE_DIRECT','O2_S1_WR_VOLTAGE','O2_S2_WR_VOLTAGE','O2_S3_WR_VOLTAGE','O2_S4_WR_VOLTAGE','O2_S5_WR_VOLTAGE','O2_S6_WR_VOLTAGE','O2_S7_WR_VOLTAGE','O2_S8_WR_VOLTAGE','COMMANDED_EGR','EGR_ERROR','EVAPORATIVE_PURGE','FUEL_LEVEL','WARMUPS_SINCE_DTC_CLEAR','DISTANCE_SINCE_DTC_CLEAR','EVAP_VAPOR_PRESSURE','BAROMETRIC_PRESSURE','O2_S1_WR_CURRENT','O2_S2_WR_CURRENT','O2_S3_WR_CURRENT','O2_S4_WR_CURRENT','O2_S5_WR_CURRENT','O2_S6_WR_CURRENT','O2_S7_WR_CURRENT','O2_S8_WR_CURRENT','CATALYST_TEMP_B1S1','CATALYST_TEMP_B2S1','CATALYST_TEMP_B1S2','CATALYST_TEMP_B2S2','PIDS_C','STATUS_DRIVE_CYCLE','CONTROL_MODULE_VOLTAGE','ABSOLUTE_LOAD','COMMANDED_EQUIV_RATIO','RELATIVE_THROTTLE_POS','AMBIANT_AIR_TEMP','THROTTLE_POS_B','THROTTLE_POS_C','ACCELERATOR_POS_D','ACCELERATOR_POS_E','ACCELERATOR_POS_F','THROTTLE_ACTUATOR','RUN_TIME_MIL','TIME_SINCE_DTC_CLEARED','unsupported','MAX_MAF','FUEL_TYPE','ETHANOL_PERCENT','EVAP_VAPOR_PRESSURE_ABS','EVAP_VAPOR_PRESSURE_ALT','SHORT_O2_TRIM_B1','LONG_O2_TRIM_B1','SHORT_O2_TRIM_B2','LONG_O2_TRIM_B2','FUEL_RAIL_PRESSURE_ABS','RELATIVE_ACCEL_POS','HYBRID_BATTERY_REMAINING','OIL_TEMP','FUEL_INJECT_TIMING','FUEL_RATE']

print('import obd')
print('connection = obd.OBD("192.168.0.10",35000)')
for sensor in sensors:
	print('print("' + sensor + '")')
	print('response = connection.query(obd.commands.' + sensor + ')')
	print('print(response)')