"use strict";
var is_fullscreen = false;
function open_fullscreen() {
	let game = document.getElementById("game-area");
	if(is_fullscreen){
		is_fullscreen = false;
		if(is_mobile_device()){
			game.style.position = "absolute";
			document.getElementById("mobile-back-button").style.display = "none";
			document.getElementById("game-player").style.display = "none";
		} else {
			if (document.exitFullscreen) {
				document.exitFullscreen();
			} else if (document.mozCancelFullScreen) {
				document.mozCancelFullScreen();
			} else if (document.webkitExitFullscreen) {
				document.webkitExitFullscreen();
			} else if (document.msExitFullscreen) {
				document.msExitFullscreen();
			}
		}
	} else {
		is_fullscreen = true;
		if(is_mobile_device()){
			document.getElementById("game-player").style.display = "block";
			game.style.position = "fixed";
			document.getElementById("mobile-back-button").style.display = "flex";
		} else {
			if (game.requestFullscreen) {
				game.requestFullscreen();
			} else if (game.mozRequestFullScreen) {
				game.mozRequestFullScreen();
			} else if (game.webkitRequestFullscreen) {
				game.webkitRequestFullscreen();
			} else if (game.msRequestFullscreen) {
				game.msRequestFullscreen();
			}
		}
	}
}

function is_mobile_device(){
	if (navigator.userAgent.match(/Android/i)
	|| navigator.userAgent.match(/webOS/i)
	|| navigator.userAgent.match(/iPhone/i)
	|| navigator.userAgent.match(/iPad/i)
	|| navigator.userAgent.match(/iPod/i)
	|| navigator.userAgent.match(/BlackBerry/i)
	|| navigator.userAgent.match(/Windows Phone/i)) {
		return true;
	} else {
		return false;
	}
}

if(document.getElementById("game-area")){
	if(document.getElementById("mobile-back-button")){
		drag_back_btn(document.getElementById("mobile-back-button"));
	}
	if(is_mobile_device()){
		if(document.getElementById('allow_mobile_version')){
			var mobilePlay = document.getElementById('mobile-play');
			var gamePlayer = document.getElementById('game-player');
			if(mobilePlay) mobilePlay.style.display = 'block';
			if(gamePlayer) gamePlayer.style.display = 'none';
		}
	}
}

function drag_back_btn(elem) {
	let is_drag = false;
	let pos_1 = 0, pos_2 = 0;
	let last_y = elem.style.top;
	let touchstart_y = 0;
	elem.addEventListener("touchend", function(e) {
		if(is_drag) is_drag = false;
	}, false);
	elem.addEventListener("touchmove", function(e) {
		e.preventDefault();
		let touch = e.changedTouches[0];
		if(!is_drag){
			if(touchstart_y < touch.clientY+5 || touchstart_y > touch.clientY-5){
				pos_2 = e.clientY;
				is_drag = true;
			}
		}
		if(is_drag){
			pos_1 = pos_2 - touch.clientY;
			pos_2 = touch.clientY;
			elem.style.top = (pos_2) + "px";
		}
	}, false);
	elem.addEventListener("touchstart", function(e) {
		let touch = e.changedTouches[0];
		last_y = elem.style.top;
		touchstart_y = touch.clientY;
	}, false);
	elem.addEventListener("click", function(e) {
		e.preventDefault();
		if(last_y == elem.style.top) open_fullscreen();
	}, false);
}

var mobilePlayBtn = document.getElementById('mobile-play-btn');
if(mobilePlayBtn){
	mobilePlayBtn.addEventListener('click', function(e) {
		open_fullscreen();
	});
}
