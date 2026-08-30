const s = `{
  "room": "level$",
  "requires": [
    [],
  ],
  "receive": ["wall:$"],
},
`
const w = `Level_1_NumberWall 200_pos_754.2_30.3_1040.2
Level_1_NumberWall -1_pos_626.8_31.3_769.4
Level_1_NumberWall -1_pos_600.4_23.8_755.2
Level_1_NumberWall -1_pos_320.6_3.8_368.7
Level_1_NumberBridge 14_pos_394.2_-19.4_586.5_rad_40_thick_1_deg_90_h_4
Level_1_NumberWall -1_pos_785.6_44.3_338.8
Level_1_NumberWall -1_pos_663.8_44.8_346.1
Level_1_NumberWall 200_pos_865.4_30.9_1045.0
Level_1_NumberWall -1_pos_354.1_7.8_131.2
Level_1_NumberBridge 14_pos_1006.2_-34.8_881.4_rad_70_thick_1_deg_90_h_2
Level_1_EndBridge_pos_1237.1_-41.1_778.0
Level_2_NumberWall -7_pos_-42.0_5.8_196.1
Level_2_NumberWallCreatorRound 3s_pos_-34.3_5.7_160.0_rad_10_thick_1_deg_360_h_3
Level_2_NumberWall -7_pos_-129.5_7.3_153.3
Level_2_NumberWall -1_pos_-434.4_15.1_883.3
Level_2_Number Wall -3_pos_234.5_28.6_-29.1
Level_2_NumberWall 2_pos_-74.4_9.0_529.7
Level_2_NumberWall 2_pos_-77.7_9.0_520.5
Level_3_NumberWallGenerator -2s_pos_632.2_-12.5_1592.3
Level_3_EndBridge_pos_363.9_-85.9_1696.1
Level_3_NumberWallGenerator -1 11ths_pos_429.7_-21.6_1622.0
Level_3_NumberWall 11_pos_520.7_1.5_1260.2
Level_3_numberwall -11_pos_526.4_3.8_1389.5
Level_3_NumberWall -1/2_pos_323.5_-3.6_836.3
Level_3_NumberWallGenerator -1 11ths_pos_361.2_-21.6_1583.9
Level_3_NumberWallGenerator -2s_pos_557.0_-6.9_1532.3
Level_4_NumberWall -9_pos_575.9_105.0_761.9
Level_4_NumberWall -9_pos_671.9_104.2_734.6
Level_4_NumberWall -9_pos_221.0_130.5_761.3
Level_4_NumberWall -4_pos_21.5_153.3_743.5
Level_5_NumberWall -3_pos_-8.9_-4.0_933.2
Level_5_NumberWall -3_pos_410.2_-22.8_336.1
Level_5_NumberWallCreator 1/3_pos_293.9_8.9_731.2
Level_5_NumberWall -3_pos_479.8_-13.8_179.5
Level_5_NumberWall -5_pos_253.4_-4.9_542.5
Level_5_NumberWallCreator round -5_pos_450.6_-21.6_342.9_rad_10_thick_1_deg_130_h_2
Level_5_NumberWall -5_pos_221.9_30.1_1032.5
Level_5_NumberWallCreator round -7_pos_467.9_-19.0_294.8_rad_10_thick_1_deg_180_h_2
Level_5_NumberWall -5_pos_244.5_30.1_1038.3
Level_5_NumberWallCreatorRound -6_pos_295.7_12.5_561.0_rad_30_thick_1_deg_170_h_2
Level_5_NumberWall -3_pos_24.9_-4.0_941.9
Level_5_NumberWall -3_pos_76.6_14.8_972.6
Level_5_NumberWall -3_pos_-79.0_-4.0_888.4
Level_5_NumberWall -3_pos_-101.0_-4.0_914.2
Level_5_NumberWall -3_pos_-42.3_-4.0_952.3
Level_5_NumberWall -3_pos_-79.1_-4.0_821.9
Level_5_NumberWall -2_pos_497.2_-13.8_150.2
Level_5_NumberWallCreator round jail_pos_99.6_89.6_1212.5_rad_14_thick_1_deg_180_h_4
Level_5_NumberWallCreator round jail_pos_99.6_89.6_1212.5_rad_28_thick_1_deg_170_h_3
Level_5_NumberWallCreator round jail_pos_99.6_89.6_1212.5_rad_36_thick_1_deg_150_h_2

`
  .split("\n")
  .map((e) => e.trim())
  .filter(Boolean)
  .map((e) => s.replace("$", e.match(/Level_(\d+)/)[1]).replace("$", e)).join("")
console.log(w)
