
local size = 5


function love.draw()
    love.graphics.circle("fill", 10, 10, size)
end

local SPD = 13

function love.update(dt)
    size = size + dt * SPD
end

