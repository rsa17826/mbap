from typing import NotRequired, TypedDict


class ProgressionNode(TypedDict):
  room: str
  receive: list[str]
  requires: list[list[str]]
  info: NotRequired[str]


PROG: list[ProgressionNode] = [
  {
    "room": "menu",
    "requires": [
      [],
    ],
    "receive": ["level:level1"],
  },
  {
    "room": "level1",
    "requires": [
      [],
    ],
    "receive": ["level:level1", "flag:beat level1"],
  },
  {
    "room": "level2",
    "requires": [
      [],
    ],
    "receive": ["level:level2", "flag:beat level2"],
  },
  {
    "room": "level3",
    "requires": [
      [],
    ],
    "receive": ["level:level3", "flag:beat level3"],
  },
  {
    "room": "level4",
    "requires": [
      [],
    ],
    "receive": ["level:level4", "flag:beat level4"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["level:level5", "flag:beat level5"],
  },
  # walls
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -3_pos_-8.9_-4.0_933.2"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -3_pos_410.2_-22.8_336.1"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWallCreator 1/3_pos_293.9_8.9_731.2"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -3_pos_479.8_-13.8_179.5"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -5_pos_253.4_-4.9_542.5"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWallCreator round -5_pos_450.6_-21.6_342.9_rad_10_thick_1_deg_130_h_2"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -5_pos_221.9_30.1_1032.5"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWallCreator round -7_pos_467.9_-19.0_294.8_rad_10_thick_1_deg_180_h_2"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -5_pos_244.5_30.1_1038.3"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWallCreatorRound -6_pos_295.7_12.5_561.0_rad_30_thick_1_deg_170_h_2"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -3_pos_24.9_-4.0_941.9"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -3_pos_76.6_14.8_972.6"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -3_pos_-79.0_-4.0_888.4"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -3_pos_-101.0_-4.0_914.2"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -3_pos_-42.3_-4.0_952.3"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -3_pos_-79.1_-4.0_821.9"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWall -2_pos_497.2_-13.8_150.2"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWallCreator round jail_pos_99.6_89.6_1212.5_rad_14_thick_1_deg_180_h_4"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWallCreator round jail_pos_99.6_89.6_1212.5_rad_28_thick_1_deg_170_h_3"],
  },
  {
    "room": "level5",
    "requires": [
      [],
    ],
    "receive": ["wall:Level_5_NumberWallCreator round jail_pos_99.6_89.6_1212.5_rad_36_thick_1_deg_150_h_2"],
  },
  # nowalls
]
