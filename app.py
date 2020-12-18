import obd
connection = obd.OBD("192.168.0.10",35000)
print("GET_CURRENT_DTC")
response = connection.query(obd.commands.GET_CURRENT_DTC)
print(response)
print("MIDS_A")
response = connection.query(obd.commands.MIDS_A)
print(response)
print("MONITOR_O2_B1S1")
response = connection.query(obd.commands.MONITOR_O2_B1S1)
print(response)
print("MONITOR_O2_B1S2")
response = connection.query(obd.commands.MONITOR_O2_B1S2)
print(response)
print("MONITOR_O2_B1S3")
response = connection.query(obd.commands.MONITOR_O2_B1S3)
print(response)
print("MONITOR_O2_B1S4")
response = connection.query(obd.commands.MONITOR_O2_B1S4)
print(response)
print("MONITOR_O2_B2S1")
response = connection.query(obd.commands.MONITOR_O2_B2S1)
print(response)
print("MONITOR_O2_B2S2")
response = connection.query(obd.commands.MONITOR_O2_B2S2)
print(response)
print("MONITOR_O2_B2S3")
response = connection.query(obd.commands.MONITOR_O2_B2S3)
print(response)
print("MONITOR_O2_B2S4")
response = connection.query(obd.commands.MONITOR_O2_B2S4)
print(response)
print("MONITOR_O2_B3S1")
response = connection.query(obd.commands.MONITOR_O2_B3S1)
print(response)
print("MONITOR_O2_B3S2")
response = connection.query(obd.commands.MONITOR_O2_B3S2)
print(response)
print("MONITOR_O2_B3S3")
response = connection.query(obd.commands.MONITOR_O2_B3S3)
print(response)
print("MONITOR_O2_B3S4")
response = connection.query(obd.commands.MONITOR_O2_B3S4)
print(response)
print("MONITOR_O2_B4S1")
response = connection.query(obd.commands.MONITOR_O2_B4S1)
print(response)
print("MONITOR_O2_B4S2")
response = connection.query(obd.commands.MONITOR_O2_B4S2)
print(response)
print("MONITOR_O2_B4S3")
response = connection.query(obd.commands.MONITOR_O2_B4S3)
print(response)
print("MONITOR_O2_B4S4")
response = connection.query(obd.commands.MONITOR_O2_B4S4)
print(response)
print("MIDS_B")
response = connection.query(obd.commands.MIDS_B)
print(response)
print("MONITOR_CATALYST_B1")
response = connection.query(obd.commands.MONITOR_CATALYST_B1)
print(response)
print("MONITOR_CATALYST_B2")
response = connection.query(obd.commands.MONITOR_CATALYST_B2)
print(response)
print("MONITOR_CATALYST_B3")
response = connection.query(obd.commands.MONITOR_CATALYST_B3)
print(response)
print("MONITOR_CATALYST_B4")
response = connection.query(obd.commands.MONITOR_CATALYST_B4)
print(response)
print("MONITOR_EGR_B1")
response = connection.query(obd.commands.MONITOR_EGR_B1)
print(response)
print("MONITOR_EGR_B2")
response = connection.query(obd.commands.MONITOR_EGR_B2)
print(response)
print("MONITOR_EGR_B3")
response = connection.query(obd.commands.MONITOR_EGR_B3)
print(response)
print("MONITOR_EGR_B4")
response = connection.query(obd.commands.MONITOR_EGR_B4)
print(response)
print("MONITOR_VVT_B1")
response = connection.query(obd.commands.MONITOR_VVT_B1)
print(response)
print("MONITOR_VVT_B2")
response = connection.query(obd.commands.MONITOR_VVT_B2)
print(response)
print("MONITOR_VVT_B3")
response = connection.query(obd.commands.MONITOR_VVT_B3)
print(response)
print("MONITOR_VVT_B4")
response = connection.query(obd.commands.MONITOR_VVT_B4)
print(response)
print("MONITOR_EVAP_150")
response = connection.query(obd.commands.MONITOR_EVAP_150)
print(response)
print("MONITOR_EVAP_090")
response = connection.query(obd.commands.MONITOR_EVAP_090)
print(response)
print("MONITOR_EVAP_040")
response = connection.query(obd.commands.MONITOR_EVAP_040)
print(response)
print("MONITOR_EVAP_020")
response = connection.query(obd.commands.MONITOR_EVAP_020)
print(response)
print("MONITOR_PURGE_FLOW")
response = connection.query(obd.commands.MONITOR_PURGE_FLOW)
print(response)
print("MIDS_C")
response = connection.query(obd.commands.MIDS_C)
print(response)
print("MONITOR_O2_HEATER_B1S1")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B1S1)
print(response)
print("MONITOR_O2_HEATER_B1S2")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B1S2)
print(response)
print("MONITOR_O2_HEATER_B1S3")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B1S3)
print(response)
print("MONITOR_O2_HEATER_B1S4")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B1S4)
print(response)
print("MONITOR_O2_HEATER_B2S1")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B2S1)
print(response)
print("MONITOR_O2_HEATER_B2S2")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B2S2)
print(response)
print("MONITOR_O2_HEATER_B2S3")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B2S3)
print(response)
print("MONITOR_O2_HEATER_B2S4")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B2S4)
print(response)
print("MONITOR_O2_HEATER_B3S1")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B3S1)
print(response)
print("MONITOR_O2_HEATER_B3S2")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B3S2)
print(response)
print("MONITOR_O2_HEATER_B3S3")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B3S3)
print(response)
print("MONITOR_O2_HEATER_B3S4")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B3S4)
print(response)
print("MONITOR_O2_HEATER_B4S1")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B4S1)
print(response)
print("MONITOR_O2_HEATER_B4S2")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B4S2)
print(response)
print("MONITOR_O2_HEATER_B4S3")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B4S3)
print(response)
print("MONITOR_O2_HEATER_B4S4")
response = connection.query(obd.commands.MONITOR_O2_HEATER_B4S4)
print(response)
print("MIDS_D")
response = connection.query(obd.commands.MIDS_D)
print(response)
print("MONITOR_HEATED_CATALYST_B1")
response = connection.query(obd.commands.MONITOR_HEATED_CATALYST_B1)
print(response)
print("MONITOR_HEATED_CATALYST_B2")
response = connection.query(obd.commands.MONITOR_HEATED_CATALYST_B2)
print(response)
print("MONITOR_HEATED_CATALYST_B3")
response = connection.query(obd.commands.MONITOR_HEATED_CATALYST_B3)
print(response)
print("MONITOR_HEATED_CATALYST_B4")
response = connection.query(obd.commands.MONITOR_HEATED_CATALYST_B4)
print(response)
print("MONITOR_SECONDARY_AIR_1")
response = connection.query(obd.commands.MONITOR_SECONDARY_AIR_1)
print(response)
print("MONITOR_SECONDARY_AIR_2")
response = connection.query(obd.commands.MONITOR_SECONDARY_AIR_2)
print(response)
print("MONITOR_SECONDARY_AIR_3")
response = connection.query(obd.commands.MONITOR_SECONDARY_AIR_3)
print(response)
print("MONITOR_SECONDARY_AIR_4")
response = connection.query(obd.commands.MONITOR_SECONDARY_AIR_4)
print(response)
print("MIDS_E")
response = connection.query(obd.commands.MIDS_E)
print(response)
print("MONITOR_FUEL_SYSTEM_B1")
response = connection.query(obd.commands.MONITOR_FUEL_SYSTEM_B1)
print(response)
print("MONITOR_FUEL_SYSTEM_B2")
response = connection.query(obd.commands.MONITOR_FUEL_SYSTEM_B2)
print(response)
print("MONITOR_FUEL_SYSTEM_B3")
response = connection.query(obd.commands.MONITOR_FUEL_SYSTEM_B3)
print(response)
print("MONITOR_FUEL_SYSTEM_B4")
response = connection.query(obd.commands.MONITOR_FUEL_SYSTEM_B4)
print(response)
print("MONITOR_BOOST_PRESSURE_B1")
response = connection.query(obd.commands.MONITOR_BOOST_PRESSURE_B1)
print(response)
print("MONITOR_BOOST_PRESSURE_B2")
response = connection.query(obd.commands.MONITOR_BOOST_PRESSURE_B2)
print(response)
print("MONITOR_NOX_ABSORBER_B1")
response = connection.query(obd.commands.MONITOR_NOX_ABSORBER_B1)
print(response)
print("MONITOR_NOX_ABSORBER_B2")
response = connection.query(obd.commands.MONITOR_NOX_ABSORBER_B2)
print(response)
print("MONITOR_NOX_CATALYST_B1")
response = connection.query(obd.commands.MONITOR_NOX_CATALYST_B1)
print(response)
print("MONITOR_NOX_CATALYST_B2")
response = connection.query(obd.commands.MONITOR_NOX_CATALYST_B2)
print(response)
print("MIDS_F")
response = connection.query(obd.commands.MIDS_F)
print(response)
print("MONITOR_MISFIRE_GENERAL")
response = connection.query(obd.commands.MONITOR_MISFIRE_GENERAL)
print(response)
print("MONITOR_MISFIRE_CYLINDER_1")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_1)
print(response)
print("MONITOR_MISFIRE_CYLINDER_2")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_2)
print(response)
print("MONITOR_MISFIRE_CYLINDER_3")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_3)
print(response)
print("MONITOR_MISFIRE_CYLINDER_4")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_4)
print(response)
print("MONITOR_MISFIRE_CYLINDER_5")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_5)
print(response)
print("MONITOR_MISFIRE_CYLINDER_6")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_6)
print(response)
print("MONITOR_MISFIRE_CYLINDER_7")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_7)
print(response)
print("MONITOR_MISFIRE_CYLINDER_8")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_8)
print(response)
print("MONITOR_MISFIRE_CYLINDER_9")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_9)
print(response)
print("MONITOR_MISFIRE_CYLINDER_10")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_10)
print(response)
print("MONITOR_MISFIRE_CYLINDER_11")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_11)
print(response)
print("MONITOR_MISFIRE_CYLINDER_12")
response = connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_12)
print(response)
print("MONITOR_PM_FILTER_B1")
response = connection.query(obd.commands.MONITOR_PM_FILTER_B1)
print(response)
print("CLEAR_DTC")
response = connection.query(obd.commands.CLEAR_DTC)
print(response)
print("GET_DTC")
response = connection.query(obd.commands.GET_DTC)
print(response)
print("STATUS")
response = connection.query(obd.commands.STATUS)
print(response)
print("FREEZE_DTC")
response = connection.query(obd.commands.FREEZE_DTC)
print(response)
print("FUEL_STATUS")
response = connection.query(obd.commands.FUEL_STATUS)
print(response)
print("ENGINE_LOAD")
response = connection.query(obd.commands.ENGINE_LOAD)
print(response)
print("COOLANT_TEMP")
response = connection.query(obd.commands.COOLANT_TEMP)
print(response)
print("SHORT_FUEL_TRIM_1")
response = connection.query(obd.commands.SHORT_FUEL_TRIM_1)
print(response)
print("LONG_FUEL_TRIM_1")
response = connection.query(obd.commands.LONG_FUEL_TRIM_1)
print(response)
print("SHORT_FUEL_TRIM_2")
response = connection.query(obd.commands.SHORT_FUEL_TRIM_2)
print(response)
print("LONG_FUEL_TRIM_2")
response = connection.query(obd.commands.LONG_FUEL_TRIM_2)
print(response)
print("FUEL_PRESSURE")
response = connection.query(obd.commands.FUEL_PRESSURE)
print(response)
print("INTAKE_PRESSURE")
response = connection.query(obd.commands.INTAKE_PRESSURE)
print(response)
print("RPM")
response = connection.query(obd.commands.RPM)
print(response)
print("SPEED")
response = connection.query(obd.commands.SPEED)
print(response)
print("TIMING_ADVANCE")
response = connection.query(obd.commands.TIMING_ADVANCE)
print(response)
print("INTAKE_TEMP")
response = connection.query(obd.commands.INTAKE_TEMP)
print(response)
print("MAF")
response = connection.query(obd.commands.MAF)
print(response)
print("THROTTLE_POS")
response = connection.query(obd.commands.THROTTLE_POS)
print(response)
print("AIR_STATUS")
response = connection.query(obd.commands.AIR_STATUS)
print(response)
print("O2_SENSORS")
response = connection.query(obd.commands.O2_SENSORS)
print(response)
print("O2_B1S1")
response = connection.query(obd.commands.O2_B1S1)
print(response)
print("O2_B1S2")
response = connection.query(obd.commands.O2_B1S2)
print(response)
print("O2_B1S3")
response = connection.query(obd.commands.O2_B1S3)
print(response)
print("O2_B1S4")
response = connection.query(obd.commands.O2_B1S4)
print(response)
print("O2_B2S1")
response = connection.query(obd.commands.O2_B2S1)
print(response)
print("O2_B2S2")
response = connection.query(obd.commands.O2_B2S2)
print(response)
print("O2_B2S3")
response = connection.query(obd.commands.O2_B2S3)
print(response)
print("O2_B2S4")
response = connection.query(obd.commands.O2_B2S4)
print(response)
print("OBD_COMPLIANCE")
response = connection.query(obd.commands.OBD_COMPLIANCE)
print(response)
print("O2_SENSORS_ALT")
response = connection.query(obd.commands.O2_SENSORS_ALT)
print(response)
print("AUX_INPUT_STATUS")
response = connection.query(obd.commands.AUX_INPUT_STATUS)
print(response)
print("RUN_TIME")
response = connection.query(obd.commands.RUN_TIME)
print(response)
print("PIDS_B")
response = connection.query(obd.commands.PIDS_B)
print(response)
print("DISTANCE_W_MIL")
response = connection.query(obd.commands.DISTANCE_W_MIL)
print(response)
print("FUEL_RAIL_PRESSURE_VAC")
response = connection.query(obd.commands.FUEL_RAIL_PRESSURE_VAC)
print(response)
print("FUEL_RAIL_PRESSURE_DIRECT")
response = connection.query(obd.commands.FUEL_RAIL_PRESSURE_DIRECT)
print(response)
print("O2_S1_WR_VOLTAGE")
response = connection.query(obd.commands.O2_S1_WR_VOLTAGE)
print(response)
print("O2_S2_WR_VOLTAGE")
response = connection.query(obd.commands.O2_S2_WR_VOLTAGE)
print(response)
print("O2_S3_WR_VOLTAGE")
response = connection.query(obd.commands.O2_S3_WR_VOLTAGE)
print(response)
print("O2_S4_WR_VOLTAGE")
response = connection.query(obd.commands.O2_S4_WR_VOLTAGE)
print(response)
print("O2_S5_WR_VOLTAGE")
response = connection.query(obd.commands.O2_S5_WR_VOLTAGE)
print(response)
print("O2_S6_WR_VOLTAGE")
response = connection.query(obd.commands.O2_S6_WR_VOLTAGE)
print(response)
print("O2_S7_WR_VOLTAGE")
response = connection.query(obd.commands.O2_S7_WR_VOLTAGE)
print(response)
print("O2_S8_WR_VOLTAGE")
response = connection.query(obd.commands.O2_S8_WR_VOLTAGE)
print(response)
print("COMMANDED_EGR")
response = connection.query(obd.commands.COMMANDED_EGR)
print(response)
print("EGR_ERROR")
response = connection.query(obd.commands.EGR_ERROR)
print(response)
print("EVAPORATIVE_PURGE")
response = connection.query(obd.commands.EVAPORATIVE_PURGE)
print(response)
print("FUEL_LEVEL")
response = connection.query(obd.commands.FUEL_LEVEL)
print(response)
print("WARMUPS_SINCE_DTC_CLEAR")
response = connection.query(obd.commands.WARMUPS_SINCE_DTC_CLEAR)
print(response)
print("DISTANCE_SINCE_DTC_CLEAR")
response = connection.query(obd.commands.DISTANCE_SINCE_DTC_CLEAR)
print(response)
print("EVAP_VAPOR_PRESSURE")
response = connection.query(obd.commands.EVAP_VAPOR_PRESSURE)
print(response)
print("BAROMETRIC_PRESSURE")
response = connection.query(obd.commands.BAROMETRIC_PRESSURE)
print(response)
print("O2_S1_WR_CURRENT")
response = connection.query(obd.commands.O2_S1_WR_CURRENT)
print(response)
print("O2_S2_WR_CURRENT")
response = connection.query(obd.commands.O2_S2_WR_CURRENT)
print(response)
print("O2_S3_WR_CURRENT")
response = connection.query(obd.commands.O2_S3_WR_CURRENT)
print(response)
print("O2_S4_WR_CURRENT")
response = connection.query(obd.commands.O2_S4_WR_CURRENT)
print(response)
print("O2_S5_WR_CURRENT")
response = connection.query(obd.commands.O2_S5_WR_CURRENT)
print(response)
print("O2_S6_WR_CURRENT")
response = connection.query(obd.commands.O2_S6_WR_CURRENT)
print(response)
print("O2_S7_WR_CURRENT")
response = connection.query(obd.commands.O2_S7_WR_CURRENT)
print(response)
print("O2_S8_WR_CURRENT")
response = connection.query(obd.commands.O2_S8_WR_CURRENT)
print(response)
print("CATALYST_TEMP_B1S1")
response = connection.query(obd.commands.CATALYST_TEMP_B1S1)
print(response)
print("CATALYST_TEMP_B2S1")
response = connection.query(obd.commands.CATALYST_TEMP_B2S1)
print(response)
print("CATALYST_TEMP_B1S2")
response = connection.query(obd.commands.CATALYST_TEMP_B1S2)
print(response)
print("CATALYST_TEMP_B2S2")
response = connection.query(obd.commands.CATALYST_TEMP_B2S2)
print(response)
print("PIDS_C")
response = connection.query(obd.commands.PIDS_C)
print(response)
print("STATUS_DRIVE_CYCLE")
response = connection.query(obd.commands.STATUS_DRIVE_CYCLE)
print(response)
print("CONTROL_MODULE_VOLTAGE")
response = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
print(response)
print("ABSOLUTE_LOAD")
response = connection.query(obd.commands.ABSOLUTE_LOAD)
print(response)
print("COMMANDED_EQUIV_RATIO")
response = connection.query(obd.commands.COMMANDED_EQUIV_RATIO)
print(response)
print("RELATIVE_THROTTLE_POS")
response = connection.query(obd.commands.RELATIVE_THROTTLE_POS)
print(response)
print("AMBIANT_AIR_TEMP")
response = connection.query(obd.commands.AMBIANT_AIR_TEMP)
print(response)
print("THROTTLE_POS_B")
response = connection.query(obd.commands.THROTTLE_POS_B)
print(response)
print("THROTTLE_POS_C")
response = connection.query(obd.commands.THROTTLE_POS_C)
print(response)
print("ACCELERATOR_POS_D")
response = connection.query(obd.commands.ACCELERATOR_POS_D)
print(response)
print("ACCELERATOR_POS_E")
response = connection.query(obd.commands.ACCELERATOR_POS_E)
print(response)
print("ACCELERATOR_POS_F")
response = connection.query(obd.commands.ACCELERATOR_POS_F)
print(response)
print("THROTTLE_ACTUATOR")
response = connection.query(obd.commands.THROTTLE_ACTUATOR)
print(response)
print("RUN_TIME_MIL")
response = connection.query(obd.commands.RUN_TIME_MIL)
print(response)
print("TIME_SINCE_DTC_CLEARED")
response = connection.query(obd.commands.TIME_SINCE_DTC_CLEARED)
print(response)
print("MAX_MAF")
response = connection.query(obd.commands.MAX_MAF)
print(response)
print("FUEL_TYPE")
response = connection.query(obd.commands.FUEL_TYPE)
print(response)
print("ETHANOL_PERCENT")
response = connection.query(obd.commands.ETHANOL_PERCENT)
print(response)
print("EVAP_VAPOR_PRESSURE_ABS")
response = connection.query(obd.commands.EVAP_VAPOR_PRESSURE_ABS)
print(response)
print("EVAP_VAPOR_PRESSURE_ALT")
response = connection.query(obd.commands.EVAP_VAPOR_PRESSURE_ALT)
print(response)
print("SHORT_O2_TRIM_B1")
response = connection.query(obd.commands.SHORT_O2_TRIM_B1)
print(response)
print("LONG_O2_TRIM_B1")
response = connection.query(obd.commands.LONG_O2_TRIM_B1)
print(response)
print("SHORT_O2_TRIM_B2")
response = connection.query(obd.commands.SHORT_O2_TRIM_B2)
print(response)
print("LONG_O2_TRIM_B2")
response = connection.query(obd.commands.LONG_O2_TRIM_B2)
print(response)
print("FUEL_RAIL_PRESSURE_ABS")
response = connection.query(obd.commands.FUEL_RAIL_PRESSURE_ABS)
print(response)
print("RELATIVE_ACCEL_POS")
response = connection.query(obd.commands.RELATIVE_ACCEL_POS)
print(response)
print("HYBRID_BATTERY_REMAINING")
response = connection.query(obd.commands.HYBRID_BATTERY_REMAINING)
print(response)
print("OIL_TEMP")
response = connection.query(obd.commands.OIL_TEMP)
print(response)
print("FUEL_INJECT_TIMING")
response = connection.query(obd.commands.FUEL_INJECT_TIMING)
print(response)
print("FUEL_RATE")
response = connection.query(obd.commands.FUEL_RATE)
print(response)