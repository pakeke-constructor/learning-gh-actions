
local size = require("my_proj.my_file")


function love.draw()
    love.graphics.circle("fill", 10, 10, size)
end

local SPD = 13

function love.update(dt)
    size = size + dt * SPD
end

