#version 330 core
out vec4 FragColor;
in vec2 TexCoord;
uniform sampler2D texture1;
void main()
{
    float x_pos = 0.0;
    int x_tam = 6;
    float x_lim = x_pos/x_tam;

    float y_pos = 0.0;
    int y_tam = 1;
    float y_lim = y_pos/y_tam;


    FragColor = texture(texture1, vec2(TexCoord.x/x_tam + x_lim, TexCoord.y/y_tam + y_lim));
}