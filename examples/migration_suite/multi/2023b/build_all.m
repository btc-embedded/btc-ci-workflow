% Define the directory containing the SLX files
directory = '.'; % Current directory

run('init.m');

% Get a list of all SLX files in the directory
slxFiles = dir(fullfile(directory, '*.slx'));

% Iterate over each SLX file
for i = 1:numel(slxFiles)
    slxFile = slxFiles(i).name;
    disp(['Building model ', slxFile]);
    
    % Build the model using slbuild
    try
        [~, modelName, ~] = fileparts(slxFile); % Extract model name without extension
        slbuild(modelName);
        disp(['Build successful for ', modelName]);
    catch e
        disp(['Error building ', modelName, ': ', e.message]);
    end

end
