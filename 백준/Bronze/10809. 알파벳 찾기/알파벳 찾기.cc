#include <iostream>
using namespace std;

const int ALPHA_CNT = 26;
const int MAX_INPUT = 100;

int main() {
    int alpha[ALPHA_CNT] = {};
    char input[MAX_INPUT + 1] = {};
    int size;

    for (int i = 0; i < ALPHA_CNT; i++) {
        alpha[i] = -1;
    }

    cin >> input;

    for (size = 0; size < MAX_INPUT && input[size] != 0; size++);

    for (int i = 0; i <= size; i++) {
        int index = input[i] - 'a';
        if (index >= 0 && index < ALPHA_CNT && alpha[index] == -1) alpha[index] = i;
    }

    for (int i = 0; i < ALPHA_CNT; i++) {
        cout << alpha[i] << " ";
    }

    return 0;
}