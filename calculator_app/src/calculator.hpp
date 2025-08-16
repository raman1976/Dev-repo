#pragma once
#include<stdexcept>

class Calculator {
public:
    static int add(int a, int b) 
    { 
        return a + b; 
    }
    static int sub(int a, int b) 
    { 
        return a - b;
    }
    static int mul(int a, int b) 
    { 
        return a * b;
    }
    static int div(int a, int b) 
    {
        if(b==0) throw std::domain_error("divide by zero");
        return a / b;
    }
};