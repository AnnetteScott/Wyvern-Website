var player = {
  health: 100
};

var pond_item = {
  'pond_hit_distance': 40,
  'pond_health': 100
};

var heart_item = {
  'health_regen': 10,
  'spawn_chance': 20,
  'heart_min_spawn_distance': 400
};

var spawn_speed = 1000
var difficulty = [
  {'level': '1', 'maxCacti': 10, 'scoreThreshold': 10, 'spawnSpeed': 1000, 'cactiMovingSpeed': 1, 'fireCacti': 2},
  {'level': '2', 'maxCacti': 15, 'scoreThreshold': 50, 'spawnSpeed': 950, 'cactiMovingSpeed': 1.1, 'fireCacti': 5},
  {'level': '3', 'maxCacti': 20, 'scoreThreshold': 75, 'spawnSpeed': 850, 'cactiMovingSpeed': 1.2, 'fireCacti': 10},
  {'level': '4', 'maxCacti': 25, 'scoreThreshold': 100, 'spawnSpeed': 800, 'cactiMovingSpeed': 1.3, 'fireCacti': 15},
  {'level': '5', 'maxCacti': 30, 'scoreThreshold': 150, 'spawnSpeed': 750, 'cactiMovingSpeed': 1.4, 'fireCacti': 20},
  {'level': '6', 'maxCacti': 35, 'scoreThreshold': 200, 'spawnSpeed': 700, 'cactiMovingSpeed': 1.5, 'fireCacti': 25},
  {'level': '7', 'maxCacti': 40, 'scoreThreshold': 300, 'spawnSpeed': 650, 'cactiMovingSpeed': 1.6, 'fireCacti': 30},
  {'level': '8', 'maxCacti': 45, 'scoreThreshold': 400, 'spawnSpeed': 600, 'cactiMovingSpeed': 1.7, 'fireCacti': 40},
  {'level': '9', 'maxCacti': 50, 'scoreThreshold': 475, 'spawnSpeed': 550, 'cactiMovingSpeed': 1.8, 'fireCacti': 50},
  {'level': '10', 'maxCacti': 55, 'scoreThreshold': 550, 'spawnSpeed': 500, 'cactiMovingSpeed': 1.9, 'fireCacti': 60},
  {'level': '11', 'maxCacti': 60, 'scoreThreshold': 625, 'spawnSpeed': 450, 'cactiMovingSpeed': 2.0, 'fireCacti': 70},
  {'level': '12', 'maxCacti': 65, 'scoreThreshold': 700, 'spawnSpeed': 400, 'cactiMovingSpeed': 2.1, 'fireCacti': 80}
];