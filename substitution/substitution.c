#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHABET_LENGTH 26

bool is_valid_key(string key);
string encrypt(string plaintext, string key);

int main(int argc, string argv[])
{

    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }

    string key = argv[1];

    if (!is_valid_key(key))
    {
        printf("Key must contain 26 unique alphabetic characters.\n");
        return 1;
    }

    string plaintext = get_string("plaintext: ");

    string ciphertext = encrypt(plaintext, key);

    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

bool is_valid_key(string key)
{

    if (strlen(key) != ALPHABET_LENGTH)
    {
        return false;
    }

    bool visited[ALPHABET_LENGTH] = {false};

    for (int i = 0; i < ALPHABET_LENGTH; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }

        int index = toupper(key[i]) - 'A';
        if (visited[index])
        {
            return false;
        }
        visited[index] = true;
    }

    return true;
}

string encrypt(string plaintext, string key)
{
    int length = strlen(plaintext);
    for (int i = 0; i < length; i++)
    {
        if (isalpha(plaintext[i]))
        {

            char base = isupper(plaintext[i]) ? 'A' : 'a';

            int index = plaintext[i] - base;

            plaintext[i] = isupper(plaintext[i]) ? toupper(key[index]) : tolower(key[index]);
        }
    }
    return plaintext;
}
