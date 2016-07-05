function Ball(radius,color) {
	if (radius === undefined) 
		radius = 40;
		
	if (color === undefined)
		color = "#FF0000";
		
	this.x = 0;
	this.y = 0;
	this.radius = radius;
	this.rotation = 0;
	this.scaleX = 1;
	this.scaleY = 1;
	this.color = color;
	this.lineWidth = 1;

	this.draw = function(ctx) {
		ctx.save();
		ctx.translate(this.x, this.y);
		ctx.rotate(this.rotation);
		ctx.scale(this.scaleX, this.scaleY);
		ctx.lineWidth = this.lineWidth;
		ctx.fillStyle = this.color;
		ctx.beginPath();
		ctx.arc(0,0,this.radius,0, Math.PI * 2, true);
		ctx.closePath();
		ctx.fill();
		if (this.lineWidth > 0)
			ctx.stroke();
		ctx.restore();
	}
	
	this.getBounds = function() {
		return {
			x: this.x - this.radius,
			y: this.y - this.radius,
			width: this.radius * 2,
			height: this.radius * 2
		}
	}
	
	this.move = function() {
		this.x += this.vx;
		this.y += this.vy;
	}
}