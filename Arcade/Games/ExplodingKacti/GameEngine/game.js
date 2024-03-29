//const page_navbar_height = parseInt(document.querySelector("nav") ? window.getComputedStyle(document.querySelector("nav")).getPropertyValue("height") : 0);
var leaderboard_data;
var game_elem = document.querySelector("game");
var game_width = game_elem.offsetWidth;
var game_height = game_elem.offsetHeight;
var center_of_game = {x: (game_width / 2), y: (game_height / 2)};

var cursor_position = {x: 0, y: 0};

var score_elem = document.querySelector("score p");
var health_bar_elem = document.querySelector("health_bar div");
var health_bar_text_elem = document.querySelector("health_bar p");
var water_meter_elem = document.querySelector("water_meter div");
var water_meter_text_elem = document.querySelector("water_meter p");

var aim_trace_elem = document.querySelector("aim_trace");
aim_trace_elem.style.left = center_of_game.x + "px";
aim_trace_elem.style.top = center_of_game.y + "px";
var crosshair_elem = document.querySelector("crosshair");
crosshair_elem.style.left = center_of_game.x + "px";
crosshair_elem.style.top = center_of_game.y + "px";

var pond_elem;

var anim_intervals = {};


/*==============Main Game Loop============*/
let game_params = {};
function gameMain(){
  document.querySelector("main_menu").classList.add("invisible");
  document.querySelector("user_interface").classList.remove("invisible");
  document.querySelector("aim_trace").classList.remove("invisible");
  document.querySelector("crosshair").classList.remove("invisible");

  spawnPond();

  anim_intervals['spawn_cacti'] = window.setInterval(function(){spawnCactus(spawnChance(cacti_types))}, spawn_speed);
  anim_intervals['move_cacti'] = window.setInterval(function(){moveAllCacti()}, 50);
}
//gameMain();



/*===========Main Game Functions==========*/

function spawnPond(){
  var pos = {x: (game_width / 2) - (64), y: (game_height / 2) - (64)};
  var id = "POND";
  var pond = document.createElement("pond");
  pond.id = id;
  pond.style.left = pos.x + "px";
  pond.style.top = pos.y + "px";
  pond.setAttribute('onclick', "changeWater(50)");
  document.querySelector("game").appendChild(pond);
  pond_elem = pond;
}


function spawnCactus(type = "normal_cactus"){
  checkScore();
  if(Object.keys(all_cacti).length < max_num_of_cacti){
    var pos = {x: center_of_game.x, y: center_of_game.y};
    while(getLinearDistance(pos, center_of_game) < cacti_min_spawn_distance || between(pos.x, (center_of_game.x - 75), (center_of_game.x + 75))){
      pos = {x: (Math.random() * game_width), y: (Math.random() * game_height)};
    }

    var cactus = document.createElement("cactus");
    var id = generateID();
    var new_cactus_object = {
      'dom_element': cactus,
      'id': id,
      'type': type,
      'position': {x: pos.x, y: pos.y},
      'remaining_health': cacti_types[type]['health']
    };
    cactus.id = id;
    cactus.classList.add(type);
    cactus.style.left = pos.x - 32 + "px";
    cactus.style.top = pos.y - 32 + "px";
    document.querySelector("cacti").appendChild(cactus);

    all_cacti[id] = new_cactus_object;

    var random = Math.floor(Math.random() * heart_item['spawn_chance']);
    if(random == 1){
      spawnHearts();
    }
    
  }
}

function spawnHearts(){
  var heart = document.createElement("heart");
  var pos = {x: center_of_game.x, y: center_of_game.y};
    while(getLinearDistance(pos, center_of_game) < heart_item['heart_min_spawn_distance']){
      pos = {x: (Math.random() * game_width), y: (Math.random() * game_height)};
    }
  heart.style.left = pos.x - 16 + "px";
  heart.style.top = pos.y - 16 + "px";

  document.querySelector("hearts").appendChild(heart);
}


function moveAllCacti(){
  Object.keys(all_cacti).forEach((k) => {
    var obj = all_cacti[k];
    var elem = document.getElementById(obj.id);
    var current_pos = obj['position'];
    var new_x = 0;
    if(current_pos.x < center_of_game.x){
      new_x = current_pos.x + cacti_movement_speed;
    } else {
      new_x = current_pos.x - cacti_movement_speed;
    }
  
    var new_y = getPosAlongHypo(current_pos, center_of_game, new_x);

    var new_pos = {x: new_x, y: new_y};

    all_cacti[k]['position'] = new_pos;
    elem.style.left = new_pos.x - 32 + "px";
    elem.style.top = new_pos.y - 32 + "px";

    cactusAttack(k);
  });
}


function checkAmmo(){
  return parseInt(water_meter_elem.style.height.split("%")[0]);
}


