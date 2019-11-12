#include <iostream>
#include <fstream>

using namespace std;

void explicita(float inicial, float final, float delta, float w, string archivo);

int main(){

	float w = 0.1;
	float x_inicial = 0.0;
	float x_final = 4/w;

	explicita(x_inicial, x_final, 0.1/w, w, "0.1ex.dat");
	explicita(x_inicial, x_final, 0.01/w, w, "0.01ex.dat");
	explicita(x_inicial, x_final, 1.0/w, w, "1ex.dat");

	return 0;
}

void explicita (float inicial, float final, float delta, float omega, string archivo) {
	float x=inicial;
  	float y=1.0;
  	ofstream outfile;
  	outfile.open(archivo);

  	while(x<final){    
    	outfile << x << " " << y << endl;
    	y = y - delta * omega  * y;
    	x = x + delta;
  	}
  	outfile.close();
}