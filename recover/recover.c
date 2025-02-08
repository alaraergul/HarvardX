#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{

    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }


    FILE *file = fopen(argv[1], "rb");
    if (file == NULL)
    {
        printf("Could not open forensic image.\n");
        return 1;
    }


    uint8_t buffer[BLOCK_SIZE];
    FILE *jpeg = NULL;
    char filename[8];
    int jpg_count = 0;


    while (fread(buffer, sizeof(uint8_t), BLOCK_SIZE, file) == BLOCK_SIZE)
    {

        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {

            if (jpeg != NULL)
            {
                fclose(jpeg);
            }

            sprintf(filename, "%03d.jpg", jpg_count);
            jpeg = fopen(filename, "wb");
            if (jpeg == NULL)
            {
                printf("Could not create JPEG file.\n");
                fclose(file);
                return 1;
            }
            jpg_count++;
        }

        if (jpeg != NULL)
        {
            fwrite(buffer, sizeof(uint8_t), BLOCK_SIZE, jpeg);
        }
    }

    fclose(file);
    if (jpeg != NULL)
    {
        fclose(jpeg);
    }

    return 0;
}
