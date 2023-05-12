% -------------------------------------------------------------------
%  Generated by MATLAB on 15-Jun-2021 12:13:48
%  MATLAB version: 9.7.0.1471314 (R2019b) Update 7
% -------------------------------------------------------------------
                               

IDT_ButtonStatus = Simulink.AliasType;
IDT_ButtonStatus.Description = '';
IDT_ButtonStatus.DataScope = 'Auto';
IDT_ButtonStatus.HeaderFile = 'Rte_Type.h';
IDT_ButtonStatus.BaseType = 'boolean';

IDT_SeatStatus = Simulink.AliasType;
IDT_SeatStatus.Description = '';
IDT_SeatStatus.DataScope = 'Auto';
IDT_SeatStatus.HeaderFile = 'Rte_Type.h';
IDT_SeatStatus.BaseType = 'boolean';

IDT_Temperature = Simulink.AliasType;
IDT_Temperature.Description = '';
IDT_Temperature.DataScope = 'Auto';
IDT_Temperature.HeaderFile = 'Rte_Type.h';
IDT_Temperature.BaseType = 'uint8';

P_IDT_ButtonStatus = Simulink.Parameter;
P_IDT_ButtonStatus.Value = 0;
P_IDT_ButtonStatus.CoderInfo.StorageClass = 'Auto';
P_IDT_ButtonStatus.Description = '';
P_IDT_ButtonStatus.DataType = 'IDT_ButtonStatus';
P_IDT_ButtonStatus.Min = [];
P_IDT_ButtonStatus.Max = [];
P_IDT_ButtonStatus.DocUnits = '';

P_IDT_Temperature = Simulink.Parameter;
P_IDT_Temperature.Value = 0;
P_IDT_Temperature.CoderInfo.StorageClass = 'Auto';
P_IDT_Temperature.Description = '';
P_IDT_Temperature.DataType = 'IDT_Temperature';
P_IDT_Temperature.Min = [];
P_IDT_Temperature.Max = [];
P_IDT_Temperature.DocUnits = '';

TemperatureRanges_TemperatureStage1 = AUTOSAR.Parameter;
TemperatureRanges_TemperatureStage1.Value = 30;
TemperatureRanges_TemperatureStage1.CoderInfo.StorageClass = 'Custom';
TemperatureRanges_TemperatureStage1.CoderInfo.Alias = '';
TemperatureRanges_TemperatureStage1.CoderInfo.Alignment = -1;
TemperatureRanges_TemperatureStage1.CoderInfo.CustomStorageClass = ...
  'CalPrm';
TemperatureRanges_TemperatureStage1.CoderInfo.CustomAttributes.HeaderFile = '';
TemperatureRanges_TemperatureStage1.CoderInfo.CustomAttributes.ElementName = ...
  'TemperatureStage1';
TemperatureRanges_TemperatureStage1.CoderInfo.CustomAttributes.PortName = ...
  'TemperatureRanges';
TemperatureRanges_TemperatureStage1.CoderInfo.CustomAttributes.InterfacePath = ...
  '/Interfaces/IF_TemperatureValues';
TemperatureRanges_TemperatureStage1.CoderInfo.CustomAttributes.CalibrationComponent = '';
TemperatureRanges_TemperatureStage1.CoderInfo.CustomAttributes.ProviderPortName = '';
TemperatureRanges_TemperatureStage1.Description = '';
TemperatureRanges_TemperatureStage1.DataType = 'IDT_Temperature';
TemperatureRanges_TemperatureStage1.Min = [];
TemperatureRanges_TemperatureStage1.Max = [];
TemperatureRanges_TemperatureStage1.DocUnits = '';
TemperatureRanges_TemperatureStage1.SwCalibrationAccess = 'ReadWrite';
TemperatureRanges_TemperatureStage1.DisplayFormat = '';

TemperatureRanges_TemperatureStage2 = AUTOSAR.Parameter;
TemperatureRanges_TemperatureStage2.Value = 35;
TemperatureRanges_TemperatureStage2.CoderInfo.StorageClass = 'Custom';
TemperatureRanges_TemperatureStage2.CoderInfo.Alias = '';
TemperatureRanges_TemperatureStage2.CoderInfo.Alignment = -1;
TemperatureRanges_TemperatureStage2.CoderInfo.CustomStorageClass = ...
  'CalPrm';
TemperatureRanges_TemperatureStage2.CoderInfo.CustomAttributes.HeaderFile = '';
TemperatureRanges_TemperatureStage2.CoderInfo.CustomAttributes.ElementName = ...
  'TemperatureStage2';
TemperatureRanges_TemperatureStage2.CoderInfo.CustomAttributes.PortName = ...
  'TemperatureRanges';
TemperatureRanges_TemperatureStage2.CoderInfo.CustomAttributes.InterfacePath = ...
  '/Interfaces/IF_TemperatureValues';
TemperatureRanges_TemperatureStage2.CoderInfo.CustomAttributes.CalibrationComponent = '';
TemperatureRanges_TemperatureStage2.CoderInfo.CustomAttributes.ProviderPortName = '';
TemperatureRanges_TemperatureStage2.Description = '';
TemperatureRanges_TemperatureStage2.DataType = 'IDT_Temperature';
TemperatureRanges_TemperatureStage2.Min = [];
TemperatureRanges_TemperatureStage2.Max = [];
TemperatureRanges_TemperatureStage2.DocUnits = '';
TemperatureRanges_TemperatureStage2.SwCalibrationAccess = 'ReadWrite';
TemperatureRanges_TemperatureStage2.DisplayFormat = '';

TemperatureRanges_TemperatureStage3 = AUTOSAR.Parameter;
TemperatureRanges_TemperatureStage3.Value = 45;
TemperatureRanges_TemperatureStage3.CoderInfo.StorageClass = 'Custom';
TemperatureRanges_TemperatureStage3.CoderInfo.Alias = '';
TemperatureRanges_TemperatureStage3.CoderInfo.Alignment = -1;
TemperatureRanges_TemperatureStage3.CoderInfo.CustomStorageClass = ...
  'CalPrm';
TemperatureRanges_TemperatureStage3.CoderInfo.CustomAttributes.HeaderFile = '';
TemperatureRanges_TemperatureStage3.CoderInfo.CustomAttributes.ElementName = ...
  'TemperatureStage3';
TemperatureRanges_TemperatureStage3.CoderInfo.CustomAttributes.PortName = ...
  'TemperatureRanges';
TemperatureRanges_TemperatureStage3.CoderInfo.CustomAttributes.InterfacePath = ...
  '/Interfaces/IF_TemperatureValues';
TemperatureRanges_TemperatureStage3.CoderInfo.CustomAttributes.CalibrationComponent = '';
TemperatureRanges_TemperatureStage3.CoderInfo.CustomAttributes.ProviderPortName = '';
TemperatureRanges_TemperatureStage3.Description = '';
TemperatureRanges_TemperatureStage3.DataType = 'IDT_Temperature';
TemperatureRanges_TemperatureStage3.Min = [];
TemperatureRanges_TemperatureStage3.Max = [];
TemperatureRanges_TemperatureStage3.DocUnits = '';
TemperatureRanges_TemperatureStage3.SwCalibrationAccess = 'ReadWrite';
TemperatureRanges_TemperatureStage3.DisplayFormat = '';

RTE_OK = 0;

try
    SeatHeatControl_defineIntEnumTypes
end
