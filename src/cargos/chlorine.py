from cargo import Cargo

cargo = Cargo(id = 'chlorine',
              type_name = 'string(STR_CARGO_NAME_CHLORINE)',
              unit_name = 'string(STR_CARGO_NAME_CHLORINE)',
              type_abbreviation = 'string(STR_CID_CHLORINE)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              cargo_payment_list_colour = '13',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_LIQUID, CC_HAZARDOUS)',
              cargo_label = 'CHLO',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '82',
              items_of_cargo = 'string(STR_CARGO_UNIT_CHLORINE)',
              penalty_lowerbound = '12',
              single_penalty_length = '255',
              price_factor = '84',
              capacity_multiplier = '1',
              icon_indices = (12, 3))

