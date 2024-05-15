from btc_embedded import migration_source, migration_target

# 2020a model files
old_model = {
    'model'  : 'shc_2020a/Wrapper_seat_heating_control.slx',
    'script' : 'shc_2020a/init_Wrapper_seat_heating_control.m'
}

# 2023b model files
new_model = {
    'model'  : 'shc_2023b/Wrapper_seat_heating_control.slx',
    'script' : 'shc_2023b/init_Wrapper_seat_heating_control.m'
}

# btc migration test
btc_project = migration_source(old_model, '2020a')
result = migration_target(new_model, '2023b', epp_file=btc_project)