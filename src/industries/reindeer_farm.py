"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='reindeer_farm',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_FARM',
                    prod_cargo_types=['FOOD'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='11',
                    prod_multiplier='[12]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='95',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='1',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'general_store': 16,
                                                                         'hotel': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_REINDEER_FARM)',
                    extra_text_fund='string(STR_FUND_REINDEER_FARM)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_FARM))',
                    fund_cost_multiplier='60',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS' )

industry.economy_variations['BASIC_ARCTIC'].enabled = True

industry.add_tile(id='reindeer_farm_tile_1',
                  location_checks=TileLocationChecks(disallow_steep_slopes=True,
                                                     disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_empty = industry.add_spriteset(
    id = 'reindeer_farm_spriteset_ground_empty',
    type = 'empty'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'reindeer_farm_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_barn1 = industry.add_spriteset(
    id = 'reindeer_farm_spriteset_barn1',
    sprites = [(10, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_silo = industry.add_spriteset(
    id = 'reindeer_farm_spriteset_silo',
    sprites = [(80, 10, 64, 52, -31, -21)],
    zextent = 48
)
spriteset_barn2 = industry.add_spriteset(
    id = 'reindeer_farm_spriteset_barn2',
    sprites = [(150, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_house = industry.add_spriteset(
    id = 'reindeer_farm_spriteset_house',
    sprites = [(220, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_cows_bw = industry.add_spriteset(
    id = 'reindeer_farm_spriteset_cows_bw',
    sprites = [(290, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_cows_brown = industry.add_spriteset(
    id = 'reindeer_farm_spriteset_cows_brown',
    sprites = [(360, 10, 64, 52, -31, -21)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'reindeer_farm_spritelayout_barn1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_barn1]
)
industry.add_spritelayout(
    id = 'reindeer_farm_spritelayout_silo',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_silo],
)
industry.add_spritelayout(
    id = 'reindeer_farm_spritelayout_barn2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_barn2],
)
industry.add_spritelayout(
    id = 'reindeer_farm_spritelayout_house',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_house],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'reindeer_farm_spritelayout_cows_bw',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_cows_bw],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'reindeer_farm_spritelayout_cows_brown',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_cows_brown],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'reindeer_farm_spritelayout_cows_bw_dirt',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_cows_bw],
)
industry.add_spritelayout(
    id = 'reindeer_farm_spritelayout_cows_brown_dirt',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_cows_brown],
)

industry.add_industry_layout(
    id = 'reindeer_farm_industry_layout_1',
    layout = [(0, 0, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_brown'),
              (0, 1, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_bw'),
              (0, 2, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_house'),
              (2, 0, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_silo'),
              (2, 1, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_bw_dirt'),
              (3, 0, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_barn1'),
              (3, 1, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_brown_dirt'),
              (3, 2, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_barn2'),
    ]
)
industry.add_industry_layout(
    id = 'reindeer_farm_industry_layout_2',
    layout = [(0, 0, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_brown_dirt'),
              (0, 1, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_bw_dirt'),
              (0, 2, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_barn1'),
              (1, 1, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_barn2'),
              (1, 2, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_silo'),
              (2, 0, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_bw'),
              (2, 1, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_brown'),
              (2, 2, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_house'),
    ]
)
industry.add_industry_layout(
    id = 'reindeer_farm_industry_layout_3',
    layout = [(0, 1, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_barn1'),
              (0, 3, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_house'),
              (1, 0, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_barn2'),
              (1, 1, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_brown_dirt'),
              (1, 3, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_bw'),
              (2, 0, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_silo'),
              (2, 1, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_bw_dirt'),
              (2, 3, 'reindeer_farm_tile_1', 'reindeer_farm_spritelayout_cows_brown'),
    ]
)