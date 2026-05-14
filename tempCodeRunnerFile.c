#include<stdio.h>
#define size 5
int hash[size];
int hashfunction(int key){
    return key%size;
}
void insert(int key){
    int index=hashfunction(key);
    hash[index]=key;
}
int main(){
    insert(4);
    insert(3);
    insert(7);
    insert(16);
    insert(20);

}