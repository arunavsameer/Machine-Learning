#include <bits/stdc++.h>
using namespace std;
//try same in python also
#define data_count 9
#define alpha 0.0001 //learning rate
#define ok_err 0.00000000001 //passable error

double w = 0;
double b = 0;

double data_x[data_count] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
double data_y[data_count] = {3, 5, 7, 9, 11, 13, 15, 17, 19};

double j_wb(double w, double b){
    double sq_err = 0;
    for(int i = 0; i < data_count; i++){
        sq_err += ((w * data_x[i]) + b - data_y[i]) * ((w * data_x[i]) + b - data_y[i]);
    }
    double mean_sq_err = sq_err / (2 * data_count);
    return mean_sq_err;
}

double derv_w_j_wb(double w, double b){
    double delta_sum = 0;
    for(int i = 0; i < data_count; i++){
        delta_sum += ((((w * data_x[i]) + b) - data_y[i]) * data_x[i]);
    }
    return (delta_sum / data_count);
}

double derv_b_j_wb(double w, double b){
    double delta_sum = 0;
    for(int i = 0; i < data_count; i++){
        delta_sum += (((w * data_x[i]) + b) - data_y[i]);
    }
    return (delta_sum / data_count);
}

void minimize_j_wb(){
    double tmp_w;
    double tmp_b;
    double err_w, err_b;
    do{
        err_w = ((alpha) * (derv_w_j_wb(w, b)));
        err_b = ((alpha) * (derv_b_j_wb(w, b)));
        w = w - err_w;
        b = b - err_b;
        //cout << err_w <<" " <<err_b <<endl;
    }while(abs(err_w) > ok_err && abs(err_b) > ok_err);
}

int main(){
    minimize_j_wb();
    cout << "w: " << w <<endl << "b: " << b <<endl;
}
