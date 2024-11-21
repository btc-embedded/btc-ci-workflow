from btc_embedded import migration_source, migration_target

# 2020a model files
old_model = {
    'model'  : 'examples/migration_suite/shc_2022b/Wrapper_seat_heating_control.slx',
    'script' : 'examples/migration_suite/shc_2022b/init_Wrapper_seat_heating_control.m',
    'scopeName' : 'runa1_sys'
}

# 2023b model files
new_model = {
    'model'  : 'examples/migration_suite/shc_2023b/Wrapper_seat_heating_control.slx',
    'script' : 'examples/migration_suite/shc_2023b/init_Wrapper_seat_heating_control.m',
    'scopeName' : 'runa1_sys'
}

# btc migration test
result = migration_source(old_model, '2022b', vector_gen_settings={ 'pllString' : 'MCDC' })
result = migration_target(new_model, '2023b')