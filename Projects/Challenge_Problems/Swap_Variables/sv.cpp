#include <stdlib.h>
#include <stdio.h>
#include <iostream>

using namespace std;

int main() {

    int v1 = 1;
    int v2 = 2;

    //Your code goes here: (Answer provided)
    int v3 = v1;
    v1 = v2;
    v2 = v3;

    
    cout << v1 << v2 << endl;
}