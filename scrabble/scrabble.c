#include <ctype.h>
#include <stdio.h>

int calculate_score(char *word)
{
    int score = 0;
    int letter_scores[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                             1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    for (int i = 0; word[i] != '\0'; i++)
    {
        if (isalpha(word[i]))
        {
            int index = toupper(word[i]) - 'A';
            score += letter_scores[index];
        }
    }

    return score;
}

int main(void)
{
    char word1[50], word2[50];

    printf("Player 1: ");
    scanf("%s", word1);
    int score1 = calculate_score(word1);

    printf("Player 2: ");
    scanf("%s", word2);
    int score2 = calculate_score(word2);

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0;
}
