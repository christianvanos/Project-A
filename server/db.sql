CREATE TABLE IF NOT EXISTS `breakingbanks_game` (
  `game_code` int(11) NOT NULL AUTO_INCREMENT,
  `winnendekaarten` text NOT NULL,
  `game_status` text NOT NULL,
  `dobbelsteen` int(9) NOT NULL,
  `dobbelsteen2` int(9) NOT NULL,
  PRIMARY KEY (`game_code`)
)

CREATE TABLE IF NOT EXISTS `breakingbanks_kaarten` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gebruiker_code` int(11) NOT NULL,
  `game_code` int(11) NOT NULL,
  `kaarten` text NOT NULL,
  PRIMARY KEY (`id`)
) 
