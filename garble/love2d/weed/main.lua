
-- These variables define the pattern and movement on the screen. Should name them better.
local time, radius, count, s, m, speed = 0, 64, 4, 4, 12, 0.5

-- Placeholder variable reference for the texture data.
local weedtexture = ""

-- Variables used to limit the framerate so that my Macbook doesn't start burning in class.
local framerate = 60
local mindt = 1 / framerate

-- This is our main entry point. Nothing special and amazing to see here.
function love.load()
	weedtexture = love.graphics.newImage("weed.png")

	-- Let's make some globals for the screen size.
	_w = love.graphics.getWidth()
	_h = love.graphics.getHeight()
	
	nextTime = love.timer.getTime()
end

-- Update function. We mainly use it to track the passed time.
function love.update(dt)
	time = time + dt
	nextTime = nextTime + mindt	
end

-- "W"here the magic happens". We draw our amazing work here with lots of lame math.
function love.draw()
	for groupIndex = 1, m do
		for objectIndex = 1, count + groupIndex * 16 do

			love.graphics.setColor(
				128 + math.sin(time * speed * 4 + objectIndex + groupIndex) * 64,
				128 + math.cos(time * speed * 6 + objectIndex + groupIndex) * 64,
				128 + math.sin(time * speed * 5 + objectIndex + groupIndex) * 64,
				255
			)

			love.graphics.draw(
				weedtexture,
				_w / 2 + math.sin(time * speed) * 1 + math.cos(time + objectIndex * speed) * radius * groupIndex,
				_h / 2 + math.cos(time * speed) * 1 + math.sin(time + objectIndex * speed) * radius * groupIndex,
				objectIndex * groupIndex * time * speed / 100,
				0.20 + math.sin(time * groupIndex) * 0.05,
				0.20 + math.sin(time * groupIndex) * 0.05
			)
			
		end
	end

	-- Framerate handling is done here.
	local curTime = love.timer.getTime()
	if nextTime <= curTime then
		nextTime = curTime
		return
	end

	-- Go to sleep if needed.
	love.timer.sleep(nextTime - curTime)
end