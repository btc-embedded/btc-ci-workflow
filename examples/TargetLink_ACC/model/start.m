% Initialization scipt for accController Demo model

% Initialize Enums
Simulink.defineIntEnumType('Pedal', ...
                            {'noPedal', 'brkPedal', 'gasPedal'}, [0;1;2],...
                            'AddClassNameToEnumNames', false);
Simulink.defineIntEnumType('vehicleDistanceRange', ...
                            {'long', 'medium', 'short', 'extraShort'}, [0;1;2;3], ...
                            'AddClassNameToEnumNames', false);

% Initialize Paramters
p_outputUpdDelayTimer = 200;        % [10 .. 1000]
pMaxAccAcceleration = 1.5;          % [0.1 .. 4]
pMaxAccDeacceleration = -1.5;       % [-0.01 .. -4]
pMaxOperatingSpeed = 180;           % [100 .. 250]
pMinOperatingSpeed = 30;            % [15 .. 50]

% Initialize Parameter Look-Up-Table
pLutAccelnSeverity = [0, 0.005, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.6, 1, 3, ...
                      5, 10, 17, 24, 32, 45, 60, 75, 100];

pLutAccelMagnitude = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, ...
                      2.5, 3, 3.5, 4, 4.5, 5, 8, 12, 20];

% Model Sample Time                
tSample = 0.01;