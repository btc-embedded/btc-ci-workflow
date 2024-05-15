import glob

from btc_embedded import migration_suite_source, migration_suite_target

# Old Matlab: 2020a
old_ml = '2020a'

# List of models to test: 2020a/*.slx
old_models = [{
    'model' : slx,
    'script' : f'multi/{old_ml}/init.m'
} for slx in glob.glob(f'multi/{old_ml}/*.slx')]

# Record reference behavior
results = migration_suite_source(old_models, old_ml)

# New Matlab: 2023b
new_ml = '2023b'

# List of models to test: 2023b/*.slx
new_models = [{
    'model' : slx,
    'script' : f'multi/{new_ml}/init.m'
} for slx in glob.glob(f'multi/{new_ml}/*.slx')]

# Perform migration test vs. reference behavior
results = migration_suite_target(new_models, new_ml, model_results=results, accept_interface_changes=True)
