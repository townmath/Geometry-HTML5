
var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
var c_width = 55.0;
var ppm = canvas.width/c_width;
var c_height = canvas.height/ppm;
ctx.setTransform(ppm, 0, 0, -ppm, 0, canvas.height);  

var worldAABB = new b2AABB();
worldAABB.lowerBound.Set(-10000.0, -10000.0);
worldAABB.upperBound.Set(10000.0, 10000.0);
var gravity = new b2Vec2(0.0, -9.8);
var world = new b2World(worldAABB, gravity, true);
window.world = world;

var groundBodyDef = new b2BodyDef();
groundBodyDef.position.Set(c_width/2.0, 3.0);
var groundBody = world.CreateBody(groundBodyDef);
var groundShapeDef = new b2PolygonDef();
groundShapeDef.restitution = 0.0;
groundShapeDef.friction = 0.5;
groundShapeDef.density = 1.0;
groundBody.w = c_width*1.0
groundBody.h = 0.1
groundShapeDef.SetAsBox(groundBody.w, groundBody.h);
groundBody.CreateShape(groundShapeDef);
groundBody.SynchronizeShapes();

var bodies = [groundBody];
var colors = ["#77358C","#008594","#BC99C3","#89C2CB","#838381"];
var mToMove=0.1;

function makeBox(x, y) {
    var bodyDef = new b2BodyDef();
    bodyDef.position.Set(x, y);
    var body = world.CreateBody(bodyDef);
    var shapeDef = new b2PolygonDef();
    body.w = Math.ceil(Math.random()*3);
    body.h = Math.ceil(Math.random()*3);
	body.color= colors[Math.floor(Math.random() * colors.length)];
	shapeDef.SetAsBox(body.w, body.h);
    shapeDef.restitution = 0.0;
    shapeDef.density = 2.0;
    shapeDef.friction = 0.9;
    body.CreateShape(shapeDef);
    body.SetMassFromShapes();
    bodies.push(body);
}

function handleKeyDown(event) {
	var distToEdge;
	var distToMove;
	var body=bodies.pop();
	if (event.keyCode == 37) {// Left arrow
		body.ApplyImpulse({x:-10, y:0}, {x:body.m_xf.position.x, y:body.m_xf.position.y});
	} else if (event.keyCode == 39) { // right arrow
		body.ApplyImpulse({x:10, y:0}, {x:body.m_xf.position.x, y:body.m_xf.position.y});
	}
	bodies.push(body);
}

makeBox(c_width/2, c_height);
var frame = 0;
window.addEventListener('keydown',handleKeyDown,true);

window.setInterval(function() {
    frame ++;
	var currentBody=bodies.pop();
	//var currentY=currentBody.m_xf.position.y;
	if (currentBody.m_xf.position.x>=(c_width-1)){
		currentBody.ApplyImpulse({x:-20, y:0}, {x:currentBody.m_xf.position.x, y:currentBody.m_xf.position.y});
	}
	else if (currentBody.m_xf.position.x<=1){
		currentBody.ApplyImpulse({x:20, y:0}, {x:currentBody.m_xf.position.x, y:currentBody.m_xf.position.y});
	}
	bodies.push(currentBody);
    if(frame%200==0) {
        makeBox(c_width/2, c_height);
    }
    world.Step(1.0/60.0, 10);
    //ctx.clearRect(0.0, 0.0, canvas.width, canvas.height);
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, c_width, c_height);
    ctx.fillStyle = 'black';
    for(var i = 0; i < bodies.length; i++){
        var body = bodies[i];
        var t = body.m_xf;
		ctx.fillStyle = body.color;
        ctx.translate(t.position.x, t.position.y)
        ctx.rotate(body.GetAngle());
        ctx.fillRect(-body.w, -body.h, body.w*2, body.h*2);
        ctx.rotate(-body.GetAngle());
        ctx.translate(-t.position.x, -t.position.y)
    }
    ctx.save();
    ctx.setTransform(1,0,0,1,0,0);
    ctx.restore();
}, 1000/30);
