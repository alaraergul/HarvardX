#include <cs50.h>
#include <stdio.h>

// Function prototypes
bool is_valid_card(long long number);
int get_num_digits(long long number);
int get_digit(long long number, int position);
void print_card_type(long long number);

int main(void)
{

    long long card_number;
    do
    {
        card_number = get_long("Number: ");
    }
    while (card_number <= 0);

    if (is_valid_card(card_number))
    {
        print_card_type(card_number);
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}

bool is_valid_card(long long number)
{
    int sum = 0;
    bool double_digit = false;

    int num_digits = get_num_digits(number);

    for (int i = 1; i <= num_digits; i++)
    {
        int digit = get_digit(number, i);

        if (double_digit)
        {
            digit *= 2;
            if (digit >= 10)
            {
                digit = digit % 10 + 1;
            }
        }

        sum += digit;
        double_digit = !double_digit;
    }

    return sum % 10 == 0;
}

int get_num_digits(long long number)
{
    int count = 0;
    while (number != 0)
    {
        number /= 10;
        count++;
    }
    return count;
}

int get_digit(long long number, int position)
{
    while (position > 1)
    {
        number /= 10;
        position--;
    }
    return number % 10;
}

void print_card_type(long long number)
{
    int num_digits = get_num_digits(number);
    int first_digit = get_digit(number, num_digits);
    int second_digit = get_digit(number, num_digits - 1);

    if (num_digits == 15 && first_digit == 3 && (second_digit == 4 || second_digit == 7))
    {
        printf("AMEX\n");
    }
    else if (num_digits == 16 && first_digit == 5 && second_digit >= 1 && second_digit <= 5)
    {
        printf("MASTERCARD\n");
    }
    else if ((num_digits == 13 || num_digits == 16) && first_digit == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
