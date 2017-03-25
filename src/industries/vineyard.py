"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='vineyard',
                    map_colour='86',
                    prob_in_game='3',
                    prob_random='10',
                    prospect_chance='0.75',
                    name='string(STR_IND_VINEYARD)',
                    extra_text_fund='string(STR_FUND_VINEYARD)',
                    layouts='AUTO',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(require_cluster=['vineyard', [20, 72, 1, 4]]),
                    prod_cargo_types=['BEER', 'FRUT'],
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_PLANTATION))',
                    fund_cost_multiplier='54',
                    prod_multiplier='[11, 8]',
                    override_default_construction_states=True)

industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].prod_multiplier = '[9, 9]'


industry.add_tile(id='vineyard_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='vineyard_tile_2', # house
             	  autoslope='return CB_RESULT_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'vineyard_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'vineyard_house',
    sprites = [(10, 10, 64, 59, -31, -28)],
)
spriteset_2 = industry.add_spriteset(
    id = 'vineyard_shed',
    sprites = [(80, 10, 64, 59, -31, -28)],
)

industry.add_spritelayout(
    id = 'vineyard_house_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
)
industry.add_spritelayout(
    id = 'vineyard_shed_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
)
industry.add_magic_spritelayout(
    type = 'slope_aware_trees',
    base_id = 'vineyard_slope_aware_ground_with_trees',
    config = {'ground_sprite': 4164,
              'trees_default': [1620, 1633, 1689, 1620]}
)

industry.add_industry_layout(
    id = 'vineyard_layout_1',
    layout = [(0, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 2, 'vineyard_tile_2', 'vineyard_shed_spritelayout'),
              (1, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 2, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (2, 1, 'vineyard_tile_2', 'vineyard_house_spritelayout'),
              (2, 2, 'vineyard_tile_2', 'vineyard_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'vineyard_layout_2',
    layout = [(0, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 2, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 3, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 2, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 3, 'vineyard_tile_2', 'vineyard_house_spritelayout'),
              (1, 4, 'vineyard_tile_2', 'vineyard_shed_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'vineyard_layout_3',
    layout = [(0, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 1, 'vineyard_tile_2', 'vineyard_shed_spritelayout'),
              (2, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (2, 1, 'vineyard_tile_2', 'vineyard_house_spritelayout'),
              (3, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (3, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
    ]
)
industry.add_industry_layout(
    id = 'vineyard_layout_4',
    layout = [(0, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 3, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 4, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 3, 'vineyard_tile_2', 'vineyard_shed_spritelayout'),
              (1, 4, 'vineyard_tile_2', 'vineyard_house_spritelayout'),
              (3, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (3, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (3, 3, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (3, 4, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (4, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (4, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (4, 3, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (4, 4, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
    ]
)
industry.add_industry_layout(
    id = 'vineyard_layout_5',
    layout = [(0, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 2, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 3, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (0, 4, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 1, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 2, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 3, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 4, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (1, 5, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (2, 0, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (2, 1, 'vineyard_tile_2', 'vineyard_house_spritelayout'),
              (2, 2, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (2, 3, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (2, 4, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (2, 5, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (3, 1, 'vineyard_tile_2', 'vineyard_shed_spritelayout'),
              (3, 2, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (3, 3, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
              (3, 4, 'vineyard_tile_1', 'vineyard_slope_aware_ground_with_trees'),
    ]
)