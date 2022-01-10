
// This problem was asked by Google.
// 
// Given the head of a singly linked list, reverse it in-place.

struct SimpleList {
    int val;
    SimpleList* next;
};

SimpleList* reverseList(SimpleList* list) {
    SimpleList* current = list;
    SimpleList* last;
    while (current->next) {
        SimpleList* next = current->next;
        current->next = last;
        last = current;
        current = next;
    }
    current->next = last;
    return current;
}