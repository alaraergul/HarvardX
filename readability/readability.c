#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int calculate_grade(int letters, int words, int sentences);

int main(void)
{

    string text = get_string("Text: ");

    int num_letters = count_letters(text);
    int num_words = count_words(text);
    int num_sentences = count_sentences(text);

    int grade = calculate_grade(num_letters, num_words, num_sentences);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }

    return 0;
}

int count_letters(string text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int count_words(string text)
{
    int count = 0;
    bool in_word = false;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isspace(text[i]))
        {

            if (in_word)
            {
                count++;
                in_word = false;
            }
        }
        else if (isalpha(text[i]))
        {

            in_word = true;
        }
    }

    if (in_word)
    {
        count++;
    }

    return count;
}

int count_sentences(string text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}

int calculate_grade(int letters, int words, int sentences)
{
    float L = ((float) letters / words) * 100;
    float S = ((float) sentences / words) * 100;
    int index = (int) (0.0588 * L - 0.296 * S - 15.8 + 0.5);
    return index;
}
