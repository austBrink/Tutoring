#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>

int main() {
    std::string filename;
    std::cout << "Enter the name of the file: ";
    std::cin >> filename;

    std::ifstream infile(filename);
    if (!infile) {
        std::cerr << "Error: could not open file " << filename << std::endl;
        return 1;
    }

    std::vector<int> numbers;
    int number;
    while (infile >> number) {
        numbers.push_back(number);
    }

    if (numbers.empty()) {
        std::cerr << "Error: file " << filename << " is empty" << std::endl;
        return 1;
    }

    int lowest = *std::min_element(numbers.begin(), numbers.end());
    int highest = *std::max_element(numbers.begin(), numbers.end());
    int total = std::accumulate(numbers.begin(), numbers.end(), 0);
    double average = static_cast<double>(total) / numbers.size();

    std::cout << "Lowest number: " << lowest << std::endl;
    std::cout << "Highest number: " << highest << std::endl;
    std::cout << "Total of the numbers: " << total << std::endl;
    std::cout << "Average of the numbers: " << average << std::endl;

    return 0;

}
