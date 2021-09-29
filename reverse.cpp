#include <iostream>
#include<cstring>

using namespace std;

int main() {
    char name[30], t;
    strcpy(name, "Kamal");

    for(int i = 0, j = 4; i < j; i++, j--) {
        cout << "i = " << i << " j = " << j << endl;
        t = name[i];
        name[i] = name[j];
        name[j] = t;
    }
    cout << "Reversed string: " << name << endl;
}
