#version 330 core
layout (location = 0) in vec2 v_pos;
layout (location = 1) in vec2 v_texture_uv;
out vec2 f_texture_uv;

uniform mat4 u_model;
uniform mat4 u_projection;

void main()
{
    gl_Position = u_projection * u_model * vec4(v_pos.x, v_pos.y, 0.0, 1.0);
    f_texture_uv = v_texture_uv;
}