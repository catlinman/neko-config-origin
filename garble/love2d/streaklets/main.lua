
-- Program settings all in one spot.
local numStreaklets = 4
local damping = 20
local range = 32
local size = 16

-- Private variables that should not be tampered with.
local streaklets = {}
local ghosts = {}
local id = 0
local ghostid = 0
local time = 0
local ghosttime = 1

-- Random range function with floating point values.
function math.randomFloat(a, b, decimal)
	local value_a = 1
	local value_b = 1

	if a ~= 0 then
		value_a = a / a
	else
		value_a = 1
	end

	if b ~= 0 then
		value_b = b / b
	else
		value_b = 1
	end

	if decimal then
		return math.random(a * (10 ^ decimal) * value_a, b * (10 * decimal) * value_b) / (10 ^ decimal)
	else
		return math.random(a * (10 ^ 5) * value_a, b * (10 ^ 5) * value_b) / (10 ^ 5)
	end
end

-- Creates a new streaklet.
local function newStreaklet()
	streaklets[id] = {} -- New empty table that will store all our information.

	-- Add basic values to the given streaklet. Keep it short and clean.
	streaklets[id].x = math.randomFloat(0, 640)
	streaklets[id].y = math.randomFloat(0, 480)
	streaklets[id].dx = 0
	streaklets[id].dy = 0
	streaklets[id].tx = math.randomFloat(0, 640)
	streaklets[id].ty = math.randomFloat(0, 480)
	streaklets[id].size = size

	id = id + 1 -- Increment the index so that we have a unique identifier.

	return streaklets[id] -- Optionally return the streaklet to the system for further use.
end

-- Function to control all the streaklets. Should be called within the main update loop.
local function moveStreaklets(dt)
	for i, streak in pairs(streaklets) do
		-- streak.x = streak.x + (streak.tx - streak.x) * dt
		-- streak.y = streak.y + (streak.ty - streak.y) * dt

		-- We do a bunch of screen clamping here. Nothing special.
		if streak.x < 0 or streak.x > 640 then
			streak.dx = -streak.dx
		end

		if streak.y < 0 or streak.y > 480 then
			streak.dy = -streak.dy
		end

		-- Linear interpolation of the directional vector of each streaklet.
		streak.dx = streak.dx + ((streak.tx - streak.x) - streak.dx) * dt
		streak.dy = streak.dy + ((streak.ty - streak.y) - streak.dy) * dt

		-- Add up the direction vector with the actual position and smooth it out a little.
		streak.x = streak.x + streak.dx / damping
		streak.y = streak.y + streak.dy / damping

		-- Check if the position has been reached. We do fast radial approximation here.
		if (streak.tx - streak.x)^2 + (streak.ty - streak.y)^2 < range^2 then
			streak.tx = math.randomFloat(0, 640)
			streak.ty = math.randomFloat(0, 480)
		end

		streak.size = size - math.min(streak.size  * 0.9, math.abs(streak.dx + streak.dy) / damping)
	end
end

-- Takes in a streaklet and generates a new ghost for it.
local function ghostStreaklets()
	for i, s in pairs(streaklets) do
		g = {}
		g.x = s.x
		g.y = s.y
		g.size = s.size
		g.life = ghosttime

		ghostid = ghostid + 1

		ghosts[ghostid] = g
	end
end

-- Guide the streaklets to a given point on the screen.
local function guideStreaklets(x, y)
	for i, streak in pairs(streaklets) do
		streak.tx = x
		streak.ty = y
	end
end

-- Removes all streaklets.
local function destroyStreaklets()
	-- TODO
end

-- Main program entry point.
function love.load()
	for i = 0, numStreaklets - 1 do
		newStreaklet()
	end
end

-- Called each frame update. Handles program logic.
function love.update(dt)
	time = time + dt
	moveStreaklets(dt)
	ghostStreaklets(dt)

	for i, g in pairs(ghosts) do
		g.life = g.life - dt
		g.size = g.size * 0.975

		if g.life < 0 then
			ghosts[i] = nil
		end
	end
end

-- Draws out each frame. Is called after love.update
function love.draw()
	love.graphics.setColor(255, 255, 255, 255)
	for i, s in pairs(streaklets) do
		love.graphics.circle("fill", s.x, s.y, s.size, 8)
	end

	for i, g in pairs(ghosts) do
		love.graphics.setColor(255, 255, 255, 255 * g.life)
		love.graphics.circle("fill", g.x, g.y, g.size, 8)
	end
end

-- Callback for mouse presses. In this case only relevant to guideStreaklets.
function love.mousepressed(x, y, button)
	guideStreaklets(x, y)
end