function checkScore(){
  var score = zeropad(parseInt(score_elem.innerHTML), 4);
  var current_level = getDifficultyLevel(score);
  max_num_of_cacti = current_level['maxCacti'];
  spawn_speed = current_level['spawnSpeed'];
  cacti_movement_speed = current_level['cactiMovingSpeed'];
  cacti_types['fire_cactus']['spawn_chance'] = current_level['fireCacti'];
  document.querySelector("level p").innerHTML = "Level " + current_level['level'];
  heart_item['spawn_chance'] = current_level['heart_spawn_chance']
}

function explode(pos, color){
  changeColour(color);
  createEmitter({clientX: pos.x, clientY: pos.y});
}


function shoot(elem){
  var cacti_type = elem.classList.value;
  var cacti_id = elem.id;
  var cactus_obj = all_cacti[cacti_id];
  if(checkAmmo() > 0){
    if(cactus_obj['remaining_health'] > 10){
      cactus_obj['remaining_health'] -= 10;
      spawnHitText({x: cactus_obj['position'].x - 14, y: cactus_obj['position'].y - 64}, 'FF0000', 20, "-10");
      explode(cactus_obj['position'], '0000FF');
    } else{
      delete all_cacti[cacti_id];
      elem.remove();
      spawnHitText({x: cactus_obj['position'].x - 14, y: cactus_obj['position'].y - 64}, 'FF0000', 20, "-10");
      explode(cactus_obj['position'], cacti_types[cacti_type]['color']);
      changeScore(cacti_types[cacti_type]['points']);
    }
    changeWater(-10);
  }else{
    spawnHitText({x: center_of_game.x - 85, y: center_of_game.y - 100}, '202020', 26, "OUT&nbsp;OF&nbsp;WATER");
  }
}


function cactusAttack(cacti_id){
  if(checkPondCollision(cacti_id)){
    delete all_cacti[cacti_id];
    document.getElementById(cacti_id).remove();
    spawnHitText({x: center_of_game.x - 14, y: center_of_game.y - 100}, 'FF0000', 20, "-10");
    explode(center_of_game, 'ff0000');
    changeHealth(-10);
    gameOver();
  }
}

function gameOver(){
  if(pond_item['pond_health'] <= 0){
    //ENDGAME
    pond_elem.classList.add("noafter");
    window.clearInterval(anim_intervals['spawn_cacti']);
    window.clearInterval(anim_intervals['move_cacti']);
    document.querySelectorAll('cactus').forEach((elem) => {
      elem.classList.add("a_cactus_celebration");
    });
    spawnHitText({x: center_of_game.x - 125, y: center_of_game.y - 100}, '202020', 36, "GAME&nbsp;OVER");

    showEndScreen();
  }
}

var playername = 'AAA';
var final_score = 0;
var can_submit_score = 1;
function updatePlayerName(event){
  playername = event.target.value;
}


function showEndScreen(){
  var endscreen = document.querySelector("end_screen");
  final_score = parseInt(score_elem.innerHTML);
  document.querySelector("#end_screen_score").innerHTML += final_score;

  endscreen.classList.remove("invisible");
}
function hideEndScreen(){
  var endscreen = document.querySelector("end_screen");
  endscreen.classList.add("invisible");
}


function submitScore(){
  if(can_submit_score === 1){
    can_submit_score = 0;
    hideEndScreen();
    transmitToServer({'name': playername, 'score': final_score});
    window.location.reload();
  }
}


function handleClickEvent(e){
  var elem = e.target;
  if(elem.tagName == "GAME_BACKGROUND"){
    if(checkAmmo() > 0){
      explode({x: e.clientX, y: e.clientY}, 'EAD997');
      changeWater(-10);
    }else{
      spawnHitText({x: center_of_game.x - 85, y: center_of_game.y - 100}, '202020', 26, "OUT&nbsp;OF&nbsp;WATER");
    }
  }else if(elem.tagName == "CACTUS"){
    shoot(elem);
  }else if(elem.tagName == "HEART"){
    explode({x: e.clientX, y: e.clientY}, 'ff0000');
    spawnHitText({x: center_of_game.x - 14, y: center_of_game.y - 100}, 'FF0000', 20, "+10");
    elem.remove();
    changeHealth(heart_item['health_regen']);
  }
}


function leaderboard(){
  var lb_list = document.querySelectorAll("leaderboard li");
  leaderboard_data.forEach((item, i) => {
    if(item && i < 10){
      lb_list[i].innerHTML = item['fields']['name'] + ": " + item['fields']['score'];
    }
  });
  document.querySelector("leaderboard").classList.remove("invisible");
}

function closeLeaderboard(){
  document.querySelector("leaderboard").classList.add("invisible");
  window.location.reload();
}
