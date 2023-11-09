% Init script for AUTOSAR wrapper model: Wrapper_seat_heating_control
init;



dsout_HeatingActivate_SetHeatingCoil_temp= Simulink.Signal;
dsout_HeatingActivate_SetHeatingCoil_temp.StorageClass = 'ExportedGlobal';
dsout_HeatingActivate_SetHeatingCoil_temp.DataType = 'IDT_Temperature';
dsout_HeatingActivate_SetHeatingCoil_temp.Dimensions = [1 1];
dsout_HeatingActivate_SetHeatingCoil_temp.Complexity = 'real';
dsout_HeatingActivate_SetHeatingCoil_temp.InitialValue = '';

dsin_HeatingRequest_GetButtonPressed_status= Simulink.Signal;
dsin_HeatingRequest_GetButtonPressed_status.StorageClass = 'ExportedGlobal';
dsin_HeatingRequest_GetButtonPressed_status.DataType = 'IDT_ButtonStatus';
dsin_HeatingRequest_GetButtonPressed_status.Dimensions = [1 1];
dsin_HeatingRequest_GetButtonPressed_status.Complexity = 'real';
dsin_HeatingRequest_GetButtonPressed_status.InitialValue = '';