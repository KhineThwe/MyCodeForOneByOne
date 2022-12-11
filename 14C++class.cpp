#include <iostream>
#include <conio.h>

using namespace std;
class NCC{
   public:
    string name;
    void myMethod(){
        cout<<"This is my method"<<endl;
    }
};
int main()
{
    NCC obj1;
    obj1.name = "Python";
    cout<<obj1.name<<endl;
    obj1.myMethod();

    return 0;
}
