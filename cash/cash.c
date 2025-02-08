#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int cal_quarters(int cents);
int cal_dimes(int cents);
int cal_nickels(int cents);
int cal_pennies(int cents);

int main(void)
{
    int cents = get_cents();
    printf("Cents: %i\n", cents);

    int quarters = cal_quarters(cents);
    printf("Quarters: %i\n", quarters);
    cents -= quarters * 25;

    int dimes = cal_dimes(cents);
    printf("Dimes: %i\n", dimes);
    cents -= dimes * 10;

    int nickels = cal_nickels(cents);
    printf("Nickels: %i\n", nickels);
    cents -= nickels * 5;

    int pennies = cal_pennies(cents);
    printf("Pennies: %i\n", pennies);

    int coins = quarters + dimes + nickels + pennies;
    printf("Total coins: %i\n", coins);
}

int get_cents(void)
{
    int no_cents;
    do
    {
        no_cents = get_int("Change owed: ");
    }
    while (no_cents < 0);
    return no_cents;
}

int cal_quarters(int cents)
{
    int quarters = cents / 25;
    cents %= 25;
    return quarters;
}

int cal_dimes(int cents)
{
    int dimes = cents / 10;
    cents %= 10;
    return dimes;
}

int cal_nickels(int cents)
{
    int nickels = cents / 5;
    cents %= 5;
    return nickels;
}

int cal_pennies(int cents)
{
    return cents;
}
