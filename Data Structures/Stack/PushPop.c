#include <stdio.h>
#define MAX 10

struct stack{
  int arr[MAX];
  int top;
};

void push(struct stack *s, int item){
    if(s -> top == MAX-1){
        printf("Stack is full\n");
    }
    s -> top++;
    s -> arr[s -> top] = item;
}

int pop(struct stack *s){
    int data;
    if(s -> top == -1){
        printf("Stack is empty\n");
        return 0;
    }
    data = s -> arr[s -> top];
    s -> top--;
    return data;
}

void initstack(struct stack *s){
    s -> top = -1;
}

int main() {
    // Write C code here
    struct stack s;
    int n,a,c;
    
    initstack(&s);
    
    printf("Enter element to push: \n");
    scanf("%d",&a);
    push(&s, a);
    
    for(int i = 0; i < MAX; i++){
        printf("If you want to push element, enter 1, for pop operation, enter 2\n");
        scanf("%d",&c);
        switch(c){
            case 1:
            printf("Enter element to push: \n");
            scanf("%d",&a);
            push(&s, a);
            break;
            
            case 2:
            n = pop(&s);
            printf("Item popped: %d\n",n);
            break;
            
            default:
            printf("Invalid Operation\n");
        };
    }
    
    return 0;
}
