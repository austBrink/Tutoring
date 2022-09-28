#include <iostream>

// function declarations...
double yearPopulation (double populationInit, double bRate, double dRate);
double getPopulationAfterXYears (int years, double populationInit, double bRate, double dRate);
double getPopulation (int a, int b, double populationInit, double bRate, double dRate);
void print(std::string val);
void print(double val);

int main() {
    double population = 0.0;
    double birth = 0.0;
    double death = 0.0;
    int years = 0;

    do {
        print("Please enter a valid initial population ( >=2 ): ");
        std:: cin >> population;
    } while(population < 2);
    
    do {
        print("cool. Now enter a positive birth rate: ");
        std::cin >> birth;
    } while (birth < 0);
    
    do {
        print("now enter a value for the death rate x_x");
        std::cin >> death;
    } while (death < 0);

    do {
        print("Enter for how many years you would like the population calculated");
        std::cin >> years;
    } while (years < 1);
    
    print(getPopulationAfterXYears(years, population, birth, death));
    print(getPopulation(1, years, population, birth, death));
}

double getPopulationAfterXYears (int years, double populationInit, double bRate, double dRate){
    double pop = populationInit;
    for (int i = 1; i <= years; i++){
        pop = yearPopulation(pop, bRate, dRate);
    }
    return pop;
}

double getPopulation (int a, int b, double populationInit, double bRate, double dRate ) {
    if (b < a) {
        return populationInit;
    }
    return getPopulation (a + 1, b, yearPopulation(populationInit, bRate, dRate), bRate, dRate);    
}

double yearPopulation (double populationInit, double bRate, double dRate){
    return populationInit*(1.00 + bRate - dRate);
}

void print(std::string val) {
    std::cout << val << std::endl;
}

void print(double val) {
    printf( "%f", val);
    std::cout<<std::endl;
}