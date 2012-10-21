"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from firs import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='textile_mill')

industry.add_tile(id='textile_mill_tile')

spriteset_ground = industry.add_spriteset(
    id = 'textile_mill_spriteset_ground',
    type = 'cobble'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'textile_mill_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_large_chimney = industry.add_spriteset(
    id = 'textile_mill_spriteset_large_chimney',
    sprites = [(10, 60, 64, 103, -31, -74)],
    zextent = 64
)
spriteset_large_building_lh_part = industry.add_spriteset(
    id = 'textile_mill_spriteset_large_building_lh_part',
    sprites = [(80, 60, 64, 103, -31, -72)],
    zextent = 64
)
spriteset_large_building_rh_part = industry.add_spriteset(
    id = 'textile_mill_spriteset_large_building_rh_part',
    sprites = [(150, 60, 64, 103, -31, -72)],
    zextent = 64
)
spriteset_crates_greeble = industry.add_spriteset(
    id = 'textile_mill_spriteset_crates_greeble',
    sprites = [(220, 60, 64, 103, -31, -72)],
    zextent = 64
)
spriteset_small_warehouse = industry.add_spriteset(
    id = 'textile_mill_spriteset_small_warehouse',
    sprites = [(290, 60, 64, 103, -31, -72)],
    zextent = 48
)
sprite_smoke = industry.add_sprite(
    sprite_number = '3701 + animation_frame',
    xoffset= 0,
    yoffset= 9,
    zoffset= 78,
    xextent= 15,
    yextent= 7,
    zextent= 7
)

industry.add_spritelayout(
    id = 'textile_mill_spritelayout_1_anim',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_large_chimney, sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_large_building_lh_part],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_large_building_rh_part],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_crates_greeble],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_small_warehouse],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'textile_mill_industry_layout_1',
    default_spritelayout = 'textile_mill_spritelayout_6',
    layout = [(0, 0, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (0, 1, 'textile_mill_tile', 'textile_mill_spritelayout_1_anim'),
              (1, 0, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (1, 1, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (2, 0, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (2, 1, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (3, 0, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (3, 1, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (4, 0, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (4, 1, 'textile_mill_tile', 'textile_mill_spritelayout_4')
    ]
)
industry.add_industry_layout(
    id = 'textile_mill_industry_layout_2',
    default_spritelayout = 'textile_mill_spritelayout_6',
    layout = [(0, 0, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (0, 1, 'textile_mill_tile', 'textile_mill_spritelayout_4'),
              (0, 2, 'textile_mill_tile', 'textile_mill_spritelayout_1_anim'),
              (1, 0, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (1, 1, 'textile_mill_tile', 'textile_mill_spritelayout_6'),
              (1, 2, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (2, 0, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (2, 1, 'textile_mill_tile', 'textile_mill_spritelayout_6'),
    ]
)
industry.add_industry_layout(
    id = 'textile_mill_industry_layout_3',
    default_spritelayout = 'textile_mill_spritelayout_6',
    layout = [(0, 0, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (0, 1, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (1, 0, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (1, 1, 'textile_mill_tile', 'textile_mill_spritelayout_4'),
              (2, 0, 'textile_mill_tile', 'textile_mill_spritelayout_1_anim'),
    ]
)
industry.add_industry_layout(
    id = 'textile_mill_industry_layout_4',
    default_spritelayout = 'textile_mill_spritelayout_6',
    layout = [(0, 0, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (0, 1, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (1, 0, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (1, 1, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (2, 0, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (2, 1, 'textile_mill_tile', 'textile_mill_spritelayout_4'),
              (3, 0, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (3, 1, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (4, 0, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (4, 1, 'textile_mill_tile', 'textile_mill_spritelayout_1_anim')
    ]
)
industry.add_industry_layout(
    id = 'textile_mill_industry_layout_5',
    default_spritelayout = 'textile_mill_spritelayout_6',
    layout = [(0, 0, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (0, 1, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (0, 2, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (0, 3, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (1, 0, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (1, 1, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (1, 2, 'textile_mill_tile', 'textile_mill_spritelayout_4'),
              (1, 3, 'textile_mill_tile', 'textile_mill_spritelayout_1_anim')
    ]
)
industry.add_industry_layout(
    id = 'textile_mill_industry_layout_6',
    default_spritelayout = 'textile_mill_spritelayout_6',
    layout = [(0, 0, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (0, 1, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (0, 2, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (1, 0, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (1, 1, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (1, 2, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (2, 0, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (2, 1, 'textile_mill_tile', 'textile_mill_spritelayout_1_anim'),
              (2, 2, 'textile_mill_tile', 'textile_mill_spritelayout_4')
    ]
)

# Templating
industry.render_and_save_pnml()