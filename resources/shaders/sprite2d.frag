#version 330 core
in vec2 f_texture_uv;

out vec4 frag_color;

uniform sampler2D u_sprite_texture;
uniform vec2 u_offset;
uniform ivec2 u_size;

void main()
{
    float x_lim = u_offset.x/u_size.x;
    float y_lim = u_offset.y/u_size.y;

    frag_color = texture(u_sprite_texture, vec2(f_texture_uv.x/u_size.x + x_lim, f_texture_uv.y/u_size.y + y_lim));
}