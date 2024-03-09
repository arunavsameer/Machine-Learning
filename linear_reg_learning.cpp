#include <bits/stdc++.h>
using namespace std;
//try same in python also
#define data_count 5
#define alpha 0.01 //learning rate
#define h 0.001 //dw and db
#define ok_err 0.001 //passable error

float w = 0;
float b = 0;

float data_x[data_count] = {1, 2, 3, 4, 7};
float data_y[data_count] = {3, 5, 7, 9, 11};

float j_wb(float w, float b){
    float sq_err = 0;
    for(int i = 0; i < data_count; i++){
        sq_err += ((w * data_x[i]) + b - data_y[i]) * ((w * data_x[i]) + b - data_y[i]);
    }
    float mean_sq_err = sq_err / (2 * data_count);
    return mean_sq_err;
}

float derv_w_j_wb(float w, float b){
    float partial_derv = (j_wb(w + h, b) - j_wb(w, b)) / h;
    return partial_derv;
}

float derv_b_j_wb(float w, float b){
    float partial_derv = (j_wb(w , b + h) - j_wb(w, b)) / h;
    return partial_derv;
}

void minimize_j_wb(){
    float tmp_w;
    float tmp_b;
    float err_w, err_b;
    do{
        err_w = ((alpha) * (derv_w_j_wb(w, b)));
        err_b = ((alpha) * (derv_b_j_wb(w, b)));
        float tmp_w = w - err_w;
        float tmp_b = b - err_b;
        w = tmp_w;
        b = tmp_b;
        //cout << err_w <<" " <<err_b <<endl;
    }while(abs(err_w) > 0.0000001 && abs(err_b) > 0.0000001);
}

int main(){
    minimize_j_wb();
    cout << "w: " << w <<endl << "b: " << b <<endl;
}
